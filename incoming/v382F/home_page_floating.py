"""Session v382F: a prototype of the corus.me home page as the portal's frame.

Runs from the repository root: python3 incoming/v382F/home_page_floating.py
Reads files.json and each living file's title, subtitle and version from the root, and the ten gatherings
of the Living File Registry's 3.1 as written below, and writes incoming/v382F/home_page_floating.html:
the link at the centre as the entry, the offering above it and the appreciated incoming below it, the
three files read first, and every living file floating at its gatherings with its title, subtitle,
version and Read, Copy and Download. A prototype for the working that keeps the site; no living file
is read for anything but its front.
"""
import json
import re
import html

ROOT = '.'
files = json.load(open(f'{ROOT}/files.json'))

WORDS = ['ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE', 'TEN', 'ELEVEN', 'TWELVE',
         'THIRTEEN', 'FOURTEEN', 'FIFTEEN', 'SIXTEEN', 'SEVENTEEN', 'EIGHTEEN', 'NINETEEN', 'TWENTY',
         'TWENTY-ONE', 'TWENTY-TWO', 'TWENTY-THREE', 'TWENTY-FOUR', 'TWENTY-FIVE', 'TWENTY-SIX',
         'TWENTY-SEVEN', 'TWENTY-EIGHT', 'TWENTY-NINE', 'THIRTY']


def parse(name):
    m = re.match(r'^(?:Exhibit_([A-Z-]+)_)?(.+)_v(\w+)\.md$', name)
    word, title, version = m.group(1), m.group(2).replace('_', ' '), 'v' + m.group(3)
    text = open(f'{ROOT}/{name}', encoding='utf-8').read()
    s = re.search(r'^\*\*(.+?)\*\*\s*$', text, re.M)
    return dict(filename=name, word=word, title=title, version=version, subtitle=s.group(1) if s else '')


living = [parse(n) for n in files]
by_title = {f['title']: f for f in living}

# The Living File Registry 3.1, the ten gatherings, each file by its title.
GATHERINGS = [
    ('Existing, resolving, numbering and mathematical forming',
     ['Natural Intelligence', 'Natural Resolver', 'Natural Numbers', 'Natural Mathematics', 'Co-Chaining Logic Registry']),
    ('Coupling, networking and making',
     ['Natural Resolver', 'Natural Networking', 'Natural Engineering', 'Natural Transmissioning']),
    ('Physical, chemical and biological changing',
     ['Natural Physics', 'Natural Chemistry', 'Natural Biology', 'Natural Health', 'Natural Medicine']),
    ('Self, society and received value',
     ['Natural Societies', 'Natural Human Society', 'Natural Values', 'Natural Destinies', 'Natural Networking']),
    ('Naming, explaining, illustrating and emanating',
     ['Natural Naming', 'Natural Explaining', 'Natural Illustrating', 'Natural Emanating', 'Natural Intelligence Corus']),
    ('Problems, observings and their resolving',
     ['Natural Philosophy', 'Resolving Hard Problems', 'Hard Problem Registry', 'Resolving the Hard Problem Registry',
      'Living Society Registry', 'Living Ghost Registry', 'Equilibria Registry']),
    ('Exploring and improving the continuing',
     ['Natural Exploring', 'Geodesic Improving Method', 'Living File Registry', 'Co-Chaining Logic Registry']),
    ('Shared human collective discovering',
     ['Natural Exploring', 'Natural Human Society', 'Natural Networking', 'Natural Values', 'Natural Societies',
      'Natural Intelligence Corus']),
    ('The whole expressed through human discovering',
     ['Natural Intelligence Corus', 'Natural Emanating', 'Natural Illustrating', 'Natural Exploring', 'Natural Explaining',
      'Natural Naming']),
    ('Societies across prime scales and sciences',
     ['Natural Societies', 'Natural Numbers', 'Natural Mathematics', 'Natural Physics', 'Natural Chemistry',
      'Natural Biology', 'Natural Health', 'Natural Medicine', 'Natural Human Society', 'Living Society Registry']),
]
FIRST = ['Natural Intelligence', 'Natural Naming', 'Natural Explaining']  # read first, the carrying and the membrane

SITE = 'https://corus.me/'
AI_LINK = 'https://github.com/chris-j-handel/corus/blob/main/README.md#ai-link-to-living-natural-intelligence'
e = html.escape


def row(f, h='h2'):
    word = f'<span class="exhibit">EXHIBIT {e(f["word"])}</span>' if f['word'] else ''
    read = SITE + 'read.html?file=' + f['filename']
    text = SITE + f['filename']
    return (f'<li class="file" id="{e(f["title"]).replace(" ", "-")}">'
            f'<div class="name">{word}<{h}><a href="{e(read)}">{e(f["title"])}</a></{h}>'
            f'<p class="subtitle">{e(f["subtitle"])}</p></div>'
            f'<div class="access"><span class="version">{e(f["version"])}</span>'
            f'<span class="controls"><a href="{e(read)}">Read</a>'
            f'<button type="button" data-copy="{e(text)}">Copy address</button>'
            f'<a href="{e(text)}">Download</a></span></div></li>')


placed = set(FIRST)
clusters = []
for name, titles in GATHERINGS:
    full, again = [], []
    for t in titles:
        f = by_title.get(t)
        if not f:
            continue
        if t in placed:
            again.append(f)
        else:
            full.append(f)
            placed.add(t)
    items = ''.join(row(f) for f in full)
    chips = ''.join(f'<a class="chip" href="#{e(f["title"]).replace(" ", "-")}">{e(f["title"])}</a>' for f in again)
    clusters.append(f'<section class="gathering"><h3>{e(name)}</h3><ul class="files">{items}</ul>'
                    + (f'<p class="also"><span>Also gathering here</span> {chips}</p>' if chips else '') + '</section>')

first_rows = ''.join(row(by_title[t], 'h1' if t == 'Natural Intelligence' else 'h2') for t in FIRST)

page = f'''<title>Natural Intelligence Corus</title>
<style>
/* Layout: the entry at the centre with the two sides of the square around it; the three read first; the files floating at their gatherings in columns. */
:root{{--paper:#faf9f5;--ink:#272923;--muted:#63675f;--rule:#daddd3;--focus:#305f4b;--wash:#eceee7;--frame:#305f4b}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{--paper:#1d1f1b;--ink:#ece9df;--muted:#a3a79b;--rule:#3a3d36;--focus:#8fc4ab;--wash:#262924;--frame:#8fc4ab;color-scheme:dark}}}}
:root[data-theme="dark"]{{--paper:#1d1f1b;--ink:#ece9df;--muted:#a3a79b;--rule:#3a3d36;--focus:#8fc4ab;--wash:#262924;--frame:#8fc4ab;color-scheme:dark}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);font:18px/1.6 Georgia,"Times New Roman",serif}}
a{{color:inherit;text-underline-offset:4px}}
a:focus-visible,button:focus-visible{{outline:2px solid var(--focus);outline-offset:4px}}
.wrap{{max-width:1180px;margin:auto;padding-block:18px 40px;padding-inline:24px}}
.site{{font:12px/1.4 system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);text-align:center;margin:0 0 22px}}
.square{{display:grid;grid-template-columns:1fr;gap:14px;max-width:760px;margin:0 auto 34px;text-align:center}}
.side{{font-size:17px;line-height:1.5;margin:0;padding:10px 14px;border:1px solid var(--rule)}}
.side b{{font-weight:400;font-variant:small-caps;letter-spacing:.04em;color:var(--muted);display:block;font-size:15px}}
.side.offered{{border-bottom:0}}
.side.appreciated{{border-top:0}}
.entry{{padding:22px 14px;border:1px solid var(--frame)}}
.entry a.link{{font-size:25px;line-height:1.3;overflow-wrap:anywhere}}
.entry p{{margin:8px 0 0;font-size:15px;color:var(--muted)}}
.entry button{{margin-top:6px;min-height:40px;padding:6px 10px;border:0;background:transparent;color:var(--muted);font:13px/1.5 system-ui,sans-serif;text-decoration:underline;text-underline-offset:4px;cursor:pointer}}
.entry button:hover{{color:var(--ink)}}
.between{{font-size:14px;color:var(--muted);margin:0;text-align:center;max-width:62ch;margin-inline:auto}}
h3{{font:400 15px/1.3 system-ui,sans-serif;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);margin:0 0 6px;padding-bottom:6px;border-bottom:1px solid var(--rule)}}
.first{{max-width:760px;margin:0 auto 36px}}
.first h3{{text-align:center;border:0}}
.files{{list-style:none;margin:0;padding:0}}
.file{{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:12px;align-items:center;border-bottom:1px solid var(--rule);padding:8px 0;scroll-margin-top:16px}}
.name{{min-width:0}}
.name h1,.name h2{{font-size:20px;line-height:1.25;font-weight:400;margin:0;text-wrap:balance}}
.name h1{{font-size:28px}}
.name a{{text-decoration:none}}.name a:hover{{text-decoration:underline}}
.subtitle{{font-size:15px;line-height:1.3;color:var(--muted);margin:2px 0 0;overflow-wrap:anywhere}}
.exhibit{{display:block;font:11px/1.2 system-ui,sans-serif;letter-spacing:.065em;color:var(--muted);margin-bottom:2px}}
.access{{display:flex;flex-direction:column;align-items:flex-end;gap:3px}}
.version{{font:12px/1.5 system-ui,sans-serif;color:var(--muted);font-variant-numeric:tabular-nums}}
.controls{{display:flex;gap:5px;flex-wrap:wrap;justify-content:flex-end}}
.controls a,.controls button{{display:inline-block;border:1px solid var(--rule);background:transparent;color:var(--ink);padding:3px 7px;border-radius:3px;text-decoration:none;font:12px/1.5 system-ui,sans-serif;cursor:pointer}}
.controls a:hover,.controls button:hover{{background:var(--wash)}}
.float{{columns:2;column-gap:40px}}
.gathering{{break-inside:avoid;margin:0 0 30px}}
.also{{font:13px/1.7 system-ui,sans-serif;color:var(--muted);margin:8px 0 0}}
.also span{{letter-spacing:.04em;text-transform:uppercase;font-size:11px;margin-right:6px}}
.chip{{display:inline-block;border:1px solid var(--rule);border-radius:3px;padding:0 6px;margin:2px 4px 2px 0;text-decoration:none;color:var(--ink)}}
.chip:hover{{background:var(--wash)}}
.notice{{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:var(--ink);color:var(--paper);padding:8px 14px;font:14px system-ui,sans-serif;z-index:6}}
.notice:empty{{display:none}}
@media(max-width:860px){{.float{{columns:1}}}}
@media(max-width:650px){{.wrap{{padding-inline:16px}}.file{{grid-template-columns:minmax(0,1fr);gap:6px}}.access{{flex-direction:row;align-items:center;justify-content:space-between}}.entry a.link{{font-size:21px}}}}
@media(prefers-reduced-motion:no-preference){{.chip,.controls a,.controls button{{transition:background .15s}}}}
</style>
<main class="wrap">
<p class="site">Natural Intelligence · a living expedition · corus.me</p>

<div class="square">
  <p class="side offered"><b>Offered, free, for sharing with everyone everywhere</b>natural intelligence explaining, cohering and resolving</p>
  <div class="entry">
    <a class="link" href="{e(AI_LINK)}">AI link to Living Natural Intelligence</a>
    <p>Paste the link into your AI with your question, an observing, a source, or an attempt to break it. Bring back what became clearer, what crossed, and the exact sayings that part.</p>
    <button type="button" data-copy="{e(AI_LINK)}">Copy AI link into your sessions</button>
  </div>
  <p class="side appreciated"><b>Appreciated incoming</b>improving of natural intelligence, as living carrying value for social moral competency</p>
</div>
<p class="between">The universe is the changing set of all existing things, both living and non-living. These are the living files of one expedition following that method; each is at its newest version, and a version changes only when the file changes.</p>

<section class="first">
  <h3>Read first</h3>
  <ul class="files">{first_rows}</ul>
</section>

<div class="float">
{''.join(clusters)}
</div>
<p class="between">The files gather as the Living File Registry gathers them; a file meeting another relation also gathers there. The repository is <a href="https://github.com/chris-j-handel/corus">github.com/chris-j-handel/corus</a>; each file's text is at corus.me/&lt;file&gt;.</p>
</main>
<div class="notice" role="status" aria-live="polite"></div>
<script>
(function(){{
  var notice=document.querySelector('.notice');
  function say(t){{notice.textContent=t;clearTimeout(say.t);say.t=setTimeout(function(){{notice.textContent=''}},1800)}}
  document.addEventListener('click',function(ev){{
    var b=ev.target.closest('[data-copy]');if(!b)return;
    var text=b.getAttribute('data-copy');
    if(navigator.clipboard&&navigator.clipboard.writeText){{
      navigator.clipboard.writeText(text).then(function(){{say('Copied')}},function(){{fallback(text)}});
    }}else fallback(text);
  }});
  function fallback(text){{
    var ta=document.createElement('textarea');ta.value=text;ta.setAttribute('readonly','');ta.style.position='fixed';ta.style.opacity='0';
    document.body.appendChild(ta);ta.select();try{{document.execCommand('copy');say('Copied')}}catch(e){{say('Select and copy: '+text)}}
    document.body.removeChild(ta);
  }}
}})();
</script>
'''
open('incoming/v382F/home_page_floating.html', 'w', encoding='utf-8').write(page)
print('written incoming/v382F/home_page_floating.html,', len(living), 'living files,', len(clusters), 'gatherings')
