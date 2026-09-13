#!/usr/bin/env python3
"""Generates the site: index.html + guide.html (English) and es/index.html + es/guide.html (Spanish)
from the same structure. Run `python3 tools/build.py` after editing and commit the output."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
REPO = 'MHGuitarte/ygd-editor-releases'
ICON = re.sub(r'\s(width|height)="1024"', '', (ROOT / 'assets/icon.svg').read_text(), count=2)
ICON = re.sub(r'<!--.*?-->', '', ICON, flags=re.S)
FP256 = '46:C5:62:27:2A:5C:22:9E:D7:85:E1:A3:0D:47:2A:A3:5B:CE:AC:F0:7D:E4:D8:A3:49:23:C9:7B:D3:74:C3:AB'
FP1 = '79A40643BDFE500AB6730154B03B336C1809C57C'

T = {
 'en': {
  'lang': 'en', 'other_lang': 'es', 'other_label': 'Español', 'prefix': '', 'other_prefix': 'es/',
  'title_index': 'ygd-editor — download', 'title_guide': 'ygd-editor — user guide',
  'desc': 'ygd-editor: run AI coding agents in separate git worktrees, review their changes and ship them, all from one window. Free for macOS, Windows and Linux.',
  'nav_download': 'Download', 'nav_guide': 'Guide', 'nav_releases': 'All versions', 'nav_issues': 'Report a problem',
  'tagline': 'Give every task its own branch and its own AI agent — and keep an eye on all of them.',
  'hero_p': 'ygd-editor opens each task in its own git worktree, runs a coding agent inside it (Claude Code, Codex or Gemini CLI), and lets you review the changes, commit, push and open the pull request without leaving the window. Free, for macOS, Windows and Linux.',
  'dl_loading': 'Finding the latest version…', 'dl_for': 'Download for {label}', 'dl_none': 'No version published yet', 'dl_none_hint': 'The first release is on its way.',
  'dl_error': 'See all versions', 'dl_error_hint': 'Could not read the latest version ({err}). The releases page has every download.',
  'dl_others': 'Other systems:', 'dl_checksums': 'Checksums', 'dl_free': 'Free · no account needed · updates itself',
  'kinds': {'mac-arm64': 'macOS · Apple Silicon (M1 and later)', 'mac-x64': 'macOS · Intel', 'win-x64': 'Windows', 'linux-appimage': 'Linux · AppImage', 'linux-deb': 'Linux · Debian / Ubuntu'},
  'shot_console': 'The console: worktrees on the left, changes and diff in the middle, the agent session on the right.',
  'what_h': 'What you get',
  'what': [
    ('One worktree per task', 'Every branch gets its own folder, so agents never step on each other and you can switch tasks without stashing anything.'),
    ('Agents where the code is', 'Start Claude Code, Codex or Gemini CLI inside a worktree, watch it work, answer its questions, and hand a session to another worktree when plans change.'),
    ('Review and ship in place', 'Stage files, read the diff, ask the agent to explain or change a selection, commit, push and open the pull request from the same screen.'),
    ('Stays out of your way', 'A single inbox for every session waiting on you, optional desktop notifications, and a daily spend meter with limits you set.'),
  ],
  'install_h': 'Install in a minute',
  'install_intro': 'Your computer will warn you the first time. That is expected: nobody paid Apple or Microsoft for a certificate, and the warning is about the missing paperwork, not about anything the app does. Here is how to get past it once.',
  'install': [
    ('macOS', ['Open the downloaded <code>.dmg</code> and drag <strong>ygd-editor</strong> into Applications.', 'The first time, <strong>right-click the app and choose Open</strong>. If macOS still refuses, go to System Settings › Privacy &amp; Security and click <em>Open Anyway</em>.', 'Not sure which Mac you have? Apple menu › About This Mac: “Apple M…” is Apple Silicon, anything with “Intel” is Intel.']),
    ('Windows', ['Run the installer. When SmartScreen says “Windows protected your PC”, click <strong>More info</strong>, then <strong>Run anyway</strong>.', 'The publisher shown is <em>ygd-editor release signing</em> — that is us. Pick the install folder if you like and finish.', 'The app appears in the Start menu as ygd-editor.']),
    ('Linux', ['<strong>AppImage:</strong> make it executable (<code>chmod +x ygd-editor-*.AppImage</code>) and run it. If it complains about FUSE, run it with <code>--appimage-extract-and-run</code>.', '<strong>Debian / Ubuntu:</strong> <code>sudo apt install ./ygd-editor-*.deb</code>, then find it in your applications menu.']),
  ],
  'need_h': 'What you need', 'need_p': 'Git on your computer, and at least one agent command line installed and signed in with your own account: <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, <a href="https://github.com/openai/codex">Codex</a> or <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a>. For pull requests, GitHub’s <code>gh</code> or GitLab’s <code>glab</code>. The app finds them and tells you what is missing under Settings › AI providers.',
  'updates_h': 'Updates take care of themselves',
  'updates_p': 'Shortly after launch the app checks for a new version, downloads it quietly and offers “Restart to update”. Settings › Notifications also has a “Check for updates” button and, if you prefer, an option to install updates by itself when nothing is running. After an update, the app tells you what version you are on and links to what changed.',
  'genuine_h': 'Is my download genuine?',
  'genuine_p': 'Two independent checks, neither of which relies on trusting a name. You do not need to run them; they are here for the people who want to.',
  'genuine_prov': '<strong>Provenance.</strong> Every version comes with <code>SHA256SUMS.txt</code>, signed through <a href="https://www.sigstore.dev/">Sigstore</a> by the project’s own release workflow. With <code>cosign</code> installed:',
  'genuine_sig': '<strong>Code signature.</strong> The macOS app and the Windows installer are signed with the project’s certificate (<a href="{pem}">public key</a>). Compare the fingerprint, not the name — anyone can name a certificate anything.',
  'guide_cta_h': 'New here?', 'guide_cta_p': 'The <a href="{prefix}guide.html">user guide</a> walks through the first ten minutes: opening a repository, creating a worktree, starting an agent, reviewing and shipping the result.',
  'footer_made': 'Made by Manu Hurtado. The app is free to use; the source code is private.',
  # guide
  'g_h1': 'User guide', 'g_lead': 'Everything you need for the first afternoon with ygd-editor, in plain words. Ten minutes to read, and you can come back to any section from the list.',
  'g_toc': 'On this page',
  'g_sections': [
   ('idea', 'The idea in one minute', [
     'A git <em>worktree</em> is a second folder for the same repository, checked out on another branch. Instead of switching branches in one folder — and stashing, rebuilding and losing your place every time — you keep one folder per task.',
     'ygd-editor is built around that: the left panel lists your worktrees, the middle shows what changed in the one you picked, and the right runs an AI agent inside it. Two agents on two tasks work in two folders and never collide. When one is waiting for an answer, the header inbox tells you.',
     '<img src="{img}start.png" alt="The start page: recent repositories and the start actions" loading="lazy">',
   ]),
   ('first', 'Your first ten minutes', [
     '<ol>'
     '<li><strong>Open a repository.</strong> On the start page choose <em>Open repository</em> and pick a folder that already has git in it, or <em>Clone repository</em> with a GitHub, GitLab or any git URL. Recent repositories stay on the start page.</li>'
     '<li><strong>Create a worktree.</strong> <em>New worktree</em> (⌘N) asks for a branch name — the prefix, base branch and where worktrees go on disk are Settings › Git. The new folder appears in the left panel, based on your main branch.</li>'
     '<li><strong>Start a session.</strong> <em>+ Session</em> in the right panel picks an agent and a model; the default agent is Settings › Default agent. Type what you want in the composer. <code>@</code> attaches files or context such as the current diff, <code>/</code> runs the agent’s commands, <code>#</code> its skills. ⌘↵ sends.</li>'
     '<li><strong>Let it work — or stop it.</strong> The transcript shows every tool the agent uses. When it needs permission for something you have not pre-approved, the session turns to <em>waiting</em>, the header inbox counts it, and you allow or deny — “Always allow” remembers your choice for that worktree. <em>Stop</em> interrupts; prompts you type while it works are queued.</li>'
     '<li><strong>Review the changes.</strong> The Changes tab lists every touched file with who changed it. Click a file for the diff; select lines and choose <em>Explain</em> or <em>Ask to change</em> to send them back to the agent. A warning marks files another worktree of the same repository also touches.</li>'
     '<li><strong>Commit, push, open the PR.</strong> Tick the files to stage, write the message or <em>Draft with AI</em>, <em>Commit</em>. <em>Push</em> sets the upstream; <em>Open pull request</em> fills title, body (drafted from the diff if you want), draft flag, reviewers and labels, and hands off to <code>gh</code> or <code>glab</code>. The worktree card then shows the PR and its checks.</li>'
     '</ol>',
     '<img src="{img}console.png" alt="The console with a diff open and a Claude Code session running" loading="lazy">',
   ]),
   ('daily', 'Day to day', [
     '<p><strong>Update from base</strong> on a worktree fetches and rebases it on the base branch; conflicts stop with the files listed, you resolve them, stage and <em>Continue</em>. <strong>Fetch</strong> refreshes ahead/behind counts. The Terminal tab is a real shell in the worktree folder; Activity is the timeline of what happened there — commits, pushes, sessions — and survives restarts.</p>'
     '<p><strong>Handing off.</strong> A session can move to another worktree from its menu, transcript included, when you realise the work belongs on another branch.</p>'
     '<p><strong>Removing a worktree</strong> ends its sessions, archives their logs and forgets its permission rules; the branch stays unless you delete it. Settings › Git can delete the worktree by itself after its PR merges.</p>'
     '<p><strong>Multiple repositories.</strong> Open as many as you like; the header switches between them, and the inbox counts waiting sessions across all of them.</p>',
   ]),
   ('providers', 'Agents and providers', [
     '<p>ygd-editor does not talk to any AI service itself. It runs the command-line tools you already have — <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, <a href="https://github.com/openai/codex">Codex</a>, <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> — with your own accounts, so your usage, billing and data terms are exactly the ones you agreed with those providers.</p>'
     '<p>Settings › AI providers shows which tools are installed and signed in, with buttons to sign in, sign out or run a short test. If a tool is missing, install it as its documentation says and click <em>Rescan</em>. The default agent and model, and the permission preset, can differ per repository.</p>',
   ]),
   ('permissions', 'Permissions', [
     '<p>Agents ask before doing things you have not pre-approved. Settings › Permissions has three presets — <em>strict</em> (read only), <em>balanced</em> (read and edit files, ask for anything else) and <em>yolo</em> (also run commands, use the web and push) — plus individual switches for reading, editing, running commands, web access, pushing and deleting. Whatever the preset, an agent can never delete without asking unless you turn that on.</p>'
     '<p>When a request comes in, <em>Allow</em> and <em>Deny</em> answer once; <em>Always allow</em> remembers that tool for that worktree, and the rule goes away with the worktree.</p>',
   ]),
   ('notifications', 'Notifications, inbox and budget', [
     '<p>Settings › Notifications chooses when the app pings you: when a session is waiting, when one finishes, when pull-request checks change. Notifications only show while the window is not in front, a click on one jumps to the session, and the dock or taskbar badge can count waiting sessions.</p>'
     '<p>The budget bar at the bottom of the left panel is today’s real spend across every session, taken from the agents’ own usage reports. Settings › Budget sets a daily and a per-session limit, a warning threshold, and whether sessions pause when the limit is reached.</p>',
   ]),
   ('settings', 'Settings', [
     '<p>Settings (⌘,) are grouped by topic. Appearance sets theme, accent colour, density and fonts; Language switches the interface between English and Spanish. Several sections carry a <em>per repo</em> badge: with a repository selected at the top you can override those for that repository only.</p>'
     '<p>Everything saves automatically to <code>settings.json</code> in the app’s folder in your home directory; <em>Open settings.json</em> edits the raw file with validation, and the header shows when it was last written.</p>',
     '<img src="{img}settings.png" alt="Settings › Appearance" loading="lazy">',
   ]),
   ('updates', 'Updates', [
     '<p>Shortly after launch the app checks this site’s releases, downloads a new version in the background and offers <em>Restart to update</em>. Settings › Notifications has the <em>Offer updates</em> switch, a <em>Check for updates</em> button with the time of the last check, and <em>Install updates automatically</em>: with it on, a downloaded update restarts the app by itself after a 15-second countdown you can cancel — only when no session is running or waiting; otherwise it installs when you quit. The first launch after an update says which version you are on and links to what changed.</p>',
   ]),
   ('shortcuts', 'Keyboard shortcuts', [
     '<table><tr><td>⌘O</td><td>Open repository</td></tr><tr><td>⇧⌘C</td><td>Clone repository</td></tr><tr><td>⌘N</td><td>New worktree</td></tr><tr><td>⌘,</td><td>Settings</td></tr><tr><td>⌘↵</td><td>Send the prompt</td></tr></table>'
     '<p>On Windows and Linux read ⌘ as Ctrl. Every shortcut can be changed under Settings › Keyboard shortcuts.</p>',
   ]),
   ('trouble', 'When something goes wrong', [
     '<p><strong>macOS says the app is damaged or cannot be checked.</strong> Right-click › Open once, or allow it under System Settings › Privacy &amp; Security. If it still refuses, in Terminal: <code>xattr -d com.apple.quarantine /Applications/ygd-editor.app</code>.</p>'
     '<p><strong>Windows blocks the installer.</strong> SmartScreen › More info › Run anyway. The publisher should read <em>ygd-editor release signing</em>.</p>'
     '<p><strong>The AppImage does not start.</strong> Run it with <code>--appimage-extract-and-run</code>, or install <code>libfuse2</code>.</p>'
     '<p><strong>“Agent not found”.</strong> The command-line tool is not installed or not on your PATH. Install it, start a terminal, check that <code>claude</code>, <code>codex</code> or <code>gemini</code> runs, then Settings › AI providers › Rescan.</p>'
     '<p><strong>Git errors.</strong> The app explains the usual ones in one sentence — credentials, a remote that moved on, a lock file, a dirty tree, conflicts — and keeps the full output in the worktree terminal.</p>'
     '<p><strong>No update appears.</strong> Check Settings › Notifications › Offer updates, then Check for updates; the app needs to reach github.com.</p>'
     '<p>Anything else: <a href="https://github.com/{repo}/issues">open an issue</a> with what you did, what you expected and what happened.</p>',
   ]),
   ('privacy', 'Privacy and security', [
     '<p>Everything runs on your computer. The app itself connects to the internet for one thing: checking this site’s releases for updates. Agents talk to their providers with your accounts; git talks to your remotes with your credentials. Provider tokens the app keeps are stored in the operating system’s keychain. The interface runs sandboxed, every request that names a path is checked against the repositories you actually opened, and no command is ever built from a shell string.</p>'
     '<p>To check that a download is really ours, see <a href="{prefix}index.html#genuine">Is my download genuine?</a> on the download page.</p>',
   ]),
  ],
 },
 'es': {
  'lang': 'es', 'other_lang': 'en', 'other_label': 'English', 'prefix': '', 'other_prefix': '../',
  'title_index': 'ygd-editor — descarga', 'title_guide': 'ygd-editor — guía de uso',
  'desc': 'ygd-editor: ejecuta agentes de programación con IA en worktrees de git separados, revisa sus cambios y publícalos, todo desde una ventana. Gratis para macOS, Windows y Linux.',
  'nav_download': 'Descargar', 'nav_guide': 'Guía', 'nav_releases': 'Todas las versiones', 'nav_issues': 'Informar de un problema',
  'tagline': 'Dale a cada tarea su propia rama y su propio agente de IA, y tenlos todos a la vista.',
  'hero_p': 'ygd-editor abre cada tarea en su propio worktree de git, ejecuta dentro un agente de programación (Claude Code, Codex o Gemini CLI) y te deja revisar los cambios, hacer commit, push y abrir el pull request sin salir de la ventana. Gratis, para macOS, Windows y Linux.',
  'dl_loading': 'Buscando la última versión…', 'dl_for': 'Descargar para {label}', 'dl_none': 'Aún no hay ninguna versión publicada', 'dl_none_hint': 'La primera está en camino.',
  'dl_error': 'Ver todas las versiones', 'dl_error_hint': 'No se pudo leer la última versión ({err}). En la página de versiones están todas las descargas.',
  'dl_others': 'Otros sistemas:', 'dl_checksums': 'Sumas de verificación', 'dl_free': 'Gratis · sin cuenta · se actualiza solo',
  'kinds': {'mac-arm64': 'macOS · Apple Silicon (M1 y posteriores)', 'mac-x64': 'macOS · Intel', 'win-x64': 'Windows', 'linux-appimage': 'Linux · AppImage', 'linux-deb': 'Linux · Debian / Ubuntu'},
  'shot_console': 'La consola: worktrees a la izquierda, cambios y diff en el centro, la sesión del agente a la derecha.',
  'what_h': 'Qué te llevas',
  'what': [
    ('Un worktree por tarea', 'Cada rama tiene su propia carpeta: los agentes nunca se pisan y cambias de tarea sin guardar nada a medias.'),
    ('Agentes donde está el código', 'Arranca Claude Code, Codex o Gemini CLI dentro de un worktree, mira cómo trabaja, responde a sus preguntas y pasa una sesión a otro worktree si cambian los planes.'),
    ('Revisa y publica sin moverte', 'Prepara archivos, lee el diff, pide al agente que explique o cambie una selección, haz commit, push y abre el pull request desde la misma pantalla.'),
    ('No molesta', 'Una sola bandeja con todas las sesiones que te esperan, notificaciones de escritorio opcionales y un medidor del gasto de hoy con los límites que tú pongas.'),
  ],
  'install_h': 'Instalación en un minuto',
  'install_intro': 'Tu ordenador te avisará la primera vez. Es lo esperado: nadie ha pagado a Apple ni a Microsoft por un certificado, y el aviso habla de ese papeleo, no de lo que hace la aplicación. Así se pasa, una sola vez.',
  'install': [
    ('macOS', ['Abre el <code>.dmg</code> descargado y arrastra <strong>ygd-editor</strong> a Aplicaciones.', 'La primera vez, <strong>haz clic derecho en la aplicación y elige Abrir</strong>. Si macOS sigue negándose, ve a Ajustes del Sistema › Privacidad y seguridad y pulsa <em>Abrir de todos modos</em>.', '¿No sabes qué Mac tienes? Menú Apple › Acerca de este Mac: «Apple M…» es Apple Silicon; si dice «Intel», es Intel.']),
    ('Windows', ['Ejecuta el instalador. Cuando SmartScreen diga «Windows protegió su PC», pulsa <strong>Más información</strong> y después <strong>Ejecutar de todas formas</strong>.', 'El editor que aparece es <em>ygd-editor release signing</em>: somos nosotros. Elige la carpeta si quieres y termina.', 'La aplicación aparece en el menú Inicio como ygd-editor.']),
    ('Linux', ['<strong>AppImage:</strong> hazlo ejecutable (<code>chmod +x ygd-editor-*.AppImage</code>) y ejecútalo. Si se queja de FUSE, lánzalo con <code>--appimage-extract-and-run</code>.', '<strong>Debian / Ubuntu:</strong> <code>sudo apt install ./ygd-editor-*.deb</code> y búscalo en el menú de aplicaciones.']),
  ],
  'need_h': 'Qué necesitas', 'need_p': 'Git en tu ordenador y al menos una herramienta de agente instalada y con sesión iniciada con tu propia cuenta: <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, <a href="https://github.com/openai/codex">Codex</a> o <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a>. Para los pull requests, <code>gh</code> de GitHub o <code>glab</code> de GitLab. La aplicación las encuentra y te dice qué falta en Ajustes › Proveedores de IA.',
  'updates_h': 'Las actualizaciones se cuidan solas',
  'updates_p': 'Poco después de arrancar, la aplicación busca una versión nueva, la descarga en silencio y ofrece «Reiniciar para actualizar». Ajustes › Notificaciones tiene además un botón «Buscar actualizaciones» y, si lo prefieres, una opción para instalarlas por sí sola cuando no hay nada en marcha. Tras actualizar, te dice en qué versión estás y enlaza a lo que ha cambiado.',
  'genuine_h': '¿Mi descarga es auténtica?',
  'genuine_p': 'Dos comprobaciones independientes, y ninguna se basa en confiar en un nombre. No hace falta hacerlas; están aquí para quien quiera.',
  'genuine_prov': '<strong>Procedencia.</strong> Cada versión incluye <code>SHA256SUMS.txt</code>, firmado mediante <a href="https://www.sigstore.dev/">Sigstore</a> por el propio flujo de publicación del proyecto. Con <code>cosign</code> instalado:',
  'genuine_sig': '<strong>Firma de código.</strong> La aplicación de macOS y el instalador de Windows están firmados con el certificado del proyecto (<a href="{pem}">clave pública</a>). Compara la huella, no el nombre: cualquiera puede llamar a un certificado como quiera.',
  'guide_cta_h': '¿Primera vez?', 'guide_cta_p': 'La <a href="{prefix}guide.html">guía de uso</a> recorre los primeros diez minutos: abrir un repositorio, crear un worktree, arrancar un agente, revisar y publicar el resultado.',
  'footer_made': 'Hecho por Manu Hurtado. La aplicación es gratuita; el código fuente es privado.',
  'g_h1': 'Guía de uso', 'g_lead': 'Todo lo necesario para la primera tarde con ygd-editor, en palabras llanas. Diez minutos de lectura, y puedes volver a cualquier sección desde la lista.',
  'g_toc': 'En esta página',
  'g_sections': [
   ('idea', 'La idea en un minuto', [
     'Un <em>worktree</em> de git es una segunda carpeta del mismo repositorio, con otra rama. En vez de cambiar de rama en una sola carpeta —guardando cambios a medias, recompilando y perdiendo el hilo cada vez— tienes una carpeta por tarea.',
     'ygd-editor gira en torno a eso: el panel izquierdo lista tus worktrees, el central muestra qué ha cambiado en el que elijas y el derecho ejecuta dentro un agente de IA. Dos agentes en dos tareas trabajan en dos carpetas y nunca chocan. Cuando uno espera una respuesta, la bandeja de la cabecera te lo dice.',
     '<img src="{img}start.png" alt="La página de inicio: repositorios recientes y acciones para empezar" loading="lazy">',
   ]),
   ('first', 'Tus primeros diez minutos', [
     '<ol>'
     '<li><strong>Abre un repositorio.</strong> En la página de inicio elige <em>Abrir repositorio</em> y escoge una carpeta que ya tenga git, o <em>Clonar repositorio</em> con una URL de GitHub, GitLab o cualquier git. Los recientes se quedan en la página de inicio.</li>'
     '<li><strong>Crea un worktree.</strong> <em>Nuevo worktree</em> (⌘N) pide un nombre de rama; el prefijo, la rama base y dónde van los worktrees en disco están en Ajustes › Git. La carpeta nueva aparece en el panel izquierdo, basada en tu rama principal.</li>'
     '<li><strong>Arranca una sesión.</strong> <em>+ Sesión</em> en el panel derecho elige agente y modelo; el agente por defecto está en Ajustes › Agente por defecto. Escribe lo que quieres en el compositor. <code>@</code> adjunta archivos o contexto como el diff actual, <code>/</code> ejecuta comandos del agente, <code>#</code> sus skills. ⌘↵ envía.</li>'
     '<li><strong>Déjalo trabajar, o páralo.</strong> La transcripción muestra cada herramienta que usa el agente. Cuando necesita permiso para algo que no has aprobado de antemano, la sesión pasa a <em>esperando</em>, la bandeja de la cabecera la cuenta y tú permites o deniegas; «Permitir siempre» recuerda tu decisión para ese worktree. <em>Detener</em> interrumpe; lo que escribas mientras trabaja se pone en cola.</li>'
     '<li><strong>Revisa los cambios.</strong> La pestaña Cambios lista cada archivo tocado y quién lo cambió. Pulsa uno para ver el diff; selecciona líneas y elige <em>Explicar</em> o <em>Pedir un cambio</em> para devolvérselas al agente. Un aviso marca los archivos que otro worktree del mismo repositorio también toca.</li>'
     '<li><strong>Commit, push y abre el PR.</strong> Marca los archivos a preparar, escribe el mensaje o <em>Redactar con IA</em>, <em>Commit</em>. <em>Push</em> configura el upstream; <em>Abrir pull request</em> rellena título, cuerpo (redactado a partir del diff si quieres), borrador, revisores y etiquetas, y se lo pasa a <code>gh</code> o <code>glab</code>. La tarjeta del worktree muestra entonces el PR y sus checks.</li>'
     '</ol>',
     '<img src="{img}console.png" alt="La consola con un diff abierto y una sesión de Claude Code en marcha" loading="lazy">',
   ]),
   ('daily', 'En el día a día', [
     '<p><strong>Actualizar desde la base</strong> en un worktree hace fetch y rebase sobre la rama base; los conflictos se detienen con los archivos listados, los resuelves, preparas y <em>Continuar</em>. <strong>Fetch</strong> refresca los contadores de adelante/atrás. La pestaña Terminal es una shell real en la carpeta del worktree; Actividad es la línea de tiempo de lo que pasó allí —commits, pushes, sesiones— y sobrevive a los reinicios.</p>'
     '<p><strong>Pasar una sesión.</strong> Una sesión puede moverse a otro worktree desde su menú, transcripción incluida, cuando te das cuenta de que el trabajo va en otra rama.</p>'
     '<p><strong>Eliminar un worktree</strong> termina sus sesiones, archiva sus registros y olvida sus reglas de permisos; la rama se queda salvo que la borres. Ajustes › Git puede borrar el worktree por sí solo cuando su PR se fusiona.</p>'
     '<p><strong>Varios repositorios.</strong> Abre los que quieras; la cabecera cambia entre ellos y la bandeja cuenta las sesiones en espera de todos.</p>',
   ]),
   ('providers', 'Agentes y proveedores', [
     '<p>ygd-editor no habla con ningún servicio de IA por sí mismo. Ejecuta las herramientas de línea de comandos que ya tienes —<a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, <a href="https://github.com/openai/codex">Codex</a>, <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a>— con tus propias cuentas, así que el uso, la facturación y las condiciones de datos son exactamente las que acordaste con esos proveedores.</p>'
     '<p>Ajustes › Proveedores de IA muestra qué herramientas están instaladas y con sesión iniciada, con botones para iniciar sesión, cerrarla o hacer una prueba corta. Si falta una, instálala como dice su documentación y pulsa <em>Volver a buscar</em>. El agente y modelo por defecto, y el preajuste de permisos, pueden ser distintos por repositorio.</p>',
   ]),
   ('permissions', 'Permisos', [
     '<p>Los agentes preguntan antes de hacer lo que no hayas aprobado de antemano. Ajustes › Permisos tiene tres preajustes —<em>estricto</em> (solo lectura), <em>equilibrado</em> (leer y editar archivos, preguntar para lo demás) y <em>yolo</em> (también ejecutar comandos, usar la web y hacer push)— más interruptores individuales para leer, editar, ejecutar comandos, acceso web, push y borrado. Sea cual sea el preajuste, un agente nunca borra sin preguntar salvo que lo actives.</p>'
     '<p>Cuando llega una petición, <em>Permitir</em> y <em>Denegar</em> responden una vez; <em>Permitir siempre</em> recuerda esa herramienta para ese worktree, y la regla desaparece con él.</p>',
   ]),
   ('notifications', 'Notificaciones, bandeja y presupuesto', [
     '<p>Ajustes › Notificaciones elige cuándo te avisa la aplicación: cuando una sesión espera, cuando una termina, cuando cambian los checks de un pull request. Las notificaciones solo aparecen con la ventana en segundo plano, un clic en una salta a la sesión, y la insignia del dock o la barra de tareas puede contar las sesiones en espera.</p>'
     '<p>La barra de presupuesto al pie del panel izquierdo es el gasto real de hoy en todas las sesiones, tomado de los informes de uso de los propios agentes. Ajustes › Presupuesto fija un límite diario y otro por sesión, un umbral de aviso y si las sesiones se pausan al llegar al límite.</p>',
   ]),
   ('settings', 'Ajustes', [
     '<p>Los Ajustes (⌘,) están agrupados por tema. Apariencia fija tema, color de acento, densidad y tipografías; Idioma cambia la interfaz entre inglés y español. Varias secciones llevan la etiqueta <em>por repo</em>: con un repositorio seleccionado arriba puedes sobrescribirlas solo para ese repositorio.</p>'
     '<p>Todo se guarda automáticamente en <code>settings.json</code>, en la carpeta de la aplicación dentro de tu directorio personal; <em>Abrir settings.json</em> edita el archivo en bruto con validación, y la cabecera muestra cuándo se escribió por última vez.</p>',
     '<img src="{img}settings.png" alt="Ajustes › Apariencia" loading="lazy">',
   ]),
   ('updates', 'Actualizaciones', [
     '<p>Poco después de arrancar, la aplicación consulta las versiones de este sitio, descarga la nueva en segundo plano y ofrece <em>Reiniciar para actualizar</em>. Ajustes › Notificaciones tiene el interruptor <em>Ofrecer actualizaciones</em>, un botón <em>Buscar actualizaciones</em> con la hora de la última comprobación e <em>Instalar actualizaciones automáticamente</em>: activado, una actualización descargada reinicia la aplicación por sí sola tras una cuenta atrás de 15 segundos que puedes cancelar, y solo cuando ninguna sesión está en marcha o esperando; si no, se instala al salir. El primer arranque tras actualizar dice en qué versión estás y enlaza a lo que ha cambiado.</p>',
   ]),
   ('shortcuts', 'Atajos de teclado', [
     '<table><tr><td>⌘O</td><td>Abrir repositorio</td></tr><tr><td>⇧⌘C</td><td>Clonar repositorio</td></tr><tr><td>⌘N</td><td>Nuevo worktree</td></tr><tr><td>⌘,</td><td>Ajustes</td></tr><tr><td>⌘↵</td><td>Enviar el mensaje</td></tr></table>'
     '<p>En Windows y Linux, lee ⌘ como Ctrl. Todos los atajos se cambian en Ajustes › Atajos de teclado.</p>',
   ]),
   ('trouble', 'Cuando algo falla', [
     '<p><strong>macOS dice que la aplicación está dañada o no se puede comprobar.</strong> Clic derecho › Abrir una vez, o permítela en Ajustes del Sistema › Privacidad y seguridad. Si sigue negándose, en Terminal: <code>xattr -d com.apple.quarantine /Applications/ygd-editor.app</code>.</p>'
     '<p><strong>Windows bloquea el instalador.</strong> SmartScreen › Más información › Ejecutar de todas formas. El editor debe ser <em>ygd-editor release signing</em>.</p>'
     '<p><strong>El AppImage no arranca.</strong> Ejecútalo con <code>--appimage-extract-and-run</code> o instala <code>libfuse2</code>.</p>'
     '<p><strong>«Agente no encontrado».</strong> La herramienta de línea de comandos no está instalada o no está en tu PATH. Instálala, abre una terminal, comprueba que <code>claude</code>, <code>codex</code> o <code>gemini</code> arranca y luego Ajustes › Proveedores de IA › Volver a buscar.</p>'
     '<p><strong>Errores de git.</strong> La aplicación explica los habituales en una frase —credenciales, un remoto que avanzó, un archivo de bloqueo, un árbol con cambios, conflictos— y guarda la salida completa en el terminal del worktree.</p>'
     '<p><strong>No aparece ninguna actualización.</strong> Revisa Ajustes › Notificaciones › Ofrecer actualizaciones y pulsa Buscar actualizaciones; la aplicación necesita llegar a github.com.</p>'
     '<p>Cualquier otra cosa: <a href="https://github.com/{repo}/issues">abre un issue</a> contando qué hiciste, qué esperabas y qué pasó.</p>',
   ]),
   ('privacy', 'Privacidad y seguridad', [
     '<p>Todo se ejecuta en tu ordenador. La aplicación en sí se conecta a internet para una sola cosa: consultar las versiones de este sitio en busca de actualizaciones. Los agentes hablan con sus proveedores con tus cuentas; git habla con tus remotos con tus credenciales. Los tokens de proveedor que la aplicación guarda van al llavero del sistema operativo. La interfaz corre en una caja de arena, cada petición que nombra una ruta se comprueba contra los repositorios que realmente abriste, y ningún comando se construye jamás a partir de una cadena de shell.</p>'
     '<p>Para comprobar que una descarga es realmente nuestra, mira <a href="{prefix}index.html#genuine">¿Mi descarga es auténtica?</a> en la página de descarga.</p>',
   ]),
  ],
 },
}

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
.top nav a { color:var(--ink); text-decoration:none; opacity:.85 } .top nav a:hover { opacity:1; text-decoration:underline }
.lang { font-size:14px; border:1px solid var(--line); border-radius:999px; padding:5px 12px; text-decoration:none; color:var(--ink); background:var(--card) }
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
footer { margin-top:56px; padding:26px 0 40px; border-top:1px solid var(--line); color:var(--muted); font-size:15px; display:flex; flex-wrap:wrap; gap:8px 22px } footer a { color:inherit }
/* guide */
.guide { display:grid; grid-template-columns:220px 1fr; gap:40px; padding-top:28px } @media (max-width: 800px) { .guide { grid-template-columns:1fr } .toc { position:static } }
.toc { position:sticky; top:20px; align-self:start; font-size:15px } .toc strong { display:block; color:var(--muted); font-weight:600; font-size:13px; letter-spacing:.06em; text-transform:uppercase; margin-bottom:8px } .toc a { display:block; color:var(--ink); text-decoration:none; padding:4px 0; opacity:.85 } .toc a:hover { opacity:1; text-decoration:underline }
.doc h1 { font-size:38px } .doc > p.lead { margin-bottom:8px } .doc section { padding:30px 0 0 } .doc section h2 { font-size:25px; scroll-margin-top:18px } .doc p { margin:10px 0 } .doc img { width:100%; height:auto; border-radius:12px; border:1px solid var(--line); box-shadow:var(--shadow); margin:14px 0 } .doc ol { padding-left:22px } .doc li { margin:10px 0 } .doc li::marker { color:var(--accent); font-weight:600 }
.doc table { border-collapse:collapse; margin:10px 0 } .doc td { padding:6px 16px 6px 0; border-bottom:1px solid var(--line) } .doc td:first-child { font:15px ui-monospace, Menlo, monospace; white-space:nowrap }
'''

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
    meta.textContent = `${rel.tag_name.replace(/^v/, S.lang === 'es' ? 'versión ' : 'version ')} · ${mb(main.asset.size)}${date ? ' · ' + date : ''} · ${S.free}`
    const span = document.createElement('span'); span.textContent = S.others; others.appendChild(span)
    for (const k of found) { if (k === main) continue; const a = document.createElement('a'); a.href = k.asset.browser_download_url; a.textContent = S.kinds[k.key]; others.appendChild(a) }
    const sums = rel.assets.find((a) => a.name === 'SHA256SUMS.txt'); if (sums) { const a = document.createElement('a'); a.href = sums.browser_download_url; a.textContent = S.checksums; others.appendChild(a) }
    for (const el of document.querySelectorAll('[data-release-url]')) el.href = rel.html_url
  } catch (e) { label.textContent = S.error; btn.href = `https://github.com/${REPO}/releases`; btn.removeAttribute('aria-disabled'); meta.textContent = S.errorHint.replace('{err}', e.message) }
})()
'''

REDIRECT = r'''
(() => { try {
  const q = new URLSearchParams(location.search).get('lang'); if (q) { localStorage.setItem('ygd-lang', q) }
  const pick = localStorage.getItem('ygd-lang') || ((navigator.language || '').toLowerCase().startsWith('es') ? 'es' : 'en')
  if (pick === 'es' && !location.pathname.includes('/es/')) location.replace('es/' + location.pathname.split('/').pop().replace(/^$/, 'index.html') + location.hash)
} catch (e) {} })()
'''

DL_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>'

def shell(t, title, body, page, extra_head=''):
    prefix = t['prefix']; other = t['other_prefix']
    asset = '../assets/' if t['lang'] == 'es' else 'assets/'
    return f'''<!doctype html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{t['desc']}">
<link rel="icon" href="{asset}icon.svg" type="image/svg+xml">
<link rel="alternate" hreflang="{t['other_lang']}" href="{other}{page}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{asset}site.css">
{extra_head}
</head>
<body>
<div class="wrap">
  <header class="top">
    <a class="brand" href="{prefix}index.html">{ICON}<span>ygd-editor</span></a>
    <nav>
      <a href="{prefix}index.html#download">{t['nav_download']}</a>
      <a href="{prefix}guide.html">{t['nav_guide']}</a>
      <a href="https://github.com/{REPO}/releases">{t['nav_releases']}</a>
      <a href="https://github.com/{REPO}/issues">{t['nav_issues']}</a>
    </nav>
    <a class="lang" href="{other}{page}?lang={t['other_lang']}" hreflang="{t['other_lang']}">{t['other_label']}</a>
  </header>
{body}
  <footer>
    <span>{t['footer_made']}</span>
    <a href="{prefix}guide.html">{t['nav_guide']}</a>
    <a href="https://github.com/{REPO}/releases">{t['nav_releases']}</a>
    <a href="https://github.com/{REPO}/issues">{t['nav_issues']}</a>
    <a href="{other}{page}?lang={t['other_lang']}">{t['other_label']}</a>
  </footer>
</div>
</body>
</html>
'''

def index(t):
    img = '../assets/img/' if t['lang'] == 'es' else 'assets/img/'
    pem = '../release-signing.pem' if t['lang'] == 'es' else 'release-signing.pem'
    import json
    strings = json.dumps({'lang': t['lang'], 'none': t['dl_none'], 'noneHint': t['dl_none_hint'], 'for': t['dl_for'], 'error': t['dl_error'], 'errorHint': t['dl_error_hint'], 'others': t['dl_others'], 'checksums': t['dl_checksums'], 'free': t['dl_free'], 'kinds': t['kinds']}, ensure_ascii=False)
    cards = ''.join(f'<div class="card"><h3>{h}</h3><p>{p}</p></div>' for h, p in t['what'])
    steps = ''.join(f'<div class="card"><h3>{os}</h3><ol>' + ''.join(f'<li>{s}</li>' for s in ss) + '</ol></div>' for os, ss in t['install'])
    body = f'''
  <main>
    <div class="hero" id="download">
      <h1>{t['tagline']}</h1>
      <p class="lead">{t['hero_p']}</p>
      <div class="dl">
        <a id="dl" class="btn" href="https://github.com/{REPO}/releases" aria-disabled="true">{DL_ICON}<span id="dl-label">{t['dl_loading']}</span></a>
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

    <section id="guide"><div class="note"><h3>{t['guide_cta_h']}</h3><p>{t['guide_cta_p'].replace('{prefix}', t['prefix'])}</p></div></section>

    <section id="genuine"><h2>{t['genuine_h']}</h2><p>{t['genuine_p']}</p>
      <details><summary>{t['genuine_h']} — {'the technical details' if t['lang']=='en' else 'los detalles técnicos'}</summary>
        <p>{t['genuine_prov']}</p>
<pre>cosign verify-blob --bundle SHA256SUMS.txt.sigstore.json \\
  --certificate-identity-regexp '^https://github.com/MHGuitarte/ygd-editor/\\.github/workflows/release\\.yml@refs/tags/v' \\
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
    head = f'<script>{REDIRECT}</script>' if t['lang'] == 'en' else ''
    return shell(t, t['title_index'], body, 'index.html', head)

def guide(t):
    img = '../assets/img/' if t['lang'] == 'es' else 'assets/img/'
    toc = ''.join(f'<a href="#{sid}">{h}</a>' for sid, h, _ in t['g_sections'])
    secs = ''
    for sid, h, parts in t['g_sections']:
        inner = ''.join(p if p.lstrip().startswith('<') else f'<p>{p}</p>' for p in parts)
        inner = inner.replace('{img}', img).replace('{repo}', REPO).replace('{prefix}', t['prefix'])
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
    return shell(t, t['title_guide'], body, 'guide.html')

(ROOT / 'assets/site.css').write_text(CSS.strip() + '\n')
(ROOT / 'index.html').write_text(index(T['en']))
(ROOT / 'guide.html').write_text(guide(T['en']))
(ROOT / 'es').mkdir(exist_ok=True)
(ROOT / 'es/index.html').write_text(index(T['es']))
(ROOT / 'es/guide.html').write_text(guide(T['es']))
print('built: index.html guide.html es/index.html es/guide.html assets/site.css')
