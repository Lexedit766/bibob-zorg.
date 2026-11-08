from tpl import page, steps, marge

URLS = []

# ---------------------------------------------------------------- vragenformulier
URLS.append(page(
    slug="bibob-vragenformulier.html",
    title="Bibob-vragenformulier invullen: checklist voor zorgaanbieders",
    desc="Het Bibob-vragenformulier (Bibob-formulier) van de gemeente stap voor stap: welke vragen, welke bewijsstukken over financiering en zeggenschap, veelgemaakte fouten en een printbare checklist voor zorgaanbieders.",
    h1="Het Bibob-vragenformulier: zo vult u het volledig en consistent in",
    intro="Het Bibob-vragenformulier is het begin van elk Bibob-onderzoek. Het vraagt naar drie dingen: wie uw onderneming bestuurt en bezit, waar het geld vandaan komt, en met wie u zakendoet. Voor zorgaanbieders zit het risico zelden in de antwoorden zelf, maar in onvolledigheid en tegenstrijdigheden tussen formulier, handelsregister en jaarrekening.",
    marge=marge([
        ("Grondslag", "Art. 30 Wet Bibob; Regeling Bibob-formulieren (laatstelijk gewijzigd 31 januari 2024)"),
        ("Varianten", ["Vergunningen", "Subsidies", "Overheidsopdrachten (met vakje open house / toelatingsprocedure zorg)", "Vastgoedtransacties"]),
        ("Termijn", "Door de gemeente gesteld; meestal twee tot vier weken. Vraag tijdig uitstel."),
        ("Gevolg onvolledig", "Kan gelden als weigering tot medewerking: ernstig gevaar (art. 4)"),
        ("Geheimhouding", "Art. 28: uw gegevens worden alleen gebruikt voor het Bibob-onderzoek"),
    ]),
    body='''
<h2>Welk formulier krijgt u</h2>
<p>De Regeling Bibob-formulieren schrijft voor welk formulier het bestuursorgaan gebruikt. Bij inkoop van Wmo-ondersteuning of jeugdhulp is dat het formulier voor overheidsopdrachten; daarop kruist de gemeente aan dat het om een (semi-)open house of toelatingsprocedure voor zorg gaat (art. 1 lid 4 Wet Bibob). Er is een versie voor natuurlijke personen (eenmanszaak, vof, maatschap) en een voor rechtspersonen (bv, stichting). Bij een holdingstructuur vult de inschrijvende vennootschap het formulier in en worden de bovenliggende vennootschappen en hun bestuurders in de bijlagen opgenomen.</p>
<p>Gemeenten mogen het landelijke model niet uitbreiden met eigen vragen, wel mogen zij aanvullende bewijsstukken vragen. Hebt u de afgelopen jaren bij dezelfde gemeente al een formulier ingevuld, dan mag u daarnaar verwijzen voor ongewijzigde onderdelen; vermeld dan datum en kenmerk.</p>

<h2>De vier onderdelen en waar het misgaat</h2>
<h3>1. De onderneming en haar structuur</h3>
<p>Rechtsvorm, KvK-nummer, vestigingen, en een organogram tot aan de natuurlijke personen aan de top. Elke bestuurder, aandeelhouder van 5% of meer, commissaris of toezichthouder en "uiteindelijk belanghebbende" wordt afzonderlijk opgegeven. Veelgemaakte fout: het organogram wijkt af van het handelsregister of van het aandeelhoudersregister, bijvoorbeeld omdat een aandelenoverdracht wel notarieel is gepasseerd maar het register niet is bijgewerkt.</p>
<h3>2. Leidinggevenden en zeggenschap</h3>
<p>Wie geeft of gaf feitelijk leiding, ook zonder formele titel? De wet kijkt naar de werkelijkheid, niet naar de functieomschrijving. Een "adviseur" die de inkoop regelt, de bank bedient en het personeel aanstuurt, is leidinggevende in de zin van de wet. Vermeld ook personen die de afgelopen jaren zijn uitgetreden, als het formulier daarnaar vraagt; de gemeente ziet hen in het handelsregister toch.</p>
<h3>3. Financiering</h3>
<p>Hoe is de onderneming gefinancierd en met welk vermogen is zij gestart? Per bron een bewijsstuk: bankfinanciering (overeenkomst), eigen inbreng (bankafschrift van de storting en de herkomst), lening van familie of derden (ondertekende leningsovereenkomst met rente, looptijd en aflossing, plus het afschrift van de overboeking), winst uit onderneming (jaarrekeningen). In de zorg is dit het onderdeel waarop de meeste onderzoeken vastlopen: contante inbreng, een lening van een familielid zonder contract, of een geldstroom via een privérekening die niet is te herleiden.</p>
<h3>4. Zakelijke relaties</h3>
<p>Met wie werkt u samen bij de uitvoering van de opdracht: onderaannemers, zzp'ers die structureel voor u werken, bemiddelingsbureaus, de verhuurder van locaties, de administrateur die ook tekenbevoegd is. Deze partijen vormen met u een zakelijk samenwerkingsverband (art. 3 lid 4 onder c) en worden meegewogen. U hoeft hun antecedenten niet te kennen, wel moet u hen volledig opgeven.</p>

<h2>Checklist bewijsstukken</h2>
<p>Print deze lijst en vink af wat u bijvoegt. De gemeente mag meer vragen, maar met deze set is het formulier voor de meeste zorgaanbieders compleet.</p>
<div class="kader inline checklist">
<p><strong>Onderneming</strong></p>
<ul>
<li>Recent uittreksel handelsregister van de inschrijver en elke bovenliggende vennootschap</li>
<li>Statuten en, bij een bv, het aandeelhoudersregister</li>
<li>Organogram tot aan de natuurlijke personen, met percentages</li>
<li>UBO-registratie (bevestiging KvK)</li>
<li>Kopieën identiteitsbewijs van bestuurders en UBO's (BSN afgeschermd, tenzij het formulier dit vraagt)</li>
</ul>
<p><strong>Financiering</strong></p>
<ul>
<li>Openingsbalans of eerste jaarrekening en de twee meest recente jaarrekeningen</li>
<li>Per lening: ondertekende overeenkomst én bankafschrift van de ontvangst</li>
<li>Per eigen inbreng: bankafschrift van de storting en toelichting op de herkomst (salaris, verkoop woning, erfenis)</li>
<li>Bankfinanciering: kredietovereenkomst</li>
<li>Rekening-courantverhoudingen met de dga of de holding: saldo en afspraken</li>
<li>Aangifte vennootschaps- of inkomstenbelasting van het laatste jaar, als het formulier daarom vraagt</li>
</ul>
<p><strong>Zakelijke relaties</strong></p>
<ul>
<li>Lijst van onderaannemers en structurele zzp'ers met KvK-nummer</li>
<li>Onderaannemingsovereenkomsten of samenwerkingsovereenkomsten</li>
<li>Huurovereenkomsten van zorglocaties en kantoor</li>
<li>Overeenkomst met administratiekantoor of bemiddelingsbureau</li>
</ul>
<p><strong>Controle voor verzending</strong></p>
<ul>
<li>Komen namen, data en percentages in formulier, handelsregister, statuten en jaarrekening overeen?</li>
<li>Is elke vraag beantwoord, ook met "niet van toepassing", en is elke bijlage genummerd en in het formulier aangehaald?</li>
<li>Is het formulier ondertekend door een tekenbevoegde volgens het handelsregister?</li>
<li>Hebt u een kopie van het volledige pakket bewaard met de datum van indiening?</li>
</ul>
<p><button type="button" class="cta" onclick="window.print()">Print de checklist</button></p>
</div>

<h2>Als u een vraag niet kunt beantwoorden</h2>
<p>Laat geen vak open. De gemeente mag een onvolledig formulier aanmerken als weigering om informatie te verstrekken, en die weigering geldt als ernstig gevaar (art. 4 lid 1 en 2 Wet Bibob); in een inkoopprocedure leidt dat tot uitsluiting zonder dat de inhoud nog wordt beoordeeld. Ontbreekt een stuk, schrijf dan wat u wél kunt aantonen en waarom het stuk ontbreekt, en vraag schriftelijk om een korte aanvullende termijn. Een gemotiveerd verzoek om uitstel wordt in de praktijk vrijwel altijd gehonoreerd; stilzwijgen niet.</p>

<h2>Wat er na indiening gebeurt</h2>
''' + steps([
        ("Ontvangst en volledigheidstoets", "De Bibob-coördinator controleert of alle vragen zijn beantwoord en alle bijlagen aanwezig zijn. Ontbreekt iets, dan krijgt u een hersteltermijn."),
        ("Eigen onderzoek (art. 7a)", "De gemeente raadpleegt het handelsregister, het Kadaster, het Bibob-register en gesloten bronnen zoals justitiële gegevens over de opgegeven personen en relaties."),
        ("Eventueel advies LBB (art. 9)", "Bij twijfel vraagt de gemeente advies aan het Landelijk Bureau Bibob; u wordt daarvan op de hoogte gesteld (art. 32). Het Bureau heeft acht weken, eenmaal te verlengen met vier (art. 15)."),
        ("Uitkomst", "Geen gevaar: u blijft in de procedure. Mindere mate van gevaar: de gemeente kan voorwaarden stellen of, als het contract dat toelaat, ontbinden. Ernstig gevaar: voornemen tot weigering of ontbinding, waartegen u een zienswijze kunt indienen (art. 33)."),
    ]) + '''
<p>Hoe het onderzoek daarna verloopt leest u in <a href="bibob-onderzoek.html">Het Bibob-onderzoek</a>; wat u doet bij een negatieve uitkomst in <a href="negatief-bibob-advies.html">Negatief advies en zienswijze</a>.</p>
''',
    faq=[
        ("Moet ik het Bibob-formulier zelf invullen of mag mijn accountant dat doen?", "Uw accountant of adviseur mag het voorbereiden, maar de onderneming (een tekenbevoegde bestuurder) ondertekent en is verantwoordelijk voor de juistheid. Onjuist of onvolledig invullen wordt aan de onderneming toegerekend."),
        ("Moet ik de financiering van jaren geleden nog aantonen?", "Als het formulier naar de startfinanciering vraagt, ja. Hebt u de stukken niet meer, vraag dan bankafschriften op bij uw bank (meestal tot tien jaar terug) en leg uit wat u niet meer kunt reconstrueren."),
        ("Moeten mijn onderaannemers ook een formulier invullen?", "Niet standaard. De gemeente kan dat wel verlangen als zij de onderaannemer als onderdeel van het samenwerkingsverband wil onderzoeken, en kan eisen dat u een onderaannemer vervangt die de toets niet doorstaat."),
        ("Wat gebeurt er met mijn gegevens?", "Zij vallen onder de geheimhoudingsplicht van art. 28 Wet Bibob en mogen alleen worden gebruikt voor het Bibob-onderzoek. Een gevaarsconclusie van het LBB wordt wel geregistreerd in het Bibob-register en is voor andere bestuursorganen raadpleegbaar."),
        ("Wordt het formulier Bibob of Bibop geschreven?", "Bibob: Bevordering integriteitsbeoordelingen door het openbaar bestuur. \"Bibop\" komt veel voor maar is een spelfout."),
    ],
    contact_h2="Formulier ontvangen?",
    contact_p="Stuur het formulier en de begeleidende brief door. U krijgt binnen één werkdag terug welke bewijsstukken u nodig hebt, waar in uw structuur de vragen gaan komen en of begeleiding zinvol is.",
    subject="Bibob-vragenformulier",
    breadcrumb="Bibob-vragenformulier",
))

# ---------------------------------------------------------------- bibob-toets
URLS.append(page(
    slug="bibob-toets.html",
    title="Bibob-toets voor zorgaanbieders: wat het is en wanneer u hem krijgt",
    desc="Wat een Bibob-toets (ook geschreven als Bibop-toets) inhoudt voor zorgaanbieders: bij aanbesteding en open house Wmo en Jeugdwet, pgb en maatwerkovereenkomsten. Wat de gemeente toetst, hoe lang het duurt en wat de uitkomsten betekenen.",
    h1="De Bibob-toets: wat de gemeente toetst en wanneer",
    intro="\"Bibob-toets\" is de praktijknaam voor de integriteitsbeoordeling die een gemeente uitvoert voordat zij met een onderneming in zee gaat. Voor zorgaanbieders komt hij voor bij inkoop van Wmo-ondersteuning en jeugdhulp. De toets gaat niet over de kwaliteit van uw zorg maar over de vraag of het contract misbruikt kan worden voor strafbare feiten of de opbrengst daarvan.",
    marge=marge([
        ("Wie toetst", "De gemeente (college van B&W), vaak via een regionaal Bibob-team of het RIEC; bij twijfel adviseert het Landelijk Bureau Bibob"),
        ("Waarop", "Art. 3: gevaar van benutten van crimineel voordeel (a-grond) of plegen van strafbare feiten (b-grond)"),
        ("Bij wie", "Uzelf, bestuurders, aandeelhouders, financiers en het zakelijk samenwerkingsverband (art. 3 lid 4)"),
        ("Uitkomsten", ["geen gevaar", "mindere mate van gevaar", "ernstig gevaar"]),
        ("Ook bekend als", "Bibop-toets, BIBOB-toets, integriteitstoets, screening"),
    ]),
    body='''
<h2>Toets, onderzoek, advies: wat is wat</h2>
<p>In de praktijk lopen drie begrippen door elkaar. De <strong>Bibob-toets</strong> of <strong>Bibob-screening</strong> is het geheel: de gemeente beoordeelt uw integriteit voordat of terwijl zij met u contracteert. Het <strong>Bibob-onderzoek</strong> is het feitelijke onderzoek dat daarvoor wordt gedaan, eerst door de gemeente zelf (eigen onderzoek, art. 7a) en zo nodig door het Landelijk Bureau Bibob. Het <strong>Bibob-advies</strong> is het schriftelijke oordeel van dat Bureau (art. 9), dat uitmondt in een van drie conclusies. De gemeente beslist; het Bureau adviseert.</p>

<h2>Waarop de gemeente toetst</h2>
<p>De maatstaf staat in art. 3 Wet Bibob. De gemeente weigert of beëindigt een overeenkomst als er ernstig gevaar bestaat dat die wordt gebruikt om uit strafbare feiten verkregen voordeel te benutten (lid 1 onder a) of om strafbare feiten te plegen (lid 1 onder b). Daarbij telt mee: hoe ernstig de feiten of vermoedens zijn, hoeveel het er zijn, hoe lang geleden, en of ze samenhangen met de activiteit waarvoor u contracteert (lid 2 en 3). Een veroordeling is niet vereist; ook een sepot, een transactie, een bestuurlijke boete of een lopend onderzoek kan meewegen, mits voldoende aannemelijk.</p>
<p>De toets strekt zich uit tot iedereen die tot u in een relevante relatie staat (lid 4): wie leiding geeft of zeggenschap heeft, wie vermogen verschaft, en wie met u in een zakelijk samenwerkingsverband staat. Voor zorgaanbieders betekent dit dat de toets vaak niet over u gaat, maar over een financier, een onderaannemer of een voormalige compagnon.</p>
<p>De uitkomst moet evenredig zijn (lid 5): de maatregel moet in verhouding staan tot de mate van gevaar en de ernst van de feiten. Bij een mindere mate van gevaar kan de gemeente voorschriften verbinden aan het contract in plaats van het te weigeren (lid 7); of zij ook mag ontbinden, hangt af van wat in het contract is afgesproken.</p>

<h2>Wanneer zorgaanbieders de toets krijgen</h2>
<h3>Bij inkoop en aanbesteding van Wmo en Jeugdwet</h3>
<p>Dit is sinds 1 oktober 2022 de hoofdroute. Een overeenkomst waarmee de gemeente zorg inkoopt op grond van art. 2.1.1 Wmo 2015 of art. 2.11 Jeugdwet via een open house of toelatingsprocedure geldt als overheidsopdracht voor de Wet Bibob (art. 1 lid 4). De gemeente kan dan bij de selectie screenen en de gunning weigeren, en tijdens de looptijd screenen en de overeenkomst ontbinden (art. 5). Voorwaarde is dat zij dit in de inkoopdocumenten en het contract heeft aangekondigd. Gemeenten die structureel toetsen, zoals in Twente, laten alle inschrijvers het vragenformulier invullen; andere toetsen op signaal.</p>
<h3>Bij subsidies</h3>
<p>Wordt uw zorg gesubsidieerd in plaats van ingekocht, bijvoorbeeld welzijnsactiviteiten of een inloopvoorziening, dan kan de gemeente de subsidie weigeren of intrekken na een Bibob-toets (art. 6). Hier geldt wel het bestuursrecht: bezwaar en beroep in plaats van de civiele rechter.</p>
<h3>Bij een Wtza-vergunning</h3>
<p>Verleent u Zvw- of Wlz-zorg met meer dan tien zorgverleners, of medisch-specialistische zorg, dan hebt u een Wtza-vergunning nodig. De minister (het CIBG) kan die weigeren of intrekken op grond van een Bibob-onderzoek (art. 5 lid 5 en 6 Wtza; Beleidsregels Wet Bibob Wtza, Stcrt. 2022, 202). Wmo- en jeugdhulpaanbieders hebben geen Wtza-vergunning nodig, alleen de meldplicht.</p>
<h3>Niet: pgb</h3>
<p>Een pgb is geen subsidie en geen overheidsopdracht (art. 2.3.6 lid 6 Wmo 2015; art. 8.1.1 lid 5 Jeugdwet). De gemeente kan een aanbieder die uitsluitend via pgb's werkt dus niet Bibob-toetsen. Zij stelt wel eisen via de verordening en het pgb-plan en kan een eerder negatief Bibob-oordeel laten meewegen bij de beoordeling of een budgethouder zijn pgb bij u mag besteden.</p>
<h3>Maatwerkovereenkomsten</h3>
<p>Een individuele overeenkomst tussen gemeente en een niet-gecontracteerde aanbieder voor één of enkele cliënten is wél een overeenkomst waarop de Wet Bibob kan worden toegepast. Gemeenten toetsen hier meestal op signaal of boven een aantal cliënten.</p>

<h2>Hoe lang een toets duurt</h2>
<p>Het eigen onderzoek van de gemeente kent geen wettelijke termijn; reken op twee tot acht weken na een volledig formulier. Wordt het Landelijk Bureau Bibob ingeschakeld, dan komen daar acht weken bij, eenmaal te verlengen met vier (art. 15). In een inkoopprocedure staat vaak dat gunning onder voorbehoud van de Bibob-uitkomst plaatsvindt, zodat u kunt starten terwijl de toets loopt. Vraag dat na als de inkoopdocumenten er niets over zeggen.</p>

<h2>De drie uitkomsten en wat ze voor u betekenen</h2>
<dl class="lijst">
<div class="item"><dt><h3>Geen gevaar<em>of geen gebleken gevaar</em></h3></dt><dd><p>De gemeente contracteert of zet het contract voort. De uitkomst wordt niet geregistreerd. Bewaar de bevestiging; bij een volgende inkoopronde of een andere gemeente kunt u ernaar verwijzen.</p></dd></div>
<div class="item"><dt><h3>Mindere mate van gevaar<em>art. 3 lid 7</em></h3></dt><dd><p>De gemeente kan voorschriften verbinden aan het contract, bijvoorbeeld periodieke rapportage of het beëindigen van een bepaalde relatie. Of zij ook mag ontbinden, hangt af van de contractbepaling; het Gerechtshof Arnhem-Leeuwarden achtte dat in mei 2026 toegestaan toen het contract dat uitdrukkelijk bepaalde en de aanbieder niet transparant was geweest. Lees de Bibob-clausule in uw raamovereenkomst dus zorgvuldig.</p></dd></div>
<div class="item"><dt><h3>Ernstig gevaar<em>art. 3 lid 1</em></h3></dt><dd><p>De gemeente kondigt aan te weigeren of te ontbinden. U krijgt het advies in te zien en twee weken voor een zienswijze (art. 33). De conclusie wordt vijf jaar geregistreerd in het Bibob-register en is voor andere bestuursorganen raadpleegbaar. Zie <a href="negatief-bibob-advies.html">Negatief advies en zienswijze</a>.</p></dd></div>
</dl>

<h2>Wat u zelf kunt doen</h2>
<p>De toets is te doorstaan voor elke aanbieder die zijn structuur, financiering en relaties op orde en gedocumenteerd heeft. Begin daarmee voordat de inkoopronde opent: breng in kaart wie in beeld komt, leg elke financiering schriftelijk vast en beëindig formeel wat feitelijk al is beëindigd. Hoe het onderzoek daarna stap voor stap verloopt leest u in <a href="bibob-onderzoek.html">Het Bibob-onderzoek</a>; wat u precies moet aanleveren in <a href="bibob-vragenformulier.html">Het vragenformulier</a>.</p>
''',
    faq=[
        ("Is een Bibob-toets hetzelfde als een VOG?", "Nee. Een Verklaring Omtrent het Gedrag gaat over één persoon en één functie en wordt door Justis afgegeven. Een Bibob-toets gaat over de onderneming en haar hele netwerk, wordt door het bestuursorgaan uitgevoerd en kan ook vermoedens en niet-vervolgde feiten meewegen."),
        ("Kan de gemeente mij toetsen zonder dat ik een formulier heb gekregen?", "Het eigen onderzoek (art. 7a) kan starten op basis van openbare bronnen en signalen. Maar voordat de gemeente een negatief besluit neemt, moet zij u om informatie vragen en u de gelegenheid geven een zienswijze te geven."),
        ("Telt een oude veroordeling van een bestuurder mee?", "Dat hangt af van ernst, aantal, tijdsverloop en samenhang met de zorgactiviteit (art. 3 lid 2 en 3). Een feit van meer dan vijf tot tien jaar geleden zonder relatie met zorg of financiën weegt in de regel licht; recente fraude, witwassen of zedendelicten wegen zwaar."),
        ("Wat is een Bibop-toets?", "Dezelfde toets; Bibop is een veelvoorkomende spelfout van Bibob."),
        ("Mag de gemeente mijn cliënten informeren over de toets?", "Niet over de inhoud. Op het onderzoek rust geheimhouding (art. 28). Wel mag de gemeente, als het contract wordt beëindigd, cliënten informeren dat zij een andere aanbieder moeten kiezen."),
    ],
    contact_h2="Staat er een Bibob-toets in uw inkoopdocumenten?",
    contact_p="Stuur de Bibob-bepaling of het vragenformulier door. U hoort binnen één werkdag waar in uw structuur de aandacht naar uit zal gaan en wat u vóór de inschrijving nog kunt regelen.",
    subject="Bibob-toets%20inkoop",
    breadcrumb="Bibob-toets",
))

# ---------------------------------------------------------------- wet bibob
URLS.append(page(
    slug="wet-bibob.html",
    title="Wat is de Wet Bibob? Betekenis en toepassing in de zorg",
    desc="De Wet Bibob uitgelegd: betekenis van de afkorting, wat de wet regelt, voor welke besluiten en overeenkomsten zij geldt, hoe zij sinds 2022 op zorgaanbieders wordt toegepast, en wat het Landelijk Bureau Bibob en het Bibob-register doen.",
    h1="Wat is de Wet Bibob?",
    intro="Bibob staat voor Bevordering integriteitsbeoordelingen door het openbaar bestuur. De wet uit 2003 geeft overheden een instrument om te voorkomen dat zij, door een vergunning te verlenen, een subsidie te verstrekken of een opdracht te gunnen, ongewild criminele activiteiten faciliteren. Sinds 2022 geldt de wet volledig voor de inkoop van zorg door gemeenten.",
    marge=marge([
        ("Officiële naam", "Wet bevordering integriteitsbeoordelingen door het openbaar bestuur"),
        ("In werking", "1 juni 2003; grote wijzigingen 2013, 2020 en 2022"),
        ("Toepassing op", ["vergunningen (art. 7)", "subsidies (art. 6)", "overheidsopdrachten, incl. open house zorg (art. 5 en art. 1 lid 4)", "vastgoedtransacties (art. 5a)"]),
        ("Uitvoering", "Bestuursorganen zelf (art. 7a) en het Landelijk Bureau Bibob (art. 8 e.v.)"),
        ("Register", "Bibob-register bij het LBB; gevaarsconclusies vijf jaar raadpleegbaar"),
    ]),
    body='''
<h2>Waarom de wet bestaat</h2>
<p>De Wet Bibob kwam voort uit de parlementaire enquête opsporingsmethoden (1996) en de constatering dat criminele organisaties zich nestelden in legale sectoren met behulp van vergunningen en overheidsgeld. De wet maakt het mogelijk om vooraf te beoordelen of een aanvrager of contractspartij integer is, met gebruik van informatie die het bestuursorgaan anders niet zou mogen gebruiken: justitiële gegevens, politiegegevens en fiscale informatie. Oorspronkelijk gold zij voor horeca, coffeeshops, prostitutie, bouw en milieu. In stappen is het bereik verbreed naar alle vergunningen die bij algemene maatregel van bestuur zijn aangewezen, alle subsidies, alle overheidsopdrachten en, sinds 2022, de inkoop van zorg via open house.</p>

<h2>Wat de wet regelt</h2>
<p>De kern is art. 3: een bestuursorgaan kan een beschikking weigeren of intrekken, of een overeenkomst niet aangaan of ontbinden, als ernstig gevaar bestaat dat die wordt gebruikt om uit strafbare feiten verkregen voordeel te benutten of om strafbare feiten te plegen. De wet regelt vervolgens wie wordt onderzocht (art. 3 lid 4: de betrokkene en zijn leidinggevenden, zeggenschaphebbenden, vermogensverschaffers en zakelijk samenwerkingsverband), hoe het onderzoek verloopt (art. 7a eigen onderzoek, art. 9 advies van het Landelijk Bureau Bibob, art. 30 vragenformulier), welke termijnen gelden (art. 15), welke rechten de betrokkene heeft (art. 32 kennisgeving, art. 33 inzage en zienswijze) en hoe met de informatie wordt omgegaan (art. 28 geheimhouding).</p>

<h2>Het Landelijk Bureau Bibob</h2>
<p>Het Landelijk Bureau Bibob (LBB) is onderdeel van Justis, de screeningsautoriteit van het ministerie van Justitie en Veiligheid. Het heeft toegang tot gesloten bronnen waartoe gemeenten zelf geen of beperkt toegang hebben en brengt op verzoek van een bestuursorgaan een advies uit: geen gevaar, een mindere mate van gevaar of ernstig gevaar. Het advies is niet bindend; het bestuursorgaan beslist en moet de beslissing zelf motiveren. Het Bureau houdt ook het Bibob-register bij, waarin eerdere gevaarsconclusies worden vastgelegd zodat een onderneming die bij de ene gemeente is geweigerd niet ongemerkt bij een andere kan aankloppen. Een kwaliteitscommissie beoordeelt jaarlijks de adviezen; het ministerie rapporteert daarover aan de Tweede Kamer.</p>

<h2>De Wet Bibob in de zorg</h2>
<p>Tot oktober 2022 konden gemeenten zorgaanbieders alleen toetsen als de zorg werd gesubsidieerd of als er sprake was van een echte aanbesteding. De meeste Wmo- en jeugdhulp wordt echter ingekocht via open house, waarbij elke aanbieder die aan de voorwaarden voldoet een contract krijgt; dat is volgens het Hof van Justitie geen overheidsopdracht (Falk Pharma, C-410/14; Tirkkonen, C-9/17), en viel dus buiten de wet. Een amendement bij de wetswijziging van 2022 heeft dat gerepareerd: art. 1 lid 4 bepaalt nu dat ook een overeenkomst waarmee zorg wordt ingekocht op grond van art. 2.11 Jeugdwet of art. 2.1.1 Wmo 2015 via een open house of toelatingsprocedure als overheidsopdracht geldt.</p>
<p>De praktijk ontwikkelt zich sindsdien. In de proeftuinen Aanpak Zorgfraude van Twente en Hart van Brabant is een werkwijze ontwikkeld om alle inschrijvers te screenen, en de VNG heeft de Bibob-bepaling in haar contractstandaarden Wmo en Jeugd uitgewerkt. Toch is het aantal gemeenten dat de wet structureel in de zorg toepast nog beperkt; de meeste toetsen op signaal. Voor een zorgaanbieder betekent dit dat de kans op een toets per regio verschilt, maar bij elke nieuwe inkoopronde aanwezig is.</p>
<p>Buiten het gemeentelijk domein speelt de wet een rol bij de Wtza-vergunning: de minister kan die weigeren of intrekken na een Bibob-onderzoek (art. 5 lid 5 en 6 Wtza). Zorgkantoren en zorgverzekeraars zijn geen bestuursorganen en kunnen de Wet Bibob niet toepassen; zij screenen op andere gronden.</p>

<h2>Rechtsbescherming</h2>
<p>Bij een beschikking (vergunning, subsidie) staan bezwaar en beroep open volgens de Algemene wet bestuursrecht, met de Afdeling bestuursrechtspraak van de Raad van State als hoogste rechter. Bij een overeenkomst, dus bij inkoop en open house, is de weg civielrechtelijk: kort geding of bodemprocedure bij de rechtbank, in hoger beroep het gerechtshof. In beide gevallen toetst de rechter of het bestuursorgaan zich op het advies mocht baseren, of het de procedure van art. 32 en 33 heeft gevolgd en of de maatregel evenredig is. Omdat de betrokkene de gesloten bronnen niet kan inzien, mag het bestuursorgaan in beginsel afgaan op het LBB-advies, tenzij het concrete aanwijzingen heeft dat het advies onjuist is; de rechter toetst vervolgens of het bestuursorgaan die vergewisplicht is nagekomen.</p>

<h2>Verder lezen op deze site</h2>
<ul>
<li><a href="bibob-toets.html">De Bibob-toets</a>: wat de gemeente toetst, bij wie en met welke uitkomsten.</li>
<li><a href="bibob-onderzoek.html">Het Bibob-onderzoek</a>: het verloop in vijf stappen, met termijnen.</li>
<li><a href="bibob-vragenformulier.html">Het vragenformulier</a>: de vragen, de bewijsstukken en een checklist.</li>
<li><a href="negatief-bibob-advies.html">Negatief advies en zienswijze</a>: wat u doet bij een voornemen tot weigering of ontbinding.</li>
</ul>
''',
    faq=[
        ("Waar staat Bibob voor?", "Bevordering integriteitsbeoordelingen door het openbaar bestuur. De officiële schrijfwijze is Bibob, met alleen de eerste letter als hoofdletter."),
        ("Voor wie geldt de Wet Bibob?", "Voor iedereen die een aangewezen vergunning, een subsidie, een overheidsopdracht of een vastgoedtransactie met de overheid aanvraagt of heeft, en voor de personen en ondernemingen die met die aanvrager verbonden zijn."),
        ("Is de Wet Bibob strafrecht?", "Nee, het is bestuursrecht. Er wordt geen straf opgelegd en geen schuld vastgesteld; het bestuursorgaan beoordeelt een risico. Daarom mogen ook niet-vervolgde feiten en vermoedens meewegen, mits voldoende aannemelijk."),
        ("Wat is het verschil tussen de Wet Bibob en de Wtza?", "De Wtza regelt de toetreding van zorgaanbieders (meldplicht en vergunning) en de eisen aan hun bestuur. De Wet Bibob is een algemeen integriteitsinstrument dat onder meer bij de Wtza-vergunning kan worden ingezet."),
        ("Geldt de Wet Bibob ook voor zorgverzekeraars en zorgkantoren?", "Nee. Zij zijn geen bestuursorganen. Zij screenen nieuwe aanbieders op grond van hun eigen inkoopbeleid en de Wet bevorderen samenwerking en rechtmatige zorg."),
    ],
    contact_h2="Vraag over de toepassing in uw situatie?",
    contact_p="Beschrijf kort uw organisatie en de inkoop, subsidie of vergunning waar het om gaat. U krijgt binnen één werkdag antwoord op de vraag of de Wet Bibob daarop van toepassing is en wat dat betekent.",
    subject="Wet%20Bibob%20toepassing",
    breadcrumb="Wat is de Wet Bibob",
))

# ---------------------------------------------------------------- negatief advies
URLS.append(page(
    slug="negatief-bibob-advies.html",
    title="Negatief Bibob-advies: zienswijze, bezwaar en kort geding",
    desc="Wat u doet na een negatief Bibob-advies of een voornemen tot weigering of ontbinding: de zienswijze binnen twee weken (art. 33 Wet Bibob), de hoorzitting, bezwaar bij een besluit en kort geding bij een zorgcontract. Met opbouw van een zienswijze.",
    h1="Negatief Bibob-advies: wat u binnen twee weken doet",
    intro="Een voornemen tot weigering, niet-gunning of ontbinding na een Bibob-onderzoek is geen eindoordeel. De wet verplicht de gemeente u eerst het advies te laten inzien en uw zienswijze te horen. Die twee weken zijn het moment waarop de meeste dossiers worden gekeerd of verloren; daarna wordt het duurder en moeilijker.",
    marge=marge([
        ("Zienswijze", "Art. 33 Wet Bibob: inzage in het advies en gelegenheid tot zienswijze vóór het besluit; termijn in de praktijk twee weken"),
        ("Hoorzitting", "Op verzoek; schriftelijk én mondeling is mogelijk"),
        ("Bezwaar (besluit)", "Zes weken na bekendmaking (art. 6:7 Awb); daarna beroep en hoger beroep bij de Raad van State"),
        ("Contract", "Civiele rechter: kort geding tegen uitsluiting of ontbinding, bodemprocedure voor schade"),
        ("Registratie", "Gevaarsconclusie vijf jaar in het Bibob-register"),
    ]),
    body='''
<h2>Lees eerst wat er precies staat</h2>
<p>Een negatief Bibob-advies kent drie varianten en elk vraagt een andere reactie. Bij <strong>ernstig gevaar</strong> kondigt de gemeente weigering of ontbinding aan. Bij een <strong>mindere mate van gevaar</strong> kan zij voorschriften stellen, of ontbinden als het contract dat toelaat; hier is vaak nog ruimte voor een oplossing in de vorm van maatregelen. Bij een <strong>weigering wegens onvolledige medewerking</strong> (art. 4) is er geen inhoudelijk oordeel en is de snelste route het alsnog volledig aanleveren. Kijk ook of het om een besluit gaat (vergunning, subsidie: bestuursrecht) of om een overeenkomst (inkoop, open house, maatwerk: civiel recht), want dat bepaalt de vervolgroute.</p>

<h2>Uw rechten in deze fase</h2>
<p>Voordat de gemeente een negatief besluit neemt of een overeenkomst beëindigt op grond van een Bibob-advies, moet zij u in de gelegenheid stellen uw zienswijze naar voren te brengen en u daartoe het advies laten inzien (art. 33 lid 1 en 2 Wet Bibob). U mag een gemachtigde meenemen en inschakelen (art. 2:1 Awb). Het advies zelf krijgt u; de onderliggende broninformatie niet, daarop rust geheimhouding (art. 28). Wel moet het advies zo zijn opgebouwd dat u kunt begrijpen welke feiten en relaties tot de conclusie hebben geleid. Is dat niet zo, benoem dat dan uitdrukkelijk in de zienswijze.</p>
<p>Hebt u al eerder een zienswijze gegeven en komt er een aanvullend advies zonder nieuwe feiten, dan hoeft de gemeente u niet opnieuw te horen (art. 33 lid 3). Het Gerechtshof Arnhem-Leeuwarden bevestigde dat in mei 2026 in een zorgzaak waarin het aanvullende advies juist was gebaseerd op wat de aanbieder zelf had aangevoerd. Zet daarom alles wat u hebt in de eerste zienswijze.</p>

<h2>Opbouw van een zienswijze</h2>
''' + steps([
        ("Feiten corrigeren", "Loop het advies na op onjuiste of verouderde gegevens: functies die niet meer bestaan, leningen die zijn afgelost, personen die zijn uitgetreden. Onderbouw elke correctie met een stuk: uittreksel, akte, bankafschrift."),
        ("Relaties duiden of beëindigen", "Gaat het om een zakenpartner of financier met antecedenten, laat dan zien wat zijn feitelijke rol is en of die is of kan worden beëindigd. Een beëindigde relatie met bewijs van beëindiging weegt zwaar; een beëindiging die pas na het advies in gang wordt gezet, moet geloofwaardig en volledig zijn."),
        ("Samenhang met de zorg bestrijden", "De wet weegt of de feiten samenhangen met de activiteit waarvoor wordt gecontracteerd (art. 3 lid 3). Een verkeersdelict van een aandeelhouder heeft weinig met jeugdhulp te maken; een eerdere pgb-fraude heeft dat wel. Benoem dit expliciet."),
        ("Evenredigheid aanvoeren", "Weigering of ontbinding moet evenredig zijn met de mate van gevaar en de ernst van de feiten (art. 3 lid 5). Wijs op alternatieven: voorschriften, een proefperiode, een externe toezichthouder, vervanging van een onderaannemer. Beschrijf de gevolgen voor cliënten en personeel feitelijk, zonder emotioneel appel."),
        ("Maatregelen aanbieden", "Een zienswijze die alleen bestrijdt, verliest vaker dan een die ook iets aanbiedt. Governance aanpassen, een onafhankelijke toezichthouder benoemen, financieringsstromen transparant maken: concreet, met datum en bewijs van uitvoering."),
    ]) + '''

<h2>Als de gemeente toch negatief beslist</h2>
<h3>Bij een besluit: bezwaar en beroep</h3>
<p>Tegen de weigering of intrekking van een vergunning of subsidie maakt u binnen zes weken bezwaar (art. 6:7 Awb). Bezwaar schorst het besluit niet; vraag zo nodig een voorlopige voorziening bij de rechtbank (art. 8:81 Awb). Daarna staat beroep bij de rechtbank en hoger beroep bij de Afdeling bestuursrechtspraak van de Raad van State open. De bestuursrechter toetst of de gemeente het advies mocht volgen, de procedure heeft nageleefd en evenredig heeft gehandeld.</p>
<h3>Bij een zorgcontract: kort geding</h3>
<p>Uitsluiting van een inkoopprocedure of ontbinding van een raamovereenkomst is privaatrechtelijk. Het middel is een kort geding bij de rechtbank, met als vordering toelating tot de procedure of voortzetting van het contract. De rechter toetst of de gemeente de Bibob-bepaling in de inkoopdocumenten en het contract correct heeft toegepast, of zij art. 33 heeft nageleefd en of ontbinding in de gegeven omstandigheden naar maatstaven van redelijkheid en billijkheid aanvaardbaar is. In de zaak van mei 2026 woog het hof zwaar dat de aanbieder vooraf wist dat ook een mindere mate van gevaar tot ontbinding kon leiden en dat zij niet transparant was geweest over het vertrek van een bestuurder. Transparantie in de voorfase is dus ook procesrechtelijk uw beste bescherming.</p>
<h3>Intussen: uw cliënten</h3>
<p>Een ontbinding werkt vaak met een korte overgangstermijn. Regel in overleg met de gemeente de overdracht of, bij een kort geding, de voortzetting van de zorg totdat de rechter heeft beslist. Houd de communicatie met cliënten feitelijk; de inhoud van het Bibob-onderzoek valt onder geheimhouding, ook voor u.</p>

<h2>Registratie en de toekomst</h2>
<p>Een conclusie "ernstig gevaar" wordt vijf jaar geregistreerd in het Bibob-register en kan door elk bestuursorgaan worden geraadpleegd. Een negatieve uitkomst bij de ene gemeente werkt dus door bij inkoop door een andere gemeente en bij een Wtza-vergunning. Wie na een negatieve uitkomst doorgaat als zorgaanbieder, doet er goed aan de oorzaak structureel weg te nemen en dat te documenteren, zodat bij een volgende toets kan worden aangetoond dat de situatie is veranderd.</p>
''',
    faq=[
        ("Hoeveel tijd heb ik voor een zienswijze?", "De wet noemt geen termijn; de gemeente stelt die en hanteert in de praktijk twee weken. Een gemotiveerd verzoek om korte verlenging wordt meestal gehonoreerd, zeker als u aangeeft welke stukken u nog opvraagt."),
        ("Kan ik het Bibob-advies laten toetsen door een onafhankelijke partij?", "Het advies zelf kunt u door een jurist laten analyseren. De onderliggende bronnen zijn niet toegankelijk; wel kunt u het Landelijk Bureau Bibob via de gemeente om een aanvullend advies laten vragen als u nieuwe feiten aanlevert."),
        ("Heeft een zienswijze zin als het advies ernstig gevaar concludeert?", "Ja. De gemeente moet de zienswijze meewegen en kan het LBB om een aanvullend advies vragen. In de praktijk wordt een deel van de ernstig-gevaarconclusies na de zienswijze bijgesteld naar een mindere mate van gevaar, zeker als relaties aantoonbaar zijn beëindigd."),
        ("Kan ik schadevergoeding vorderen als het advies onjuist blijkt?", "In theorie, van de Staat (voor het LBB) of de gemeente, maar de Hoge Raad heeft de lat hoog gelegd (HR 23 mei 2014, ECLI:NL:HR:2014:1212): er moet causaal verband zijn tussen het onjuiste advies en de schade, en kosten van rechtsbijstand in de voorfase komen zelden voor vergoeding in aanmerking."),
        ("Wat gebeurt er met mijn pgb-cliënten na een negatief oordeel?", "De gemeente kan het Bibob-oordeel meewegen bij de beoordeling of budgethouders hun pgb bij u mogen besteden, en lopende pgb-besluiten herzien. Dat zijn afzonderlijke besluiten jegens de budgethouder, waartegen bezwaar openstaat."),
    ],
    contact_h2="Voornemen of negatief advies ontvangen?",
    contact_p="Stuur het voornemen en het advies door. U hoort binnen één werkdag hoeveel tijd er is, welke route openstaat en wat de zienswijze in uw geval moet bevatten. Bij een korte termijn: bel of mail direct, dan wordt uitstel aangevraagd.",
    subject="Negatief%20Bibob-advies",
    breadcrumb="Negatief Bibob-advies",
))

print("\n".join(URLS))
