# Polski. Strings of the download page, the guide and the versions page. HTML fragments and
# {placeholders} stay as they are; keys match tools/strings/en.py, which is the reference.
T = {
 'title_index': 'ygd-editor — pobieranie', 'title_guide': 'ygd-editor — przewodnik użytkownika',
 'desc': 'ygd-editor: uruchamiaj agentów programujących AI w osobnych worktree git, przeglądaj ich zmiany i publikuj je, wszystko z jednego okna. Bezpłatnie dla macOS, Windows i Linux.',
 'nav_download': 'Pobierz', 'nav_guide': 'Przewodnik', 'nav_releases': 'Wszystkie wersje', 'nav_issues': 'Zgłoś problem',
 'tagline': 'Daj każdemu zadaniu własną gałąź i własnego agenta AI — i miej wszystkie na oku.',
 'hero_p': 'ygd-editor otwiera każde zadanie w osobnym worktree git, uruchamia w nim agenta programującego (Claude Code, Codex lub Gemini CLI) i pozwala przejrzeć zmiany, zrobić commit, push i otworzyć pull request bez wychodzenia z okna. Bezpłatnie, dla macOS, Windows i Linux.',
 'dl_loading': 'Szukam najnowszej wersji…', 'dl_for': 'Pobierz dla {label}', 'dl_none': 'Nie opublikowano jeszcze żadnej wersji', 'dl_none_hint': 'Pierwsze wydanie jest w drodze.',
 'dl_error': 'Zobacz wszystkie wersje', 'dl_error_hint': 'Nie udało się odczytać najnowszej wersji ({err}). Na stronie wersji są wszystkie pliki do pobrania.',
 'dl_others': 'Inne systemy:', 'dl_checksums': 'Sumy kontrolne', 'dl_free': 'Bezpłatnie · bez konta · aktualizuje się sam',
 'kinds': {'mac-arm64': 'macOS · Apple Silicon (M1 i nowsze)', 'mac-x64': 'macOS · Intel', 'win-x64': 'Windows', 'linux-appimage': 'Linux · AppImage', 'linux-deb': 'Linux · Debian / Ubuntu'},
 'shot_console': 'Konsola: worktree po lewej, zmiany i diff w środku, sesja agenta po prawej.',
 'what_h': 'Co dostajesz',
 'what': [
   ('Jeden worktree na zadanie', 'Każda gałąź ma własny folder, więc agenci nigdy nie wchodzą sobie w drogę, a ty przełączasz się między zadaniami bez odkładania czegokolwiek na stash.'),
   ('Agenci tam, gdzie jest kod', 'Uruchom Claude Code, Codex lub Gemini CLI w worktree, patrz, jak pracuje, odpowiadaj na jego pytania i przekaż sesję do innego worktree, gdy plany się zmienią.'),
   ('Przeglądaj i publikuj na miejscu', 'Dodaj pliki do stage, przeczytaj diff, poproś agenta o wyjaśnienie lub zmianę zaznaczonego fragmentu, zrób commit, push i otwórz pull request z tego samego ekranu.'),
   ('Nie przeszkadza', 'Jedna skrzynka ze wszystkimi sesjami, które na ciebie czekają, opcjonalne powiadomienia na pulpicie i licznik dzisiejszych wydatków z limitami, które sam ustawiasz.'),
 ],
 'install_h': 'Instalacja w minutę',
 'install_intro': 'Twój komputer ostrzeże cię za pierwszym razem. Tak ma być: nikt nie zapłacił Apple ani Microsoftowi za certyfikat, a ostrzeżenie dotyczy brakujących papierów, nie tego, co robi aplikacja. Oto jak je ominąć — raz, i nigdy więcej na tym komputerze.',
 'install': [
   ('macOS', ['Otwórz pobrany plik <code>.dmg</code>. Okno pokaże te kroki w twoim języku — kliknij <em>Dalej</em> — a potem przeciągnij <strong>ygd-editor</strong> do folderu Aplikacje.', 'Otwórz aplikację. macOS powie, że <em>nie mógł sprawdzić</em> aplikacji, i zaproponuje <em>Przenieś do Kosza</em> lub <em>Gotowe</em>: kliknij <strong>Gotowe</strong>.', 'Otwórz <strong>Ustawienia systemowe › Prywatność i ochrona</strong>, przewiń w dół do sekcji <em>Ochrona</em> i kliknij <strong>Otwórz mimo to</strong> obok ygd-editor. Potwierdź hasłem. To wszystko — macOS nie zapyta ponownie.', 'W macOS 14 lub starszym <strong>kliknij aplikację prawym przyciskiem › Otwórz</strong> — to samo w jednym kroku.', 'Nie wiesz, jakiego masz Maca? Menu Apple › Ten Mac: „Apple M…” to Apple Silicon, cokolwiek z „Intel” to Intel.']),
   ('Windows', ['Uruchom instalator. Gdy SmartScreen powie „System Windows ochronił ten komputer”, kliknij <strong>Więcej informacji</strong>, a potem <strong>Uruchom mimo to</strong>.', 'Wydawca to <em>ygd-editor release signing</em> — to my. Wybierz folder instalacji, jeśli chcesz, i dokończ.', 'Aplikacja pojawi się w menu Start jako ygd-editor.']),
   ('Linux', ['<strong>AppImage:</strong> nadaj mu prawa do uruchamiania (<code>chmod +x ygd-editor-*.AppImage</code>) i uruchom. Jeśli narzeka na FUSE, uruchom go z <code>--appimage-extract-and-run</code>.', '<strong>Debian / Ubuntu:</strong> <code>sudo apt install ./ygd-editor-*.deb</code>, a potem znajdź go w menu aplikacji.']),
 ],
 'need_h': 'Czego potrzebujesz', 'need_p': 'Gita na komputerze i konta u co najmniej jednego dostawcy. <a href="https://github.com/openai/codex">Codex</a> i <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> nie są w instalatorze — dlatego jest mały —: aplikacja pobiera ten, który wybierzesz, gdy pierwszy raz o niego poprosisz (około 100 MB dla Codex, 20 MB dla Gemini CLI), i sprawdza go względem wersji, z którą zbudowano to wydanie, zanim go uruchomi; dla <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, którego licencja nie pozwala go dołączyć, Ustawienia › Dostawcy AI oferują jedno kliknięcie, które uruchamia za ciebie oficjalny instalator Anthropic. Połączenie z dostawcą otwiera jego stronę logowania w przeglądarce. Do pull requestów: <code>gh</code> (GitHub) lub <code>glab</code> (GitLab).',
 'updates_h': 'Aktualizacje dbają o siebie same',
 'updates_p': 'Krótko po uruchomieniu aplikacja sprawdza, czy jest nowa wersja, pobiera ją po cichu i proponuje „Uruchom ponownie, aby zaktualizować”. Ustawienia › Powiadomienia mają też przycisk „Sprawdź aktualizacje” i, jeśli wolisz, opcję samodzielnego instalowania aktualizacji, gdy nic nie działa. Po aktualizacji aplikacja mówi, jaką masz wersję, i linkuje do listy zmian.',
 'genuine_h': 'Czy pobrany plik jest autentyczny?',
 'genuine_p': 'Dwie niezależne kontrole, z których żadna nie opiera się na zaufaniu do nazwy. Nie musisz ich wykonywać; są tu dla tych, którzy chcą.',
 'genuine_prov': '<strong>Pochodzenie.</strong> Każda wersja ma plik <code>SHA256SUMS.txt</code>, podpisany za pośrednictwem <a href="https://www.sigstore.dev/">Sigstore</a> przez własny workflow wydawniczy projektu. Z zainstalowanym <code>cosign</code>:',
 'genuine_sig': '<strong>Podpis kodu.</strong> Aplikacja na macOS i instalator na Windows są podpisane certyfikatem projektu (<a href="{pem}">klucz publiczny</a>). Porównuj odcisk palca, nie nazwę — każdy może nazwać certyfikat, jak chce.',
 'guide_cta_h': 'Pierwszy raz tutaj?', 'guide_cta_p': '<a href="{prefix}guide.html">Przewodnik użytkownika</a> prowadzi przez pierwsze dziesięć minut: otwarcie repozytorium, utworzenie worktree, uruchomienie agenta, przejrzenie i opublikowanie wyniku.',
 'footer_made': 'Autor: Manu Hurtado. Aplikacja jest bezpłatna; kod źródłowy jest prywatny.',
 # przewodnik
 'g_h1': 'Przewodnik użytkownika', 'g_lead': 'Wszystko, czego potrzebujesz na pierwsze popołudnie z ygd-editor, prostymi słowami. Dziesięć minut czytania, a do każdej sekcji możesz wrócić z listy.',
 'g_toc': 'Na tej stronie',
 'g_sections': [
  ('idea', 'Pomysł w jedną minutę', [
    'Git <em>worktree</em> to drugi folder tego samego repozytorium, przełączony na inną gałąź. Zamiast przełączać gałęzie w jednym folderze — i za każdym razem robić stash, przebudowywać i tracić wątek — masz jeden folder na zadanie.',
    'ygd-editor jest zbudowany wokół tego: lewy panel wyświetla listę twoich worktree, środkowy pokazuje, co się zmieniło w wybranym, a prawy uruchamia w nim agenta AI. Dwóch agentów przy dwóch zadaniach pracuje w dwóch folderach i nigdy się nie zderza. Gdy jeden czeka na odpowiedź, skrzynka w nagłówku ci o tym mówi.',
    '<img src="{img}start.png" alt="Strona startowa: ostatnie repozytoria i akcje na start" loading="lazy">',
  ]),
  ('first', 'Twoje pierwsze dziesięć minut', [
    '<ol>'
    '<li><strong>Otwórz repozytorium.</strong> Na stronie startowej wybierz <em>Otwórz repozytorium</em> i wskaż folder, w którym już jest git, albo <em>Sklonuj repozytorium</em> z adresem URL z GitHub, GitLab lub dowolnego serwera git. Ostatnie repozytoria zostają na stronie startowej.</li>'
    '<li><strong>Utwórz worktree.</strong> <em>Nowy worktree</em> (⌘N) proponuje nazwę gałęzi na podstawie zadania i folder, w którym ją umieścić; oba możesz zmienić na dowolną konwencję, której używasz. Git nie pozwala na spacje w nazwie gałęzi, więc zamieniają się w myślniki, a okno pokazuje wynik, zanim cokolwiek utworzy. Gdzie worktree trafiają na dysku i opcjonalny sugerowany prefiks ustawisz w Ustawienia › Git.</li>'
    '<li><strong>Uruchom sesję.</strong> <em>+ Sesja</em> w prawym panelu wybiera agenta i model; domyślny agent to Ustawienia › Domyślny agent. Wpisz, czego chcesz, w kompozytorze. <code>@</code> dołącza pliki lub kontekst, na przykład bieżący diff, <code>/</code> uruchamia polecenia agenta, <code>#</code> jego skille. ⌘↵ wysyła.</li>'
    '<li><strong>Pozwól mu pracować — albo go zatrzymaj.</strong> Transkrypcja pokazuje każde narzędzie, którego agent używa. Gdy potrzebuje zgody na coś, czego wcześniej nie zatwierdzono, sesja przechodzi w stan <em>Czeka na odpowiedź</em>, skrzynka w nagłówku ją zlicza, a ty zezwalasz lub odmawiasz — „Zawsze zezwalaj” zapamiętuje twój wybór dla tego worktree. <em>Zatrzymaj</em> przerywa; wiadomości wpisane w trakcie pracy trafiają do kolejki.</li>'
    '<li><strong>Przejrzyj zmiany.</strong> Zakładka Zmiany wyświetla każdy zmieniony plik razem z tym, kto go zmienił. Kliknij plik, aby zobaczyć diff; zaznacz linie i wybierz <em>Wyjaśnij</em> lub <em>Poproś o zmianę</em>, aby odesłać je do agenta. Ostrzeżenie oznacza pliki, których dotyka też inny worktree tego samego repozytorium.</li>'
    '<li><strong>Commit, push, otwórz PR.</strong> Zaznacz pliki do dodania do stage, napisz wiadomość albo <em>Napisz z AI</em>, <em>Commit</em>. <em>Push</em> ustawia upstream; <em>Otwórz pull request</em> wypełnia tytuł, opis (napisany na podstawie diffu, jeśli chcesz), flagę draft, recenzentów i etykiety, po czym przekazuje sprawę do <code>gh</code> lub <code>glab</code>. Karta worktree pokazuje wtedy PR i jego checki.</li>'
    '</ol>',
    '<img src="{img}console.png" alt="Konsola z otwartym diffem i działającą sesją Claude Code" loading="lazy">',
  ]),
  ('daily', 'Na co dzień', [
    '<p><strong>Główny worktree</strong> — folder, z którego otworzono repozytorium — jest na liście razem z pozostałymi i to od niego odgałęziają się nowe worktree. Wybierz go i kliknij nazwę jego gałęzi w nagłówku: rozwinie się pole wyszukiwania ze wszystkimi gałęziami — twoimi albo takimi, które istnieją tylko na zdalnym repozytorium i które pobierze jako nową gałąź śledzącą. Pisz, aby zawęzić listę, strzałki i Enter, aby się przełączyć. Gałąź, którą ma już inny worktree, jest na liście, ale wyszarzona, bo git pozwala na jedną gałąź w jednym worktree naraz.</p>'
    '<p><strong>Aktualizuj z bazy</strong> na worktree robi fetch i rebase na gałęzi bazowej; konflikty zatrzymują proces z listą plików, rozwiązujesz je, dodajesz do stage i <em>Kontynuuj</em>. <strong>Fetch</strong> odświeża liczniki przed/za. Zakładka Terminal to prawdziwa powłoka w folderze worktree; Aktywność to oś czasu tego, co się tam działo — commity, pushe, sesje — i przetrwa restarty.</p>'
    '<p><strong>Przekazywanie.</strong> Sesję można przenieść do innego worktree z jej menu, razem z transkrypcją, gdy zorientujesz się, że praca należy do innej gałęzi.</p>'
    '<p><strong>Usunięcie worktree</strong> kończy jego sesje, archiwizuje ich logi i zapomina jego reguły uprawnień; gałąź zostaje, chyba że ją usuniesz. Ustawienia › Git mogą same usunąć worktree, gdy jego PR zostanie scalony.</p>'
    '<p><strong>Wiele repozytoriów.</strong> Otwórz, ile chcesz; nagłówek przełącza między nimi, a skrzynka zlicza oczekujące sesje ze wszystkich.</p>',
  ]),
  ('workspaces', 'Praca z kilkoma repozytoriami: przestrzenie robocze', [
    '<em>Przestrzeń robocza</em> to nazwany zestaw folderów, które aplikacja trzyma otwarte razem. Gateway, konsola webowa i folder z notatkami to często jeden kawałek pracy, a pytanie o jeden z nich zwykle znajduje odpowiedź w innym — przestrzeń robocza to sposób, by powiedzieć aplikacji, że należą do siebie.',
    '<img src="{img}workspace.png" alt="Przestrzeń robocza z dwoma repozytoriami: pasek boczny grupuje worktree według repozytorium" loading="lazy">',
    '<strong>Tworzenie.</strong> Otwórz drugie repozytorium, gdy jedno jest już otwarte, a aplikacja zapyta, gdzie je umieścić: dodać do tego, nad czym pracujesz, utworzyć nową przestrzeń roboczą z obydwoma albo otworzyć osobno. Escape oznacza „osobno”. Możesz też utworzyć przestrzeń ze strony startowej przez <em>Nowa przestrzeń robocza</em>, a foldery dodawać i usuwać później przyciskiem Przestrzenie robocze w nagłówku. Usunięcie folderu z przestrzeni roboczej nigdy niczego nie kasuje — zmienia się tylko zestaw.',
    '<strong>Z VS Code.</strong> Jeśli twój zespół ma już plik <code>.code-workspace</code>, <em>Otwórz plik przestrzeni roboczej…</em> go wczyta: te same foldery, w tej samej kolejności, nazwane tak, jak nazywa je VS Code. Komentarze i końcowe przecinki w pliku nie przeszkadzają. Foldery, które nie są repozytoriami git, zostają — po prostu nie mają worktree — a o folderze, który zniknął, aplikacja informuje, zamiast po cichu go pominąć. <em>Zapisz do pliku</em> zapisuje go z powrotem, nie ruszając części, których aplikacja nie używa, więc ten sam plik dalej działa w obu narzędziach.',
    '<strong>Co pokazuje pasek boczny.</strong> Worktree pogrupowane według repozytorium, każda grupa zwijana, a filtr dopasowuje nazwę gałęzi lub repozytorium, więc znajdziesz gałąź bez pamiętania, gdzie mieszka. Zwinięta grupa nadal pokazuje, co w niej działa, i nadal mówi, gdy jakaś sesja czeka. Przy jednym repozytorium grup nie ma wcale.',
    '<strong>Co widzą agenci.</strong> Sesja nadal działa <em>w</em> swoim worktree — tam należą git i każda ścieżka względna — ale może też czytać pozostałe foldery przestrzeni roboczej, więc na „gdzie trafia to wywołanie?” da się odpowiedzieć z obu stron. Sesja, która tylko czyta, nadal może tylko czytać, wszędzie. Nad grupami jest też wiersz <em>W całej przestrzeni roboczej</em>, dla sesji, które nie należą do żadnego worktree: im zadawaj pytania obejmujące cały stack. Nie mają gałęzi, zmian ani terminala, bo to należy do worktree.',
    '<strong>Ustawienia.</strong> Teraz trzy poziomy: Globalne, przestrzeń robocza, potem pojedyncze repozytorium. Domyślny agent, preset uprawnień i gałąź bazowa są zwykle cechą całego stacku, a nie każdego repozytorium z osobna, więc ustaw je raz w przestrzeni roboczej; repozytorium, które potrzebuje czegoś innego, nadal może je nadpisać. Selektor zakresu w Ustawieniach wybiera poziom, a sekcja, która nie nadpisuje, mówi, skąd biorą się jej wartości.',
    'Aplikacja pamięta każdą przestrzeń roboczą osobno: wróć do jednego z nich i wylądujesz w repozytorium, worktree i układzie paneli, które były otwarte przy wyjściu.',
  ]),
  ('providers', 'Agenci i dostawcy', [
    '<p>ygd-editor sam nie rozmawia z żadną usługą AI. Uruchamia narzędzia wiersza poleceń, które już masz — <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, <a href="https://github.com/openai/codex">Codex</a>, <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> — z twoimi własnymi kontami, więc zużycie, rozliczenia i warunki dotyczące danych są dokładnie te, które obowiązują cię u tych dostawców.</p>'
    '<p>Ustawienia › Dostawcy AI łączą każdego dostawcę z twoim własnym kontem: <em>Połącz</em> otwiera stronę logowania dostawcy w przeglądarce, a karta pokazuje potem konto, plan oraz <em>Zmień konto</em> / <em>Odłącz</em> / <em>Testuj połączenie</em>. Codex i Gemini CLI aplikacja pobiera, gdy wybierzesz je po raz pierwszy — karta podaje wersję i rozmiar, pokazuje postęp, a <em>Usuń pobrane</em> znów je usuwa; jeśli masz zainstalowaną własną kopię, aplikacja używa właśnie jej. Licencja Claude Code nie pozwala go dołączyć, więc jego karta oferuje <em>Zainstaluj Claude Code</em>, co uruchamia oficjalny instalator Anthropic w terminalu na karcie, do twojego folderu domowego, bez hasła administratora. Domyślny agent i model oraz preset uprawnień mogą się różnić dla każdego repozytorium.</p>',
  ]),
  ('permissions', 'Uprawnienia', [
    '<p>Agenci pytają, zanim zrobią coś, czego wcześniej nie zatwierdzono. Ustawienia › Uprawnienia mają trzy presety — <em>ścisły</em> (tylko odczyt), <em>zrównoważony</em> (odczyt i edycja plików, pytanie o wszystko inne) i <em>yolo</em> (dodatkowo uruchamianie poleceń, dostęp do sieci i push) — plus osobne przełączniki dla odczytu, edycji, uruchamiania poleceń, dostępu do sieci, pusha i usuwania. Niezależnie od presetu agent nigdy nie usuwa bez pytania, chyba że to włączysz.</p>'
    '<p>Gdy przychodzi prośba, <em>Zatwierdź</em> i <em>Odmów</em> odpowiadają jednorazowo; <em>Zawsze zezwalaj</em> zapamiętuje to narzędzie dla tego worktree, a reguła znika razem z worktree.</p>',
  ]),
  ('notifications', 'Powiadomienia, skrzynka i budżet', [
    '<p>Ustawienia › Powiadomienia decydują, kiedy aplikacja da ci znać: gdy sesja czeka, gdy jakaś się skończy, gdy zmienią się checki pull requesta. Powiadomienia pokazują się tylko wtedy, gdy okno nie jest na pierwszym planie, kliknięcie w jedno z nich przenosi do sesji, a plakietka w Docku lub na pasku zadań może zliczać oczekujące sesje.</p>'
    '<p>Pasek budżetu na dole lewego panelu to dzisiejsze rzeczywiste wydatki we wszystkich sesjach, wzięte z raportów zużycia samych agentów. Ustawienia › Budżet ustawiają limit dzienny i limit na sesję, próg ostrzeżenia oraz to, czy sesje mają się wstrzymywać po osiągnięciu limitu.</p>',
  ]),
  ('settings', 'Ustawienia', [
    '<p>Ustawienia (⌘,) są pogrupowane tematycznie. Wygląd ustawia motyw, kolor akcentu, gęstość i czcionki; Język przełącza interfejs między angielskim, hiszpańskim, włoskim, polskim, francuskim, niemieckim i tureckim. Kilka sekcji ma plakietkę <em>na repo</em>: z repozytorium wybranym u góry możesz je nadpisać tylko dla tego repozytorium.</p>'
    '<p>Wszystko zapisuje się automatycznie do <code>settings.json</code> w folderze aplikacji w twoim katalogu domowym; <em>Otwórz settings.json</em> edytuje surowy plik z walidacją, a nagłówek pokazuje, kiedy został ostatnio zapisany.</p>',
    '<img src="{img}settings.png" alt="Ustawienia › Wygląd" loading="lazy">',
  ]),
  ('updates', 'Aktualizacje', [
    '<p>Krótko po uruchomieniu aplikacja sprawdza wydania na tej stronie, pobiera nową wersję w tle i proponuje <em>Uruchom ponownie, aby zaktualizować</em>. Ustawienia › Powiadomienia mają przełącznik <em>Proponuj aktualizacje</em>, przycisk <em>Sprawdź aktualizacje</em> z godziną ostatniego sprawdzenia oraz <em>Instaluj aktualizacje automatycznie</em>: gdy jest włączony, pobrana aktualizacja sama restartuje aplikację po 15-sekundowym odliczaniu, które możesz anulować — tylko gdy żadna sesja nie działa ani nie czeka; w przeciwnym razie instaluje się przy wyjściu. Pierwsze uruchomienie po aktualizacji mówi, jaką masz wersję, i linkuje do listy zmian.</p>',
  ]),
  ('shortcuts', 'Skróty klawiszowe', [
    '<table><tr><td>⌘O</td><td>Otwórz repozytorium</td></tr><tr><td>⇧⌘C</td><td>Sklonuj repozytorium</td></tr><tr><td>⌘N</td><td>Nowy worktree</td></tr><tr><td>⌘,</td><td>Ustawienia</td></tr><tr><td>⌘↵</td><td>Wyślij wiadomość</td></tr></table>'
    '<p>W Windows i Linux czytaj ⌘ jako Ctrl. Każdy skrót można zmienić w Ustawienia › Skróty klawiszowe.</p>',
  ]),
  ('trouble', 'Gdy coś pójdzie nie tak', [
    '<p><strong>macOS mówi, że nie mógł sprawdzić aplikacji (Przenieś do Kosza / Gotowe).</strong> Kliknij Gotowe, potem Ustawienia systemowe › Prywatność i ochrona › przewiń do sekcji Ochrona › <em>Otwórz mimo to</em> i potwierdź hasłem. W macOS 14 lub starszym prawy przycisk › Otwórz robi to w jednym kroku. Jeśli nadal odmawia, w Terminalu: <code>xattr -d com.apple.quarantine /Applications/ygd-editor.app</code>. Jeśli mówi, że aplikacja jest <em>uszkodzona</em>, pobrany plik jest uszkodzony: pobierz go ponownie i porównaj z <code>SHA256SUMS.txt</code>.</p>'
    '<p><strong>Windows blokuje instalator.</strong> SmartScreen › Więcej informacji › Uruchom mimo to. Wydawca powinien brzmieć <em>ygd-editor release signing</em>.</p>'
    '<p><strong>AppImage się nie uruchamia.</strong> Uruchom go z <code>--appimage-extract-and-run</code> albo zainstaluj <code>libfuse2</code>.</p>'
    '<p><strong>Dostawca pokazuje „Nie zainstalowano”.</strong> Codex i Gemini CLI są pobierane na żądanie: kliknij <em>Pobierz</em> na karcie; jeśli pobieranie się nie uda, karta mówi dlaczego (brak sieci albo plik, który nie zgadzał się z sumą kontrolną i został odrzucony). W przypadku Claude Code kliknij <em>Zainstaluj Claude Code</em> na jego karcie; jeśli to twoja własna instalacja, otwórz terminal, sprawdź, czy <code>claude --version</code> działa, a potem Ustawienia › Dostawcy AI › Skanuj ponownie.</p>'
    '<p><strong>Błędy gita.</strong> Aplikacja wyjaśnia typowe w jednym zdaniu — dane logowania, zdalne repozytorium, które poszło dalej, plik blokady, niezacommitowane zmiany, konflikty — a pełne wyjście trzyma w terminalu worktree.</p>'
    '<p><strong>Nie pojawia się żadna aktualizacja.</strong> Sprawdź Ustawienia › Powiadomienia › Proponuj aktualizacje, potem Sprawdź aktualizacje; aplikacja musi mieć dostęp do github.com.</p>'
    '<p>Cokolwiek innego: <a href="https://github.com/{repo}/issues">zgłoś issue</a>, opisując swoje kroki, oczekiwany wynik i to, co się stało.</p>',
  ]),
  ('privacy', 'Prywatność i bezpieczeństwo', [
    '<p>Wszystko działa na twoim komputerze. Sama aplikacja łączy się z internetem w jednym celu: sprawdza wydania na tej stronie w poszukiwaniu aktualizacji. Agenci rozmawiają ze swoimi dostawcami przez twoje konta; git rozmawia z twoimi zdalnymi repozytoriami przez twoje dane logowania. Tokeny dostawców, które aplikacja przechowuje, trafiają do pęku kluczy systemu operacyjnego. Interfejs działa w piaskownicy, każde żądanie, które wskazuje ścieżkę, jest sprawdzane względem repozytoriów, które faktycznie otwarto, a żadne polecenie nie jest nigdy budowane z ciągu znaków powłoki.</p>'
    '<p>Aby sprawdzić, czy pobrany plik naprawdę pochodzi od nas, zobacz <a href="{prefix}index.html#genuine">Czy pobrany plik jest autentyczny?</a> na stronie pobierania.</p>',
  ]),
 ],
 # strona wersji i wspólne krótkie teksty
 'dl_version': 'wersja {v}',
 'genuine_details': 'szczegóły techniczne',
 'lang_label': 'Język',
 'title_releases': 'ygd-editor — wszystkie wersje',
 'r_h1': 'Wszystkie wersje',
 'r_lead': 'Każda opublikowana wersja ygd-editor. Najpierw najnowsza dla każdego systemu, potem cała historia, system po systemie. Strona pobierania zawsze oferuje najnowszą kompletną wersję; ta lista jest dla tych, którzy potrzebują konkretnej.',
 'r_latest_h': 'Najnowsza dla każdego systemu',
 'r_all_h': 'Każda wersja, według systemu',
 'r_systems': {'mac': 'macOS', 'win': 'Windows', 'linux': 'Linux'},
 'r_loading': 'Wczytuję wersje…',
 'r_error': 'Nie udało się odczytać listy wersji ({err}).',
 'r_github': 'Wydania na GitHub',
 'r_none': 'Nie opublikowano jeszcze żadnej wersji.',
 'r_notes': 'Co się zmieniło',
 'r_checksums': 'Sumy kontrolne',
 'r_updates': 'Zainstalowane aplikacje same aktualizują się do najnowszej kompletnej wersji; niczego stąd nie trzeba pobierać ręcznie, chyba że chcesz konkretną.',
}
