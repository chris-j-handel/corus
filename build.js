#!/usr/bin/env node
/* corus.me · build.js
   Rebuilds files.json and the file list embedded in index.html and read.html
   from whatever files are in this folder, so nothing has to be edited by hand
   when a file is added, renamed, or given a new version.

   Which files are listed, and in what order, is decided by corus.js (the same
   code the browser runs), so the two can never disagree:
     · Natural_Intelligence_v###.md          first
     · Exhibit_<NUMBER>_<Title>_v###.md      in exhibit number order
     · Natural_Intelligence_Corus_v###.md    next
     · any other *_v###.md / .py / .zip      after that
   Files without a _v### version suffix are ignored. When two versions of the
   same document are present, the newest is listed.

   Run by hand with:  node build.js
   Run automatically on every push by .github/workflows/files.yml */
'use strict';
const fs = require('fs'), path = require('path'), crypto = require('crypto');
const Corus = require('./corus.js');
const root = __dirname;

const escape = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#x27;' }[c]));
const href = name => escape(encodeURIComponent(name));
const readHref = name => 'read.html?file=' + href(name);
const label = f => (f.word ? f.word + ' · ' : '') + f.title;

// Mirrors fileRow() in corus.js, so the page looks the same before and after scripts run.
function fileRow(f) {
  const main = f.id === 'natural-intelligence', tag = main ? 'header' : 'div', h = main ? 'h1' : 'h2';
  return `<li class="file-row" data-id="${escape(f.id)}"><${tag} class="file-name">`
    + (f.word ? `<span class="exhibit">EXHIBIT ${escape(f.word)}</span>` : '')
    + `<${h}><a href="${readHref(f.filename)}">${escape(f.title)}</a></${h}>`
    + (f.subtitle ? `<p class="subtitle">${escape(f.subtitle)}</p>` : '')
    + `</${tag}><div class="file-access"><span class="version">${escape(f.version)}</span><div class="controls">`
    + `<a href="${readHref(f.filename)}" aria-label="Read · ${escape(label(f))}">Read</a>`
    + `<button type="button" data-copy="${escape(f.filename)}" aria-label="Copy · ${escape(label(f))}"${f.format === 'zip' ? ' disabled title="ZIP"' : ''}>Copy</button>`
    + `<a href="${href(f.filename)}" download="${escape(f.filename)}" aria-label="Download · ${escape(label(f))}">Download</a>`
    + '</div></div></li>';
}

function replaceBetween(html, open, close, content) {
  const start = html.indexOf(open), end = start < 0 ? -1 : html.indexOf(close, start + open.length);
  if (start < 0 || end < 0) throw new Error(`Could not find ${open} … ${close}`);
  return html.slice(0, start + open.length) + content + html.slice(end);
}

function write(name, content) {
  const target = path.join(root, name);
  if (fs.existsSync(target) && fs.readFileSync(target, 'utf8') === content) { console.log(`unchanged  ${name}`); return; }
  fs.writeFileSync(target, content); console.log(`updated    ${name}`);
}

function warn(message) { console.log((process.env.GITHUB_ACTIONS ? '::warning::' : 'warning: ') + message); }

// 1. Decide which files are listed.
const names = fs.readdirSync(root).filter(n => { try { return fs.statSync(path.join(root, n)).isFile(); } catch { return false; } }).sort();
const chosen = Corus.selection(names), chosenNames = new Set(chosen.map(f => f.filename));

for (const name of names) {
  if (chosenNames.has(name)) continue;
  let record = null, reason = null;
  try { record = Corus.identify(name); } catch (error) { reason = error.message; }
  if (record) console.log(`superseded ${name}  (${chosen.find(f => f.id === record.id).filename} is listed instead)`);
  else if (/^exhibit/i.test(name) || /_v\d+[a-z]*(\(\d+\))?\.(md|py|zip)$/i.test(name)) warn(`${name} is not listed: ${reason}`);
}

// 2. Read titles and subtitles from the documents themselves.
const files = chosen.map(f => {
  const buffer = fs.readFileSync(path.join(root, f.filename));
  let record = f;
  if (f.format === 'md') {
    record = Corus.metadata(buffer.toString('utf8'), f, false);
    if (record.title === f.title && !/^# /m.test(buffer.toString('utf8'))) warn(`${f.filename} has no "# Title" heading; using the filename as its title`);
  }
  return {
    id: f.id, title: record.title, subtitle: record.subtitle, role: f.format === 'md' ? 'subject' : 'instrument',
    version: f.version, number: f.number, filename: f.filename,
    sha256: crypto.createHash('sha256').update(buffer).digest('hex'), bytes: buffer.length,
    format: f.format, display_title: label(record), word: f.word
  };
});

// 3. Write files.json and refresh both pages.
const json = JSON.stringify(files).replace(/</g, '\\u003c');
const initial = '<script type="application/json" id="initial-files">';
write('files.json', JSON.stringify(files.map(f => f.filename), null, 2) + '\n');
write('index.html', replaceBetween(replaceBetween(fs.readFileSync(path.join(root, 'index.html'), 'utf8'),
  '<ol class="files" id="files">', '</ol>', files.map(fileRow).join('')), initial, '</script>', json));
write('read.html', replaceBetween(fs.readFileSync(path.join(root, 'read.html'), 'utf8'), initial, '</script>', json));

console.log('\nListed, in order:');
for (const f of files) console.log(`  ${(f.word ? f.word + ' · ' : '') + f.title}  ${f.version}`);
