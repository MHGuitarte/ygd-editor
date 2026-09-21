# Español. Strings of the download page, the guide and the versions page. HTML fragments and
# {placeholders} stay as they are; keys match tools/strings/en.py, which is the reference.
T = {
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
   ('macOS', ['Abre el <code>.dmg</code> descargado. Una ventana muestra estos pasos en tu idioma —pulsa <em>Continuar</em>— y después arrastra <strong>ygd-editor</strong> a Aplicaciones.', 'Ábrela. macOS dice que <em>no ha podido verificar</em> la aplicación y ofrece <em>Trasladar a la Papelera</em> o <em>Aceptar</em>: pulsa <strong>Aceptar</strong>.', 'Abre <strong>Ajustes del Sistema › Privacidad y seguridad</strong>, baja hasta <em>Seguridad</em> y pulsa <strong>Abrir de todos modos</strong> junto a ygd-editor. Confirma con tu contraseña. Ya está: macOS no volverá a preguntar.', 'En macOS 14 o anterior, <strong>clic derecho en la aplicación › Abrir</strong> hace lo mismo en un paso.', '¿No sabes qué Mac tienes? Menú Apple › Acerca de este Mac: «Apple M…» es Apple Silicon; si dice «Intel», es Intel.']),
   ('Windows', ['Ejecuta el instalador. Cuando SmartScreen diga «Windows protegió su PC», pulsa <strong>Más información</strong> y después <strong>Ejecutar de todas formas</strong>.', 'El editor que aparece es <em>ygd-editor release signing</em>: somos nosotros. Elige la carpeta si quieres y termina.', 'La aplicación aparece en el menú Inicio como ygd-editor.']),
   ('Linux', ['<strong>AppImage:</strong> hazlo ejecutable (<code>chmod +x ygd-editor-*.AppImage</code>) y ejecútalo. Si se queja de FUSE, lánzalo con <code>--appimage-extract-and-run</code>.', '<strong>Debian / Ubuntu:</strong> <code>sudo apt install ./ygd-editor-*.deb</code> y búscalo en el menú de aplicaciones.']),
 ],
 'need_h': 'Qué necesitas', 'need_p': 'Git en tu ordenador y una cuenta en al menos un proveedor. <a href="https://github.com/openai/codex">Codex</a> y <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> vienen dentro de la aplicación, sin nada que instalar; para <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, cuya licencia no permite incluirlo, Ajustes › Proveedores de IA ofrece un clic que ejecuta por ti el instalador oficial de Anthropic. Conectar un proveedor abre su página de inicio de sesión en tu navegador. Para los pull requests, <code>gh</code> de GitHub o <code>glab</code> de GitLab.',
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
    '<li><strong>Crea un worktree.</strong> <em>Nuevo worktree</em> (⌘N) sugiere un nombre de rama a partir de la tarea y una carpeta donde ponerla; ambos son tuyos para renombrarlos con la convención que uses. Git no admite espacios en el nombre de una rama, así que se convierten en guiones y el diálogo te enseña el resultado antes de crear nada. Dónde van los worktrees en disco, y un prefijo sugerido opcional, están en Ajustes › Git.</li>'
    '<li><strong>Arranca una sesión.</strong> <em>+ Sesión</em> en el panel derecho elige agente y modelo; el agente por defecto está en Ajustes › Agente por defecto. Escribe lo que quieres en el compositor. <code>@</code> adjunta archivos o contexto como el diff actual, <code>/</code> ejecuta comandos del agente, <code>#</code> sus skills. ⌘↵ envía.</li>'
    '<li><strong>Déjalo trabajar, o páralo.</strong> La transcripción muestra cada herramienta que usa el agente. Cuando necesita permiso para algo que no has aprobado de antemano, la sesión pasa a <em>esperando</em>, la bandeja de la cabecera la cuenta y tú permites o deniegas; «Permitir siempre» recuerda tu decisión para ese worktree. <em>Detener</em> interrumpe; lo que escribas mientras trabaja se pone en cola.</li>'
    '<li><strong>Revisa los cambios.</strong> La pestaña Cambios lista cada archivo tocado y quién lo cambió. Pulsa uno para ver el diff; selecciona líneas y elige <em>Explicar</em> o <em>Pedir un cambio</em> para devolvérselas al agente. Un aviso marca los archivos que otro worktree del mismo repositorio también toca.</li>'
    '<li><strong>Commit, push y abre el PR.</strong> Marca los archivos a preparar, escribe el mensaje o <em>Redactar con IA</em>, <em>Commit</em>. <em>Push</em> configura el upstream; <em>Abrir pull request</em> rellena título, cuerpo (redactado a partir del diff si quieres), borrador, revisores y etiquetas, y se lo pasa a <code>gh</code> o <code>glab</code>. La tarjeta del worktree muestra entonces el PR y sus checks.</li>'
    '</ol>',
    '<img src="{img}console.png" alt="La consola con un diff abierto y una sesión de Claude Code en marcha" loading="lazy">',
  ]),
  ('daily', 'En el día a día', [
    '<p><strong>El worktree principal</strong> —la carpeta con la que abriste el repositorio— aparece junto a los demás y es aquel del que se ramifican los nuevos. Selecciónalo y pulsa el nombre de su rama en la cabecera: se despliega un buscador con todas las ramas —las tuyas o alguna que solo exista en el remoto, que se crea como rama de seguimiento—. Escribe para filtrar, flechas y Enter para cambiar. Una rama que ya tenga otro worktree aparece en gris, porque git solo permite una rama en un worktree a la vez.</p>'
    '<p><strong>Actualizar desde la base</strong> en un worktree hace fetch y rebase sobre la rama base; los conflictos se detienen con los archivos listados, los resuelves, preparas y <em>Continuar</em>. <strong>Fetch</strong> refresca los contadores de adelante/atrás. La pestaña Terminal es una shell real en la carpeta del worktree; Actividad es la línea de tiempo de lo que pasó allí —commits, pushes, sesiones— y sobrevive a los reinicios.</p>'
    '<p><strong>Pasar una sesión.</strong> Una sesión puede moverse a otro worktree desde su menú, transcripción incluida, cuando te das cuenta de que el trabajo va en otra rama.</p>'
    '<p><strong>Eliminar un worktree</strong> termina sus sesiones, archiva sus registros y olvida sus reglas de permisos; la rama se queda salvo que la borres. Ajustes › Git puede borrar el worktree por sí solo cuando su PR se fusiona.</p>'
    '<p><strong>Varios repositorios.</strong> Abre los que quieras; la cabecera cambia entre ellos y la bandeja cuenta las sesiones en espera de todos.</p>',
  ]),
  ('workspaces', 'Trabajar con varios repositorios: espacios de trabajo', [
    'Un <em>espacio de trabajo</em> es un conjunto de carpetas con nombre que la app mantiene abiertas a la vez. Una pasarela, una consola web y una carpeta de notas son muchas veces un mismo trabajo, y una pregunta sobre una se responde casi siempre en otra: el espacio de trabajo es cómo le dices a la app que van juntas.',
    '<img src="{img}workspace.png" alt="Un espacio de trabajo con dos repositorios: la barra lateral agrupa los worktrees por repositorio" loading="lazy">',
    '<strong>Crear uno.</strong> Si abres un segundo repositorio teniendo ya otro abierto, la app te pregunta dónde va: añadirlo a lo que tienes abierto, crear un espacio de trabajo nuevo con los dos, o abrirlo por su cuenta. Escape significa «por su cuenta». También puedes crear uno desde la página de inicio con <em>Nuevo espacio de trabajo</em>, y añadir o quitar carpetas después desde el botón de espacios de trabajo de la cabecera. Quitar una carpeta no borra nada: solo cambia el conjunto.',
    '<strong>Desde VS Code.</strong> Si tu equipo ya tiene un archivo <code>.code-workspace</code>, <em>Abrir archivo de espacio de trabajo…</em> lo lee: las mismas carpetas, en el mismo orden y con los nombres que les da VS Code. Los comentarios y las comas finales del archivo no son problema. Las carpetas que no son repositorios git se conservan —simplemente no tienen worktrees— y una carpeta que ya no está se te avisa en vez de desaparecer sin más. <em>Guardar en archivo</em> lo reescribe sin tocar las partes que la app no usa, así que el mismo archivo sigue sirviendo en las dos herramientas.',
    '<strong>Qué ves en la barra lateral.</strong> Los worktrees agrupados por repositorio, cada grupo plegable, con el filtro buscando tanto en el nombre de la rama como en el del repositorio, para que encuentres una rama sin acordarte de dónde vive. Un grupo plegado sigue mostrando lo que se está ejecutando dentro y sigue avisando si una sesión espera. Con un solo repositorio no hay grupos.',
    '<strong>Qué ven los agentes.</strong> Una sesión sigue ejecutándose <em>dentro</em> de su worktree —ahí es donde viven git y las rutas relativas— pero además puede leer las otras carpetas del espacio de trabajo, así que «¿dónde acaba esta llamada?» tiene respuesta desde cualquiera de los dos lados. Una sesión que solo lee sigue pudiendo solo leer, en todas partes. También hay una fila encima de los grupos, <em>En todo el espacio de trabajo</em>, para sesiones que no pertenecen a ningún worktree: hazles ahí las preguntas que abarcan todo. No tienen rama, ni cambios, ni terminal, porque eso es de un worktree.',
    '<strong>Ajustes.</strong> Ahora hay tres niveles: Global, el espacio de trabajo y un repositorio concreto. El agente por defecto, el preajuste de permisos y la rama base suelen ser propiedad del conjunto y no de cada repositorio, así que ponlos una vez en el espacio de trabajo; el repositorio que necesite otra cosa lo sigue pudiendo anular. El selector de ámbito de Ajustes elige el nivel, y una sección que no está anulando te dice de dónde vienen sus valores.',
    'La app recuerda cada espacio de trabajo por separado: al volver a uno apareces en el repositorio, el worktree y la disposición de paneles en los que lo dejaste.',
  ]),
  ('providers', 'Agentes y proveedores', [
    '<p>ygd-editor no habla con ningún servicio de IA por sí mismo. Ejecuta las herramientas de línea de comandos que ya tienes —<a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, <a href="https://github.com/openai/codex">Codex</a>, <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a>— con tus propias cuentas, así que el uso, la facturación y las condiciones de datos son exactamente las que acordaste con esos proveedores.</p>'
    '<p>Ajustes › Proveedores de IA conecta cada proveedor con tu propia cuenta: <em>Conectar</em> abre la página de inicio de sesión del proveedor en tu navegador, y la tarjeta muestra después la cuenta, el plan y <em>Cambiar de cuenta</em> / <em>Desconectar</em> / <em>Probar conexión</em>. Codex y Gemini CLI vienen dentro de la aplicación, así que no hay nada que instalar; si tienes tu propia copia instalada, la aplicación usa esa. La licencia de Claude Code no permite incluirlo, así que su tarjeta ofrece <em>Instalar Claude Code</em>, que ejecuta el instalador oficial de Anthropic en el terminal de la tarjeta, en tu carpeta personal y sin contraseña de administrador. El agente y modelo por defecto, y el preajuste de permisos, pueden ser distintos por repositorio.</p>',
  ]),
  ('permissions', 'Permisos', [
    '<p>Los agentes preguntan antes de hacer lo que no hayas aprobado de antemano. Ajustes › Permisos tiene tres preajustes —<em>estricto</em> (solo lectura), <em>equilibrado</em> (leer y editar archivos, preguntar para lo demás) y <em>yolo</em> (también ejecutar comandos, usar la web y hacer push)— más interruptores individuales para leer, editar, ejecutar comandos, acceso web, push y borrado. Sea cual sea el preajuste, un agente nunca borra sin preguntar salvo que lo actives.</p>'
    '<p>Cuando llega una petición, <em>Aprobar</em> y <em>Denegar</em> responden una vez; <em>Permitir siempre</em> recuerda esa herramienta para ese worktree, y la regla desaparece con él.</p>',
  ]),
  ('notifications', 'Notificaciones, bandeja y presupuesto', [
    '<p>Ajustes › Notificaciones elige cuándo te avisa la aplicación: cuando una sesión espera, cuando una termina, cuando cambian los checks de un pull request. Las notificaciones solo aparecen con la ventana en segundo plano, un clic en una salta a la sesión, y la insignia del dock o la barra de tareas puede contar las sesiones en espera.</p>'
    '<p>La barra de presupuesto al pie del panel izquierdo es el gasto real de hoy en todas las sesiones, tomado de los informes de uso de los propios agentes. Ajustes › Presupuesto fija un límite diario y otro por sesión, un umbral de aviso y si las sesiones se pausan al llegar al límite.</p>',
  ]),
  ('settings', 'Ajustes', [
    '<p>Los Ajustes (⌘,) están agrupados por tema. Apariencia fija tema, color de acento, densidad y tipografías; Idioma cambia la interfaz entre inglés, español, italiano, polaco, francés, alemán y turco. Varias secciones llevan la etiqueta <em>por repo</em>: con un repositorio seleccionado arriba puedes sobrescribirlas solo para ese repositorio.</p>'
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
    '<p><strong>macOS dice que no ha podido verificar la aplicación (Trasladar a la Papelera / Aceptar).</strong> Pulsa Aceptar y después Ajustes del Sistema › Privacidad y seguridad › baja hasta Seguridad › <em>Abrir de todos modos</em>, y confirma con tu contraseña. En macOS 14 o anterior, clic derecho › Abrir lo hace en un paso. Si sigue negándose, en Terminal: <code>xattr -d com.apple.quarantine /Applications/ygd-editor.app</code>. Si dice que la aplicación está <em>dañada</em>, la descarga se corrompió: descárgala de nuevo y compárala con <code>SHA256SUMS.txt</code>.</p>'
    '<p><strong>Windows bloquea el instalador.</strong> SmartScreen › Más información › Ejecutar de todas formas. El editor debe ser <em>ygd-editor release signing</em>.</p>'
    '<p><strong>El AppImage no arranca.</strong> Ejecútalo con <code>--appimage-extract-and-run</code> o instala <code>libfuse2</code>.</p>'
    '<p><strong>Un proveedor aparece como «No instalado».</strong> Codex y Gemini CLI vienen con la aplicación, así que significa que la copia de la aplicación está dañada: reinstálala. Para Claude Code, pulsa <em>Instalar Claude Code</em> en su tarjeta; si lo instalaste tú, abre una terminal, comprueba que <code>claude --version</code> funciona y luego Ajustes › Proveedores de IA › Volver a buscar.</p>'
    '<p><strong>Errores de git.</strong> La aplicación explica los habituales en una frase —credenciales, un remoto que avanzó, un archivo de bloqueo, un árbol con cambios, conflictos— y guarda la salida completa en el terminal del worktree.</p>'
    '<p><strong>No aparece ninguna actualización.</strong> Revisa Ajustes › Notificaciones › Ofrecer actualizaciones y pulsa Buscar actualizaciones; la aplicación necesita llegar a github.com.</p>'
    '<p>Cualquier otra cosa: <a href="https://github.com/{repo}/issues">abre un issue</a> contando qué hiciste, qué esperabas y qué pasó.</p>',
  ]),
  ('privacy', 'Privacidad y seguridad', [
    '<p>Todo se ejecuta en tu ordenador. La aplicación en sí se conecta a internet para una sola cosa: consultar las versiones de este sitio en busca de actualizaciones. Los agentes hablan con sus proveedores con tus cuentas; git habla con tus remotos con tus credenciales. Los tokens de proveedor que la aplicación guarda van al llavero del sistema operativo. La interfaz corre en una caja de arena, cada petición que nombra una ruta se comprueba contra los repositorios que realmente abriste, y ningún comando se construye jamás a partir de una cadena de shell.</p>'
    '<p>Para comprobar que una descarga es realmente nuestra, mira <a href="{prefix}index.html#genuine">¿Mi descarga es auténtica?</a> en la página de descarga.</p>',
  ]),
 ],
 # página de versiones y cadenas compartidas
 'dl_version': 'versión {v}',
 'genuine_details': 'los detalles técnicos',
 'lang_label': 'Idioma',
 'title_releases': 'ygd-editor — todas las versiones',
 'r_h1': 'Todas las versiones',
 'r_lead': 'Todas las versiones de ygd-editor que se han publicado. Primero la más reciente para cada sistema y después el historial completo, sistema por sistema. La página de descarga ofrece siempre la versión completa más reciente; esta lista es para quien necesite una en concreto.',
 'r_latest_h': 'La más reciente para cada sistema',
 'r_all_h': 'Todas las versiones, por sistema',
 'r_systems': {'mac': 'macOS', 'win': 'Windows', 'linux': 'Linux'},
 'r_loading': 'Cargando las versiones…',
 'r_error': 'No se pudo leer la lista de versiones ({err}).',
 'r_github': 'Las versiones en GitHub',
 'r_none': 'Aún no hay ninguna versión publicada.',
 'r_notes': 'Qué ha cambiado',
 'r_checksums': 'Sumas de verificación',
 'r_updates': 'Las aplicaciones instaladas se actualizan solas a la versión completa más reciente; nada de lo que hay aquí hace falta descargarlo a mano salvo que quieras una en concreto.',
}
