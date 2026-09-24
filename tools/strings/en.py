# English. Strings of the download page, the guide and the versions page. HTML fragments and
# {placeholders} stay as they are; keys match tools/strings/en.py, which is the reference.
T = {
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
 'install_intro': 'Your computer will warn you the first time. That is expected: nobody paid Apple or Microsoft for a certificate, and the warning is about the missing paperwork, not about anything the app does. Here is how to get past it — once, and never again for that computer.',
 'install': [
   ('macOS', ['Open the downloaded <code>.dmg</code>. A window shows these steps in your language — click <em>Continue</em> — then drag <strong>ygd-editor</strong> into Applications.', 'Open it. macOS says it <em>could not verify</em> the app and offers <em>Move to Trash</em> or <em>Done</em>: click <strong>Done</strong>.', 'Open <strong>System Settings › Privacy &amp; Security</strong>, scroll down to <em>Security</em> and click <strong>Open Anyway</strong> next to ygd-editor. Confirm with your password. That is it — macOS will not ask again.', 'On macOS 14 or older, <strong>right-click the app › Open</strong> does the same in one step.', 'Not sure which Mac you have? Apple menu › About This Mac: “Apple M…” is Apple Silicon, anything with “Intel” is Intel.']),
   ('Windows', ['Run the installer. When SmartScreen says “Windows protected your PC”, click <strong>More info</strong>, then <strong>Run anyway</strong>.', 'The publisher shown is <em>ygd-editor release signing</em> — that is us. Pick the install folder if you like and finish.', 'The app appears in the Start menu as ygd-editor.']),
   ('Linux', ['<strong>AppImage:</strong> make it executable (<code>chmod +x ygd-editor-*.AppImage</code>) and run it. If it complains about FUSE, run it with <code>--appimage-extract-and-run</code>.', '<strong>Debian / Ubuntu:</strong> <code>sudo apt install ./ygd-editor-*.deb</code>, then find it in your applications menu.']),
 ],
 'cli_h': 'Skip the warning: install from Terminal.',
 'cli_p': 'Paste this into Terminal (Applications › Utilities). It downloads the latest version for your Mac, checks its checksum and that it is signed with the project’s certificate, and puts it in Applications. macOS asks nothing, because nothing came through a browser. Run it again any time to reinstall.',
 'cli_copy': 'Copy', 'cli_copied': 'Copied',
 'cli_or': 'Or, with the disk image from the button above:',
 'need_h': 'What you need', 'need_p': 'Git on your computer and an account with at least one provider. <a href="https://github.com/openai/codex">Codex</a> and <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> are not inside the installer — that is what keeps it small — the app downloads the one you pick the first time you ask for it (about 100 MB for Codex, 20 MB for Gemini CLI) and checks it against the version this release was built with before running it; for <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, whose licence does not allow shipping it, Settings › AI providers offers one click that runs Anthropic’s official installer for you. Connecting a provider opens its sign-in page in your browser. For pull requests, GitHub’s <code>gh</code> or GitLab’s <code>glab</code>.',
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
    '<li><strong>Create a worktree.</strong> <em>New worktree</em> (⌘N) suggests a branch name from the task and a folder to put it in; both are yours to rename to whatever convention you use. Git does not allow spaces in a branch name, so they become dashes and the dialog shows you the result before creating anything. Where worktrees go on disk, and an optional suggested prefix, are Settings › Git.</li>'
    '<li><strong>Start a session.</strong> <em>+ Session</em> in the right panel picks an agent and a model; the default agent is Settings › Default agent. Type what you want in the composer. <code>@</code> attaches files or context such as the current diff, <code>/</code> runs the agent’s commands, <code>#</code> its skills. ⌘↵ sends.</li>'
    '<li><strong>Let it work — or stop it.</strong> The transcript shows every tool the agent uses. When it needs permission for something you have not pre-approved, the session turns to <em>waiting</em>, the header inbox counts it, and you allow or deny — “Always allow” remembers your choice for that worktree. <em>Stop</em> interrupts; prompts you type while it works are queued.</li>'
    '<li><strong>Review the changes.</strong> The Changes tab lists every touched file with who changed it. Click a file for the diff; select lines and choose <em>Explain</em> or <em>Ask to change</em> to send them back to the agent. A warning marks files another worktree of the same repository also touches.</li>'
    '<li><strong>Commit, push, open the PR.</strong> Tick the files to stage, write the message or <em>Draft with AI</em>, <em>Commit</em>. <em>Push</em> sets the upstream; <em>Open pull request</em> fills title, body (drafted from the diff if you want), draft flag, reviewers and labels, and hands off to <code>gh</code> or <code>glab</code>. The worktree card then shows the PR and its checks.</li>'
    '</ol>',
    '<img src="{img}console.png" alt="The console with a diff open and a Claude Code session running" loading="lazy">',
  ]),
  ('daily', 'Day to day', [
    '<p><strong>The main worktree</strong> — the folder you opened the repository at — is listed with the others and is the one new worktrees branch from. Select it and click its branch name in the header: a search box drops down over every branch — yours, or one that only exists on the remote, which it checks out as a new tracking branch. Type to narrow it, arrow keys and Enter to switch. A branch another worktree already holds is listed but greyed out, because git allows a branch in one worktree at a time.</p>'
    '<p><strong>Update from base</strong> on a worktree fetches and rebases it on the base branch; conflicts stop with the files listed, you resolve them, stage and <em>Continue</em>. <strong>Fetch</strong> refreshes ahead/behind counts. The Terminal tab is a real shell in the worktree folder; Activity is the timeline of what happened there — commits, pushes, sessions — and survives restarts.</p>'
    '<p><strong>Handing off.</strong> A session can move to another worktree from its menu, transcript included, when you realise the work belongs on another branch.</p>'
    '<p><strong>Removing a worktree</strong> ends its sessions, archives their logs and forgets its permission rules; the branch stays unless you delete it. Settings › Git can delete the worktree by itself after its PR merges.</p>'
    '<p><strong>Multiple repositories.</strong> Open as many as you like; the header switches between them, and the inbox counts waiting sessions across all of them.</p>',
  ]),
  ('workspaces', 'Working on several repositories: workspaces', [
    'A <em>workspace</em> is a named set of folders the app holds open together. A gateway, a web console and a folder of notes are often one piece of work, and a question about one of them is usually answered in another — a workspace is how you tell the app they belong together.',
    '<img src="{img}workspace.png" alt="A workspace of two repositories: the sidebar groups worktrees by repository" loading="lazy">',
    '<strong>Making one.</strong> Open a second repository while one is already open and the app asks where it goes: add it to what you are working in, start a new workspace with both, or open it on its own. Escape means “on its own”. You can also start one from the start page with <em>New workspace</em>, and add or remove folders later from the workspaces button in the header. Removing a folder from a workspace never deletes anything — only the set changes.',
    '<strong>From VS Code.</strong> If your team already keeps a <code>.code-workspace</code> file, <em>Open workspace file…</em> reads it: the same folders, in the same order, named the way VS Code names them. Comments and trailing commas in the file are fine. Folders that are not git repositories are kept — they just have no worktrees — and a folder that has gone missing is reported rather than quietly dropped. <em>Save to file</em> writes it back, leaving the parts the app does not use untouched, so the same file keeps working in both tools.',
    '<strong>What the sidebar shows.</strong> Worktrees grouped by repository, each group foldable, with the filter matching a branch or a repository name so you can find a branch without remembering where it lives. A folded group still shows what is running inside it, and still says when a session is waiting. One repository shows no groups at all.',
    '<strong>What the agents can see.</strong> A session still runs <em>in</em> its worktree — that is where git and every relative path belong — but it can read the workspace’s other folders too, so “where does this call end up?” can be answered from either side. A session that only reads is still only allowed to read, everywhere. There is also a row above the groups, <em>Across the workspace</em>, for sessions that belong to no single worktree: ask those the questions that span the whole stack. They have no branch, no changes and no terminal, because those belong to a worktree.',
    '<strong>Settings.</strong> Three levels now: Global, the workspace, then a single repository. The default agent, the permission preset and the base branch are usually a property of the stack rather than of each repository in it, so set them once on the workspace; a repository that needs something different still overrides it. The scope selector in Settings picks the level, and a section that is not overriding says where its values are coming from.',
    'The app remembers each workspace separately: come back to one and you land on the repository, worktree and panel layout you left it in.',
  ]),
  ('current', 'Testing a worktree in the default one', [
    'The place to try a change is the repository\'s own folder — the <em>default worktree</em> — because that is where <code>node_modules</code>, <code>.env</code>, the build cache and the running dev server already are. The work happens in the other worktrees. <strong>Make current</strong> brings one of them into the default worktree: its commits, what it has not committed yet and its new files, on top of the default worktree\'s branch. From then on the header says, on every screen, what the default worktree is running — <code>DEFAULT · feat-a + feat-b · 1 edit</code> — and the sidebar tags the <em>default</em> worktree and the <em>current</em> ones.',
    '<img src="{img}current.png" alt="The header strip, open: where the default worktree came from, the two current worktrees and what can be done next" loading="lazy">',
    '<strong>Swap</strong> puts another worktree in its place. <strong>Add</strong> stacks another one on top, to try two changes together; where both touch the same lines the load stops on a conflict in the default worktree, and for each file you keep the default side, take the incoming one, or edit it and mark it resolved — then <em>Continue</em>, or <em>Abort</em> back to what was running before.',
    '<strong>Fixes made while testing go home.</strong> If you — or an agent in the default worktree — fix something while trying a change, <em>Send edits back</em> returns it to the worktree it belongs to, as uncommitted changes there, to review and commit; <em>Undo</em> takes it back until the next step. A file that belongs to several current worktrees, or to none, is asked about rather than guessed. Swap, Add, Refresh and End send the edits back first, so nothing done in the default worktree is lost to them.',
    '<strong>End</strong> gives the default worktree back exactly as it was: its branch, and its own changes, staged and not staged. Every step opens a short preview first — what comes in, what is kept aside, which files would conflict, and anything that stops it right now with the way out. You find them in the <code>···</code> menu of a worktree, on a right-click in the sidebar, in the header strip, and on ⌘⇧D / ⌘⇧E.',
    'Settings › Git can refresh a current worktree by itself when its agent keeps working, and run a command after each load — <code>pnpm install</code> when <code>pnpm-lock.yaml</code> changed, say — in the default worktree\'s terminal, where you see it. Your own <code>git stash</code> is never touched. It needs git 2.40 or newer.',
  ]),
  ('providers', 'Agents and providers', [
    '<p>ygd-editor does not talk to any AI service itself. It runs the command-line tools you already have — <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, <a href="https://github.com/openai/codex">Codex</a>, <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> — with your own accounts, so your usage, billing and data terms are exactly the ones you agreed with those providers.</p>'
    '<p>Settings › AI providers connects each provider with your own account: <em>Connect</em> opens the provider’s sign-in page in your browser, and the card then shows the account, the plan and <em>Switch account</em> / <em>Disconnect</em> / <em>Test connection</em>. Codex and Gemini CLI are downloaded by the app the first time you pick them — the card says the version and the size, shows the progress, and <em>Remove download</em> takes it away again; if you have your own copy installed, the app uses that one. Claude Code’s licence does not allow shipping it, so its card offers <em>Install Claude Code</em>, which runs Anthropic’s official installer in the card’s terminal, into your home folder, without an administrator password. The default agent and model, and the permission preset, can differ per repository.</p>',
  ]),
  ('permissions', 'Permissions', [
    '<p>Agents ask before doing things you have not pre-approved. Settings › Permissions has three presets — <em>strict</em> (read only), <em>balanced</em> (read and edit files, ask for anything else) and <em>yolo</em> (also run commands, use the web and push) — plus individual switches for reading, editing, running commands, web access, pushing and deleting. Whatever the preset, an agent can never delete without asking unless you turn that on.</p>'
    '<p>When a request comes in, <em>Approve</em> and <em>Deny</em> answer once; <em>Always allow</em> remembers that tool for that worktree, and the rule goes away with the worktree.</p>',
  ]),
  ('notifications', 'Notifications, inbox and budget', [
    '<p>Settings › Notifications chooses when the app pings you: when a session is waiting, when one finishes, when pull-request checks change. Notifications only show while the window is not in front, a click on one jumps to the session, and the dock or taskbar badge can count waiting sessions.</p>'
    '<p>The budget bar at the bottom of the left panel is today’s real spend across every session, taken from the agents’ own usage reports. Settings › Budget sets a daily and a per-session limit, a warning threshold, and whether sessions pause when the limit is reached.</p>',
  ]),
  ('settings', 'Settings', [
    '<p>Settings (⌘,) are grouped by topic. Appearance sets theme, accent colour, density and fonts; Language switches the interface between English, Spanish, Italian, Polish, French, German and Turkish. Several sections carry a <em>per repo</em> badge: with a repository selected at the top you can override those for that repository only.</p>'
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
    '<p><strong>macOS says it could not verify the app (Move to Trash / Done).</strong> Click Done, then System Settings › Privacy &amp; Security › scroll to Security › <em>Open Anyway</em>, and confirm with your password. On macOS 14 or older, right-click › Open does it in one step. If it still refuses, in Terminal: <code>xattr -d com.apple.quarantine /Applications/ygd-editor.app</code>. If it says the app is <em>damaged</em>, the download was corrupted: download it again and compare it against <code>SHA256SUMS.txt</code>.</p>'
    '<p><strong>Avoiding the prompt altogether.</strong> Install from Terminal instead: <code>curl -fsSL https://mhguitarte.github.io/ygd-editor/install.sh | bash</code>. It checks the download the way macOS would have and puts the app in Applications; see the download page.</p>'
    '<p><strong>Windows blocks the installer.</strong> SmartScreen › More info › Run anyway. The publisher should read <em>ygd-editor release signing</em>.</p>'
    '<p><strong>The AppImage does not start.</strong> Run it with <code>--appimage-extract-and-run</code>, or install <code>libfuse2</code>.</p>'
    '<p><strong>A provider shows “Not installed”.</strong> Codex and Gemini CLI are downloaded on request: click <em>Download</em> on the card, and if the download fails the card says why (offline, or a file that did not match its checksum and was discarded). For Claude Code, click <em>Install Claude Code</em> on its card; if you installed it yourself, open a terminal, check that <code>claude --version</code> works, then Settings › AI providers › Rescan.</p>'
    '<p><strong>Git errors.</strong> The app explains the usual ones in one sentence — credentials, a remote that moved on, a lock file, a dirty tree, conflicts — and keeps the full output in the worktree terminal.</p>'
    '<p><strong>No update appears.</strong> Check Settings › Notifications › Offer updates, then Check for updates; the app needs to reach github.com.</p>'
    '<p>Anything else: <a href="https://github.com/{repo}/issues">open an issue</a> with what you did, what you expected and what happened.</p>',
  ]),
  ('privacy', 'Privacy and security', [
    '<p>Everything runs on your computer. The app itself connects to the internet for one thing: checking this site’s releases for updates. Agents talk to their providers with your accounts; git talks to your remotes with your credentials. Provider tokens the app keeps are stored in the operating system’s keychain. The interface runs sandboxed, every request that names a path is checked against the repositories you actually opened, and no command is ever built from a shell string.</p>'
    '<p>To check that a download is really ours, see <a href="{prefix}index.html#genuine">Is my download genuine?</a> on the download page.</p>',
  ]),
 ],
 # versions page and small shared strings
 'dl_version': 'version {v}',
 'genuine_details': 'the technical details',
 'lang_label': 'Language',
 'title_releases': 'ygd-editor — all versions',
 'r_h1': 'All versions',
 'r_lead': 'Every version of ygd-editor that has been published. First the newest one for each system, then the whole history, system by system. The download page always offers the newest complete version; this list is for anyone who needs a particular one.',
 'r_latest_h': 'Newest for each system',
 'r_all_h': 'Every version, by system',
 'r_systems': {'mac': 'macOS', 'win': 'Windows', 'linux': 'Linux'},
 'r_loading': 'Loading the versions…',
 'r_error': 'Could not read the list of versions ({err}).',
 'r_github': 'The releases on GitHub',
 'r_none': 'No version published yet.',
 'r_notes': 'What changed',
 'r_checksums': 'Checksums',
 'r_updates': 'Installed apps update themselves to the newest complete version; nothing here needs downloading by hand unless you want a specific one.',
}
