/* corus.me · v345a */
(function (root) {
  'use strict';
  const small = 'ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ELEVEN TWELVE THIRTEEN FOURTEEN FIFTEEN SIXTEEN SEVENTEEN EIGHTEEN NINETEEN'.split(' ');
  const tens = { TWENTY: 20, THIRTY: 30, FORTY: 40, FIFTY: 50, SIXTY: 60, SEVENTY: 70, EIGHTY: 80, NINETY: 90 };
  const scales = { THOUSAND: 1000, MILLION: 1000000, BILLION: 1000000000, TRILLION: 1000000000000 };
  function exhibitNumber(word) {
    if (/^\d+$/.test(word)) { const n = Number(word); return Number.isSafeInteger(n) && n > 0 ? n : null; }
    let total = 0, group = 0, previousScale = Infinity;
    for (const token of word.toUpperCase().split('-')) {
      if (token === 'AND') continue;
      if (small.includes(token)) group += small.indexOf(token);
      else if (tens[token]) group += tens[token];
      else if (token === 'HUNDRED' && group > 0 && group < 10) group *= 100;
      else if (scales[token] && scales[token] < previousScale && group > 0) {
        total += group * scales[token]; group = 0; previousScale = scales[token];
      } else return null;
    }
    const n = total + group;
    return Number.isSafeInteger(n) && n > 0 ? n : null;
  }
  function safeFilename(name) {
    return typeof name === 'string' && /^[A-Za-z0-9][A-Za-z0-9_(). -]*\.(md|py|zip)$/i.test(name) && !name.includes('..');
  }
  function identify(filename) {
    if (!safeFilename(filename)) throw new Error('Invalid filename');
    const version = filename.match(/_v(\d+[a-z]*)(?:\(\d+\))?\.(md|py|zip)$/i);
    if (!version) throw new Error('Missing version');
    const format = version[2].toLowerCase();
    let id, number = null, word = null, title;
    const exhibit = filename.match(/^Exhibit_([A-Z0-9-]+)_(.+?)_v\d/i);
    if (exhibit && format !== 'zip') {
      word = exhibit[1].toUpperCase(); number = exhibitNumber(word);
      if (number === null) throw new Error('Invalid exhibit number');
      id = 'exhibit-' + String(number).padStart(2, '0'); title = exhibit[2].replaceAll('_', ' ');
    } else if (/^Natural_Intelligence_v/i.test(filename) && format === 'md') {
      id = 'natural-intelligence'; title = 'Natural Intelligence';
    } else if (/^Natural_Intelligence_Corus_v/i.test(filename) && format === 'md') {
      id = 'corus'; title = 'Natural Intelligence Corus';
    } else if (/^Natural_Networking_Test_Kit_v/i.test(filename) && format === 'zip') {
      id = 'networking-kit'; title = 'Natural Networking Test Kit';
    } else throw new Error('Unlisted file type');
    return { id, filename, number, word, title, subtitle: null, version: 'v' + version[1], format };
  }
  function compareFiles(a, b) {
    const rank = f => f.id === 'natural-intelligence' ? 0 : f.number !== null ? 1 : f.id === 'corus' ? 2 : 3;
    return rank(a) - rank(b) || (a.number || 0) - (b.number || 0);
  }
  function selection(names) {
    if (!Array.isArray(names)) throw new Error('Invalid file list');
    const records = names.map(identify), ids = new Set(records.map(f => f.id));
    if (ids.size !== records.length || !ids.has('natural-intelligence')) throw new Error('Duplicate or missing file');
    return records.sort(compareFiles);
  }
  function metadata(text, record, strict = true) {
    const heading = /^# (.+)$/m.exec(text), subtitle = heading && /^\*\*(.+)\*\*\r?$/m.exec(text.slice(heading.index + heading[0].length));
    if (strict && record.format === 'md' && (!heading || !subtitle)) throw new Error('Missing title or subtitle');
    return { ...record, title: heading ? heading[1].trim() : record.title, subtitle: subtitle ? subtitle[1].trim() : null };
  }
  function zipContents(buffer) {
    const bytes = new Uint8Array(buffer), view = new DataView(buffer);
    let end = -1;
    for (let p = bytes.length - 22; p >= Math.max(0, bytes.length - 65557); p--) {
      if (view.getUint32(p, true) === 0x06054b50 && p + 22 + view.getUint16(p + 20, true) === bytes.length) { end = p; break; }
    }
    if (end < 0 || view.getUint16(end + 4, true) || view.getUint16(end + 6, true)) throw new Error('Unavailable');
    const count = view.getUint16(end + 10, true), size = view.getUint32(end + 12, true), offset = view.getUint32(end + 16, true);
    if (count === 65535 || offset + size > end || view.getUint16(end + 8, true) !== count) throw new Error('Unavailable');
    const names = []; let p = offset;
    for (let i = 0; i < count; i++) {
      if (p + 46 > offset + size || view.getUint32(p, true) !== 0x02014b50) throw new Error('Unavailable');
      const n = view.getUint16(p + 28, true), extra = view.getUint16(p + 30, true), comment = view.getUint16(p + 32, true);
      if (p + 46 + n + extra + comment > offset + size) throw new Error('Unavailable');
      names.push(new TextDecoder('utf-8').decode(bytes.subarray(p + 46, p + 46 + n)));
      p += 46 + n + extra + comment;
    }
    if (p !== offset + size) throw new Error('Unavailable');
    return names;
  }
  const api = { exhibitNumber, safeFilename, identify, compareFiles, selection, metadata, zipContents };
  if (typeof module === 'object' && module.exports) module.exports = api;
  root.Corus = api;
  if (typeof document === 'undefined') return;

  const $ = id => document.getElementById(id);
  const initial = JSON.parse($('initial-files').textContent), initialByName = new Map(initial.map(f => [f.filename, f]));
  const bytesCache = new Map(); let noticeTimer, readingText = null, readingFile = null;
  const href = name => encodeURIComponent(name);
  const readHref = name => 'read.html?file=' + encodeURIComponent(name);
  const label = f => (f.word ? f.word + ' · ' : '') + f.title;
  function notify(text) {
    $('notice').textContent = text; clearTimeout(noticeTimer);
    noticeTimer = setTimeout(() => { $('notice').textContent = ''; }, 2500);
  }
  async function fileBytes(filename) {
    if (!safeFilename(filename)) throw new Error('Invalid filename');
    if (!bytesCache.has(filename)) {
      const pending = fetch(href(filename)).then(response => {
        if (!response.ok) throw new Error('Unavailable');
        return response.arrayBuffer();
      });
      bytesCache.set(filename, pending);
      pending.catch(() => bytesCache.delete(filename));
    }
    return bytesCache.get(filename);
  }
  function decode(buffer) { return new TextDecoder('utf-8', { fatal: true, ignoreBOM: true }).decode(buffer); }
  async function catalogue() {
    const response = await fetch('files.json', { cache: 'no-cache' });
    if (!response.ok) throw new Error('Unavailable');
    const records = selection(await response.json());
    return Promise.all(records.map(async f => {
      if (initialByName.has(f.filename)) return { ...initialByName.get(f.filename), ...f, title: initialByName.get(f.filename).title, subtitle: initialByName.get(f.filename).subtitle };
      if (f.format !== 'md') return f;
      try { return metadata(decode(await fileBytes(f.filename)), f); }
      catch { return f; }
    }));
  }
  function controls(f, reading = false) {
    const box = document.createElement('div'); box.className = 'controls';
    const read = document.createElement('a'); read.href = readHref(f.filename); read.textContent = 'Read';
    read.setAttribute('aria-label', 'Read · ' + label(f));
    if (reading) read.setAttribute('aria-current', 'page');
    const copy = document.createElement('button'); copy.type = 'button'; copy.dataset.copy = f.filename; copy.textContent = 'Copy';
    copy.setAttribute('aria-label', 'Copy · ' + label(f)); copy.disabled = f.format === 'zip' || (reading && readingText === null);
    if (f.format === 'zip') copy.title = 'ZIP';
    const download = document.createElement('a'); download.href = href(f.filename); download.download = f.filename; download.textContent = 'Download';
    download.setAttribute('aria-label', 'Download · ' + label(f));
    box.append(read, copy, download); return box;
  }
  function fileRow(f) {
    const row = document.createElement('li'); row.className = 'file-row'; row.dataset.id = f.id;
    const name = document.createElement(f.id === 'natural-intelligence' ? 'header' : 'div'); name.className = 'file-name';
    if (f.word) { const number = document.createElement('span'); number.className = 'exhibit'; number.textContent = 'EXHIBIT ' + f.word; name.append(number); }
    const heading = document.createElement(f.id === 'natural-intelligence' ? 'h1' : 'h2'), link = document.createElement('a');
    link.href = readHref(f.filename); link.textContent = f.title; heading.append(link); name.append(heading);
    if (f.subtitle) { const subtitle = document.createElement('p'); subtitle.className = 'subtitle'; subtitle.textContent = f.subtitle; name.append(subtitle); }
    const access = document.createElement('div'); access.className = 'file-access';
    const version = document.createElement('span'); version.className = 'version'; version.textContent = f.version;
    access.append(version, controls(f)); row.append(name, access); return row;
  }
  async function copyFile(filename) {
    try {
      const text = readingFile === filename && readingText !== null ? readingText : decode(await fileBytes(filename));
      try { await navigator.clipboard.writeText(text); notify('Copied'); }
      catch {
        const dialog = $('copy-dialog'), field = $('copy-text'); field.value = text; dialog.showModal(); field.focus(); field.select();
        let copied = false; try { copied = document.execCommand('copy'); } catch {}
        if (copied) { dialog.close(); notify('Copied'); }
      }
    } catch { notify('Unavailable'); }
  }
  // Markdown is parsed in an inert template, then copied through this allowlist.
  const allowed = new Set('p h1 h2 h3 h4 h5 h6 ul ol li blockquote pre code table thead tbody tfoot tr th td em strong del s a br hr div span sup sub dl dt dd kbd details summary'.split(' '));
  const drop = new Set('script style iframe object embed svg math form input button textarea link meta base'.split(' '));
  function safeLink(raw) {
    const value = raw.trim();
    if (value.startsWith('#')) return value;
    let url; try { url = new URL(value, location.href); } catch { return null; }
    if (!['http:', 'https:', 'mailto:'].includes(url.protocol)) return null;
    if (url.origin === location.origin) {
      let filename;
      try { filename = decodeURIComponent(url.pathname.slice(url.pathname.lastIndexOf('/') + 1)); } catch { return null; }
      const folder = new URL('.', location.href).pathname;
      if (url.pathname.startsWith(folder) && safeFilename(filename) && /\.(md|py|zip)$/i.test(filename)) {
        return readHref(filename) + url.hash;
      }
    }
    return url.href;
  }
  function safeMarkdown(markup) {
    const template = document.createElement('template'); template.innerHTML = markup;
    const fragment = document.createDocumentFragment();
    function append(node, parent) {
      if (node.nodeType === 3) { parent.append(document.createTextNode(node.textContent)); return; }
      if (node.nodeType !== 1) return;
      const tag = node.localName.toLowerCase();
      if (drop.has(tag)) return;
      if (tag === 'img') { parent.append(document.createTextNode(node.getAttribute('alt') || '')); return; }
      if (!allowed.has(tag)) { for (const child of node.childNodes) append(child, parent); return; }
      const clean = document.createElement(tag);
      if (tag === 'a' && node.hasAttribute('href')) {
        const link = safeLink(node.getAttribute('href'));
        if (link) { clean.setAttribute('href', link); if (/^https?:/i.test(link)) { clean.target = '_blank'; clean.rel = 'noopener noreferrer'; } }
      }
      for (const attr of tag === 'ol' ? ['start'] : ['td', 'th'].includes(tag) ? ['colspan', 'rowspan'] : []) {
        const value = node.getAttribute(attr); if (value && /^\d+$/.test(value)) clean.setAttribute(attr, value);
      }
      for (const child of node.childNodes) append(child, clean);
      parent.append(clean);
    }
    for (const child of template.content.childNodes) append(child, fragment);
    return fragment;
  }
  api.safeLink = safeLink; api.safeMarkdown = safeMarkdown;
  function finishDocument(f) {
    const content = $('read-content'), seen = new Map();
    for (const heading of content.querySelectorAll('h1,h2,h3,h4,h5,h6')) {
      const base = heading.textContent.toLowerCase().replace(/[^\p{L}\p{N}_\s-]/gu, '').replace(/[\s_]+/g, '-').replace(/^-+|-+$/g, '') || 'section';
      const count = (seen.get(base) || 0) + 1; seen.set(base, count); heading.id = base + (count > 1 ? '-' + count : '');
      if (['H1', 'H2'].includes(heading.tagName)) {
        const li = document.createElement('li'), a = document.createElement('a'); a.href = '#' + encodeURIComponent(heading.id); a.textContent = heading.textContent; li.append(a); $('contents-list').append(li);
      }
    }
    $('contents').hidden = !$('contents-list').children.length;
    for (const table of content.querySelectorAll('table')) {
      const wrap = document.createElement('div'); wrap.className = 'table-wrap'; wrap.tabIndex = 0; wrap.setAttribute('role', 'region'); wrap.setAttribute('aria-label', f.title);
      table.replaceWith(wrap); wrap.append(table);
    }
    scrollSection();
  }
  function scrollSection() {
    let id; try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    if (!id) return;
    const target = Array.from($('read-content').querySelectorAll('[id]')).find(el => el.id === id);
    if (target) target.scrollIntoView();
  }
  async function initReader() {
    try {
      const params = new URLSearchParams(location.search), requested = params.get('file') || params.get('id');
      if (!requested) throw new Error('Unavailable');
      let filename = requested, record;
      if (!safeFilename(filename)) {
        const records = await catalogue();
        const matches = records.filter(f => f.id === requested || f.filename.replace(/_v\d+[a-z]*(?:\(\d+\))?\.(md|py|zip)$/i, '') === requested);
        if (matches.length !== 1) throw new Error('Unavailable');
        record = matches[0]; filename = record.filename;
      } else {
        try { record = initialByName.get(filename) || identify(filename); }
        catch { record = { filename, title: filename, format: filename.split('.').pop().toLowerCase(), version: (filename.match(/_v(\d+[a-z]*)/i) || ['', ''])[1] }; }
      }
      readingFile = filename; $('read-meta').textContent = filename;
      $('read-controls').replaceChildren(...controls(record, true).children);
      const buffer = await fileBytes(filename);
      if (record.format === 'zip') {
        const heading = document.createElement('h1'), pre = document.createElement('pre'); heading.textContent = record.title; pre.textContent = zipContents(buffer).join('\n');
        $('read-content').replaceChildren(heading, pre);
      } else {
        readingText = decode(buffer); record = metadata(readingText, record, false);
        if (record.format === 'py') {
          const pre = document.createElement('pre'), code = document.createElement('code'); code.textContent = readingText; pre.append(code); $('read-content').replaceChildren(pre);
        } else {
          if (!root.marked || typeof root.marked.parse !== 'function') throw new Error('Unavailable');
          $('read-content').replaceChildren(safeMarkdown(root.marked.parse(readingText)));
        }
      }
      $('read-controls').replaceChildren(...controls(record, true).children);
      $('read-status').hidden = true; document.title = record.title + (record.version ? ' · ' + record.version : ''); finishDocument(record);
    } catch { readingText = null; $('read-status').textContent = 'Unavailable'; $('read-status').hidden = false; }
  }
  async function initIndex() {
    try {
      const records = await catalogue();
      if (JSON.stringify(records.map(f => [f.filename, f.title, f.subtitle])) !== JSON.stringify(initial.map(f => [f.filename, f.title, f.subtitle]))) {
        $('files').replaceChildren(...records.map(fileRow));
      }
      if (location.hash.startsWith('#file=')) {
        const params = new URLSearchParams(location.hash.slice(1)), file = records.find(f => f.id === params.get('file'));
        if (file) location.replace(readHref(file.filename) + (params.get('section') ? '#' + encodeURIComponent(params.get('section')) : ''));
      }
    } catch { notify('Unavailable'); }
  }
  document.addEventListener('click', event => {
    const button = event.target.closest('button[data-copy]');
    if (button && !button.disabled && !/\.zip$/i.test(button.dataset.copy)) copyFile(button.dataset.copy);
  });
  $('copy-dialog').addEventListener('close', () => { $('copy-text').value = ''; });
  if (document.body.dataset.page === 'read') { window.addEventListener('hashchange', scrollSection); initReader(); }
  else initIndex();
})(typeof globalThis === 'object' ? globalThis : this);
