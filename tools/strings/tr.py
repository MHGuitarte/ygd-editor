# Türkçe. Strings of the download page, the guide and the versions page. HTML fragments and
# {placeholders} stay as they are; keys match tools/strings/en.py, which is the reference.
T = {
 'title_index': 'ygd-editor — indir', 'title_guide': 'ygd-editor — kullanım kılavuzu',
 'desc': 'ygd-editor: yapay zekâ kodlama ajanlarını ayrı git worktree’lerinde çalıştır, değişikliklerini incele ve yayınla; hepsi tek pencereden. macOS, Windows ve Linux için ücretsiz.',
 'nav_download': 'İndir', 'nav_guide': 'Kılavuz', 'nav_releases': 'Tüm sürümler', 'nav_issues': 'Sorun bildir',
 'tagline': 'Her göreve kendi dalını ve kendi yapay zekâ ajanını ver — ve hepsini gözünün önünde tut.',
 'hero_p': 'ygd-editor her görevi kendi git worktree’sinde açar, içinde bir kodlama ajanı çalıştırır (Claude Code, Codex veya Gemini CLI) ve pencereden çıkmadan değişiklikleri incelemene, commit ve push yapmana ve pull request açmana izin verir. macOS, Windows ve Linux için ücretsiz.',
 'dl_loading': 'En son sürüm aranıyor…', 'dl_for': '{label} için indir', 'dl_none': 'Henüz yayınlanmış sürüm yok', 'dl_none_hint': 'İlk sürüm yolda.',
 'dl_error': 'Tüm sürümleri gör', 'dl_error_hint': 'En son sürüm okunamadı ({err}). Sürümler sayfasında tüm indirmeler var.',
 'dl_others': 'Diğer sistemler:', 'dl_checksums': 'Sağlama toplamları', 'dl_free': 'Ücretsiz · hesap gerekmez · kendini günceller',
 'kinds': {'mac-arm64': 'macOS · Apple Silicon (M1 ve sonrası)', 'mac-x64': 'macOS · Intel', 'win-x64': 'Windows', 'linux-appimage': 'Linux · AppImage', 'linux-deb': 'Linux · Debian / Ubuntu'},
 'shot_console': 'Konsol: solda worktree’ler, ortada değişiklikler ve diff, sağda ajan oturumu.',
 'what_h': 'Neler sunuyor',
 'what': [
   ('Her göreve bir worktree', 'Her dalın kendi klasörü var; ajanlar birbirinin ayağına basmaz ve hiçbir şeyi stash’lemeden görev değiştirirsin.'),
   ('Ajanlar kodun olduğu yerde', 'Claude Code, Codex veya Gemini CLI’ı bir worktree’nin içinde başlat, çalışmasını izle, sorularını yanıtla ve planlar değişince oturumu başka bir worktree’ye devret.'),
   ('Yerinden kalkmadan incele ve yayınla', 'Dosyaları stage’e al, diff’i oku, ajandan bir seçimi açıklamasını veya değiştirmesini iste, commit ve push yap, pull request’i aynı ekrandan aç.'),
   ('İşine karışmaz', 'Seni bekleyen tüm oturumlar için tek bir gelen kutusu, isteğe bağlı masaüstü bildirimleri ve senin belirlediğin limitlerle günlük harcama göstergesi.'),
 ],
 'install_h': 'Bir dakikada kur',
 'install_intro': 'Bilgisayarın ilk seferinde seni uyaracak. Bu beklenen bir şey: kimse Apple’a ya da Microsoft’a sertifika parası ödemedi ve uyarı eksik evrak işiyle ilgili, uygulamanın yaptığı bir şeyle değil. Şöyle geçilir — bir kez, ve o bilgisayarda bir daha asla.',
 'install': [
   ('macOS', ['İndirdiğin <code>.dmg</code> dosyasını aç. Bir pencere bu adımları senin dilinde gösterir — <em>Devam</em>’a tıkla — sonra <strong>ygd-editor</strong>’ü Uygulamalar klasörüne sürükle.', 'Uygulamayı aç. macOS uygulamayı <em>doğrulayamadığını</em> söyler ve <em>Çöp Sepeti’ne Taşı</em> ya da <em>Bitti</em> seçeneklerini sunar: <strong>Bitti</strong>’ye tıkla.', '<strong>Sistem Ayarları › Gizlilik ve Güvenlik</strong>’i aç, <em>Güvenlik</em> bölümüne kadar in ve ygd-editor’ün yanındaki <strong>Yine de Aç</strong>’a tıkla. Parolanla onayla. Hepsi bu — macOS bir daha sormaz.', 'macOS 14 veya daha eskisinde <strong>uygulamaya sağ tıkla › Aç</strong> aynı şeyi tek adımda yapar.', 'Hangi Mac’e sahip olduğundan emin değil misin? Apple menüsü › Bu Mac Hakkında: “Apple M…” yazıyorsa Apple Silicon, “Intel” geçiyorsa Intel.']),
   ('Windows', ['Yükleyiciyi çalıştır. SmartScreen “Windows bilgisayarınızı korudu” dediğinde <strong>Ek bilgi</strong>’ye, sonra <strong>Yine de çalıştır</strong>’a tıkla.', 'Gösterilen yayımcı <em>ygd-editor release signing</em> — o biziz. İstersen kurulum klasörünü seç ve bitir.', 'Uygulama Başlat menüsünde ygd-editor olarak görünür.']),
   ('Linux', ['<strong>AppImage:</strong> çalıştırılabilir yap (<code>chmod +x ygd-editor-*.AppImage</code>) ve çalıştır. FUSE hakkında şikâyet ederse <code>--appimage-extract-and-run</code> ile çalıştır.', '<strong>Debian / Ubuntu:</strong> <code>sudo apt install ./ygd-editor-*.deb</code>, sonra uygulama menünde bul.']),
 ],
 'need_h': 'Neye ihtiyacın var', 'need_p': 'Bilgisayarında Git ve en az bir sağlayıcıda bir hesap. <a href="https://github.com/openai/codex">Codex</a> ve <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> yükleyicinin içinde değildir — onu küçük tutan da budur —: uygulama seçtiğini ilk istediğinde indirir (Codex için yaklaşık 100 MB, Gemini CLI için 20 MB) ve çalıştırmadan önce bu sürümün yapıldığı sürümle karşılaştırıp doğrular; lisansı birlikte dağıtılmasına izin vermeyen <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a> için Ayarlar › Yapay zekâ sağlayıcıları, Anthropic’in resmî yükleyicisini senin için çalıştıran tek tıklık bir seçenek sunar. Bir sağlayıcıyı bağlamak, giriş sayfasını tarayıcında açar. Pull request’ler için GitHub’da <code>gh</code>, GitLab’da <code>glab</code>.',
 'updates_h': 'Güncellemeler kendi kendine olur',
 'updates_p': 'Açılıştan kısa süre sonra uygulama yeni bir sürüm olup olmadığına bakar, sessizce indirir ve “Güncellemek için yeniden başlat” seçeneğini sunar. Ayarlar › Bildirimler’de ayrıca bir “Güncellemeleri kontrol et” düğmesi ve istersen, hiçbir şey çalışmıyorken güncellemeleri kendi başına kurma seçeneği var. Güncellemeden sonra uygulama hangi sürümde olduğunu söyler ve nelerin değiştiğine bağlantı verir.',
 'genuine_h': 'İndirdiğim dosya gerçek mi?',
 'genuine_p': 'Birbirinden bağımsız iki kontrol; ikisi de bir isme güvenmeye dayanmaz. Bunları çalıştırman gerekmez; isteyenler için buradalar.',
 'genuine_prov': '<strong>Köken.</strong> Her sürüm, projenin kendi yayın iş akışı tarafından <a href="https://www.sigstore.dev/">Sigstore</a> ile imzalanmış bir <code>SHA256SUMS.txt</code> dosyasıyla gelir. <code>cosign</code> kuruluyken:',
 'genuine_sig': '<strong>Kod imzası.</strong> macOS uygulaması ve Windows yükleyicisi projenin sertifikasıyla imzalanmıştır (<a href="{pem}">açık anahtar</a>). İsmi değil parmak izini karşılaştır — bir sertifikaya herkes istediği ismi verebilir.',
 'guide_cta_h': 'Yeni misin?', 'guide_cta_p': '<a href="{prefix}guide.html">Kullanım kılavuzu</a> ilk on dakikayı adım adım anlatır: bir depo açmak, bir worktree oluşturmak, bir ajan başlatmak, sonucu incelemek ve yayınlamak.',
 'footer_made': 'Manu Hurtado tarafından yapıldı. Uygulama ücretsizdir; kaynak kodu kapalıdır.',
 # guide
 'g_h1': 'Kullanım kılavuzu', 'g_lead': 'ygd-editor ile ilk öğleden sonran için gereken her şey, sade sözlerle. Okuması on dakika; listeden istediğin bölüme geri dönebilirsin.',
 'g_toc': 'Bu sayfada',
 'g_sections': [
  ('idea', 'Fikir, bir dakikada', [
    'Bir git <em>worktree</em>’si, aynı deponun başka bir dalda checkout edilmiş ikinci bir klasörüdür. Tek klasörde dal değiştirmek — ve her seferinde stash’lemek, yeniden derlemek ve kaldığın yeri kaybetmek — yerine görev başına bir klasör tutarsın.',
    'ygd-editor bunun etrafında kurulu: sol panel worktree’lerini listeler, ortadaki seçtiğinde neyin değiştiğini gösterir, sağdaki ise içinde bir yapay zekâ ajanı çalıştırır. İki görevdeki iki ajan iki klasörde çalışır ve asla çarpışmaz. Biri yanıt beklerken üst bardaki gelen kutusu sana haber verir.',
    '<img src="{img}start.png" alt="Başlangıç sayfası: son depolar ve başlangıç eylemleri" loading="lazy">',
  ]),
  ('first', 'İlk on dakikan', [
    '<ol>'
    '<li><strong>Bir depo aç.</strong> Başlangıç sayfasında <em>Depo aç</em>’ı seç ve içinde zaten git olan bir klasör seç, ya da <em>Depo klonla</em> ile bir GitHub, GitLab veya herhangi bir git URL’si kullan. Son depolar başlangıç sayfasında kalır.</li>'
    '<li><strong>Bir worktree oluştur.</strong> <em>Yeni worktree</em> (⌘N) görevden bir dal adı ve onu koyacak bir klasör önerir; ikisini de kullandığın kurala göre dilediğin gibi yeniden adlandırabilirsin. Git dal adında boşluğa izin vermez, bu yüzden boşluklar tireye dönüşür ve iletişim kutusu bir şey oluşturmadan önce sonucu gösterir. Worktree’lerin diskte nereye gideceği ve isteğe bağlı önerilen önek Ayarlar › Git’te.</li>'
    '<li><strong>Bir oturum başlat.</strong> Sağ paneldeki <em>+ Oturum</em> bir ajan ve bir model seçer; varsayılan ajan Ayarlar › Varsayılan ajan’da. Ne istediğini yazma alanına yaz. <code>@</code> dosya ya da geçerli diff gibi bağlam ekler, <code>/</code> ajanın komutlarını, <code>#</code> skill’lerini çalıştırır. ⌘↵ gönderir.</li>'
    '<li><strong>Çalışmasına izin ver — ya da durdur.</strong> Transkript ajanın kullandığı her aracı gösterir. Önceden onaylamadığın bir şey için izin gerektiğinde oturum <em>bekliyor</em> durumuna geçer, üst bardaki gelen kutusu onu sayar ve sen onaylar ya da reddedersin — “Her zaman izin ver” seçimini o worktree için hatırlar. <em>Durdur</em> keser; o çalışırken yazdığın istemler sıraya alınır.</li>'
    '<li><strong>Değişiklikleri incele.</strong> Değişiklikler sekmesi dokunulan her dosyayı kimin değiştirdiğiyle birlikte listeler. Diff için bir dosyaya tıkla; satırları seç ve ajana geri göndermek için <em>Açıkla</em> ya da <em>Değişiklik iste</em>’yi seç. Aynı deponun başka bir worktree’sinin de dokunduğu dosyaları bir uyarı işaretler.</li>'
    '<li><strong>Commit, push, PR’ı aç.</strong> Stage’e alınacak dosyaları işaretle, mesajı yaz ya da <em>Yapay zekâ ile yaz</em>, <em>Commit</em>. <em>Push</em> upstream’i ayarlar; <em>Pull request aç</em> başlığı, gövdeyi (istersen diff’ten taslak olarak), taslak işaretini, gözden geçirenleri ve etiketleri doldurur ve işi <code>gh</code> ya da <code>glab</code>’a devreder. Worktree kartı sonra PR’ı ve kontrollerini gösterir.</li>'
    '</ol>',
    '<img src="{img}console.png" alt="Açık bir diff ve çalışan bir Claude Code oturumuyla konsol" loading="lazy">',
  ]),
  ('daily', 'Günlük kullanımda', [
    '<p><strong>Ana worktree</strong> — depoyu açtığın klasör — diğerleriyle birlikte listelenir ve yeni worktree’lerin dallandığı yerdir. Onu seç ve üst barda dal adına tıkla: tüm dalları kapsayan bir arama kutusu açılır — seninkiler ya da yalnızca uzak depoda bulunan ve yeni bir izleme dalı olarak checkout edilen bir dal. Daraltmak için yaz, geçmek için ok tuşları ve Enter. Başka bir worktree’nin zaten tuttuğu bir dal listelenir ama gri görünür, çünkü git bir dala aynı anda tek bir worktree’de izin verir.</p>'
    '<p>Bir worktree’de <strong>Temel daldan güncelle</strong> fetch yapar ve onu temel dalın üzerine rebase eder; çakışmalar dosyalar listelenmiş halde durur, onları çözersin, stage’e alırsın ve <em>Devam</em>. <strong>Fetch</strong> ileri/geri sayaçlarını yeniler. Terminal sekmesi worktree klasöründe gerçek bir kabuktur; Etkinlik, orada olanların — commit’ler, push’lar, oturumlar — zaman çizelgesidir ve yeniden başlatmalarda kaybolmaz.</p>'
    '<p><strong>Devretme.</strong> İşin başka bir dala ait olduğunu fark ettiğinde bir oturum, menüsünden, transkriptiyle birlikte başka bir worktree’ye taşınabilir.</p>'
    '<p><strong>Bir worktree’yi kaldırmak</strong> oturumlarını sonlandırır, günlüklerini arşivler ve izin kurallarını unutur; sen silmezsen dal kalır. Ayarlar › Git, PR’ı birleştikten sonra worktree’yi kendi başına silebilir.</p>'
    '<p><strong>Birden fazla depo.</strong> İstediğin kadar aç; üst bar aralarında geçiş yapar ve gelen kutusu hepsindeki bekleyen oturumları sayar.</p>',
  ]),
  ('workspaces', 'Birden fazla depoyla çalışmak: çalışma alanları', [
    'Bir <em>çalışma alanı</em>, uygulamanın birlikte açık tuttuğu adlandırılmış bir klasör kümesidir. Bir gateway, bir web konsolu ve bir not klasörü çoğu zaman tek bir işin parçasıdır ve birindeki bir sorunun yanıtı genellikle diğerindedir — çalışma alanı, uygulamaya bunların birbirine ait olduğunu söyleme yolundur.',
    '<img src="{img}workspace.png" alt="İki depolu bir çalışma alanı: kenar çubuğu worktree’leri depoya göre gruplar" loading="lazy">',
    '<strong>Bir tane oluşturmak.</strong> Biri zaten açıkken ikinci bir depo aç; uygulama nereye gideceğini sorar: üzerinde çalıştığına ekle, ikisiyle yeni bir çalışma alanı başlat ya da kendi başına aç. Escape “kendi başına” demektir. Başlangıç sayfasından <em>Yeni çalışma alanı</em> ile de bir tane başlatabilir, sonra üst bardaki çalışma alanları düğmesinden klasör ekleyip çıkarabilirsin. Bir klasörü çalışma alanından çıkarmak hiçbir şeyi silmez — yalnızca küme değişir.',
    '<strong>VS Code’dan.</strong> Ekibin zaten bir <code>.code-workspace</code> dosyası tutuyorsa <em>Çalışma alanı dosyası aç…</em> onu okur: aynı klasörler, aynı sırada, VS Code’un adlandırdığı gibi. Dosyadaki yorumlar ve sondaki virgüller sorun değil. Git deposu olmayan klasörler korunur — yalnızca worktree’leri olmaz — ve kaybolmuş bir klasör sessizce atılmak yerine bildirilir. <em>Dosyaya kaydet</em> onu geri yazar ve uygulamanın kullanmadığı kısımlara dokunmaz; böylece aynı dosya iki araçta da çalışmaya devam eder.',
    '<strong>Kenar çubuğu ne gösterir.</strong> Depoya göre gruplanmış worktree’ler, her grup katlanabilir; filtre dal adıyla da depo adıyla da eşleşir, böylece nerede yaşadığını hatırlamadan bir dalı bulabilirsin. Katlanmış bir grup içinde neyin çalıştığını yine gösterir ve bir oturum beklerken yine söyler. Tek depoda hiç grup görünmez.',
    '<strong>Ajanlar ne görebilir.</strong> Bir oturum yine worktree’sinin <em>içinde</em> çalışır — git ve her göreli yol oraya aittir — ama çalışma alanının diğer klasörlerini de okuyabilir, böylece “bu çağrı nerede bitiyor?” sorusu iki taraftan da yanıtlanabilir. Yalnızca okuyan bir oturumun her yerde yalnızca okumaya izni vardır. Grupların üstünde bir de <em>Çalışma alanı genelinde</em> satırı var: tek bir worktree’ye ait olmayan oturumlar için. Bütün yığını kapsayan soruları onlara sor. Dalları, değişiklikleri ve terminalleri yok, çünkü bunlar bir worktree’ye aittir.',
    '<strong>Ayarlar.</strong> Artık üç düzey var: Genel, çalışma alanı ve tek bir depo. Varsayılan ajan, izin ön ayarı ve temel dal genellikle içindeki her deponun değil yığının bir özelliğidir; o yüzden onları çalışma alanında bir kez ayarla, farklı bir şeye ihtiyaç duyan depo yine geçersiz kılabilir. Ayarlar’daki kapsam seçici düzeyi seçer ve geçersiz kılmayan bir bölüm değerlerinin nereden geldiğini söyler.',
    'Uygulama her çalışma alanını ayrı hatırlar: birine geri döndüğünde bıraktığın depoya, worktree’ye ve panel düzenine düşersin.',
  ]),
  ('providers', 'Ajanlar ve sağlayıcılar', [
    '<p>ygd-editor hiçbir yapay zekâ servisiyle kendisi konuşmaz. Zaten sahip olduğun komut satırı araçlarını — <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a>, <a href="https://github.com/openai/codex">Codex</a>, <a href="https://github.com/google-gemini/gemini-cli">Gemini CLI</a> — kendi hesaplarınla çalıştırır; yani kullanım, faturalama ve veri koşulları tam olarak o sağlayıcılarla anlaştığın koşullardır.</p>'
    '<p>Ayarlar › Yapay zekâ sağlayıcıları her sağlayıcıyı kendi hesabınla bağlar: <em>Bağla</em> sağlayıcının giriş sayfasını tarayıcında açar, kart sonra hesabı, planı ve <em>Hesap değiştir</em> / <em>Bağlantıyı kes</em> / <em>Bağlantıyı test et</em> seçeneklerini gösterir. Codex ve Gemini CLI’yi uygulama ilk seçtiğinde indirir — kart sürümü ve boyutu söyler, ilerlemeyi gösterir ve <em>İndirmeyi kaldır</em> onu yeniden siler; kendi kopyan kuruluysa uygulama onu kullanır. Claude Code’un lisansı birlikte dağıtılmasına izin vermez, bu yüzden kartı <em>Claude Code kur</em> seçeneğini sunar: Anthropic’in resmî yükleyicisini kartın terminalinde, ev klasörüne, yönetici parolası olmadan çalıştırır. Varsayılan ajan ve model ile izin ön ayarı depo başına farklı olabilir.</p>',
  ]),
  ('permissions', 'İzinler', [
    '<p>Ajanlar önceden onaylamadığın şeyleri yapmadan önce sorar. Ayarlar › İzinler’de üç ön ayar var — <em>katı</em> (yalnızca okuma), <em>dengeli</em> (dosya okuma ve düzenleme, geri kalan her şey için sorma) ve <em>yolo</em> (ayrıca komut çalıştırma, web kullanma ve push) — ayrıca okuma, düzenleme, komut çalıştırma, web erişimi, push ve silme için tekil anahtarlar. Ön ayar ne olursa olsun, sen açmadığın sürece bir ajan asla sormadan silemez.</p>'
    '<p>Bir istek geldiğinde <em>Onayla</em> ve <em>Reddet</em> bir kez yanıtlar; <em>Her zaman izin ver</em> o aracı o worktree için hatırlar ve kural worktree ile birlikte gider.</p>',
  ]),
  ('notifications', 'Bildirimler, gelen kutusu ve bütçe', [
    '<p>Ayarlar › Bildirimler uygulamanın sana ne zaman haber vereceğini seçer: bir oturum beklerken, biri bittiğinde, pull request kontrolleri değiştiğinde. Bildirimler yalnızca pencere önde değilken görünür, birine tıklamak oturuma atlar ve dock ya da görev çubuğu rozeti bekleyen oturumları sayabilir.</p>'
    '<p>Sol panelin altındaki bütçe çubuğu, ajanların kendi kullanım raporlarından alınan, tüm oturumlardaki bugünkü gerçek harcamadır. Ayarlar › Bütçe günlük ve oturum başına bir limit, bir uyarı eşiği ve limite ulaşıldığında oturumların duraklatılıp duraklatılmayacağını belirler.</p>',
  ]),
  ('settings', 'Ayarlar', [
    '<p>Ayarlar (⌘,) konuya göre gruplanmıştır. Görünüm temayı, vurgu rengini, yoğunluğu ve yazı tiplerini belirler; Dil, arayüzü İngilizce, İspanyolca, İtalyanca, Lehçe, Fransızca, Almanca ve Türkçe arasında değiştirir. Birkaç bölümde <em>depo başına</em> rozeti var: üstte bir depo seçiliyken bunları yalnızca o depo için geçersiz kılabilirsin.</p>'
    '<p>Her şey, ev dizinindeki uygulama klasöründe bulunan <code>settings.json</code> dosyasına otomatik kaydedilir; <em>settings.json dosyasını aç</em> ham dosyayı doğrulamayla düzenler ve üst bar en son ne zaman yazıldığını gösterir.</p>',
    '<img src="{img}settings.png" alt="Ayarlar › Görünüm" loading="lazy">',
  ]),
  ('updates', 'Güncellemeler', [
    '<p>Açılıştan kısa süre sonra uygulama bu sitenin sürümlerine bakar, yeni bir sürümü arka planda indirir ve <em>Güncellemek için yeniden başlat</em> seçeneğini sunar. Ayarlar › Bildirimler’de <em>Güncellemeleri öner</em> anahtarı, son kontrolün saatini gösteren bir <em>Güncellemeleri kontrol et</em> düğmesi ve <em>Güncellemeleri otomatik kur</em> var: açıkken, indirilen bir güncelleme iptal edebileceğin 15 saniyelik bir geri sayımdan sonra uygulamayı kendi başına yeniden başlatır — yalnızca hiçbir oturum çalışmıyor ya da beklemiyorken; aksi halde çıkışta kurulur. Güncellemeden sonraki ilk açılış hangi sürümde olduğunu söyler ve nelerin değiştiğine bağlantı verir.</p>',
  ]),
  ('shortcuts', 'Klavye kısayolları', [
    '<table><tr><td>⌘O</td><td>Depo aç</td></tr><tr><td>⇧⌘C</td><td>Depo klonla</td></tr><tr><td>⌘N</td><td>Yeni worktree</td></tr><tr><td>⌘,</td><td>Ayarlar</td></tr><tr><td>⌘↵</td><td>İstemi gönder</td></tr></table>'
    '<p>Windows ve Linux’ta ⌘’yi Ctrl olarak oku. Her kısayol Ayarlar › Klavye kısayolları altında değiştirilebilir.</p>',
  ]),
  ('trouble', 'Bir şeyler ters gittiğinde', [
    '<p><strong>macOS uygulamayı doğrulayamadığını söylüyor (Çöp Sepeti’ne Taşı / Bitti).</strong> Bitti’ye tıkla, sonra Sistem Ayarları › Gizlilik ve Güvenlik › Güvenlik’e kadar in › <em>Yine de Aç</em>, ve parolanla onayla. macOS 14 veya daha eskisinde sağ tık › Aç tek adımda yapar. Hâlâ reddediyorsa Terminal’de: <code>xattr -d com.apple.quarantine /Applications/ygd-editor.app</code>. Uygulamanın <em>hasarlı</em> olduğunu söylüyorsa indirme bozulmuştur: yeniden indir ve <code>SHA256SUMS.txt</code> ile karşılaştır.</p>'
    '<p><strong>Windows yükleyiciyi engelliyor.</strong> SmartScreen › Ek bilgi › Yine de çalıştır. Yayımcı <em>ygd-editor release signing</em> olmalı.</p>'
    '<p><strong>AppImage başlamıyor.</strong> <code>--appimage-extract-and-run</code> ile çalıştır ya da <code>libfuse2</code> kur.</p>'
    '<p><strong>Bir sağlayıcı “Kurulu değil” gösteriyor.</strong> Codex ve Gemini CLI istek üzerine indirilir: karttaki <em>İndir</em>’e tıkla; indirme başarısız olursa kart nedenini söyler (çevrimdışı ya da sağlama toplamıyla eşleşmeyip atılan bir dosya). Claude Code için kartındaki <em>Claude Code kur</em>’a tıkla; kendin kurduysan bir terminal aç, <code>claude --version</code> komutunun çalıştığını kontrol et, sonra Ayarlar › Yapay zekâ sağlayıcıları › Yeniden tara.</p>'
    '<p><strong>Git hataları.</strong> Uygulama sık görülenleri tek cümleyle açıklar — kimlik bilgileri, ilerlemiş bir uzak depo, bir kilit dosyası, kirli bir çalışma ağacı, çakışmalar — ve tam çıktıyı worktree terminalinde tutar.</p>'
    '<p><strong>Güncelleme görünmüyor.</strong> Ayarlar › Bildirimler › Güncellemeleri öner’i kontrol et, sonra Güncellemeleri kontrol et; uygulamanın github.com’a erişebilmesi gerekir.</p>'
    '<p>Başka bir şey varsa: ne yaptığını, ne beklediğini ve ne olduğunu anlatan <a href="https://github.com/{repo}/issues">bir issue aç</a>.</p>',
  ]),
  ('privacy', 'Gizlilik ve güvenlik', [
    '<p>Her şey bilgisayarında çalışır. Uygulamanın kendisi internete tek bir şey için bağlanır: güncellemeler için bu sitenin sürümlerine bakmak. Ajanlar sağlayıcılarıyla senin hesaplarınla konuşur; git uzak depolarınla senin kimlik bilgilerinle konuşur. Uygulamanın sakladığı sağlayıcı token’ları işletim sisteminin anahtar zincirinde tutulur. Arayüz sandbox içinde çalışır, bir yol adı geçen her istek gerçekten açtığın depolara karşı kontrol edilir ve hiçbir komut asla bir kabuk dizesinden oluşturulmaz.</p>'
    '<p>Bir indirmenin gerçekten bize ait olduğunu kontrol etmek için indirme sayfasındaki <a href="{prefix}index.html#genuine">İndirdiğim dosya gerçek mi?</a> bölümüne bak.</p>',
  ]),
 ],
 # sürümler sayfası ve ortak küçük dizeler
 'dl_version': 'sürüm {v}',
 'genuine_details': 'teknik ayrıntılar',
 'lang_label': 'Dil',
 'title_releases': 'ygd-editor — tüm sürümler',
 'r_h1': 'Tüm sürümler',
 'r_lead': 'ygd-editor’ün yayınlanmış her sürümü. Önce her sistem için en yenisi, sonra sistem sistem tüm geçmiş. İndirme sayfası her zaman en yeni tam sürümü sunar; bu liste belirli bir sürüme ihtiyacı olanlar için.',
 'r_latest_h': 'Her sistem için en yenisi',
 'r_all_h': 'Her sürüm, sisteme göre',
 'r_systems': {'mac': 'macOS', 'win': 'Windows', 'linux': 'Linux'},
 'r_loading': 'Sürümler yükleniyor…',
 'r_error': 'Sürüm listesi okunamadı ({err}).',
 'r_github': 'GitHub’daki sürümler',
 'r_none': 'Henüz yayınlanmış sürüm yok.',
 'r_notes': 'Neler değişti',
 'r_checksums': 'Sağlama toplamları',
 'r_updates': 'Kurulu uygulamalar kendilerini en yeni tam sürüme günceller; belirli bir sürüm istemiyorsan buradaki hiçbir şeyi elle indirmen gerekmez.',
}
