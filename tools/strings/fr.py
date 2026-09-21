# Français. Strings of the download page, the guide and the versions page. HTML fragments and
# {placeholders} stay as they are; keys match tools/strings/en.py, which is the reference.
T = {
 'title_index': 'ygd-editor — téléchargement', 'title_guide': 'ygd-editor — guide d’utilisation',
 'desc': 'ygd-editor : exécutez des agents de programmation IA dans des worktrees git séparés, relisez leurs modifications et livrez-les, le tout depuis une seule fenêtre. Gratuit pour macOS, Windows et Linux.',
 'nav_download': 'Télécharger', 'nav_guide': 'Guide', 'nav_releases': 'Toutes les versions', 'nav_issues': 'Signaler un problème',
 'tagline': 'Donnez à chaque tâche sa propre branche et son propre agent IA, et gardez-les tous à l’œil.',
 'hero_p': 'ygd-editor ouvre chaque tâche dans son propre worktree git, y exécute un agent de programmation (Claude Code, Codex ou Gemini CLI) et vous laisse relire les modifications, faire le commit, le push et ouvrir la pull request sans quitter la fenêtre. Gratuit, pour macOS, Windows et Linux.',
 'dl_loading': 'Recherche de la dernière version…', 'dl_for': 'Télécharger pour {label}', 'dl_none': 'Aucune version publiée pour l’instant', 'dl_none_hint': 'La première est en route.',
 'dl_error': 'Voir toutes les versions', 'dl_error_hint': 'Impossible de lire la dernière version ({err}). La page des versions contient tous les téléchargements.',
 'dl_others': 'Autres systèmes :', 'dl_checksums': 'Sommes de contrôle', 'dl_free': 'Gratuit · sans compte · se met à jour tout seul',
 'kinds': {'mac-arm64': 'macOS · Apple Silicon (M1 et suivants)', 'mac-x64': 'macOS · Intel', 'win-x64': 'Windows', 'linux-appimage': 'Linux · AppImage', 'linux-deb': 'Linux · Debian / Ubuntu'},
 'shot_console': 'La console : les worktrees à gauche, les modifications et le diff au centre, la session de l’agent à droite.',
 'what_h': 'Ce que vous obtenez',
 'what': [
   ('Un worktree par tâche', 'Chaque branche a son propre dossier : les agents ne se marchent jamais sur les pieds et vous changez de tâche sans rien mettre de côté.'),
   ('Les agents là où est le code', 'Lancez Claude Code, Codex ou Gemini CLI dans un worktree, regardez-le travailler, répondez à ses questions et transférez une session vers un autre worktree quand les plans changent.'),
   ('Relire et livrer sur place', 'Indexez des fichiers, lisez le diff, demandez à l’agent d’expliquer ou de modifier une sélection, faites le commit, le push et ouvrez la pull request depuis le même écran.'),
   ('Ne vous dérange pas', 'Une seule boîte de réception pour toutes les sessions qui vous attendent, des notifications de bureau facultatives et un compteur de dépenses du jour avec les limites que vous fixez.'),
 ],
 'install_h': 'Installation en une minute',
 'install_intro': 'Votre ordinateur vous avertira la première fois. C’est normal : personne n’a payé Apple ni Microsoft pour un certificat, et l’avertissement concerne cette paperasse manquante, pas ce que fait l’application. Voici comment passer outre, une seule fois et plus jamais sur cet ordinateur.',
 'install': [
   ('macOS', ['Ouvrez le <code>.dmg</code> téléchargé. Une fenêtre affiche ces étapes dans votre langue — cliquez sur <em>Continuer</em> — puis glissez <strong>ygd-editor</strong> dans Applications.', 'Ouvrez-la. macOS dit qu’il <em>n’a pas pu vérifier</em> l’application et propose <em>Placer dans la corbeille</em> ou <em>Terminé</em> : cliquez sur <strong>Terminé</strong>.', 'Ouvrez <strong>Réglages Système › Confidentialité et sécurité</strong>, descendez jusqu’à <em>Sécurité</em> et cliquez sur <strong>Ouvrir quand même</strong> à côté de ygd-editor. Confirmez avec votre mot de passe. C’est tout : macOS ne redemandera plus.', 'Sous macOS 14 ou antérieur, <strong>clic droit sur l’application › Ouvrir</strong> fait la même chose en une étape.', 'Vous ne savez pas quel Mac vous avez ? Menu Pomme › À propos de ce Mac : « Apple M… » est un Apple Silicon, tout ce qui mentionne « Intel » est un Intel.']),
   ('Windows', ['Lancez l’installateur. Quand SmartScreen dit « Windows a protégé votre ordinateur », cliquez sur <strong>Informations complémentaires</strong>, puis sur <strong>Exécuter quand même</strong>.', 'L’éditeur affiché est <em>ygd-editor release signing</em> : c’est nous. Choisissez le dossier d’installation si vous le souhaitez et terminez.', 'L’application apparaît dans le menu Démarrer sous le nom ygd-editor.']),
   ('Linux', ['<strong>AppImage :</strong> rendez-le exécutable (<code>chmod +x ygd-editor-*.AppImage</code>) et lancez-le. S’il se plaint de FUSE, lancez-le avec <code>--appimage-extract-and-run</code>.', '<strong>Debian / Ubuntu :</strong> <code>sudo apt install ./ygd-editor-*.deb</code>, puis retrouvez-le dans votre menu d’applications.']),
 ],
 'need_h': 'Ce dont vous avez besoin', 'need_p': 'Git sur votre ordinateur et un compte chez au moins un fournisseur. <a href="https://github.com/openai/codex">Codex</a> et <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> sont inclus dans l’application, rien à installer ; pour <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, dont la licence ne permet pas de l’inclure, Réglages › Fournisseurs d’IA propose un clic qui exécute pour vous l’installateur officiel d’Anthropic. Connecter un fournisseur ouvre sa page de connexion dans votre navigateur. Pour les pull requests, <code>gh</code> de GitHub ou <code>glab</code> de GitLab.',
 'updates_h': 'Les mises à jour se font toutes seules',
 'updates_p': 'Peu après le lancement, l’application cherche une nouvelle version, la télécharge discrètement et propose « Redémarrer pour mettre à jour ». Réglages › Notifications a aussi un bouton « Rechercher des mises à jour » et, si vous préférez, une option pour les installer toute seule quand rien n’est en cours. Après une mise à jour, l’application vous dit quelle version vous utilisez et renvoie vers ce qui a changé.',
 'genuine_h': 'Mon téléchargement est-il authentique ?',
 'genuine_p': 'Deux vérifications indépendantes, dont aucune ne repose sur la confiance en un nom. Vous n’êtes pas obligé de les faire ; elles sont là pour ceux qui le souhaitent.',
 'genuine_prov': '<strong>Provenance.</strong> Chaque version est accompagnée de <code>SHA256SUMS.txt</code>, signé via <a href="https://www.sigstore.dev/">Sigstore</a> par le workflow de publication du projet lui-même. Avec <code>cosign</code> installé :',
 'genuine_sig': '<strong>Signature du code.</strong> L’application macOS et l’installateur Windows sont signés avec le certificat du projet (<a href="{pem}">clé publique</a>). Comparez l’empreinte, pas le nom : n’importe qui peut donner n’importe quel nom à un certificat.',
 'guide_cta_h': 'Première visite ?', 'guide_cta_p': 'Le <a href="{prefix}guide.html">guide d’utilisation</a> parcourt les dix premières minutes : ouvrir un dépôt, créer un worktree, lancer un agent, relire et livrer le résultat.',
 'footer_made': 'Réalisé par Manu Hurtado. L’application est gratuite ; le code source est privé.',
 # guide
 'g_h1': 'Guide d’utilisation', 'g_lead': 'Tout ce qu’il vous faut pour le premier après-midi avec ygd-editor, en termes simples. Dix minutes de lecture, et vous pouvez revenir à n’importe quelle section depuis la liste.',
 'g_toc': 'Sur cette page',
 'g_sections': [
  ('idea', 'L’idée en une minute', [
    'Un <em>worktree</em> git est un second dossier du même dépôt, sur une autre branche. Au lieu de changer de branche dans un seul dossier — en mettant de côté, en recompilant et en perdant le fil à chaque fois — vous gardez un dossier par tâche.',
    'ygd-editor est construit autour de cela : le panneau de gauche liste vos worktrees, celui du centre montre ce qui a changé dans celui que vous avez choisi, et celui de droite y exécute un agent IA. Deux agents sur deux tâches travaillent dans deux dossiers et ne se heurtent jamais. Quand l’un attend une réponse, la boîte de réception de l’en-tête vous le signale.',
    '<img src="{img}start.png" alt="La page d’accueil : dépôts récents et actions de démarrage" loading="lazy">',
  ]),
  ('first', 'Vos dix premières minutes', [
    '<ol>'
    '<li><strong>Ouvrez un dépôt.</strong> Sur la page d’accueil, choisissez <em>Ouvrir un dépôt</em> et sélectionnez un dossier qui contient déjà git, ou <em>Cloner un dépôt</em> avec une URL GitHub, GitLab ou n’importe quelle URL git. Les dépôts récents restent sur la page d’accueil.</li>'
    '<li><strong>Créez un worktree.</strong> <em>Nouveau worktree</em> (⌘N) propose un nom de branche tiré de la tâche et un dossier où la placer ; vous pouvez renommer les deux selon la convention que vous utilisez. Git n’accepte pas les espaces dans un nom de branche, ils deviennent donc des tirets et la boîte de dialogue vous montre le résultat avant de créer quoi que ce soit. L’emplacement des worktrees sur le disque, et un préfixe suggéré facultatif, se trouvent dans Réglages › Git.</li>'
    '<li><strong>Lancez une session.</strong> <em>+ Session</em> dans le panneau de droite choisit un agent et un modèle ; l’agent par défaut est dans Réglages › Agent par défaut. Tapez ce que vous voulez dans le compositeur. <code>@</code> joint des fichiers ou du contexte comme le diff actuel, <code>/</code> exécute les commandes de l’agent, <code>#</code> ses skills. ⌘↵ envoie.</li>'
    '<li><strong>Laissez-le travailler, ou arrêtez-le.</strong> La transcription montre chaque outil que l’agent utilise. Quand il a besoin d’une permission pour quelque chose que vous n’avez pas pré-approuvé, la session passe <em>en attente</em>, la boîte de réception de l’en-tête la compte, et vous autorisez ou refusez ; « Toujours autoriser » mémorise votre choix pour ce worktree. <em>Arrêter</em> interrompt ; ce que vous tapez pendant qu’il travaille est mis en file d’attente.</li>'
    '<li><strong>Relisez les modifications.</strong> L’onglet Modifications liste chaque fichier touché et qui l’a modifié. Cliquez sur un fichier pour le diff ; sélectionnez des lignes et choisissez <em>Expliquer</em> ou <em>Demander une modification</em> pour les renvoyer à l’agent. Un avertissement marque les fichiers qu’un autre worktree du même dépôt touche aussi.</li>'
    '<li><strong>Commit, push, ouvrez la PR.</strong> Cochez les fichiers à indexer, écrivez le message ou <em>Rédiger avec l’IA</em>, <em>Commit</em>. <em>Push</em> configure l’upstream ; <em>Ouvrir une pull request</em> remplit le titre, le corps (rédigé à partir du diff si vous le souhaitez), l’état de brouillon, les relecteurs et les étiquettes, et passe la main à <code>gh</code> ou <code>glab</code>. La carte du worktree affiche ensuite la PR et ses checks.</li>'
    '</ol>',
    '<img src="{img}console.png" alt="La console avec un diff ouvert et une session Claude Code en cours" loading="lazy">',
  ]),
  ('daily', 'Au quotidien', [
    '<p><strong>Le worktree principal</strong> — le dossier avec lequel vous avez ouvert le dépôt — figure avec les autres et c’est de lui que partent les nouveaux worktrees. Sélectionnez-le et cliquez sur le nom de sa branche dans l’en-tête : un champ de recherche se déplie sur toutes les branches — les vôtres, ou une qui n’existe que sur le dépôt distant, qu’il extrait comme nouvelle branche de suivi. Tapez pour filtrer, flèches et Entrée pour changer. Une branche déjà tenue par un autre worktree est listée mais grisée, parce que git n’autorise une branche que dans un seul worktree à la fois.</p>'
    '<p><strong>Mettre à jour depuis la base</strong> sur un worktree fait un fetch et un rebase sur la branche de base ; les conflits s’arrêtent avec la liste des fichiers, vous les résolvez, vous indexez et <em>Continuer</em>. <strong>Fetch</strong> rafraîchit les compteurs d’avance/retard. L’onglet Terminal est un vrai shell dans le dossier du worktree ; Activité est la chronologie de ce qui s’y est passé — commits, pushes, sessions — et survit aux redémarrages.</p>'
    '<p><strong>Transférer une session.</strong> Une session peut être transférée vers un autre worktree depuis son menu, transcription comprise, quand vous réalisez que le travail appartient à une autre branche.</p>'
    '<p><strong>Supprimer un worktree</strong> termine ses sessions, archive leurs journaux et oublie ses règles de permissions ; la branche reste sauf si vous la supprimez. Réglages › Git peut supprimer le worktree tout seul une fois sa PR fusionnée.</p>'
    '<p><strong>Plusieurs dépôts.</strong> Ouvrez-en autant que vous voulez ; l’en-tête passe de l’un à l’autre, et la boîte de réception compte les sessions en attente de tous.</p>',
  ]),
  ('workspaces', 'Travailler sur plusieurs dépôts : les espaces de travail', [
    'Un <em>espace de travail</em> est un ensemble nommé de dossiers que l’application garde ouverts ensemble. Une passerelle, une console web et un dossier de notes forment souvent un seul travail, et une question sur l’un trouve généralement sa réponse dans un autre : un espace de travail est la façon de dire à l’application qu’ils vont ensemble.',
    '<img src="{img}workspace.png" alt="Un espace de travail de deux dépôts : la barre latérale regroupe les worktrees par dépôt" loading="lazy">',
    '<strong>En créer un.</strong> Ouvrez un second dépôt alors qu’un autre est déjà ouvert et l’application vous demande où il va : l’ajouter à ce sur quoi vous travaillez, démarrer un nouvel espace de travail avec les deux, ou l’ouvrir tout seul. Échap signifie « tout seul ». Vous pouvez aussi en démarrer un depuis la page d’accueil avec <em>Nouvel espace de travail</em>, et ajouter ou retirer des dossiers plus tard depuis le bouton des espaces de travail dans l’en-tête. Retirer un dossier d’un espace de travail ne supprime jamais rien : seul l’ensemble change.',
    '<strong>Depuis VS Code.</strong> Si votre équipe tient déjà un fichier <code>.code-workspace</code>, <em>Ouvrir un fichier d’espace de travail…</em> le lit : les mêmes dossiers, dans le même ordre, nommés comme VS Code les nomme. Les commentaires et les virgules finales dans le fichier ne posent aucun problème. Les dossiers qui ne sont pas des dépôts git sont conservés — ils n’ont simplement pas de worktrees — et un dossier qui a disparu est signalé plutôt que discrètement écarté. <em>Enregistrer dans le fichier</em> le réécrit en laissant intactes les parties que l’application n’utilise pas, de sorte que le même fichier continue de fonctionner dans les deux outils.',
    '<strong>Ce que montre la barre latérale.</strong> Les worktrees regroupés par dépôt, chaque groupe repliable, avec le filtre qui cherche dans le nom de branche comme dans le nom du dépôt, pour que vous trouviez une branche sans vous souvenir d’où elle vit. Un groupe replié montre toujours ce qui tourne à l’intérieur, et signale toujours quand une session attend. Avec un seul dépôt, il n’y a aucun groupe.',
    '<strong>Ce que voient les agents.</strong> Une session s’exécute toujours <em>dans</em> son worktree — c’est là que vivent git et tous les chemins relatifs — mais elle peut aussi lire les autres dossiers de l’espace de travail, si bien que « où aboutit cet appel ? » peut trouver sa réponse de chaque côté. Une session qui ne fait que lire n’a toujours que le droit de lire, partout. Il y a aussi une ligne au-dessus des groupes, <em>Sur tout l’espace de travail</em>, pour les sessions qui n’appartiennent à aucun worktree en particulier : posez-leur les questions qui couvrent toute la pile. Elles n’ont ni branche, ni modifications, ni terminal, parce que cela appartient à un worktree.',
    '<strong>Réglages.</strong> Trois niveaux désormais : Global, l’espace de travail, puis un dépôt en particulier. L’agent par défaut, le préréglage de permissions et la branche de base sont généralement une propriété de la pile plutôt que de chaque dépôt qui la compose, alors définissez-les une fois sur l’espace de travail ; un dépôt qui a besoin d’autre chose peut toujours les remplacer. Le sélecteur de portée dans Réglages choisit le niveau, et une section qui ne remplace rien indique d’où viennent ses valeurs.',
    'L’application mémorise chaque espace de travail séparément : revenez sur l’un d’eux et vous retrouvez le dépôt, le worktree et la disposition des panneaux que vous aviez laissés.',
  ]),
  ('providers', 'Agents et fournisseurs', [
    '<p>ygd-editor ne parle lui-même à aucun service d’IA. Il exécute les outils en ligne de commande que vous avez déjà — <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, <a href="https://github.com/openai/codex">Codex</a>, <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> — avec vos propres comptes, si bien que votre utilisation, votre facturation et vos conditions de traitement des données sont exactement celles que vous avez acceptées auprès de ces fournisseurs.</p>'
    '<p>Réglages › Fournisseurs d’IA connecte chaque fournisseur avec votre propre compte : <em>Connecter</em> ouvre la page de connexion du fournisseur dans votre navigateur, et la carte affiche ensuite le compte, le forfait et <em>Changer de compte</em> / <em>Déconnecter</em> / <em>Tester la connexion</em>. Codex et Gemini CLI sont inclus dans l’application, il n’y a donc rien à installer ; si vous avez votre propre copie installée, l’application utilise celle-là. La licence de Claude Code ne permet pas de l’inclure, sa carte propose donc <em>Installer Claude Code</em>, qui exécute l’installateur officiel d’Anthropic dans le terminal de la carte, dans votre dossier personnel, sans mot de passe administrateur. L’agent et le modèle par défaut, ainsi que le préréglage de permissions, peuvent varier selon le dépôt.</p>',
  ]),
  ('permissions', 'Permissions', [
    '<p>Les agents demandent avant de faire ce que vous n’avez pas pré-approuvé. Réglages › Permissions propose trois préréglages — <em>strict</em> (lecture seule), <em>équilibré</em> (lire et modifier les fichiers, demander pour tout le reste) et <em>yolo</em> (aussi exécuter des commandes, utiliser le web et faire des push) — plus des interrupteurs individuels pour la lecture, la modification, l’exécution de commandes, l’accès web, le push et la suppression. Quel que soit le préréglage, un agent ne peut jamais supprimer sans demander, sauf si vous l’activez.</p>'
    '<p>Quand une demande arrive, <em>Approuver</em> et <em>Refuser</em> répondent une fois ; <em>Toujours autoriser</em> mémorise cet outil pour ce worktree, et la règle disparaît avec le worktree.</p>',
  ]),
  ('notifications', 'Notifications, boîte de réception et budget', [
    '<p>Réglages › Notifications choisit quand l’application vous prévient : quand une session attend, quand une session se termine, quand les checks d’une pull request changent. Les notifications ne s’affichent que lorsque la fenêtre n’est pas au premier plan, un clic sur l’une d’elles ouvre la session, et le badge du Dock ou de la barre des tâches peut compter les sessions en attente.</p>'
    '<p>La barre de budget en bas du panneau de gauche est la dépense réelle du jour sur toutes les sessions, tirée des rapports d’utilisation des agents eux-mêmes. Réglages › Budget fixe une limite quotidienne et une limite par session, un seuil d’avertissement, et si les sessions se mettent en pause quand la limite est atteinte.</p>',
  ]),
  ('settings', 'Réglages', [
    '<p>Les Réglages (⌘,) sont regroupés par thème. Apparence définit le thème, la couleur d’accent, la densité et les polices ; Langue bascule l’interface entre anglais, espagnol, italien, polonais, français, allemand et turc. Plusieurs sections portent le badge <em>par dépôt</em> : avec un dépôt sélectionné en haut, vous pouvez les remplacer pour ce dépôt uniquement.</p>'
    '<p>Tout s’enregistre automatiquement dans <code>settings.json</code>, dans le dossier de l’application au sein de votre répertoire personnel ; <em>Ouvrir settings.json</em> modifie le fichier brut avec validation, et l’en-tête indique quand il a été écrit pour la dernière fois.</p>',
    '<img src="{img}settings.png" alt="Réglages › Apparence" loading="lazy">',
  ]),
  ('updates', 'Mises à jour', [
    '<p>Peu après le lancement, l’application consulte les versions de ce site, télécharge la nouvelle en arrière-plan et propose <em>Redémarrer pour mettre à jour</em>. Réglages › Notifications a l’interrupteur <em>Proposer les mises à jour</em>, un bouton <em>Rechercher des mises à jour</em> avec l’heure de la dernière vérification, et <em>Installer les mises à jour automatiquement</em> : activé, une mise à jour téléchargée redémarre l’application toute seule après un décompte de 15 secondes que vous pouvez annuler — seulement quand aucune session n’est en cours ou en attente ; sinon, elle s’installe quand vous quittez. Le premier lancement après une mise à jour indique quelle version vous utilisez et renvoie vers ce qui a changé.</p>',
  ]),
  ('shortcuts', 'Raccourcis clavier', [
    '<table><tr><td>⌘O</td><td>Ouvrir un dépôt</td></tr><tr><td>⇧⌘C</td><td>Cloner un dépôt</td></tr><tr><td>⌘N</td><td>Nouveau worktree</td></tr><tr><td>⌘,</td><td>Réglages</td></tr><tr><td>⌘↵</td><td>Envoyer le prompt</td></tr></table>'
    '<p>Sous Windows et Linux, lisez ⌘ comme Ctrl. Chaque raccourci peut être modifié dans Réglages › Raccourcis clavier.</p>',
  ]),
  ('trouble', 'Quand quelque chose ne va pas', [
    '<p><strong>macOS dit qu’il n’a pas pu vérifier l’application (Placer dans la corbeille / Terminé).</strong> Cliquez sur Terminé, puis Réglages Système › Confidentialité et sécurité › descendez jusqu’à Sécurité › <em>Ouvrir quand même</em>, et confirmez avec votre mot de passe. Sous macOS 14 ou antérieur, clic droit › Ouvrir le fait en une étape. S’il refuse toujours, dans le Terminal : <code>xattr -d com.apple.quarantine /Applications/ygd-editor.app</code>. S’il dit que l’application est <em>endommagée</em>, le téléchargement a été corrompu : téléchargez-la de nouveau et comparez-la à <code>SHA256SUMS.txt</code>.</p>'
    '<p><strong>Windows bloque l’installateur.</strong> SmartScreen › Informations complémentaires › Exécuter quand même. L’éditeur doit indiquer <em>ygd-editor release signing</em>.</p>'
    '<p><strong>L’AppImage ne démarre pas.</strong> Lancez-le avec <code>--appimage-extract-and-run</code>, ou installez <code>libfuse2</code>.</p>'
    '<p><strong>Un fournisseur affiche « Non installé ».</strong> Codex et Gemini CLI sont livrés avec l’application, cela signifie donc que la copie de l’application est endommagée : réinstallez l’application. Pour Claude Code, cliquez sur <em>Installer Claude Code</em> sur sa carte ; si vous l’avez installé vous-même, ouvrez un terminal, vérifiez que <code>claude --version</code> fonctionne, puis Réglages › Fournisseurs d’IA › Rechercher à nouveau.</p>'
    '<p><strong>Erreurs git.</strong> L’application explique les plus courantes en une phrase — identifiants, un dépôt distant qui a avancé, un fichier de verrouillage, un arbre de travail modifié, des conflits — et garde la sortie complète dans le terminal du worktree.</p>'
    '<p><strong>Aucune mise à jour n’apparaît.</strong> Vérifiez Réglages › Notifications › Proposer les mises à jour, puis Rechercher des mises à jour ; l’application doit pouvoir joindre github.com.</p>'
    '<p>Pour tout le reste : <a href="https://github.com/{repo}/issues">ouvrez une issue</a> en décrivant ce que vous avez fait, ce que vous attendiez et ce qui s’est passé.</p>',
  ]),
  ('privacy', 'Confidentialité et sécurité', [
    '<p>Tout s’exécute sur votre ordinateur. L’application elle-même se connecte à internet pour une seule chose : consulter les versions de ce site à la recherche de mises à jour. Les agents parlent à leurs fournisseurs avec vos comptes ; git parle à vos dépôts distants avec vos identifiants. Les jetons de fournisseur que l’application conserve sont stockés dans le trousseau du système d’exploitation. L’interface s’exécute dans un bac à sable, chaque requête qui nomme un chemin est vérifiée par rapport aux dépôts que vous avez réellement ouverts, et aucune commande n’est jamais construite à partir d’une chaîne shell.</p>'
    '<p>Pour vérifier qu’un téléchargement est bien le nôtre, voir <a href="{prefix}index.html#genuine">Mon téléchargement est-il authentique ?</a> sur la page de téléchargement.</p>',
  ]),
 ],
 # page des versions et petites chaînes partagées
 'dl_version': 'version {v}',
 'genuine_details': 'les détails techniques',
 'lang_label': 'Langue',
 'title_releases': 'ygd-editor — toutes les versions',
 'r_h1': 'Toutes les versions',
 'r_lead': 'Toutes les versions de ygd-editor qui ont été publiées. D’abord la plus récente pour chaque système, puis tout l’historique, système par système. La page de téléchargement propose toujours la version complète la plus récente ; cette liste est pour qui a besoin d’une version en particulier.',
 'r_latest_h': 'La plus récente pour chaque système',
 'r_all_h': 'Toutes les versions, par système',
 'r_systems': {'mac': 'macOS', 'win': 'Windows', 'linux': 'Linux'},
 'r_loading': 'Chargement des versions…',
 'r_error': 'Impossible de lire la liste des versions ({err}).',
 'r_github': 'Les versions sur GitHub',
 'r_none': 'Aucune version publiée pour l’instant.',
 'r_notes': 'Ce qui a changé',
 'r_checksums': 'Sommes de contrôle',
 'r_updates': 'Les applications installées se mettent à jour toutes seules vers la version complète la plus récente ; rien ici n’a besoin d’être téléchargé à la main, sauf si vous voulez une version en particulier.',
}
