#!/usr/bin/env python3
"""Generates the site: index.html (download), guide.html (user guide) and releases.html (every version)
in each language of the app — English at the root, the others under <code>/ (es/, it/, …). The strings
live in tools/strings/<code>.py, English being the reference; the pages are the same structure filled
from one dictionary. Run `python3 tools/build.py` after editing and commit the output."""
from pathlib import Path
import importlib.util
import json
import re

ROOT = Path(__file__).resolve().parent.parent
REPO = 'MHGuitarte/ygd-editor'
ICON = re.sub(r'\s(width|height)="1024"', '', (ROOT / 'assets/icon.svg').read_text(), count=2)
ICON = re.sub(r'<!--.*?-->', '', ICON, flags=re.S)
FP256 = '46:C5:62:27:2A:5C:22:9E:D7:85:E1:A3:0D:47:2A:A3:5B:CE:AC:F0:7D:E4:D8:A3:49:23:C9:7B:D3:74:C3:AB'
FP1 = '79A40643BDFE500AB6730154B03B336C1809C57C'

# The languages of the app (src/i18n in the code repository), in the order the menu shows them, with the
# name each one gives itself. English lives at the root of the site; every other language under <code>/.
LANGS = {'en': 'English', 'es': 'Español', 'it': 'Italiano', 'pl': 'Polski', 'fr': 'Français', 'de': 'Deutsch', 'tr': 'Türkçe'}
PAGES = ('index.html', 'guide.html', 'releases.html')


def load(code):
    spec = importlib.util.spec_from_file_location(f'strings_{code}', ROOT / 'tools/strings' / f'{code}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    t = dict(module.T)
    t['lang'] = code
    t['root'] = '' if code == 'en' else '../'  # from this language's pages to the root of the site
    return t


def lang_dir(code):
    return '' if code == 'en' else f'{code}/'


T = {code: load(code) for code in LANGS if (ROOT / 'tools/strings' / f'{code}.py').exists()}
for code in LANGS:
    if code not in T:
        print(f'no tools/strings/{code}.py yet — {LANGS[code]} is not built and not offered in the menu')
missing = {code: sorted(set(T['en']) - set(t)) for code, t in T.items() if set(T['en']) - set(t)}
if missing:
    raise SystemExit(f'strings missing (English is the reference): {missing}')

CSS = r'''
:root { --bg:#f6f5f2; --card:#ffffff; --ink:#1f2328; --muted:#616974; --line:#e1e1dd; --accent:#5980a6; --accent-ink:#fff; --soft:#e9eff5; --code:#eeeeea; --shadow:0 12px 40px rgba(31,35,40,.10); color-scheme: light dark; }
@media (prefers-color-scheme: dark) { :root { --bg:#14161a; --card:#1d2025; --ink:#e7e9ec; --muted:#9aa3ad; --line:#2c3138; --accent:#7ea3c8; --accent-ink:#0f1318; --soft:#232c36; --code:#262a31; --shadow:0 12px 40px rgba(0,0,0,.45); } }
* { box-sizing:border-box } html { scroll-behavior:smooth }
body { margin:0; background:var(--bg); color:var(--ink); font:17px/1.6 Barlow, system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; -webkit-font-smoothing:antialiased }
a { color:var(--accent) } a:hover { text-decoration-thickness:2px }
.wrap { max-width:960px; margin:0 auto; padding:0 22px }
.top { display:flex; align-items:center; gap:14px; padding:18px 0; flex-wrap:wrap }
.top .brand { display:flex; align-items:center; gap:10px; text-decoration:none; color:inherit; font-weight:600; font-size:19px; margin-right:auto }
.top .brand svg { width:34px; height:34px }
.top nav { display:flex; gap:18px; flex-wrap:wrap; font-size:15px }
.top nav a { color:var(--ink); text-decoration:none; opacity:.85 } .top nav a:hover { opacity:1; text-decoration:underline } .top nav a[aria-current] { opacity:1; font-weight:600 }
.lang { position:relative; display:inline-flex; align-items:center; gap:6px; font-size:14px; border:1px solid var(--line); border-radius:999px; padding:5px 12px; color:var(--ink); background:var(--card) }
.lang svg { width:15px; height:15px; opacity:.75 } .lang select { appearance:none; -webkit-appearance:none; border:0; background:transparent; color:inherit; font:inherit; padding-right:14px; cursor:pointer } .lang::after { content:''; position:absolute; right:12px; top:50%; width:6px; height:6px; border-right:1.5px solid var(--muted); border-bottom:1.5px solid var(--muted); transform:translateY(-70%) rotate(45deg); pointer-events:none }
.hero { padding:36px 0 12px; display:grid; gap:22px }
h1 { font-size:clamp(30px, 4.6vw, 44px); line-height:1.12; margin:0; letter-spacing:-.015em; font-weight:700 }
.lead { font-size:19px; color:var(--muted); margin:0; max-width:62ch }
.dl { display:grid; gap:12px; justify-items:start }
.btn { display:inline-flex; align-items:center; gap:10px; background:var(--accent); color:var(--accent-ink); text-decoration:none; font-weight:600; font-size:19px; padding:15px 26px; border-radius:12px; box-shadow:0 6px 18px rgba(89,128,166,.28) }
.btn:hover { filter:brightness(1.06); text-decoration:none } .btn[aria-disabled="true"] { opacity:.55; pointer-events:none; box-shadow:none }
.btn svg { width:22px; height:22px; flex:none }
.meta { color:var(--muted); font-size:15px }
.others { font-size:15px; display:flex; flex-wrap:wrap; gap:6px 16px; align-items:center } .others span { color:var(--muted) } .others a { color:var(--ink) }
.shot { margin:26px 0 0; } .shot img { width:100%; height:auto; display:block; border-radius:12px; border:1px solid var(--line); box-shadow:var(--shadow) } .shot figcaption { color:var(--muted); font-size:14px; margin-top:10px; text-align:center }
section { padding:44px 0 6px } h2 { font-size:28px; margin:0 0 14px; letter-spacing:-.01em } h3 { font-size:19px; margin:0 0 8px }
.cards { display:grid; grid-template-columns:repeat(auto-fit, minmax(230px, 1fr)); gap:16px }
.card { background:var(--card); border:1px solid var(--line); border-radius:14px; padding:22px 22px 20px } .card p { margin:0; color:var(--muted); font-size:16px }
.steps { display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px } .steps .card ol { margin:8px 0 0; padding-left:22px } .steps .card li { margin:8px 0; font-size:16px } .steps .card li::marker { color:var(--accent); font-weight:600 }
.note { background:var(--soft); border-radius:14px; padding:20px 22px; margin-top:18px } .note p { margin:0 }
details { background:var(--card); border:1px solid var(--line); border-radius:14px; padding:6px 22px; margin-top:14px } summary { cursor:pointer; font-weight:600; padding:12px 0; font-size:18px } details[open] summary { border-bottom:1px solid var(--line); margin-bottom:8px }
code, pre, .fp { font:14px/1.55 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; background:var(--code); border-radius:6px } code { padding:1px 6px } pre { padding:14px 16px; overflow-x:auto; margin:10px 0 } .fp { display:block; padding:12px 14px; word-break:break-all; margin:8px 0 }
footer { margin-top:56px; padding:26px 0 40px; border-top:1px solid var(--line); color:var(--muted); font-size:15px; display:flex; flex-wrap:wrap; gap:8px 22px } footer a { color:inherit } footer .langs { display:flex; flex-wrap:wrap; gap:6px 14px; width:100%; margin-top:4px } footer .langs a[aria-current] { color:var(--ink); font-weight:600; text-decoration:none }
/* guide */
.guide { display:grid; grid-template-columns:220px 1fr; gap:40px; padding-top:28px } @media (max-width: 800px) { .guide { grid-template-columns:1fr } .toc { position:static } }
.toc { position:sticky; top:20px; align-self:start; font-size:15px } .toc strong { display:block; color:var(--muted); font-weight:600; font-size:13px; letter-spacing:.06em; text-transform:uppercase; margin-bottom:8px } .toc a { display:block; color:var(--ink); text-decoration:none; padding:4px 0; opacity:.85 } .toc a:hover { opacity:1; text-decoration:underline }
.doc h1 { font-size:38px } .doc > p.lead { margin-bottom:8px } .doc section { padding:30px 0 0 } .doc section h2 { font-size:25px; scroll-margin-top:18px } .doc p { margin:10px 0 } .doc img { width:100%; height:auto; border-radius:12px; border:1px solid var(--line); box-shadow:var(--shadow); margin:14px 0 } .doc ol { padding-left:22px } .doc li { margin:10px 0 } .doc li::marker { color:var(--accent); font-weight:600 }
.doc table { border-collapse:collapse; margin:10px 0 } .doc td { padding:6px 16px 6px 0; border-bottom:1px solid var(--line) } .doc td:first-child { font:15px ui-monospace, Menlo, monospace; white-space:nowrap }
/* versions */
.releases h1 { font-size:38px } .releases .status { color:var(--muted); font-size:15px; margin:18px 0 0; min-height:1.6em }
.latest { display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:16px } .latest .card h3 { display:flex; align-items:baseline; justify-content:space-between; gap:12px } .latest .card h3 .v { font-weight:500; color:var(--muted); font-size:15px; white-space:nowrap }
.latest .card .when { color:var(--muted); font-size:14px; margin:0 0 10px } .files { display:grid; gap:6px; margin:0; padding:0; list-style:none } .files li { display:flex; justify-content:space-between; gap:12px; font-size:15px } .files a { color:var(--ink); text-decoration:none } .files a:hover { text-decoration:underline } .files .size { color:var(--muted); font-size:14px; white-space:nowrap }
.card .links { margin:12px 0 0; font-size:14px; display:flex; flex-wrap:wrap; gap:4px 14px }
.history { display:grid; gap:30px } .history h3 { margin-bottom:4px } .history table { width:100%; border-collapse:collapse; font-size:15px } .history td { text-align:left; padding:9px 12px 9px 0; border-bottom:1px solid var(--line); vertical-align:top }
.history td.v { font-weight:600; white-space:nowrap } .history td.d { color:var(--muted); white-space:nowrap } .history td .files li { justify-content:flex-start; gap:8px } .history td.n { white-space:nowrap } .history td.n a { margin-right:12px }
@media (max-width: 640px) { .history td.d { display:none } .history td.n { white-space:normal } }
'''

# The download button: the newest release, the installer for this computer first.
JS = r'''
(async () => {
  const REPO = '%(repo)s', S = %(strings)s
  const kinds = [
    { key: 'mac-arm64', test: (n) => /-mac-arm64\.dmg$/.test(n) }, { key: 'mac-x64', test: (n) => /-mac-x64\.dmg$/.test(n) },
    { key: 'win-x64', test: (n) => /-win-x64-setup\.exe$/.test(n) }, { key: 'linux-appimage', test: (n) => /\.AppImage$/.test(n) }, { key: 'linux-deb', test: (n) => /\.deb$/.test(n) },
  ]
  const detect = () => { const ua = navigator.userAgent, plat = (navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || ''
    if (/Windows/i.test(plat) || /Windows/.test(ua)) return 'win-x64'; if (/Mac/i.test(plat) || /Macintosh/.test(ua)) return 'mac-arm64'; if (/Linux/i.test(plat) || /Linux/.test(ua)) return 'linux-appimage'; return null }
  const btn = document.getElementById('dl'), label = document.getElementById('dl-label'), meta = document.getElementById('dl-meta'), others = document.getElementById('dl-others')
  const mb = (b) => (b / 1e6).toFixed(0) + ' MB'
  try {
    const res = await fetch(`https://api.github.com/repos/${REPO}/releases/latest`, { headers: { Accept: 'application/vnd.github+json' } })
    if (res.status === 404) { label.textContent = S.none; meta.textContent = S.noneHint; return }
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    const rel = await res.json()
    const found = kinds.map((k) => ({ ...k, asset: rel.assets.find((a) => k.test(a.name)) })).filter((k) => k.asset)
    const main = found.find((k) => k.key === detect()) || found[0]
    if (!main) { label.textContent = S.none; return }
    btn.href = main.asset.browser_download_url; btn.removeAttribute('aria-disabled')
    label.textContent = S.for.replace('{label}', S.kinds[main.key])
    const date = rel.published_at ? new Date(rel.published_at).toLocaleDateString(S.lang, { year: 'numeric', month: 'long', day: 'numeric' }) : ''
    meta.textContent = `${S.version.replace('{v}', rel.tag_name.replace(/^v/, ''))} · ${mb(main.asset.size)}${date ? ' · ' + date : ''} · ${S.free}`
    const span = document.createElement('span'); span.textContent = S.others; others.appendChild(span)
    for (const k of found) { if (k === main) continue; const a = document.createElement('a'); a.href = k.asset.browser_download_url; a.textContent = `${S.kinds[k.key]} · ${mb(k.asset.size)}`; others.appendChild(a) }
    const sums = rel.assets.find((a) => a.name === 'SHA256SUMS.txt'); if (sums) { const a = document.createElement('a'); a.href = sums.browser_download_url; a.textContent = S.checksums; others.appendChild(a) }
    for (const el of document.querySelectorAll('[data-release-url]')) el.href = rel.html_url
  } catch (e) { label.textContent = S.error; btn.href = 'releases.html'; btn.removeAttribute('aria-disabled'); meta.textContent = S.errorHint.replace('{err}', e.message) }
})()
'''

# The versions page: every published release, read once from the GitHub API. First the newest release
# that has installers for each system — a release can be built for macOS only, so "newest" is per
# system, not the newest tag — then the whole history, grouped by system.
RELEASES_JS = r'''
(async () => {
  const REPO = '%(repo)s', S = %(strings)s
  const KINDS = [
    { key: 'mac-arm64', sys: 'mac', test: (n) => /-mac-arm64\.dmg$/.test(n) }, { key: 'mac-x64', sys: 'mac', test: (n) => /-mac-x64\.dmg$/.test(n) },
    { key: 'win-x64', sys: 'win', test: (n) => /-win-x64-setup\.exe$/.test(n) },
    { key: 'linux-appimage', sys: 'linux', test: (n) => /\.AppImage$/.test(n) }, { key: 'linux-deb', sys: 'linux', test: (n) => /\.deb$/.test(n) },
  ]
  const SYSTEMS = ['mac', 'win', 'linux']
  const status = document.getElementById('status'), latest = document.getElementById('latest'), history = document.getElementById('history')
  const mb = (b) => (b / 1e6).toFixed(0) + ' MB'
  const when = (r) => r.published_at ? new Date(r.published_at).toLocaleDateString(S.lang, { year: 'numeric', month: 'long', day: 'numeric' }) : ''
  const semver = (tag) => tag.replace(/^v/, '').split(/[.-]/).map((p) => (/^\d+$/.test(p) ? Number(p) : p))
  const newer = (a, b) => { const x = semver(a.tag_name), y = semver(b.tag_name); for (let i = 0; i < Math.max(x.length, y.length); i++) { const p = x[i] ?? 0, q = y[i] ?? 0; if (p === q) continue; return typeof p === 'number' && typeof q === 'number' ? q - p : String(q).localeCompare(String(p)) } return 0 }
  const el = (tag, attrs, ...children) => { const n = document.createElement(tag); for (const [k, v] of Object.entries(attrs || {})) { if (k === 'class') n.className = v; else if (k === 'text') n.textContent = v; else n.setAttribute(k, v) } for (const c of children) if (c) n.append(c); return n }
  const files = (r, sys) => { const ul = el('ul', { class: 'files' })
    for (const k of KINDS) { if (k.sys !== sys) continue; const a = r.assets.find((x) => k.test(x.name)); if (!a) continue
      ul.append(el('li', {}, el('a', { href: a.browser_download_url, text: S.kinds[k.key] }), el('span', { class: 'size', text: mb(a.size) }))) }
    return ul }
  const links = (r) => { const p = el('p', { class: 'links' }, el('a', { href: r.html_url, text: S.notes }))
    const sums = r.assets.find((a) => a.name === 'SHA256SUMS.txt'); if (sums) p.append(el('a', { href: sums.browser_download_url, text: S.checksums })); return p }
  try {
    const res = await fetch(`https://api.github.com/repos/${REPO}/releases?per_page=100`, { headers: { Accept: 'application/vnd.github+json' } })
    if (!res.ok) throw new Error(`HTTP ${res.status}`)
    const all = (await res.json()).filter((r) => !r.draft && !r.prerelease).sort(newer)
    const has = (r, sys) => KINDS.some((k) => k.sys === sys && r.assets.some((a) => k.test(a.name)))
    if (!all.length) { status.textContent = S.none; return }
    status.textContent = ''
    for (const sys of SYSTEMS) { const r = all.find((x) => has(x, sys)); if (!r) continue
      latest.append(el('div', { class: 'card' }, el('h3', {}, S.systems[sys], el('span', { class: 'v', text: S.version.replace('{v}', r.tag_name.replace(/^v/, '')) })), el('p', { class: 'when', text: when(r) }), files(r, sys), links(r))) }
    for (const sys of SYSTEMS) { const rows = all.filter((x) => has(x, sys)); if (!rows.length) continue
      const table = el('table'), body = el('tbody'); table.append(body)
      for (const r of rows) body.append(el('tr', {}, el('td', { class: 'v', text: r.tag_name.replace(/^v/, '') }), el('td', { class: 'd', text: when(r) }), el('td', {}, files(r, sys)), el('td', { class: 'n' }, el('a', { href: r.html_url, text: S.notes }), (() => { const s = r.assets.find((a) => a.name === 'SHA256SUMS.txt'); return s ? el('a', { href: s.browser_download_url, text: S.checksums }) : null })())))
      history.append(el('div', {}, el('h3', { text: S.systems[sys] }), table)) }
  } catch (e) { status.textContent = S.error.replace('{err}', e.message) }
})()
'''

# On the English pages only: send a first visit to the browser's language, when the site has it, and
# remember a choice made through the menu (`?lang=`). The `?lang=` half runs on every page (STORE).
REDIRECT = r'''
(() => { try {
  const LANGS = %(langs)s
  const q = new URLSearchParams(location.search).get('lang'); if (q && LANGS.includes(q)) localStorage.setItem('ygd-lang', q)
  const wanted = (navigator.languages || [navigator.language || '']).map((l) => l.toLowerCase().slice(0, 2)).find((l) => LANGS.includes(l))
  const pick = localStorage.getItem('ygd-lang') || wanted || 'en'
  if (pick !== 'en') location.replace(pick + '/' + (location.pathname.split('/').pop() || 'index.html') + location.hash)
} catch (e) {} })()
'''
STORE = r'''
(() => { try { const q = new URLSearchParams(location.search).get('lang'); if (q && %(langs)s.includes(q)) localStorage.setItem('ygd-lang', q) } catch (e) {} })()
'''

DL_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>'
GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'


def shell(t, title, body, page, extra_head=''):
    root = t['root']
    alternates = ''.join(f'\n<link rel="alternate" hreflang="{c}" href="{root}{lang_dir(c)}{page}">' for c in T if c != t['lang'])
    options = ''.join(f'<option value="{root}{lang_dir(c)}{page}?lang={c}"{" selected" if c == t["lang"] else ""}>{name}</option>' for c, name in LANGS.items() if c in T)
    footer_langs = ''.join(f'<a href="{root}{lang_dir(c)}{page}?lang={c}" hreflang="{c}"{" aria-current=\"true\"" if c == t["lang"] else ""}>{name}</a>' for c, name in LANGS.items() if c in T)
    store = '' if t['lang'] == 'en' else f'<script>{STORE % {"langs": json.dumps(list(T))}}</script>'
    return f'''<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{t['desc']}">
<link rel="icon" href="{root}assets/icon.svg" type="image/svg+xml">{alternates}
<link rel="alternate" hreflang="x-default" href="{root}{page}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/site.css">
{extra_head}{store}
</head>
<body>
<div class="wrap">
  <header class="top">
    <a class="brand" href="index.html">{ICON}<span>ygd-editor</span></a>
    <nav>
      <a href="index.html#download"{' aria-current="page"' if page == 'index.html' else ''}>{t['nav_download']}</a>
      <a href="guide.html"{' aria-current="page"' if page == 'guide.html' else ''}>{t['nav_guide']}</a>
      <a href="releases.html"{' aria-current="page"' if page == 'releases.html' else ''}>{t['nav_releases']}</a>
      <a href="https://github.com/{REPO}/issues">{t['nav_issues']}</a>
    </nav>
    <label class="lang">{GLOBE}<select aria-label="{t['lang_label']}" onchange="location.href=this.value">{options}</select></label>
  </header>
{body}
  <footer>
    <span>{t['footer_made']}</span>
    <a href="guide.html">{t['nav_guide']}</a>
    <a href="releases.html">{t['nav_releases']}</a>
    <a href="https://github.com/{REPO}/issues">{t['nav_issues']}</a>
    <div class="langs">{footer_langs}</div>
  </footer>
</div>
</body>
</html>
'''


def index(t):
    root = t['root']
    img = f'{root}assets/img/'
    pem = f'{root}release-signing.pem'
    strings = json.dumps({'lang': t['lang'], 'none': t['dl_none'], 'noneHint': t['dl_none_hint'], 'for': t['dl_for'], 'error': t['dl_error'], 'errorHint': t['dl_error_hint'], 'others': t['dl_others'], 'checksums': t['dl_checksums'], 'free': t['dl_free'], 'version': t['dl_version'], 'kinds': t['kinds']}, ensure_ascii=False)
    cards = ''.join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in t['what'])
    steps = ''.join(f'<div class="card"><h3>{os}</h3><ol>' + ''.join(f'<li>{s}</li>' for s in ss) + '</ol></div>' for os, ss in t['install'])
    body = f'''
  <main>
    <div class="hero" id="download">
      <h1>{t['tagline']}</h1>
      <p class="lead">{t['hero_p']}</p>
      <div class="dl">
        <a id="dl" class="btn" href="releases.html" aria-disabled="true">{DL_ICON}<span id="dl-label">{t['dl_loading']}</span></a>
        <div id="dl-meta" class="meta"></div>
        <div id="dl-others" class="others"></div>
      </div>
      <figure class="shot"><img src="{img}console.png" alt="{t['shot_console']}" width="1440" height="900"><figcaption>{t['shot_console']}</figcaption></figure>
    </div>

    <section id="what"><h2>{t['what_h']}</h2><div class="cards">{cards}</div></section>

    <section id="install"><h2>{t['install_h']}</h2><p class="lead" style="font-size:17px">{t['install_intro']}</p>
      <div class="steps" style="margin-top:18px">{steps}</div>
      <div class="note"><h3>{t['need_h']}</h3><p>{t['need_p']}</p></div>
    </section>

    <section id="updates"><h2>{t['updates_h']}</h2><p>{t['updates_p']}</p></section>

    <section id="guide"><div class="note"><h3>{t['guide_cta_h']}</h3><p>{t['guide_cta_p'].replace('{prefix}', '')}</p></div></section>

    <section id="genuine"><h2>{t['genuine_h']}</h2><p>{t['genuine_p']}</p>
      <details><summary>{t['genuine_h']} — {t['genuine_details']}</summary>
        <p>{t['genuine_prov']}</p>
<pre>cosign verify-blob --bundle SHA256SUMS.txt.sigstore.json \\
  --certificate-identity-regexp '^https://github.com/MHGuitarte/ygd-editor(-app)?/\\.github/workflows/release\\.yml@refs/tags/v' \\
  --certificate-oidc-issuer https://token.actions.githubusercontent.com SHA256SUMS.txt
sha256sum --check --ignore-missing SHA256SUMS.txt   # macOS: shasum -a 256 -c SHA256SUMS.txt</pre>
        <p>{t['genuine_sig'].replace('{pem}', pem)}</p>
        <span class="fp">SHA-256 {FP256}</span>
        <span class="fp">SHA-1 (macOS codesign · Windows thumbprint) {FP1}</span>
<pre># macOS
codesign --verify --deep --strict /Applications/ygd-editor.app &amp;&amp; codesign -dvv /Applications/ygd-editor.app 2&gt;&amp;1 | grep Authority
# Windows (PowerShell)
(Get-AuthenticodeSignature .\\ygd-editor-*-setup.exe).SignerCertificate.Thumbprint</pre>
      </details>
    </section>
  </main>
  <script>{JS % {'repo': REPO, 'strings': strings}}</script>
'''
    return shell(t, t['title_index'], body, 'index.html', redirect_head(t))


def redirect_head(t):
    return f'<script>{REDIRECT % {"langs": json.dumps(list(T))}}</script>' if t['lang'] == 'en' else ''


def guide(t):
    img = f'{t["root"]}assets/img/'
    toc = ''.join(f'<a href="#{sid}">{h}</a>' for sid, h, _ in t['g_sections'])
    secs = ''
    for sid, h, parts in t['g_sections']:
        inner = ''.join(p if p.lstrip().startswith('<') else f'<p>{p}</p>' for p in parts)
        inner = inner.replace('{img}', img).replace('{repo}', REPO).replace('{prefix}', '')
        secs += f'<section id="{sid}"><h2>{h}</h2>{inner}</section>'
    body = f'''
  <main class="guide">
    <aside class="toc"><strong>{t['g_toc']}</strong>{toc}</aside>
    <article class="doc">
      <h1>{t['g_h1']}</h1>
      <p class="lead">{t['g_lead']}</p>
      {secs}
    </article>
  </main>
'''
    return shell(t, t['title_guide'], body, 'guide.html', redirect_head(t))


def releases(t):
    strings = json.dumps({'lang': t['lang'], 'none': t['r_none'], 'error': t['r_error'], 'notes': t['r_notes'], 'checksums': t['r_checksums'], 'version': t['dl_version'], 'kinds': t['kinds'], 'systems': t['r_systems']}, ensure_ascii=False)
    body = f'''
  <main class="releases">
    <div class="hero">
      <h1>{t['r_h1']}</h1>
      <p class="lead">{t['r_lead']}</p>
      <p class="meta"><a href="https://github.com/{REPO}/releases">{t['r_github']}</a></p>
    </div>
    <p id="status" class="status">{t['r_loading']}</p>
    <section id="latest-section"><h2>{t['r_latest_h']}</h2><div id="latest" class="latest"></div></section>
    <section id="history-section"><h2>{t['r_all_h']}</h2><div id="history" class="history"></div>
      <div class="note"><p>{t['r_updates']}</p></div>
    </section>
  </main>
  <script>{RELEASES_JS % {'repo': REPO, 'strings': strings}}</script>
'''
    return shell(t, t['title_releases'], body, 'releases.html', redirect_head(t))


(ROOT / 'assets/site.css').write_text(CSS.strip() + '\n')
built = ['assets/site.css']
for code, t in T.items():
    out = ROOT / lang_dir(code) if code != 'en' else ROOT
    out.mkdir(exist_ok=True)
    for page, render in (('index.html', index), ('guide.html', guide), ('releases.html', releases)):
        (out / page).write_text(render(t))
        built.append(f'{lang_dir(code)}{page}')
print('built:', ' '.join(built))
