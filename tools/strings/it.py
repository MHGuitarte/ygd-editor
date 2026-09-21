# Italiano. Strings of the download page, the guide and the versions page. HTML fragments and
# {placeholders} stay as they are; keys match tools/strings/en.py, which is the reference.
T = {
 'title_index': 'ygd-editor — download', 'title_guide': 'ygd-editor — guida per l’utente',
 'desc': 'ygd-editor: esegui agenti di programmazione con IA in worktree git separati, rivedi le loro modifiche e pubblicale, tutto da una sola finestra. Gratis per macOS, Windows e Linux.',
 'nav_download': 'Scarica', 'nav_guide': 'Guida', 'nav_releases': 'Tutte le versioni', 'nav_issues': 'Segnala un problema',
 'tagline': 'Dai a ogni compito il suo branch e il suo agente di IA, e tienili tutti sotto controllo.',
 'hero_p': 'ygd-editor apre ogni compito nel suo worktree git, ci esegue dentro un agente di programmazione (Claude Code, Codex o Gemini CLI) e ti lascia rivedere le modifiche, fare commit, push e aprire la pull request senza uscire dalla finestra. Gratis, per macOS, Windows e Linux.',
 'dl_loading': 'Ricerca dell’ultima versione…', 'dl_for': 'Scarica per {label}', 'dl_none': 'Ancora nessuna versione pubblicata', 'dl_none_hint': 'La prima è in arrivo.',
 'dl_error': 'Vedi tutte le versioni', 'dl_error_hint': 'Non è stato possibile leggere l’ultima versione ({err}). Nella pagina delle versioni ci sono tutti i download.',
 'dl_others': 'Altri sistemi:', 'dl_checksums': 'Checksum', 'dl_free': 'Gratis · senza account · si aggiorna da solo',
 'kinds': {'mac-arm64': 'macOS · Apple Silicon (M1 e successivi)', 'mac-x64': 'macOS · Intel', 'win-x64': 'Windows', 'linux-appimage': 'Linux · AppImage', 'linux-deb': 'Linux · Debian / Ubuntu'},
 'shot_console': 'La console: i worktree a sinistra, modifiche e diff al centro, la sessione dell’agente a destra.',
 'what_h': 'Cosa ottieni',
 'what': [
   ('Un worktree per compito', 'Ogni branch ha la sua cartella: gli agenti non si pestano mai i piedi e cambi compito senza mettere niente nello stash.'),
   ('Gli agenti dove sta il codice', 'Avvia Claude Code, Codex o Gemini CLI dentro un worktree, guardalo lavorare, rispondi alle sue domande e passa una sessione a un altro worktree se i piani cambiano.'),
   ('Rivedi e pubblica sul posto', 'Metti i file in stage, leggi il diff, chiedi all’agente di spiegare o modificare una selezione, fai commit, push e apri la pull request dalla stessa schermata.'),
   ('Non ti intralcia', 'Una sola casella per tutte le sessioni che aspettano te, notifiche desktop facoltative e un contatore della spesa di oggi con i limiti che decidi tu.'),
 ],
 'install_h': 'Installazione in un minuto',
 'install_intro': 'Il tuo computer ti avviserà la prima volta. È normale: nessuno ha pagato Apple o Microsoft per un certificato, e l’avviso riguarda quella pratica mancante, non ciò che fa l’app. Ecco come superarlo: una volta sola, e mai più su quel computer.',
 'install': [
   ('macOS', ['Apri il <code>.dmg</code> scaricato. Una finestra mostra questi passaggi nella tua lingua — fai clic su <em>Continua</em> — poi trascina <strong>ygd-editor</strong> in Applicazioni.', 'Aprila. macOS dice che <em>non è stato possibile verificare</em> l’app e offre <em>Sposta nel Cestino</em> o <em>Fine</em>: fai clic su <strong>Fine</strong>.', 'Apri <strong>Impostazioni di Sistema › Privacy e sicurezza</strong>, scorri fino a <em>Sicurezza</em> e fai clic su <strong>Apri comunque</strong> accanto a ygd-editor. Conferma con la tua password. Fatto: macOS non lo chiederà più.', 'Su macOS 14 o precedente, <strong>clic destro sull’app › Apri</strong> fa lo stesso in un passaggio.', 'Non sai che Mac hai? Menu Apple › Informazioni su questo Mac: «Apple M…» è Apple Silicon, se c’è scritto «Intel» è Intel.']),
   ('Windows', ['Esegui l’installer. Quando SmartScreen dice «PC protetto da Windows», fai clic su <strong>Ulteriori informazioni</strong> e poi su <strong>Esegui comunque</strong>.', 'L’autore indicato è <em>ygd-editor release signing</em>: siamo noi. Scegli la cartella di installazione se vuoi e concludi.', 'L’app compare nel menu Start come ygd-editor.']),
   ('Linux', ['<strong>AppImage:</strong> rendilo eseguibile (<code>chmod +x ygd-editor-*.AppImage</code>) ed eseguilo. Se si lamenta di FUSE, avvialo con <code>--appimage-extract-and-run</code>.', '<strong>Debian / Ubuntu:</strong> <code>sudo apt install ./ygd-editor-*.deb</code>, poi cercalo nel menu delle applicazioni.']),
 ],
 'need_h': 'Cosa ti serve', 'need_p': 'Git sul tuo computer e un account presso almeno un provider. <a href="https://github.com/openai/codex">Codex</a> e <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> sono inclusi nell’app, niente da installare; per <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, la cui licenza non ne consente la distribuzione, Impostazioni › Provider di IA offre un clic che esegue per te l’installer ufficiale di Anthropic. Collegare un provider apre la sua pagina di accesso nel browser. Per le pull request, <code>gh</code> di GitHub o <code>glab</code> di GitLab.',
 'updates_h': 'Gli aggiornamenti si gestiscono da soli',
 'updates_p': 'Poco dopo l’avvio l’app cerca una nuova versione, la scarica in silenzio e propone «Riavvia per aggiornare». Impostazioni › Notifiche ha anche un pulsante «Cerca aggiornamenti» e, se preferisci, un’opzione per installare gli aggiornamenti da sola quando non c’è niente in corso. Dopo un aggiornamento, l’app ti dice che versione hai e rimanda a cosa è cambiato.',
 'genuine_h': 'Il mio download è autentico?',
 'genuine_p': 'Due verifiche indipendenti, e nessuna delle due si basa sulla fiducia in un nome. Non sei obbligato a farle; sono qui per chi vuole.',
 'genuine_prov': '<strong>Provenienza.</strong> Ogni versione arriva con <code>SHA256SUMS.txt</code>, firmato tramite <a href="https://www.sigstore.dev/">Sigstore</a> dal flusso di rilascio del progetto stesso. Con <code>cosign</code> installato:',
 'genuine_sig': '<strong>Firma del codice.</strong> L’app per macOS e l’installer per Windows sono firmati con il certificato del progetto (<a href="{pem}">chiave pubblica</a>). Confronta l’impronta, non il nome: chiunque può chiamare un certificato come vuole.',
 'guide_cta_h': 'Prima volta qui?', 'guide_cta_p': 'La <a href="{prefix}guide.html">guida per l’utente</a> ripercorre i primi dieci minuti: aprire un repository, creare un worktree, avviare un agente, rivedere e pubblicare il risultato.',
 'footer_made': 'Fatto da Manu Hurtado. L’app è gratuita; il codice sorgente è privato.',
 # guide
 'g_h1': 'Guida per l’utente', 'g_lead': 'Tutto quello che ti serve per il primo pomeriggio con ygd-editor, in parole semplici. Dieci minuti di lettura, e puoi tornare a qualsiasi sezione dall’elenco.',
 'g_toc': 'In questa pagina',
 'g_sections': [
  ('idea', 'L’idea in un minuto', [
    'Un <em>worktree</em> di git è una seconda cartella dello stesso repository, con il checkout di un altro branch. Invece di cambiare branch in un’unica cartella — e ogni volta mettere le modifiche nello stash, ricompilare e perdere il filo — tieni una cartella per compito.',
    'ygd-editor è costruito intorno a questo: il pannello di sinistra elenca i tuoi worktree, quello centrale mostra cosa è cambiato in quello che hai scelto e quello di destra ci esegue dentro un agente di IA. Due agenti su due compiti lavorano in due cartelle e non si scontrano mai. Quando uno aspetta una risposta, la casella delle attese nell’intestazione te lo dice.',
    '<img src="{img}start.png" alt="La pagina iniziale: repository recenti e le azioni per cominciare" loading="lazy">',
  ]),
  ('first', 'I tuoi primi dieci minuti', [
    '<ol>'
    '<li><strong>Apri un repository.</strong> Nella pagina iniziale scegli <em>Apri repository</em> e indica una cartella che ha già git dentro, oppure <em>Clona repository</em> con un URL di GitHub, GitLab o di qualsiasi git. I repository recenti restano nella pagina iniziale.</li>'
    '<li><strong>Crea un worktree.</strong> <em>Nuovo worktree</em> (⌘N) suggerisce un nome di branch a partire dal compito e una cartella dove metterlo; entrambi sono tuoi da rinominare secondo la convenzione che usi. Git non ammette spazi nel nome di un branch, quindi diventano trattini e la finestra ti mostra il risultato prima di creare qualcosa. Dove finiscono i worktree su disco, e un prefisso suggerito facoltativo, stanno in Impostazioni › Git.</li>'
    '<li><strong>Avvia una sessione.</strong> <em>+ Sessione</em> nel pannello di destra sceglie un agente e un modello; l’agente predefinito è in Impostazioni › Agente predefinito. Scrivi quello che vuoi nel compositore. <code>@</code> allega file o contesto come il diff attuale, <code>/</code> esegue i comandi dell’agente, <code>#</code> le sue skill. ⌘↵ invia.</li>'
    '<li><strong>Lascialo lavorare — o fermalo.</strong> La trascrizione mostra ogni strumento che l’agente usa. Quando ha bisogno di un permesso per qualcosa che non hai approvato in anticipo, la sessione passa a <em>in attesa</em>, la casella delle attese nell’intestazione la conta e tu consenti o neghi; «Consenti sempre» ricorda la tua scelta per quel worktree. <em>Ferma</em> interrompe; i messaggi che scrivi mentre lavora vanno in coda.</li>'
    '<li><strong>Rivedi le modifiche.</strong> La scheda Modifiche elenca ogni file toccato e chi lo ha cambiato. Fai clic su un file per il diff; seleziona delle righe e scegli <em>Spiega</em> o <em>Chiedi una modifica</em> per rimandarle all’agente. Un avviso segnala i file che anche un altro worktree dello stesso repository sta toccando.</li>'
    '<li><strong>Commit, push, apri la PR.</strong> Spunta i file da mettere in stage, scrivi il messaggio o <em>Scrivi con l’IA</em>, <em>Commit</em>. <em>Push</em> imposta l’upstream; <em>Apri pull request</em> compila titolo, descrizione (scritta a partire dal diff, se vuoi), bozza, revisori ed etichette, e passa la mano a <code>gh</code> o <code>glab</code>. Il riquadro del worktree mostra poi la PR e i suoi controlli.</li>'
    '</ol>',
    '<img src="{img}console.png" alt="La console con un diff aperto e una sessione di Claude Code in corso" loading="lazy">',
  ]),
  ('daily', 'Nell’uso quotidiano', [
    '<p><strong>Il worktree principale</strong> — la cartella con cui hai aperto il repository — è elencato insieme agli altri ed è quello da cui si diramano i nuovi worktree. Selezionalo e fai clic sul nome del suo branch nell’intestazione: si apre una casella di ricerca su tutti i branch — i tuoi, o uno che esiste solo sul remoto, di cui fa il checkout come nuovo branch di tracciamento. Scrivi per restringere, frecce e Invio per cambiare. Un branch che un altro worktree ha già è elencato ma in grigio, perché git permette un branch in un solo worktree alla volta.</p>'
    '<p><strong>Aggiorna dalla base</strong> su un worktree fa fetch e rebase sul branch di base; i conflitti fermano tutto con l’elenco dei file, li risolvi, li metti in stage e <em>Continua</em>. <strong>Fetch</strong> aggiorna i contatori di commit avanti/indietro. La scheda Terminale è una shell vera nella cartella del worktree; Attività è la cronologia di quello che è successo lì — commit, push, sessioni — e sopravvive ai riavvii.</p>'
    '<p><strong>Passare una sessione.</strong> Una sessione può spostarsi in un altro worktree dal suo menu, trascrizione inclusa, quando ti accorgi che il lavoro appartiene a un altro branch.</p>'
    '<p><strong>Rimuovere un worktree</strong> termina le sue sessioni, archivia i loro log e dimentica le sue regole di permesso; il branch resta, a meno che tu non lo elimini. Da Impostazioni › Git l’app può eliminare il worktree da sola quando la sua PR viene unita.</p>'
    '<p><strong>Più repository.</strong> Aprine quanti ne vuoi; l’intestazione passa dall’uno all’altro e la casella conta le sessioni in attesa di tutti.</p>',
  ]),
  ('workspaces', 'Lavorare su più repository: gli spazi di lavoro', [
    'Uno <em>spazio di lavoro</em> è un insieme di cartelle con un nome che l’app tiene aperte insieme. Un gateway, una console web e una cartella di appunti sono spesso un unico lavoro, e una domanda su una di esse trova di solito risposta in un’altra: lo spazio di lavoro è il modo in cui dici all’app che vanno insieme.',
    '<img src="{img}workspace.png" alt="Uno spazio di lavoro con due repository: la barra laterale raggruppa i worktree per repository" loading="lazy">',
    '<strong>Crearne uno.</strong> Apri un secondo repository mentre ne hai già uno aperto e l’app ti chiede dove va: aggiungerlo a quello su cui stai lavorando, creare un nuovo spazio di lavoro con entrambi, o aprirlo da solo. Esc vuol dire «da solo». Puoi anche crearne uno dalla pagina iniziale con <em>Nuovo spazio di lavoro</em>, e aggiungere o togliere cartelle in seguito dal pulsante degli spazi di lavoro nell’intestazione. Togliere una cartella da uno spazio di lavoro non elimina mai nulla: cambia solo l’insieme.',
    '<strong>Da VS Code.</strong> Se il tuo team ha già un file <code>.code-workspace</code>, <em>Apri file dello spazio di lavoro…</em> lo legge: le stesse cartelle, nello stesso ordine, con i nomi che dà loro VS Code. Commenti e virgole finali nel file non sono un problema. Le cartelle che non sono repository git vengono mantenute — semplicemente non hanno worktree — e una cartella che non c’è più viene segnalata invece di sparire in silenzio. <em>Salva su file</em> lo riscrive lasciando intatte le parti che l’app non usa, così lo stesso file continua a funzionare in entrambi gli strumenti.',
    '<strong>Cosa mostra la barra laterale.</strong> I worktree raggruppati per repository, ogni gruppo ripiegabile, con il filtro che cerca sia nel nome del branch sia in quello del repository, così trovi un branch senza ricordarti dove vive. Un gruppo ripiegato mostra comunque cosa sta girando al suo interno e continua ad avvisarti quando una sessione è in attesa. Con un solo repository non ci sono gruppi.',
    '<strong>Cosa vedono gli agenti.</strong> Una sessione continua a girare <em>dentro</em> il suo worktree — è lì che stanno git e ogni percorso relativo — ma può leggere anche le altre cartelle dello spazio di lavoro, così «dove finisce questa chiamata?» ha una risposta da entrambi i lati. Una sessione che può solo leggere continua a poter solo leggere, ovunque. C’è anche una riga sopra i gruppi, <em>Su tutto lo spazio di lavoro</em>, per le sessioni che non appartengono a nessun worktree in particolare: a quelle fai le domande che attraversano tutto lo stack. Non hanno branch, né modifiche, né terminale, perché quelli appartengono a un worktree.',
    '<strong>Impostazioni.</strong> Ora i livelli sono tre: Globale, lo spazio di lavoro, poi il singolo repository. L’agente predefinito, la preimpostazione dei permessi e il branch di base sono di solito una proprietà dello stack più che di ogni repository al suo interno, quindi impostali una volta sullo spazio di lavoro; un repository che ha bisogno di qualcosa di diverso può comunque sovrascriverli. Il selettore di ambito nelle Impostazioni sceglie il livello, e una sezione che non sta sovrascrivendo nulla ti dice da dove arrivano i suoi valori.',
    'L’app ricorda ogni spazio di lavoro separatamente: quando torni a uno, ritrovi il repository, il worktree e la disposizione dei pannelli in cui lo avevi lasciato.',
  ]),
  ('providers', 'Agenti e provider', [
    '<p>ygd-editor non parla da solo con nessun servizio di IA. Esegue gli strumenti a riga di comando che hai già — <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, <a href="https://github.com/openai/codex">Codex</a>, <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> — con i tuoi account, quindi utilizzo, fatturazione e condizioni sui dati sono esattamente quelle che hai accettato con quei provider.</p>'
    '<p>Impostazioni › Provider di IA collega ogni provider con il tuo account: <em>Collega</em> apre la pagina di accesso del provider nel browser, e il riquadro mostra poi l’account, il piano e <em>Cambia account</em> / <em>Scollega</em> / <em>Prova la connessione</em>. Codex e Gemini CLI sono inclusi nell’app, quindi non c’è niente da installare; se hai una tua copia installata, l’app usa quella. La licenza di Claude Code non ne consente la distribuzione, quindi il suo riquadro offre <em>Installa Claude Code</em>, che esegue l’installer ufficiale di Anthropic nel terminale del riquadro, nella tua cartella personale, senza password di amministratore. L’agente e il modello predefiniti, e la preimpostazione dei permessi, possono cambiare da repository a repository.</p>',
  ]),
  ('permissions', 'Permessi', [
    '<p>Gli agenti chiedono prima di fare ciò che non hai approvato in anticipo. Impostazioni › Permessi ha tre preimpostazioni — <em>rigorosa</em> (sola lettura), <em>bilanciata</em> (leggere e modificare file, chiedere per tutto il resto) e <em>yolo</em> (anche eseguire comandi, usare il web e fare push) — più interruttori singoli per lettura, modifica, esecuzione di comandi, accesso al web, push ed eliminazione. Qualunque sia la preimpostazione, un agente non può mai eliminare senza chiedere, a meno che tu non lo attivi.</p>'
    '<p>Quando arriva una richiesta, <em>Consenti</em> e <em>Nega</em> rispondono una volta; <em>Consenti sempre</em> ricorda quello strumento per quel worktree, e la regola sparisce insieme al worktree.</p>',
  ]),
  ('notifications', 'Notifiche, casella e budget', [
    '<p>Impostazioni › Notifiche sceglie quando l’app ti avvisa: quando una sessione è in attesa, quando una finisce, quando cambiano i controlli di una pull request. Le notifiche compaiono solo mentre la finestra non è in primo piano, un clic su una porta alla sessione, e il badge nel Dock o nella barra delle applicazioni può contare le sessioni in attesa.</p>'
    '<p>La barra del budget in fondo al pannello di sinistra è la spesa reale di oggi su tutte le sessioni, presa dai report di utilizzo degli agenti stessi. Impostazioni › Budget fissa un limite giornaliero e uno per sessione, una soglia di avviso, e se le sessioni vanno in pausa al raggiungimento del limite.</p>',
  ]),
  ('settings', 'Impostazioni', [
    '<p>Le Impostazioni (⌘,) sono raggruppate per argomento. Aspetto imposta tema, colore di accento, densità e caratteri; Lingua cambia l’interfaccia tra inglese, spagnolo, italiano, polacco, francese, tedesco e turco. Diverse sezioni portano l’etichetta <em>per repo</em>: con un repository selezionato in alto puoi sovrascriverle solo per quel repository.</p>'
    '<p>Tutto si salva automaticamente in <code>settings.json</code>, nella cartella dell’app dentro la tua cartella personale; <em>Apri settings.json</em> modifica il file grezzo con validazione, e l’intestazione mostra quando è stato scritto l’ultima volta.</p>',
    '<img src="{img}settings.png" alt="Impostazioni › Aspetto" loading="lazy">',
  ]),
  ('updates', 'Aggiornamenti', [
    '<p>Poco dopo l’avvio l’app controlla le versioni pubblicate su questo sito, scarica quella nuova in background e propone <em>Riavvia per aggiornare</em>. Impostazioni › Notifiche ha l’interruttore <em>Proponi gli aggiornamenti</em>, un pulsante <em>Cerca aggiornamenti</em> con l’ora dell’ultimo controllo e <em>Installa gli aggiornamenti automaticamente</em>: se è attivo, un aggiornamento scaricato riavvia l’app da solo dopo un conto alla rovescia di 15 secondi che puoi annullare — solo quando nessuna sessione è in corso o in attesa; altrimenti si installa all’uscita. Il primo avvio dopo un aggiornamento dice che versione hai e rimanda a cosa è cambiato.</p>',
  ]),
  ('shortcuts', 'Scorciatoie da tastiera', [
    '<table><tr><td>⌘O</td><td>Apri repository</td></tr><tr><td>⇧⌘C</td><td>Clona repository</td></tr><tr><td>⌘N</td><td>Nuovo worktree</td></tr><tr><td>⌘,</td><td>Impostazioni</td></tr><tr><td>⌘↵</td><td>Invia messaggio</td></tr></table>'
    '<p>Su Windows e Linux leggi ⌘ come Ctrl. Ogni scorciatoia si può cambiare in Impostazioni › Scorciatoie da tastiera.</p>',
  ]),
  ('trouble', 'Quando qualcosa va storto', [
    '<p><strong>macOS dice che non è stato possibile verificare l’app (Sposta nel Cestino / Fine).</strong> Fai clic su Fine, poi Impostazioni di Sistema › Privacy e sicurezza › scorri fino a Sicurezza › <em>Apri comunque</em>, e conferma con la tua password. Su macOS 14 o precedente, clic destro › Apri lo fa in un passaggio. Se si rifiuta ancora, nel Terminale: <code>xattr -d com.apple.quarantine /Applications/ygd-editor.app</code>. Se dice che l’app è <em>danneggiata</em>, il download si è corrotto: scaricala di nuovo e confrontala con <code>SHA256SUMS.txt</code>.</p>'
    '<p><strong>Windows blocca l’installer.</strong> SmartScreen › Ulteriori informazioni › Esegui comunque. L’autore deve risultare <em>ygd-editor release signing</em>.</p>'
    '<p><strong>L’AppImage non si avvia.</strong> Eseguilo con <code>--appimage-extract-and-run</code>, oppure installa <code>libfuse2</code>.</p>'
    '<p><strong>Un provider risulta «Non installato».</strong> Codex e Gemini CLI arrivano con l’app, quindi vuol dire che la copia dell’app è danneggiata: reinstalla l’app. Per Claude Code, fai clic su <em>Installa Claude Code</em> nel suo riquadro; se lo hai installato tu, apri un terminale, verifica che <code>claude --version</code> funzioni, poi Impostazioni › Provider di IA › Ripeti la ricerca.</p>'
    '<p><strong>Errori di git.</strong> L’app spiega quelli più comuni in una frase — credenziali, un remoto andato avanti, un file di lock, un albero con modifiche, conflitti — e conserva l’output completo nel terminale del worktree.</p>'
    '<p><strong>Non compare nessun aggiornamento.</strong> Controlla Impostazioni › Notifiche › Proponi gli aggiornamenti, poi Cerca aggiornamenti; l’app deve poter raggiungere github.com.</p>'
    '<p>Per tutto il resto: <a href="https://github.com/{repo}/issues">apri una issue</a> raccontando cosa hai fatto, cosa ti aspettavi e cosa è successo.</p>',
  ]),
  ('privacy', 'Privacy e sicurezza', [
    '<p>Tutto gira sul tuo computer. L’app in sé si collega a internet per una cosa sola: controllare le versioni pubblicate su questo sito in cerca di aggiornamenti. Gli agenti parlano con i loro provider con i tuoi account; git parla con i tuoi remoti con le tue credenziali. I token dei provider che l’app conserva stanno nel portachiavi del sistema operativo. L’interfaccia gira in una sandbox, ogni richiesta che nomina un percorso viene verificata rispetto ai repository che hai davvero aperto, e nessun comando viene mai costruito a partire da una stringa di shell.</p>'
    '<p>Per verificare che un download sia davvero nostro, vedi <a href="{prefix}index.html#genuine">Il mio download è autentico?</a> nella pagina di download.</p>',
  ]),
 ],
 # versions page and small shared strings
 'dl_version': 'versione {v}',
 'genuine_details': 'i dettagli tecnici',
 'lang_label': 'Lingua',
 'title_releases': 'ygd-editor — tutte le versioni',
 'r_h1': 'Tutte le versioni',
 'r_lead': 'Tutte le versioni di ygd-editor pubblicate finora. Prima la più recente per ogni sistema, poi la cronologia completa, sistema per sistema. La pagina di download offre sempre la versione completa più recente; questo elenco è per chi ne ha bisogno di una in particolare.',
 'r_latest_h': 'La più recente per ogni sistema',
 'r_all_h': 'Tutte le versioni, per sistema',
 'r_systems': {'mac': 'macOS', 'win': 'Windows', 'linux': 'Linux'},
 'r_loading': 'Caricamento delle versioni…',
 'r_error': 'Non è stato possibile leggere l’elenco delle versioni ({err}).',
 'r_github': 'Le release su GitHub',
 'r_none': 'Ancora nessuna versione pubblicata.',
 'r_notes': 'Cosa è cambiato',
 'r_checksums': 'Checksum',
 'r_updates': 'Le app installate si aggiornano da sole alla versione completa più recente; niente di quello che c’è qui va scaricato a mano, a meno che tu non voglia una versione in particolare.',
}
