# Reeks "Het belang van de Bibob-toets" + aanpalende thema's + regio's
from tpl import page, steps, marge

P = []  # (slug, titel, korte omschrijving, groep)

def add(slug, kop, oms, groep, **kw):
    page(slug=slug, breadcrumb=kop, **kw)
    P.append((slug, kop, oms, groep))

CONTACT_STD = dict(
    contact_h2="Vraag over uw eigen situatie?",
    contact_p="Beschrijf kort uw organisatie en waar de gemeente mee komt: inkoopdocument, formulier of voornemen. U hoort binnen één werkdag wat het voor u betekent en wat u nu kunt doen.",
    subject="Bibob%20zorgaanbieder",
)

# =====================================================================
# A. HET BELANG VAN DE BIBOB-TOETS
# =====================================================================

add("waarom-bibob-toets-zorg.html", "Waarom de Bibob-toets in de zorg", "Waarom gemeenten zorgaanbieders screenen en waarom dat ook bonafide aanbieders raakt.", "belang",
    title="Waarom de Bibob-toets in de zorg belangrijk is — ook voor bonafide aanbieders",
    desc="Waarom gemeenten de Wet Bibob inzetten tegen zorgfraude, wat dat betekent voor eerlijke Wmo-, jeugdhulp- en pgb-aanbieders, en waarom voorbereiding op de Bibob-toets een voorwaarde is geworden om in de zorg te ondernemen.",
    h1="Waarom de Bibob-toets in de zorg belangrijk is",
    intro="De Wet Bibob was lang een instrument voor horeca, coffeeshops en vastgoed. Dat de wet sinds 2022 ook op de inkoop van zorg wordt toegepast, komt door één ontwikkeling: de constatering dat een klein deel van de zorgaanbieders publiek geld wegsluist terwijl de controle achteraf te laat komt. De Bibob-toets verplaatst die controle naar de voorkant. Dat raakt ook de aanbieders die niets te verbergen hebben.",
    marge=marge([
        ("Aanleiding", "Rapporten IKZ, Nieuwsuur en Pointer 2019–2023 over fraude met Wmo- en pgb-zorg"),
        ("Wetswijziging", "Art. 1 lid 4 Wet Bibob, in werking 1 oktober 2022"),
        ("Beleid", "Proeftuinen Aanpak Zorgfraude (Twente, Hart van Brabant), VNG-contractstandaarden, programma Aanpak Zorgfraude 2025–2028"),
        ("Voor u", "Geen kwaliteitstoets, wel een netwerktoets: structuur, geld en relaties"),
    ]),
    body='''
<h2>Wat eraan voorafging</h2>
<p>Gemeenten kregen in 2015 de verantwoordelijkheid voor Wmo-ondersteuning en jeugdhulp, met een inkoopmodel waarin vrijwel elke aanbieder die aan de voorwaarden voldeed een contract kreeg. Het aantal aanbieders groeide snel; het toezicht groeide niet mee. Onderzoeksjournalistiek en het Informatie Knooppunt Zorgfraude lieten vanaf 2019 zien hoe eenvoudig het was om met een paar cliënten, een bv en een pgb-constructie forse bedragen te declareren voor zorg die niet of nauwelijks werd geleverd, en hoe vaak dezelfde personen na een beëindiging elders opnieuw begonnen. De schade werd niet alleen in euro's geteld, maar ook in kwetsbare cliënten die zonder zorg kwamen te zitten.</p>
<p>De bestaande instrumenten werkten achteraf: rechtmatigheidsonderzoek, terugvordering, strafrecht. Tegen de tijd dat zij effect hadden, was het geld weg en de aanbieder verdwenen. Gemeenten vroegen om een instrument aan de voorkant, en wezen op de Wet Bibob, die zij in andere sectoren al kenden. Het probleem was dat open house juridisch geen overheidsopdracht is en de wet daardoor niet gold. Dat is met de wijziging van 2022 gerepareerd.</p>

<h2>Wat de toets doet wat andere instrumenten niet doen</h2>
<p>De Bibob-toets kijkt niet naar de zorg maar naar de mensen en het geld eromheen. Andere instrumenten, zoals de Wtza-meldplicht, de VOG, de vergewisplicht en het kwaliteitstoezicht, beoordelen de organisatie of de individuele medewerker. De Bibob-toets beoordeelt het netwerk: wie financiert, wie beslist, wie profiteert en met wie wordt samengewerkt. Zij mag daarbij gebruikmaken van justitiële en fiscale informatie die het bestuursorgaan anders niet mag inzien, en zij mag vermoedens meewegen, niet alleen veroordelingen. Dat is precies het terrein waarop zorgfraude zich afspeelt: niet in het dossier van de cliënt, maar in de holdingstructuur, de rekening-courant en de onderaannemer.</p>

<h2>Waarom dit ook u raakt</h2>
<p>Voor de bonafide aanbieder is de Bibob-toets in eerste instantie een last: een formulier van tientallen pagina's, bewijsstukken van jaren terug, een onderzoek van weken waarin uw netwerk wordt doorgelicht. Drie redenen waarom hij toch van belang is, ook voor u.</p>
<p><strong>Hij is niet te vermijden.</strong> Wie Wmo- of jeugdhulp wil leveren via een gemeentelijk contract, komt de toets tegen, nu in een aantal regio's structureel en elders op signaal, en de komende jaren breder. De VNG en het ministerie van VWS zetten in op landelijke uitrol via het programma Aanpak Zorgfraude. Voorbereiding is daarmee geen optie maar een bedrijfsvoeringsvereiste, net als een kwaliteitssysteem.</p>
<p><strong>Hij beschermt uw markt.</strong> Een aanbieder die eerlijk werkt, concurreert nu met partijen die tarieven kunnen bieden omdat zij niet leveren wat zij declareren. Elke malafide aanbieder die aan de voorkant wordt tegengehouden, is een concurrent minder en een argument minder voor gemeenten om tarieven te verlagen en de controledruk voor iedereen op te voeren.</p>
<p><strong>Hij dwingt tot orde die u toch nodig hebt.</strong> Wat de Bibob-toets vraagt, is wat een bank, een accountant of een overnemende partij ook vraagt: een kloppend organogram, gedocumenteerde financiering, schriftelijke afspraken met onderaannemers, een UBO-registratie die klopt. Wie dat op orde brengt voor de Bibob-toets, heeft het op orde voor alles.</p>

<h2>Het risico voor wie zich niet voorbereidt</h2>
<p>De toets is streng voor onvolledigheid en onverschillig voor goede bedoelingen. Een aanbieder met uitstekende cliënttevredenheid en schone inspectierapporten kan een contract verliezen door een lening van een familielid zonder overeenkomst, een voormalige compagnon die nog in het handelsregister staat of een onderaannemer met een verleden. De gemeente hoeft daarbij niet te bewijzen dat u iets verkeerd deed; zij beoordeelt een risico. En een conclusie "ernstig gevaar" wordt vijf jaar geregistreerd, zodat zij doorwerkt bij elke andere gemeente en bij een Wtza-vergunning.</p>
<p>Daartegenover staat dat de toets voor wie zich voorbereidt goed te doorstaan is. In de regio's die structureel toetsen, krijgt de overgrote meerderheid van de aanbieders de uitkomst "geen gevaar". De aanbieders die vastlopen, zijn vrijwel altijd degenen die het formulier onderschatten.</p>

<h2>Wat het belang van de toets voor uw praktijk betekent</h2>
''' + steps([
        ("Zie de toets als vast onderdeel van de inkoop", "Reken bij elke inkoopronde en elke contractverlenging op een Bibob-bepaling en lees die zoals u de tariefbijlage leest."),
        ("Breng uw netwerk in kaart voordat de gemeente het doet", "Bestuurders, aandeelhouders, financiers, onderaannemers, verhuurders: wie zijn het, wat is hun rol en is die vastgelegd?"),
        ("Documenteer het geld", "Elke euro die de onderneming in is gekomen, heeft een herkomst en een papier. Ontbreekt dat, herstel het nu."),
        ("Houd het actueel", "Een Bibob-dossier is geen eenmalige exercitie. Elke wijziging in bestuur, aandelen of samenwerking hoort erin."),
    ]) + '''
<p>Hoe de toets precies werkt leest u in <a href="bibob-toets.html">De Bibob-toets</a>; hoe u uw organisatie erop voorbereidt in <a href="bibob-proof-zorgonderneming.html">Bibob-proof ondernemen in de zorg</a>.</p>
''',
    faq=[
        ("Is de Bibob-toets niet vooral bedoeld voor criminelen?", "De toets is bedoeld om te voorkomen dat de overheid criminele activiteiten faciliteert. Maar hij wordt toegepast op iedereen die inschrijft, en de uitkomst hangt af van wat u aanlevert en wie in uw netwerk zit. Ook een bonafide aanbieder kan vastlopen op onvolledigheid."),
        ("Worden alle zorgaanbieders getoetst?", "Nog niet. Een aantal regio's toetst structureel bij inkoop; de meeste gemeenten toetsen op signaal. De verwachting is dat structurele toetsing de komende jaren uitbreidt."),
        ("Kan ik de toets ontlopen door alleen met pgb's te werken?", "Een pgb-aanbieder kan niet rechtstreeks worden getoetst, maar gemeenten stellen via de verordening steeds meer eisen aan pgb-aanbieders en de VNG onderzoekt hoe screening daar alsnog mogelijk wordt. Het is geen duurzame strategie."),
        ("Wat kost het om me voor te bereiden?", "Voor een aanbieder met een eenvoudige structuur en gedocumenteerde financiering: enkele uren werk en geen externe kosten. Voor een holdingstructuur met meerdere financiers en onderaannemers: een dagdeel tot enkele dagen, eventueel met begeleiding."),
    ],
    **CONTACT_STD)

add("bibob-proof-zorgonderneming.html", "Bibob-proof ondernemen in de zorg", "Hoe u structuur, financiering en relaties zo inricht dat de toets geen verrassingen oplevert.", "belang",
    title="Bibob-proof ondernemen in de zorg: structuur, geld en relaties op orde",
    desc="Praktische leidraad om uw zorgonderneming voor te bereiden op een Bibob-toets: rechtsvorm en organogram, documentatie van financiering, afspraken met onderaannemers en verhuurders, UBO-registratie en een actueel Bibob-dossier.",
    h1="Bibob-proof ondernemen in de zorg",
    intro="Bibob-proof betekent niet dat u de toets ontloopt, maar dat u hem zonder verrassingen doorstaat: elke vraag op het formulier is in een uur te beantwoorden met een stuk uit uw eigen dossier. Dit is wat daarvoor nodig is, in de volgorde waarin de gemeente ernaar kijkt.",
    marge=marge([
        ("Grondslag toets", "Art. 3 Wet Bibob: betrokkene, leidinggevenden, zeggenschaphebbenden, vermogensverschaffers, zakelijk samenwerkingsverband"),
        ("Hulpmiddelen", ["Handelsregister en UBO-register (KvK)", "Aandeelhoudersregister (art. 2:194 BW)", "Leningsovereenkomsten", "Onderaannemingsovereenkomsten"]),
        ("Tijdsbeslag", "Eenvoudige structuur: een dagdeel. Holding met meerdere financiers: enkele dagen."),
    ]),
    body='''
<h2>1. Structuur: één waarheid in alle registers</h2>
<p>De gemeente legt uw organogram naast het handelsregister, het UBO-register, de statuten en het aandeelhoudersregister. Elke afwijking roept een vraag op en elke vraag kost tijd. Controleer daarom of bestuurders, aandeelhouders en percentages overal gelijk zijn, of uitgetreden bestuurders zijn uitgeschreven, of een aandelenoverdracht ook in het aandeelhoudersregister staat en of de UBO-registratie klopt. Een stichting met een bv eronder, een holding met een werkmaatschappij, een vof die later een bv werd: leg de geschiedenis vast in een kort memo met data en aktes, zodat u niet hoeft te reconstrueren onder tijdsdruk.</p>
<p>Houd de structuur zo eenvoudig als uw bedrijfsvoering toelaat. Elke extra vennootschap, elke stille vennoot en elk certificaat is een extra persoon die wordt onderzocht. Een structuur die om fiscale redenen is opgetuigd, kan Bibob-technisch meer kosten dan zij fiscaal oplevert.</p>

<h2>2. Financiering: elke euro heeft een papier</h2>
<p>Dit is het onderdeel waarop zorgdossiers vastlopen. De gemeente wil weten waar het startkapitaal vandaan kwam en hoe de onderneming daarna is gefinancierd. Voor elke bron geldt dezelfde eis: een document dat de afspraak vastlegt én een bankafschrift dat de geldstroom laat zien.</p>
<ul>
<li><strong>Eigen inbreng:</strong> bankafschrift van de storting plus een stuk over de herkomst (salarisstroken, verkoopakte woning, verklaring van erfrecht).</li>
<li><strong>Lening van familie of bekenden:</strong> een ondertekende leningsovereenkomst met bedrag, rente, looptijd en aflossing, plus het afschrift van de overboeking. Een mondelinge afspraak uit 2019 kan alsnog schriftelijk worden vastgelegd, met de werkelijke datum van de lening erin; dat is geen antedatering maar vastlegging achteraf, en zo moet u het ook noemen.</li>
<li><strong>Bank of financier:</strong> de kredietovereenkomst.</li>
<li><strong>Rekening-courant met de dga of de holding:</strong> een overeenkomst en een jaarlijks saldo-overzicht.</li>
<li><strong>Contante inbreng:</strong> vermijd die. Is zij er geweest, documenteer dan zo goed mogelijk de herkomst en wees er open over.</li>
</ul>
<p>De gemeente kijkt ook naar wie meeprofiteert. Een financier die een hoge rente of een winstdeel ontvangt, is voor de wet een vermogensverschaffer wiens antecedenten meewegen. Weet wie uw financiers zijn.</p>

<h2>3. Relaties: schriftelijk en opzegbaar</h2>
<p>Onderaannemers, structurele zzp'ers, bemiddelingsbureaus, administratiekantoren met tekenbevoegdheid en verhuurders van zorglocaties vormen met u een zakelijk samenwerkingsverband (art. 3 lid 4 onder c). U hoeft hun antecedenten niet te onderzoeken, maar u moet weten wie zij zijn en de relatie moet zijn vastgelegd. Zorg voor een overeenkomst met elke onderaannemer, met een bepaling dat deze meewerkt aan een Bibob-onderzoek van de gemeente en dat u de overeenkomst kunt beëindigen als de gemeente dat op grond van de Wet Bibob verlangt. Zonder die bepaling zit u klem tussen de gemeente die vervanging eist en de onderaannemer die zich op het contract beroept.</p>

<h2>4. Personen: wie er nog meer in beeld komen</h2>
<p>Een voormalige bestuurder die nog een lening heeft uitstaan, een echtgenoot die de administratie doet, een adviseur die feitelijk de inkoop regelt: de wet kijkt naar de werkelijke rol, niet naar de titel. Loop na wie feitelijk invloed heeft op uw onderneming en of die invloed is geformaliseerd of beëindigd. Is iemand vertrokken, maak dat dan compleet: uitschrijving, afwikkeling van leningen en aandelen, en een vastgelegde datum.</p>

<h2>5. Het Bibob-dossier: één map, altijd actueel</h2>
<p>Leg alles uit de punten 1 tot en met 4 vast in één dossier, digitaal of fysiek, met een inhoudsopgave die de volgorde van het Bibob-vragenformulier volgt. Werk het bij bij elke wijziging in bestuur, aandelen, financiering of samenwerking. Als de gemeente dan het formulier stuurt, is het een kwestie van invullen en bijlagen nummeren. De <a href="bibob-vragenformulier.html">checklist bij het vragenformulier</a> is bruikbaar als inhoudsopgave.</p>

<h2>6. Wat u niet moet doen</h2>
<ul>
<li>Een vak openlaten of een relatie weglaten omdat u denkt dat de gemeente het niet ziet. Zij ziet het, en weglaten weegt zwaarder dan het feit zelf.</li>
<li>Een structuur optuigen met stromannen om personen buiten beeld te houden. Dat is precies wat de wet beoogt te vinden en het maakt van een bonafide dossier een verdacht dossier.</li>
<li>Wachten met opruimen tot het formulier er is. Een relatie die pas na het voornemen wordt beëindigd, overtuigt minder dan een die een jaar eerder al is afgewikkeld.</li>
</ul>
<p>Wilt u weten waar uw organisatie staat? Een <a href="./#diensten">quickscan vooraf</a> loopt deze vijf punten in een dagdeel met u door.</p>
''',
    faq=[
        ("Moet ik mijn structuur vereenvoudigen om Bibob-proof te zijn?", "Niet per se. Een holdingstructuur is op zichzelf geen probleem, zolang elke laag is gedocumenteerd en de personen erachter bekend en integer zijn. Wel geldt: hoe meer lagen, hoe meer werk en hoe meer personen worden onderzocht."),
        ("Mijn startkapitaal kwam van mijn ouders, zonder contract. Is dat een probleem?", "Het is een veelvoorkomende situatie en op zichzelf geen gevaar. Leg de lening of schenking alsnog schriftelijk vast met de werkelijke datum en voeg het bankafschrift van destijds toe. Wees in het formulier open over het feit dat de vastlegging achteraf is gebeurd."),
        ("Moet ik mijn onderaannemers zelf screenen?", "De wet verplicht u daar niet toe, maar u draagt wel het risico. Vraag in elk geval een recent uittreksel en een eigen verklaring, en neem een Bibob-medewerkingsbepaling op in de overeenkomst."),
        ("Hoe vaak moet ik het Bibob-dossier bijwerken?", "Bij elke wijziging in bestuur, aandelen, financiering of structurele samenwerking, en in elk geval jaarlijks bij het vaststellen van de jaarrekening."),
    ],
    **CONTACT_STD)

add("bibob-financiering-zorgonderneming.html", "Financiering en de Bibob-toets", "Waarom de herkomst van uw geld het zwaarst weegt en hoe u die aantoont.", "belang",
    title="Financiering van een zorgonderneming en de Bibob-toets: herkomst van geld aantonen",
    desc="Hoe de gemeente bij een Bibob-toets kijkt naar de financiering van uw zorgonderneming: startkapitaal, leningen van familie, rekening-courant, financiers en vermogensverschaffers. Welke bewijsstukken u nodig hebt en wat problemen oplevert.",
    h1="Financiering en de Bibob-toets: waarom de herkomst van uw geld het zwaarst weegt",
    intro="Van alle onderdelen van het Bibob-onderzoek is de financiering het onderdeel waarop zorgaanbieders het vaakst vastlopen. Niet omdat het geld fout is, maar omdat de herkomst niet is te bewijzen. De wet kijkt naar twee dingen: of de onderneming met crimineel geld is gefinancierd, en of degenen die het geld verschaften integer zijn.",
    marge=marge([
        ("Grondslag", "Art. 3 lid 1 onder a (benutten van voordeel uit strafbare feiten); art. 3 lid 4 onder c (vermogensverschaffer)"),
        ("Gevraagd", ["Startkapitaal en herkomst", "Alle leningen en financiers", "Rekening-courant met dga/holding", "Jaarrekeningen"]),
        ("Bewijs", "Per bron: de afspraak op papier én het bankafschrift van de geldstroom"),
        ("Fiscaal", "De gemeente mag fiscale informatie betrekken; onverklaard vermogen is een signaal"),
    ]),
    body='''
<h2>Wat de wet met financiering wil</h2>
<p>De a-grond van art. 3 Wet Bibob gaat over het benutten van voordeel uit strafbare feiten: het gevaar dat crimineel geld via uw onderneming wordt witgewassen of dat de onderneming draait op geld dat niet legaal is verdiend. De gemeente onderzoekt daarom hoe de onderneming is gestart en gefinancierd, en of de omvang van het vermogen past bij het inkomen en de geschiedenis van de betrokkenen. Daarnaast is iedereen die vermogen heeft verschaft een "betrokkene" in de zin van art. 3 lid 4: zijn of haar antecedenten wegen mee alsof het uw eigen antecedenten zijn.</p>
<p>In de zorg is dit extra relevant omdat de sector weinig kapitaal vraagt om te starten en snel omzet genereert. Dat maakt haar aantrekkelijk voor wie geld een legale herkomst wil geven. De gemeente kijkt dus met argwaan naar startkapitaal zonder herkomst, naar leningen van personen zonder aantoonbaar vermogen en naar een omzet die niet past bij het aantal cliënten.</p>

<h2>De vijf financieringsbronnen en hun bewijs</h2>
<dl class="lijst">
<div class="item"><dt><h3>Eigen inbreng<em>Spaargeld, verkoop woning, erfenis</em></h3></dt><dd><p>Bankafschrift van de storting in de onderneming, plus een stuk dat de herkomst laat zien: salarisstroken of aangiften van de jaren ervoor, de verkoopakte, de verklaring van erfrecht. Hoe groter het bedrag in verhouding tot uw inkomen, hoe belangrijker dit stuk.</p></dd></div>
<div class="item"><dt><h3>Lening van familie of bekenden<em>De meest voorkomende valkuil</em></h3></dt><dd><p>Een ondertekende leningsovereenkomst met bedrag, datum, rente, looptijd en aflossingsschema, en het bankafschrift van de overboeking. Ontbreekt de overeenkomst, leg de afspraak dan alsnog vast met de werkelijke datum en vermeld dat het een vastlegging achteraf is. De gemeente kan daarnaast willen weten waar de uitlener het geld vandaan had; vraag uw financier daar nu al om.</p></dd></div>
<div class="item"><dt><h3>Bank of externe financier<em>Krediet, lease, factoring</em></h3></dt><dd><p>De overeenkomst volstaat meestal. Bij een niet-bancaire financier onderzoekt de gemeente ook die financier; een onbekende investeringsmaatschappij met hoge rente en een winstdeel trekt aandacht.</p></dd></div>
<div class="item"><dt><h3>Rekening-courant en interne leningen<em>Dga, holding, zustervennootschap</em></h3></dt><dd><p>Een rekening-courantovereenkomst en de jaarlijkse saldi uit de jaarrekening. Een oplopende schuld van de dga aan de bv zonder afspraken wordt gelezen als onttrekking en roept fiscale vragen op die de gemeente mag betrekken.</p></dd></div>
<div class="item"><dt><h3>Winst uit onderneming<em>Herinvestering</em></h3></dt><dd><p>De jaarrekeningen. Let op consistentie: een omzet die niet past bij het aantal gedeclareerde uren of cliënten is een signaal dat gemeenten expliciet onderzoeken sinds de zorgfraudezaken.</p></dd></div>
</dl>

<h2>Wat problemen oplevert</h2>
<ul>
<li><strong>Contant geld.</strong> Een contante storting van enige omvang is zonder sluitende herkomst vrijwel niet te verklaren. Als het is gebeurd, documenteer dan wat u kunt en wees er open over.</li>
<li><strong>Geld via privérekeningen.</strong> Zakelijke ontvangsten of leningen die via de privérekening van een bestuurder of familielid lopen, maken de geldstroom onherleidbaar. Zet alles om naar de zakelijke rekening en documenteer de overgang.</li>
<li><strong>Financiers met een verleden.</strong> Een lening van iemand met een strafblad of een eerdere Bibob-weigering telt tegen u, ook als de lening zelf netjes is. Weet van wie u geld aanneemt. Een lening aflossen en de relatie beëindigen is mogelijk; doe dat voordat de gemeente ernaar vraagt.</li>
<li><strong>Onverklaarde groei.</strong> Een vermogen of omzet die niet is te rijmen met de activiteiten is op zichzelf een vermoeden van een strafbaar feit dat de gemeente mag meewegen.</li>
</ul>

<h2>Als u de stukken niet meer hebt</h2>
<p>Banken bewaren afschriften doorgaans zeven tot tien jaar en verstrekken ze op verzoek. Notarissen bewaren aktes. De Belastingdienst heeft uw aangiften. Wat u niet kunt reconstrueren, beschrijft u: wat er is gebeurd, wanneer, waarom er geen stuk is en wat u wél kunt aantonen. Een eerlijke, gedocumenteerde lacune weegt lichter dan een leeg vak of een verhaal zonder papier.</p>
<p>Zie ook <a href="bibob-vragenformulier.html">het vragenformulier</a> voor de volledige checklist en <a href="bibob-bestuurder-aandeelhouder.html">bestuurders en aandeelhouders</a> voor de personen die bij de financiering in beeld komen.</p>
''',
    faq=[
        ("Hoe ver terug kijkt de gemeente naar de financiering?", "Tot aan de start van de onderneming als het formulier daarnaar vraagt. In de praktijk ligt de nadruk op de laatste vijf jaar en op het startkapitaal."),
        ("Moet mijn financier ook zijn financiering aantonen?", "Niet standaard, maar de gemeente of het LBB kan ernaar vragen als de financier zelf niet over aantoonbaar vermogen beschikt. Bespreek dit vooraf met uw financier."),
        ("Is een lening van een familielid verdacht?", "Nee, het is de normaalste financieringsvorm voor kleine ondernemers. Het probleem ontstaat alleen als de lening niet is vastgelegd of de herkomst van het geld bij het familielid onduidelijk is."),
        ("Mag de gemeente mijn belastingaangiften inzien?", "De gemeente kan fiscale informatie betrekken via het LBB, dat toegang heeft tot gegevens van de Belastingdienst. Daarnaast kan het formulier u vragen zelf aangiften bij te voegen."),
    ],
    **CONTACT_STD)

add("bibob-bestuurder-aandeelhouder.html", "Bestuurders, aandeelhouders en de Bibob-toets", "Wie er precies worden onderzocht en wat een verleden van één persoon voor de onderneming betekent.", "belang",
    title="Bestuurders, aandeelhouders en leidinggevenden bij de Bibob-toets",
    desc="Wie de gemeente onderzoekt bij een Bibob-toets van een zorgaanbieder: bestuurders, aandeelhouders, UBO's, feitelijk leidinggevenden en voormalige betrokkenen. Hoe antecedenten van één persoon de hele onderneming raken en wat u kunt doen.",
    h1="Bestuurders, aandeelhouders en leidinggevenden: wie de gemeente onderzoekt",
    intro="Een Bibob-toets gaat zelden over de rechtspersoon alleen. De wet rekent de antecedenten van bestuurders, aandeelhouders, feitelijk leidinggevenden en financiers toe aan de onderneming. Eén persoon met een verleden kan daardoor het contract van een hele organisatie kosten, ook als die persoon niets met de zorg te maken heeft.",
    marge=marge([
        ("Grondslag", "Art. 3 lid 4 Wet Bibob: betrokkene is ook wie direct of indirect leiding geeft, zeggenschap heeft of vermogen verschaft"),
        ("In beeld", ["statutair bestuurders", "aandeelhouders en certificaathouders", "UBO's (≥ 25% of feitelijke zeggenschap)", "feitelijk leidinggevenden zonder titel", "commissarissen en toezichthouders", "voormalige betrokkenen met voortdurende invloed"]),
        ("Weging", "Art. 3 lid 2 en 3: ernst, aantal, tijdsverloop, samenhang met de activiteit"),
    ]),
    body='''
<h2>Wie wordt onderzocht</h2>
<p>De wet gebruikt een ruim begrip van "betrokkene". Naast de onderneming zelf gaat het om iedereen die direct of indirect leiding geeft of heeft gegeven, zeggenschap heeft of heeft gehad, of vermogen verschaft of heeft verschaft (art. 3 lid 4 onder a tot en met c). Dat betekent in de praktijk: de statutair bestuurders, alle aandeelhouders van betekenis en de uiteindelijk belanghebbenden daarachter, de raad van toezicht of commissarissen, en iedereen die feitelijk de dienst uitmaakt zonder dat het in het handelsregister staat. Ook personen die zijn vertrokken maar nog invloed hebben, bijvoorbeeld via een lening, een adviesovereenkomst of een familieband met de huidige bestuurder, kunnen worden meegewogen.</p>
<p>Het LBB kijkt daarbij door structuren heen. Een stichting met een bv eronder wordt onderzocht tot aan de natuurlijke personen in het stichtingsbestuur; een holding tot aan de dga; een stichting administratiekantoor tot aan de certificaathouders. Wie denkt een persoon buiten beeld te houden door hem geen formele rol te geven, bereikt het tegendeel: feitelijk leidinggeven zonder registratie is op zichzelf een signaal.</p>

<h2>Hoe antecedenten worden gewogen</h2>
<p>Niet elk feit telt even zwaar. Art. 3 lid 2 en 3 noemen de factoren: de ernst van het feit, het aantal feiten, het tijdsverloop en de samenhang met de activiteit waarvoor wordt gecontracteerd. Een verkeersovertreding van een aandeelhouder van tien jaar geleden weegt niet; een veroordeling voor fraude, witwassen, uitkeringsfraude of een zedendelict van een bestuurder weegt zwaar, en in de zorg weegt alles wat met declaraties, kwetsbare personen of de omgang met publiek geld te maken heeft extra. Ook vermoedens tellen: een lopend strafrechtelijk onderzoek, een sepot wegens gebrek aan bewijs, een bestuurlijke boete, een eerdere beëindiging van een zorgcontract wegens onrechtmatigheid of een vermelding in het Waarschuwingsregister zorgfraude.</p>
<p>Een veroordeling is dus niet vereist en een vrijspraak is niet altijd voldoende: het bestuursorgaan beoordeelt een risico, geen schuld. Dat voelt onrechtvaardig, en de rechter toetst daarom streng of het bestuursorgaan de feiten voldoende aannemelijk heeft gemaakt en de weging heeft gemotiveerd.</p>

<h2>Als één persoon het probleem is</h2>
<p>Blijkt uit het advies dat de gevaarsconclusie rust op één persoon, dan hebt u in de zienswijze drie wegen. De eerste is bestrijden: de feiten kloppen niet, zijn verjaard of hebben geen samenhang met de zorg. De tweede is duiden: de persoon heeft feitelijk geen invloed op de zorg of de geldstromen, en dat is vastgelegd. De derde, vaak de meest effectieve, is beëindigen: de persoon treedt terug, draagt aandelen over, de lening wordt afgelost en dit alles wordt gedocumenteerd. De gemeente kan een beëindiging als voorwaarde stellen (art. 3 lid 7) in plaats van het contract te weigeren. Een beëindiging die alleen op papier gebeurt terwijl de invloed blijft, wordt bij een volgend onderzoek gevonden en maakt het dossier er niet beter op.</p>

<h2>Wat u vooraf kunt doen</h2>
<ul>
<li>Vraag bij toetreding van een bestuurder, aandeelhouder of financier naar zijn verleden en leg zijn verklaring vast. Een VOG is daarbij een hulpmiddel, geen garantie: de Bibob-toets kijkt breder.</li>
<li>Neem in aandeelhoudersovereenkomsten en bestuurdersovereenkomsten een bepaling op dat een betrokkene meewerkt aan Bibob-onderzoeken en terugtreedt als de gemeente dat op grond van de Wet Bibob verlangt.</li>
<li>Rond vertrek volledig af: uitschrijving, overdracht van aandelen, aflossing van leningen, beëindiging van adviesrelaties, en een datum die in alle registers klopt.</li>
<li>Formaliseer wie feitelijk leiding geeft. Doet een partner of adviseur dat zonder titel, geef hem dan een titel of beperk zijn rol aantoonbaar.</li>
</ul>
<p>Over de financiers afzonderlijk: <a href="bibob-financiering-zorgonderneming.html">Financiering en de Bibob-toets</a>. Over het geheel: <a href="bibob-proof-zorgonderneming.html">Bibob-proof ondernemen</a>.</p>
''',
    faq=[
        ("Telt een strafblad van mijn partner mee als die niet in de onderneming zit?", "Alleen als uw partner feitelijk invloed heeft, vermogen heeft verschaft of met u in een zakelijk samenwerkingsverband staat. Een huwelijk alleen is geen grond, maar een gezamenlijke rekening waaruit de onderneming is gefinancierd kan dat wel maken."),
        ("Kan een VOG een Bibob-toets vervangen?", "Nee. Een VOG betreft één persoon, één functie en alleen justitiële gegevens. De Bibob-toets betreft het hele netwerk en mag ook vermoedens, fiscale informatie en bestuurlijke boetes meewegen."),
        ("Hoe lang blijft een oud feit meetellen?", "De wet noemt geen termijn; het tijdsverloop is een wegingsfactor. In de rechtspraak wordt een feit van meer dan vijf jaar geleden zonder herhaling en zonder samenhang met de activiteit doorgaans licht gewogen; voor ernstige feiten ligt die grens verder."),
        ("Mijn medebestuurder heeft iets verzwegen. Wat nu?", "Meld het de gemeente zelf voordat zij het vindt, met uw voorstel voor de gevolgen. Een onderneming die zelf opruimt, wordt anders beoordeeld dan een die wordt betrapt."),
    ],
    **CONTACT_STD)

add("bibob-register.html", "Het Bibob-register en de gevolgen", "Wat registratie van een gevaarsconclusie betekent voor uw toekomst als zorgaanbieder.", "belang",
    title="Het Bibob-register: registratie, bewaartermijn en gevolgen voor zorgaanbieders",
    desc="Wat het Bibob-register bij het Landelijk Bureau Bibob is, welke uitkomsten worden geregistreerd, hoe lang, wie het mag raadplegen en hoe een registratie doorwerkt bij andere gemeenten, de Wtza-vergunning en een doorstart.",
    h1="Het Bibob-register: waarom een negatieve uitkomst u jaren achtervolgt",
    intro="Een negatieve Bibob-uitkomst eindigt niet bij één gemeente. Het Landelijk Bureau Bibob registreert gevaarsconclusies, en elk bestuursorgaan dat later een Bibob-onderzoek naar u instelt, ziet die registratie. Dat is het belangrijkste argument om een toets serieus te nemen vóórdat hij negatief uitvalt.",
    marge=marge([
        ("Grondslag", "Art. 11a Wet Bibob (register), art. 12 en 20 (gegevensverwerking LBB)"),
        ("Geregistreerd", "Adviezen met conclusie ernstig gevaar en mindere mate van gevaar; eigen onderzoeken van bestuursorganen met gevaarsconclusie"),
        ("Bewaartermijn", "Vijf jaar"),
        ("Raadpleging", "Door bestuursorganen die zelf een Bibob-onderzoek doen of advies vragen; niet openbaar"),
    ]),
    body='''
<h2>Wat wordt geregistreerd</h2>
<p>Het Landelijk Bureau Bibob houdt een register bij van eerdere Bibob-onderzoeken. Daarin worden opgenomen de adviezen van het Bureau die uitmonden in ernstig gevaar of een mindere mate van gevaar, en sinds de wetswijziging van 2020 ook de uitkomsten van eigen onderzoeken van bestuursorganen waarin een gevaarsconclusie is getrokken. Een uitkomst "geen gevaar" wordt niet geregistreerd. Geregistreerd worden de naam van de betrokkene, de personen en ondernemingen die in het onderzoek zijn betrokken, de conclusie en het bestuursorgaan dat het onderzoek deed.</p>

<h2>Wie het register mag raadplegen</h2>
<p>Het register is niet openbaar. Een bestuursorgaan dat zelf een eigen onderzoek doet (art. 7a) kan bij het Bureau navragen of u of de aan u verbonden personen voorkomen in het register; het Bureau raadpleegt het register bij elk adviesverzoek. Zorgkantoren, zorgverzekeraars, banken en werkgevers hebben geen toegang. Wel kunnen gegevens uit een Bibob-onderzoek onder voorwaarden worden gedeeld met andere bestuursorganen (art. 28 lid 2 en art. 11a), bijvoorbeeld als een andere gemeente dezelfde aanbieder onderzoekt.</p>

<h2>Hoe een registratie doorwerkt</h2>
<p>Een registratie is geen automatische weigering, maar wel een zwaarwegend signaal. Drie situaties waarin zij zorgaanbieders raakt:</p>
<ul>
<li><strong>Inkoop door een andere gemeente.</strong> Schrijft u na een weigering in Twente in bij een inkoop in Zuid-Holland, dan ziet die gemeente bij haar eigen onderzoek de eerdere conclusie en zal zij die betrekken. Zij moet wel zelfstandig beoordelen of de situatie sindsdien is veranderd.</li>
<li><strong>Wtza-vergunning.</strong> Het CIBG kan een Bibob-onderzoek instellen bij een vergunningaanvraag en raadpleegt dan het register. Een eerdere gemeentelijke gevaarsconclusie kan zo een vergunning voor Zvw- of Wlz-zorg in de weg staan.</li>
<li><strong>Doorstart in een nieuwe rechtspersoon.</strong> Het register is persoonsgebonden. Een nieuwe bv met dezelfde bestuurder of financier wordt aan de eerdere conclusie gekoppeld. Een doorstart onder een andere naam is daarmee geen schone lei.</li>
</ul>

<h2>Hoe lang</h2>
<p>De bewaartermijn is vijf jaar na de conclusie. Daarna worden de gegevens verwijderd. In die vijf jaar kunt u wel aantonen dat de situatie is veranderd: een beëindigde relatie, een afgeloste lening, een vertrokken bestuurder. Een bestuursorgaan dat de registratie ziet, moet die nieuwe feiten meewegen en mag niet volstaan met verwijzing naar de oude conclusie.</p>

<h2>Inzage en correctie</h2>
<p>U kunt bij het Landelijk Bureau Bibob op grond van de AVG inzage vragen in de gegevens die over u zijn geregistreerd, en om correctie vragen als zij feitelijk onjuist zijn. De inhoud van het onderliggende advies krijgt u via die weg niet; dat valt onder de geheimhouding van art. 28. Een conclusie die u onjuist acht, bestrijdt u in de zienswijze en zo nodig bij de rechter; wordt het besluit vernietigd, dan wordt de registratie aangepast.</p>

<h2>Wat dit betekent voor uw strategie</h2>
<p>Het register maakt de eerste toets de belangrijkste. Een "ernstig gevaar" dat niet in de zienswijze wordt gekeerd, beperkt vijf jaar lang uw mogelijkheden in heel Nederland. Investeer daarom in de voorbereiding en in de zienswijze, en overweeg bij een voornemen eerder de inschrijving in te trekken dan een registratie te riskeren als het dossier niet te redden is. Zie <a href="negatief-bibob-advies.html">Negatief advies en zienswijze</a>.</p>
''',
    faq=[
        ("Kan ik zelf controleren of ik in het Bibob-register sta?", "U kunt een inzageverzoek doen bij het Landelijk Bureau Bibob (Justis). U krijgt dan te zien welke gegevens over u zijn geregistreerd, niet de inhoud van het advies."),
        ("Wordt een uitkomst \"geen gevaar\" ook geregistreerd?", "Nee. Alleen conclusies van ernstig gevaar en mindere mate van gevaar worden opgenomen."),
        ("Ziet mijn zorgkantoor de registratie?", "Nee. Zorgkantoren en zorgverzekeraars zijn geen bestuursorganen en hebben geen toegang tot het register. Zij kunnen wel via het Waarschuwingsregister zorgfraude en eigen screening tot een vergelijkbaar oordeel komen."),
        ("Kan ik de registratie laten verwijderen als ik mijn bedrijf heb aangepast?", "Niet voortijdig; de termijn is vijf jaar. Wel kunt u bij elk nieuw onderzoek aantonen dat de omstandigheden zijn veranderd, en het bestuursorgaan moet dat meewegen."),
    ],
    **CONTACT_STD)

# =====================================================================
# B. SITUATIES
# =====================================================================

add("bibob-aanbesteding-zorg.html", "Bibob bij aanbesteding en open house", "Hoe de toets in de inkoop van Wmo en Jeugdwet is ingebouwd en wat u vooraf moet lezen.", "situaties",
    title="Bibob bij aanbesteding en open house: inkoop Wmo en Jeugdwet",
    desc="Hoe gemeenten de Bibob-toets inzetten bij aanbesteding, open house en toelatingsprocedures voor Wmo-ondersteuning en jeugdhulp: de Bibob-bepaling in inkoopdocumenten en contract, screening bij selectie en tijdens de looptijd, gunning onder voorbehoud en ontbinding.",
    h1="Bibob bij aanbesteding en open house in de zorg",
    intro="Bij de inkoop van Wmo-ondersteuning en jeugdhulp is de Bibob-toets sinds 2022 een vast onderdeel van wat gemeenten kúnnen doen en in steeds meer regio's een vast onderdeel van wat zij dóen. Hoe de toets in uw inkoop is ingebouwd, staat in twee documenten die u vóór inschrijving moet lezen: de inkoopleidraad en de concept-raamovereenkomst.",
    marge=marge([
        ("Grondslag", "Art. 1 lid 4 en art. 5 Wet Bibob; art. 2.1.1 Wmo 2015; art. 2.11 Jeugdwet"),
        ("Momenten", ["bij inschrijving of toelating", "vóór gunning (gunning onder voorbehoud)", "tijdens de looptijd bij signalen", "bij verlenging of nieuwe ronde"]),
        ("Gevolgen", "Uitsluiting, niet-gunnen, voorschriften, ontbinding"),
        ("Rechtsbescherming", "Civiel: kort geding bij de rechtbank"),
    ]),
    body='''
<h2>Waarom open house onder de wet is gebracht</h2>
<p>Open house is een inkoopmodel waarbij de gemeente de voorwaarden en het tarief vaststelt en elke aanbieder die eraan voldoet een overeenkomst krijgt; de cliënt kiest daarna. Het Hof van Justitie oordeelde in Falk Pharma (C-410/14) en Tirkkonen (C-9/17) dat dit geen overheidsopdracht is, omdat de gemeente niet selecteert. Daarmee viel het grootste deel van de zorginkoop buiten de Wet Bibob, terwijl juist daar de problemen zaten. Art. 1 lid 4 Wet Bibob bepaalt sinds 1 oktober 2022 dat een overeenkomst waarmee zorg wordt ingekocht op grond van art. 2.11 Jeugdwet of art. 2.1.1 Wmo 2015 via een open house of toelatingsprocedure voor de toepassing van de wet als overheidsopdracht geldt. Een echte aanbesteding viel al onder de wet (art. 5).</p>

<h2>De Bibob-bepaling in inkoopdocumenten en contract</h2>
<p>De gemeente kan de toets alleen inzetten als zij dat heeft aangekondigd. Zoek in de inkoopleidraad naar een paragraaf over integriteit, Bibob of screening, en in de concept-raamovereenkomst naar een artikel met dezelfde titel. De VNG-contractstandaarden Wmo (versie 1.2) en Jeugd (versie 1.4) bevatten een modelbepaling die veel gemeenten overnemen. Lees daarin vier dingen:</p>
<ul>
<li><strong>Wanneer de gemeente toetst:</strong> bij elke inschrijving, steekproefsgewijs, of alleen bij signalen.</li>
<li><strong>Wat u moet aanleveren:</strong> het vragenformulier bij inschrijving of pas op verzoek, en binnen welke termijn.</li>
<li><strong>Welke gevolgen welke uitkomst heeft:</strong> met name of de gemeente ook bij een <em>mindere mate van gevaar</em> mag ontbinden, of alleen voorschriften mag stellen. Dit verschil bepaalt uw risico.</li>
<li><strong>Onderaannemers:</strong> of u verplicht bent hen op te geven, of zij zelf een formulier moeten invullen en of de gemeente vervanging kan eisen.</li>
</ul>
<p>Is de bepaling onduidelijk, stel dan een vraag in de nota van inlichtingen. Dat is het enige moment waarop u de tekst nog kunt beïnvloeden, en het antwoord bindt de gemeente.</p>

<h2>De vier toetsmomenten</h2>
''' + steps([
        ("Bij inschrijving", "Structureel toetsende regio's laten elke inschrijver het Bibob-vragenformulier invullen als onderdeel van de inschrijving. Een onvolledig formulier kan dan tot uitsluiting leiden vóór de inhoudelijke beoordeling. Begin met het formulier op de dag dat de inkoopdocumenten verschijnen."),
        ("Vóór gunning", "Veel gemeenten gunnen onder voorbehoud van de Bibob-uitkomst, zodat u kunt starten terwijl het onderzoek loopt. Zonder dat voorbehoud kan de toets uw startdatum met maanden opschuiven; vraag ernaar."),
        ("Tijdens de looptijd", "Op basis van signalen (meldingen, toezichtsbevindingen, media, een andere gemeente) kan de gemeente een onderzoek starten en bij een gevaarsconclusie ontbinden. De contractbepaling bepaalt bij welke conclusie dat mag."),
        ("Bij verlenging of nieuwe ronde", "Een eerdere uitkomst \"geen gevaar\" vrijwaart niet van een nieuwe toets, maar u kunt naar het eerdere formulier verwijzen voor ongewijzigde onderdelen."),
    ]) + '''

<h2>Als het misgaat: de civiele route</h2>
<p>Uitsluiting van een inkoopprocedure en ontbinding van een raamovereenkomst zijn privaatrechtelijke handelingen. Bezwaar en beroep staan niet open; het middel is een kort geding bij de rechtbank, meestal binnen de standstill- of opzegtermijn die de inkoopdocumenten noemen. De rechter toetst of de gemeente haar eigen Bibob-bepaling en de procedure van art. 32 en 33 Wet Bibob heeft gevolgd, of de gevaarsconclusie voldoende is gemotiveerd en of ontbinding naar maatstaven van redelijkheid en billijkheid aanvaardbaar is. Het Gerechtshof Arnhem-Leeuwarden stond in mei 2026 ontbinding bij een mindere mate van gevaar toe omdat het contract dat uitdrukkelijk bepaalde en de aanbieder niet transparant was geweest over een bestuurswisseling. De les: lees de bepaling, en wees transparant tijdens de looptijd.</p>
<p>Zie ook <a href="bibob-onderaannemer-zorg.html">onderaanneming en het samenwerkingsverband</a> en <a href="negatief-bibob-advies.html">de zienswijze</a>.</p>
''',
    faq=[
        ("Geldt de Bibob-toets ook bij een raamovereenkomst die vóór oktober 2022 is gesloten?", "Alleen als die overeenkomst zelf een Bibob-bepaling bevat. Zonder contractuele grondslag kan de gemeente een lopende open-houseovereenkomst van vóór 2022 niet op grond van de wet ontbinden; wel bij verlenging of een nieuwe ronde."),
        ("Mag de gemeente alle inschrijvers toetsen of alleen bij signalen?", "Beide, mits aangekondigd. Structurele toetsing van alle inschrijvers is toegestaan en wordt in Twente toegepast; de meeste gemeenten kiezen voor signaalgestuurde toetsing."),
        ("Kan ik starten met zorg leveren terwijl de toets loopt?", "Als de gemeente gunt onder voorbehoud, ja. Staat dat niet in de inkoopdocumenten, vraag het dan in de nota van inlichtingen."),
        ("Wat als de gemeente mijn onderaannemer afwijst?", "De contractbepaling bepaalt meestal dat u de onderaannemer binnen een termijn vervangt. Zorg dat uw onderaannemingsovereenkomst dat mogelijk maakt."),
    ],
    **CONTACT_STD)

add("bibob-pgb-zorgaanbieder.html", "Pgb-zorgaanbieders en de Bibob-toets", "Waarom de gemeente u niet rechtstreeks kan toetsen en welke eisen zij wél stelt.", "situaties",
    title="Pgb-zorgaanbieder en de Wet Bibob: wat de gemeente wel en niet mag",
    desc="Kan de gemeente een pgb-zorgaanbieder Bibob-toetsen? Waarom het pgb buiten de Wet Bibob valt (art. 2.3.6 lid 6 Wmo 2015, art. 8.1.1 lid 5 Jeugdwet), welke eisen gemeenten via verordening en pgb-plan wel stellen, hoe een eerder Bibob-oordeel doorwerkt en wat er verandert.",
    h1="Pgb-zorgaanbieders en de Bibob-toets: wat de gemeente wel en niet mag",
    intro="Zorgaanbieders die uitsluitend via persoonsgebonden budgetten werken, vallen buiten het bereik van de Wet Bibob: de gemeente heeft geen overeenkomst met hen en verstrekt hun geen subsidie. Toch komen pgb-aanbieders de Bibob-toets tegen, indirect en in toenemende mate. Dit is hoe dat werkt.",
    marge=marge([
        ("Pgb is geen subsidie", "Art. 2.3.6 lid 6 Wmo 2015; art. 8.1.1 lid 5 Jeugdwet"),
        ("Pgb is geen overheidsopdracht", "De overeenkomst loopt tussen budgethouder en aanbieder; de gemeente is geen partij"),
        ("Wel mogelijk", ["eisen in de verordening en het pgb-plan", "weigering of intrekking van het pgb bij de budgethouder", "doorwerking van een eerder Bibob-oordeel", "Wmo-toezicht en rechtmatigheidsonderzoek"]),
        ("In ontwikkeling", "VNG laat onderzoeken hoe pgb-aanbieders alsnog gescreend kunnen worden"),
    ]),
    body='''
<h2>Waarom het pgb buiten de wet valt</h2>
<p>De Wet Bibob geldt voor beschikkingen (vergunningen, subsidies), overheidsopdrachten en vastgoedtransacties. Het pgb past in geen van die categorieën. De Wmo 2015 en de Jeugdwet bepalen uitdrukkelijk dat het pgb geen subsidie is (art. 2.3.6 lid 6 Wmo 2015; art. 8.1.1 lid 5 Jeugdwet). En de overeenkomst voor de zorg wordt gesloten tussen de budgethouder en de aanbieder, niet met de gemeente; de gemeente verstrekt het budget aan de cliënt en de SVB betaalt uit. De gemeente kan de aanbieder dus niet op grond van art. 3 Wet Bibob weigeren of een overeenkomst met hem ontbinden, want die overeenkomst bestaat niet. De VNG heeft dit in 2024 bevestigd in antwoord op vragen van gemeenten.</p>

<h2>Wat de gemeente wél kan</h2>
<h3>Eisen via de verordening</h3>
<p>Gemeenten mogen in de Wmo- en jeugdverordening eisen stellen aan de kwaliteit van zorg die met een pgb wordt ingekocht, en aan de vraag of de budgethouder in staat is het pgb te beheren. Steeds meer gemeenten eisen een pgb-plan waarin de aanbieder wordt genoemd, een "lichte toets" van die aanbieder (KvK-inschrijving, VOG van zorgverleners, kwaliteitseisen) en soms een gesprek met de aanbieder. Dat is geen Bibob-toets, maar het geeft de gemeente informatie en een weigeringsgrond jegens de budgethouder.</p>
<h3>Doorwerking van een Bibob-oordeel</h3>
<p>Heeft een aanbieder eerder bij dezelfde of een andere gemeente een conclusie "ernstig gevaar" gekregen, dan kan de gemeente dat betrekken bij de beoordeling of een budgethouder zijn pgb bij die aanbieder mag besteden. Het besluit richt zich dan tegen de budgethouder (weigering of intrekking van het pgb, of een voorwaarde dat een andere aanbieder wordt gekozen), niet tegen de aanbieder. Voor de aanbieder is het effect hetzelfde: de cliënten verdwijnen. In Alkmaar leidde een Bibob-onderzoek naar een gecontracteerde aanbieder zo ook tot beëindiging van de pgb's van haar cliënten.</p>
<h3>Wmo-toezicht en rechtmatigheidsonderzoek</h3>
<p>De gemeentelijke toezichthouder (art. 6.1 Wmo 2015) kan onderzoek doen naar de kwaliteit en rechtmatigheid van pgb-gefinancierde zorg, de aanbieder bezoeken en dossiers opvragen. Dit is de route waarlangs gemeenten als Rotterdam pgb-aanbieders doorlichten, met openbaarmaking van de rapporten. Een negatief toezichtsrapport is op zijn beurt een signaal dat bij een latere Bibob-toets meeweegt.</p>

<h2>Van pgb naar zorg in natura</h2>
<p>Veel aanbieders beginnen met pgb-cliënten en willen na enkele jaren een gemeentelijk contract. Op dat moment komt de Bibob-toets alsnog, en zij kijkt terug: naar de financiering van de start, naar de personen die er toen bij betrokken waren en naar de rechtmatigheid van de pgb-jaren. Een aanbieder die in de pgb-fase onzorgvuldig was met administratie, met zorgovereenkomsten of met de scheiding tussen privé en zakelijk, ziet dat terugkomen. Begin dus met het <a href="bibob-proof-zorgonderneming.html">Bibob-dossier</a> in de pgb-fase, niet pas bij de inschrijving.</p>

<h2>Wat eraan komt</h2>
<p>De VNG heeft in 2025 juridisch onderzoek laten doen naar mogelijkheden om pgb- en maatwerkaanbieders te screenen, omdat gemeenten zien dat partijen die de inkoop niet doorkomen via het pgb doorwerken. Mogelijke richtingen zijn een wettelijke grondslag voor screening van pgb-aanbieders, strengere verordeningseisen en betere gegevensuitwisseling via de Wet bevorderen samenwerking en rechtmatige zorg. Reken erop dat de ruimte voor ongetoetst pgb-aanbieden de komende jaren kleiner wordt.</p>
''',
    faq=[
        ("Kan de gemeente mij als pgb-aanbieder een Bibob-vragenformulier sturen?", "Zij kan het vragen, maar u bent niet verplicht het in te vullen zolang er geen overeenkomst, subsidie of vergunning aan de orde is. Weigeren kan wel gevolgen hebben voor de beoordeling van pgb-aanvragen van uw cliënten."),
        ("Mijn pgb-cliënten krijgen van de gemeente te horen dat zij een andere aanbieder moeten kiezen. Wat kan ik doen?", "Het besluit is gericht aan de budgethouder; die kan bezwaar maken en u kunt hem daarbij helpen. U kunt de gemeente ook zelf om een gesprek vragen en uw dossier aanbieden."),
        ("Geldt dit ook voor het Wlz-pgb via het zorgkantoor?", "Het zorgkantoor is geen bestuursorgaan in de zin van de Wet Bibob en kan de wet niet toepassen. Het screent wel op grond van zijn eigen beleid en de Wbsrz."),
        ("Is het verstandig om alleen met pgb's te blijven werken om de toets te vermijden?", "Het vermijdt de toets op korte termijn, maar beperkt uw groei en wordt door gemeenten als signaal gezien. Bovendien wordt de regelgeving voor pgb-aanbieders strenger."),
    ],
    **CONTACT_STD)

add("maatwerkovereenkomst-zorg.html", "Maatwerkovereenkomsten en de Bibob-toets", "Individuele contracten met niet-gecontracteerde aanbieders: wanneer de gemeente toetst.", "situaties",
    title="Maatwerkovereenkomst met de gemeente: eisen, signaalgestuurde Bibob-toets en risico's",
    desc="Wat een maatwerkovereenkomst of maatwerkcontract tussen gemeente en een niet-gecontracteerde zorgaanbieder is, wanneer gemeenten daarbij de Wet Bibob toepassen (op signaal of boven een aantal cliënten), welke eisen gelden en hoe u zich voorbereidt.",
    h1="Maatwerkovereenkomsten: zorg leveren zonder raamcontract, met Bibob-toets op signaal",
    intro="Een maatwerkovereenkomst is een individuele overeenkomst tussen de gemeente en een aanbieder die niet is gecontracteerd via de reguliere inkoop, voor één of enkele cliënten voor wie het gecontracteerde aanbod niet passend is. Het is een overeenkomst, dus de Wet Bibob is erop van toepassing. Gemeenten gebruiken die mogelijkheid selectief, maar steeds vaker.",
    marge=marge([
        ("Ook genoemd", "Maatwerkcontract, individuele overeenkomst, overeenkomst op cliëntniveau, niet-gecontracteerde aanbieder"),
        ("Grondslag toets", "Art. 5 Wet Bibob (overheidsopdracht); bij open-housekarakter art. 1 lid 4"),
        ("Praktijk", "Toets op signaal of vanaf een aantal cliënten (bijv. Nijmegen: vanaf 25 cliënten in pilot)"),
        ("Let op", "VNG signaleert maatwerk en pgb als sluiproute voor afgewezen aanbieders; toezicht neemt toe"),
    ]),
    body='''
<h2>Wat een maatwerkovereenkomst is</h2>
<p>Gemeenten kopen Wmo-ondersteuning en jeugdhulp in via raamovereenkomsten met gecontracteerde aanbieders. Voor cliënten voor wie binnen dat aanbod geen passende zorg beschikbaar is, kan de gemeente een afzonderlijke overeenkomst sluiten met een aanbieder van buiten het contract: een maatwerkovereenkomst. Zij wordt per cliënt of per kleine groep gesloten, vaak voor specialistische zorg, zorg met een bepaalde culturele of levensbeschouwelijke achtergrond of zorg in een regio waar weinig aanbod is. De voorwaarden zijn meestal de kwaliteitseisen uit de reguliere inkoop en het reguliere tarief.</p>

<h2>Waarom gemeenten hier de Bibob-toets inzetten</h2>
<p>De VNG constateert dat aanbieders die de reguliere inkoop niet doorkomen, of daar zijn beëindigd, hun cliënten soms behouden via maatwerkovereenkomsten en pgb's. De voorkant is dichtgezet, de zijdeur staat open. Gemeenten reageren door ook bij maatwerk te toetsen. Omdat maatwerk om kleine aantallen gaat en een volledige toets per cliënt onevenredig is, kiezen zij voor een signaalgestuurde aanpak: een toets bij meldingen of toezichtsbevindingen, of zodra een aanbieder een bepaald aantal maatwerkcliënten heeft. Nijmegen hanteerde in een pilot de grens van 25 cliënten en toetst daarnaast bij signalen. Vraag bij de gemeente naar de beleidsregel Bibob; daarin staat hoe zij met maatwerk omgaat.</p>

<h2>Waar u bij het sluiten op let</h2>
<ul>
<li><strong>De Bibob-bepaling.</strong> Staat er een bepaling in de maatwerkovereenkomst die de gemeente toestaat te toetsen en bij welke uitkomst zij mag ontbinden? Zonder bepaling is ontbinding op grond van de wet lastiger; met bepaling weet u waar u aan toe bent.</li>
<li><strong>De looptijd en opzegging.</strong> Maatwerkovereenkomsten zijn vaak kort en opzegbaar met een korte termijn. Bij een gevaarsconclusie kan de gemeente dan ook zonder beroep op de Wet Bibob opzeggen; de toets is dan vooral van belang voor het register.</li>
<li><strong>De relatie met de reguliere inkoop.</strong> Een maatwerkovereenkomst is voor veel aanbieders de opstap naar een raamcontract. Alles wat u in de maatwerkfase aanlevert en doet, komt terug bij de toets voor dat raamcontract.</li>
</ul>

<h2>Niet-gecontracteerd blijven: het risicoprofiel</h2>
<p>Een aanbieder die structureel via maatwerkovereenkomsten werkt en niet inschrijft op de reguliere inkoop, heeft voor de gemeente een afwijkend profiel. Dat kan een goede reden hebben (specialisme, regio, omvang), maar het is ook het profiel dat de VNG als risico benoemt. Wees daarom proactief: leg uit waarom u niet inschrijft, bied uw Bibob-dossier aan en zorg dat uw financiering en relaties gedocumenteerd zijn. Een aanbieder die het gesprek zelf opent, wordt anders behandeld dan een die wacht op het signaal.</p>
<p>Zie <a href="bibob-pgb-zorgaanbieder.html">pgb-aanbieders</a> voor de vergelijkbare situatie zonder overeenkomst en <a href="bibob-toets.html">De Bibob-toets</a> voor de uitkomsten en gevolgen.</p>
''',
    faq=[
        ("Is een maatwerkovereenkomst een overheidsopdracht?", "In de meeste gevallen wel: de gemeente koopt tegen betaling een dienst in. Daarmee valt zij onder art. 5 Wet Bibob. Heeft de gemeente een vaste regeling waarbij elke aanbieder die voldoet een maatwerkovereenkomst kan krijgen, dan geldt via art. 1 lid 4 hetzelfde."),
        ("Moet ik bij elke maatwerkovereenkomst een Bibob-formulier invullen?", "Alleen als de gemeente dat vraagt. De meeste gemeenten toetsen op signaal of boven een aantal cliënten, niet standaard."),
        ("Kan de gemeente mijn maatwerkovereenkomsten ontbinden na een Bibob-onderzoek?", "Als de overeenkomst daarin voorziet of de wet van toepassing is, ja. Vaak kan zij ook gewoon opzeggen met de contractuele termijn."),
        ("Wordt een Bibob-toets bij maatwerk geregistreerd?", "Een gevaarsconclusie wel, net als bij elke andere toets. Dat is de reden om ook een maatwerktoets serieus te nemen."),
    ],
    **CONTACT_STD)

add("bibob-onderaannemer-zorg.html", "Onderaannemers en het samenwerkingsverband", "Waarom de gemeente uw onderaannemers meeweegt en hoe u dat contractueel regelt.", "situaties",
    title="Onderaannemers, zzp'ers en het zakelijk samenwerkingsverband bij de Bibob-toets",
    desc="Hoe onderaannemers, structurele zzp'ers, bemiddelingsbureaus en verhuurders als zakelijk samenwerkingsverband (art. 3 lid 4 onder c Wet Bibob) meewegen bij de Bibob-toets van een zorgaanbieder, welke verplichtingen de hoofdaannemer heeft en welke contractbepalingen u nodig hebt.",
    h1="Onderaannemers en het zakelijk samenwerkingsverband",
    intro="Een zorgaanbieder die met onderaannemers werkt, wordt bij de Bibob-toets mede beoordeeld op die onderaannemers. De wet noemt dit het zakelijk samenwerkingsverband. Voor hoofdaannemers in de Wmo en jeugdhulp, waar onderaanneming de norm is, is dit het onderdeel van de toets waarop zij het minste grip hebben en het meeste risico lopen.",
    marge=marge([
        ("Grondslag", "Art. 3 lid 4 onder c Wet Bibob: in een zakelijk samenwerkingsverband staan tot de betrokkene"),
        ("Wie", ["onderaannemers", "structurele zzp'ers", "bemiddelingsbureaus", "administratiekantoren met bevoegdheden", "verhuurders van zorglocaties", "franchisegever of -nemer"]),
        ("Contract", "VNG-standaard: hoofdaannemer meldt onderaannemers; gemeente kan vervanging eisen"),
        ("Regel", "Medewerkings- en beëindigingsbepaling in elke onderaannemingsovereenkomst"),
    ]),
    body='''
<h2>Wat een zakelijk samenwerkingsverband is</h2>
<p>De wet rekent tot de betrokkene ook degene die "in een zakelijk samenwerkingsverband" tot hem staat (art. 3 lid 4 onder c). De term is bewust ruim en wordt in de rechtspraak ingevuld als een zakelijke relatie die gericht is op samenwerking en een zeker duurzaam en structureel karakter heeft. Een eenmalige inhuur valt erbuiten; een onderaannemer die een deel van uw cliënten begeleidt, een zzp'er die wekelijks voor u werkt, een bemiddelingsbureau dat uw cliënten aanlevert of een verhuurder die ook meedeelt in de omzet, vallen erbinnen. Ook een franchiserelatie en een structurele samenwerking met een andere zorgaanbieder tellen.</p>
<p>Het gevolg is dat antecedenten van de samenwerkingspartner aan u worden toegerekend bij de gevaarsbeoordeling. De gemeente hoeft niet aan te tonen dat u van die antecedenten wist. Wel weegt mee hoe nauw de relatie is en of u er iets aan kon doen.</p>

<h2>Wat de gemeente van de hoofdaannemer verwacht</h2>
<p>De VNG-contractstandaarden en de meeste inkoopdocumenten verplichten de hoofdaannemer om onderaannemers vooraf te melden en soms om goedkeuring te vragen. Bij een Bibob-toets kan de gemeente eisen dat de onderaannemer eveneens een vragenformulier invult, en zij kan de hoofdaannemer opdragen een onderaannemer te vervangen die de toets niet doorstaat. Komt de hoofdaannemer die opdracht niet na, dan is dat een tekortkoming in het contract en tegelijk een Bibob-signaal: wie vasthoudt aan een partner met antecedenten, maakt die antecedenten tot de zijne.</p>

<h2>Wat u contractueel moet regelen</h2>
<p>Elke onderaannemingsovereenkomst en elke structurele overeenkomst met een zzp'er of bureau hoort vier bepalingen te bevatten:</p>
<ul>
<li><strong>Informatie:</strong> de onderaannemer verstrekt op eerste verzoek de gegevens en stukken die de gemeente in het kader van de Wet Bibob verlangt, en meldt wijzigingen in zijn bestuur, eigendom en financiering.</li>
<li><strong>Medewerking:</strong> de onderaannemer werkt mee aan een Bibob-onderzoek van de gemeente en vult desgevraagd zelf een vragenformulier in.</li>
<li><strong>Verklaring:</strong> de onderaannemer verklaart dat tegen hem, zijn bestuurders en financiers geen omstandigheden bekend zijn die tot een gevaarsconclusie kunnen leiden, en meldt het als dat verandert.</li>
<li><strong>Beëindiging:</strong> u kunt de overeenkomst met onmiddellijke ingang beëindigen als de gemeente dat op grond van de Wet Bibob verlangt of als de onderaannemer de bovenstaande verplichtingen schendt, zonder schadeplichtigheid.</li>
</ul>
<p>Zonder de laatste bepaling komt u klem te zitten tussen een gemeente die vervanging eist en een onderaannemer die zich op het contract beroept.</p>

<h2>Wat u zelf kunt controleren</h2>
<p>U bent niet verplicht uw onderaannemers te screenen, maar u draagt het risico. Een minimale eigen controle bij aanvang en jaarlijks: uittreksel handelsregister en UBO-registratie, VOG van de zorgverleners (vaak toch al verplicht), een eigen verklaring als hierboven, en een korte internetcontrole op toezichtsrapporten en nieuws. Leg vast dat u dit hebt gedaan; het toont de gemeente dat u uw verantwoordelijkheid als hoofdaannemer serieus neemt en het weegt mee bij de evenredigheidstoets.</p>

<h2>Als onderaannemer</h2>
<p>Bent u zelf onderaannemer, dan kunt u via de hoofdaannemer in een Bibob-onderzoek worden betrokken zonder zelf partij te zijn. U hebt dan geen eigen zienswijzerecht jegens de gemeente; uw positie loopt via de hoofdaannemer. Zorg dat uw eigen dossier op orde is en dat uw overeenkomst met de hoofdaannemer regelt wat er gebeurt als de gemeente vervanging eist, inclusief de overdracht van cliënten.</p>
<p>Verder: <a href="bibob-aanbesteding-zorg.html">Bibob bij aanbesteding en open house</a> en <a href="bibob-proof-zorgonderneming.html">Bibob-proof ondernemen</a>.</p>
''',
    faq=[
        ("Telt een zzp'er die drie dagen per week voor mij werkt als samenwerkingsverband?", "Waarschijnlijk wel: de relatie is structureel en gericht op samenwerking. Zorg voor een overeenkomst met de vier bepalingen en een VOG."),
        ("Moet ik mijn verhuurder opgeven?", "Als het formulier naar zakelijke relaties vraagt, ja. Een verhuurder die alleen huur ontvangt weegt licht; een verhuurder die meedeelt in de omzet of ook financier is, weegt zwaar."),
        ("De gemeente eist dat ik een onderaannemer vervang. Moet ik dat doen?", "Als het contract dat bepaalt, ja, binnen de gestelde termijn. Weigeren is een tekortkoming en een Bibob-signaal. U kunt wel om de motivering vragen en de onderaannemer gelegenheid geven zelf te reageren."),
        ("Kan ik aansprakelijk zijn jegens mijn onderaannemer als ik moet beëindigen?", "Alleen als uw overeenkomst daarin niet voorziet. Met een Bibob-beëindigingsbepaling zonder schadeplichtigheid niet."),
    ],
    **CONTACT_STD)

add("zorgaanbieder-worden-toetsen.html", "Zorgaanbieder worden: welke toetsen u tegenkomt", "Van meldplicht tot Bibob: het overzicht voor starters.", "situaties",
    title="Zorgaanbieder worden: de toetsen en eisen van meldplicht tot Bibob",
    desc="Overzicht voor startende zorgaanbieders van alle toetsen en eisen: Wtza-meldplicht en -vergunning, VOG en vergewisplicht, Wkkgz, Wmo- en Jeugdwetinkoop, pgb-eisen, UBO-registratie en de Bibob-toets. Wat u in welke volgorde regelt.",
    h1="Zorgaanbieder worden: welke toetsen u tegenkomt en in welke volgorde",
    intro="Wie een zorgonderneming start, krijgt te maken met een reeks toetsen van verschillende instanties. Zij overlappen deels en verwijzen naar elkaar: wat u voor de een vastlegt, hebt u voor de ander nodig. Dit overzicht zet ze in de volgorde waarin u ze tegenkomt, met de Bibob-toets als sluitstuk dat alles bij elkaar brengt.",
    marge=marge([
        ("Toetreding", "Wtza: meldplicht (art. 2) en vergunningplicht (art. 4) voor Zvw/Wlz-zorg"),
        ("Personeel", "VOG en vergewisplicht (art. 4 Wkkgz; art. 4.1.6 Jeugdwet)"),
        ("Kwaliteit", "Wkkgz, Jeugdwet hoofdstuk 4, gemeentelijke kwaliteitseisen"),
        ("Contract", "Inkoop Wmo/Jeugdwet, pgb-eisen verordening"),
        ("Integriteit", "UBO-registratie, Bibob-toets (art. 1 lid 4 Wet Bibob), Wibz (in voorbereiding)"),
    ]),
    body='''
<h2>1. Rechtsvorm en registraties</h2>
<p>Kies een rechtsvorm en schrijf in bij de Kamer van Koophandel, inclusief de UBO-registratie. Dit is het moment waarop uw Bibob-dossier begint: leg vast wie de aandeelhouders zijn, waar het startkapitaal vandaan komt en wie welke rol heeft. Een stichting met raad van toezicht is in de zorg gebruikelijk en wordt door gemeenten als vertrouwenwekkend gezien; een bv is prima, mits de structuur eenvoudig en gedocumenteerd is. Vermijd constructies met certificaten of buitenlandse vennootschappen zonder goede reden: elke laag is een extra onderzoek.</p>

<h2>2. Wtza: melden of vergunning</h2>
<p>Elke nieuwe zorgaanbieder die zorg levert als bedoeld in de Wkkgz, dus ook Wmo- en jeugdhulpaanbieders, meldt zich vóór aanvang bij het CIBG (art. 2 Wtza). Aanbieders van Zvw- of Wlz-zorg met meer dan tien zorgverleners, en aanbieders van medisch-specialistische zorg, hebben daarnaast een Wtza-vergunning nodig (art. 4 Wtza). De vergunning kan worden geweigerd na een Bibob-onderzoek (art. 5 Wtza; Beleidsregels Wet Bibob Wtza). Wmo- en jeugdhulpaanbieders hebben geen vergunning nodig; zij komen de Bibob-toets tegen bij de gemeente.</p>

<h2>3. Personeel: VOG en vergewisplicht</h2>
<p>De Wkkgz verplicht u na te gaan of een nieuwe zorgverlener geschikt is (vergewisplicht, art. 4 lid 1 onder a Wkkgz) en voor bepaalde zorg een VOG te vragen (art. 4 lid 1 onder b). De Jeugdwet eist een VOG van alle medewerkers die met jeugdigen werken (art. 4.1.6 Jeugdwet). Gemeenten nemen deze eisen over in hun inkoop en pgb-verordening. Leg de VOG's en uw vergewisonderzoek vast; bij een Bibob-toets laat dit zien dat u uw personeel kent.</p>

<h2>4. Kwaliteit en klachten</h2>
<p>Een kwaliteitssysteem, een klachtenregeling en een geschilleninstantie (Wkkgz), een meldcode huiselijk geweld, en voor jeugdhulp de eisen van hoofdstuk 4 Jeugdwet. Gemeenten stellen daarnaast eigen eisen, zoals een keurmerk of ISO-certificering, en vragen in de inkoop naar toezichtsrapporten. Dit staat los van de Bibob-toets, maar toezichtsbevindingen zijn signalen die een Bibob-onderzoek kunnen uitlokken.</p>

<h2>5. Contract of pgb</h2>
<p>Wilt u zorg in natura leveren, dan schrijft u in op de inkoop van de gemeente of regio. Daar komt de <a href="bibob-aanbesteding-zorg.html">Bibob-toets</a>: bij inschrijving of op signaal, afhankelijk van de regio. Wilt u via pgb's werken, dan gelden de eisen van de gemeentelijke verordening en het pgb-plan; de Bibob-toets komt dan niet rechtstreeks, maar <a href="bibob-pgb-zorgaanbieder.html">wel indirect</a>. Veel starters beginnen met pgb en groeien naar een contract; wat u in de pgb-fase vastlegt, bepaalt hoe de toets later verloopt.</p>

<h2>6. De Bibob-toets als sluitstuk</h2>
<p>De Bibob-toets vraagt niets dat u niet al voor de stappen 1 tot en met 5 nodig had, maar zij vraagt het allemaal tegelijk en legt het naast elkaar. Een starter die vanaf dag één een <a href="bibob-proof-zorgonderneming.html">Bibob-dossier</a> bijhoudt, is bij de eerste inkoopronde in een dag klaar. Een starter die het laat liggen, reconstrueert onder tijdsdruk en met het risico op tegenstrijdigheden. De investering is klein; het verschil bij de toets is groot.</p>

<h2>7. Wat eraan komt: de Wibz</h2>
<p>De Wet integere bedrijfsvoering zorg- en jeugdhulpaanbieders (wetsvoorstel 36 686) voegt eisen toe over winstuitkering, tegenstrijdige belangen en de integriteit van bestuurders, met toezicht door de NZa. Het voorstel is in 2026 aangepast en nog niet in werking. Lees <a href="wibz-zorgaanbieders.html">wat de Wibz voor kleine aanbieders betekent</a>.</p>
''',
    faq=[
        ("Moet ik mij als pgb-aanbieder melden bij het CIBG?", "Ja, als u zorg levert in de zin van de Wkkgz of jeugdhulp. De meldplicht geldt ongeacht de financieringsvorm."),
        ("Heb ik als Wmo-aanbieder een Wtza-vergunning nodig?", "Nee. De vergunningplicht geldt voor Zvw- en Wlz-zorg met meer dan tien zorgverleners en voor medisch-specialistische zorg. Wmo- en jeugdhulpaanbieders hebben alleen de meldplicht."),
        ("Kan ik als starter al een Bibob-toets krijgen?", "Bij de eerste inschrijving op een gemeentelijke inkoop, ja. Juist bij starters kijkt de gemeente naar de herkomst van het startkapitaal en de achtergrond van de oprichters."),
        ("Wat is de eerste stap als ik vandaag begin?", "Leg vast waar het startkapitaal vandaan komt, met bankafschriften en overeenkomsten. Dat is het stuk dat later het moeilijkst te reconstrueren is."),
    ],
    **CONTACT_STD)

# =====================================================================
# C. AANPALENDE WETGEVING
# =====================================================================

add("wtza-bibob.html", "Wtza-vergunning en Bibob", "Hoe het CIBG de Bibob-toets inzet bij de Wtza-vergunning en wie daarmee te maken krijgt.", "wetgeving",
    title="Wtza-vergunning en de Wet Bibob: toetsing door het CIBG",
    desc="Wanneer een zorgaanbieder een Wtza-vergunning nodig heeft, hoe het CIBG de Wet Bibob kan toepassen bij verlening en intrekking (art. 5 Wtza, Beleidsregels Wet Bibob Wtza), het verschil met de meldplicht en de samenhang met gemeentelijke Bibob-toetsen.",
    h1="Wtza-vergunning en de Wet Bibob",
    intro="De Wet toetreding zorgaanbieders regelt dat nieuwe zorgaanbieders zich melden en dat grotere aanbieders van Zvw- en Wlz-zorg een vergunning nodig hebben. Bij die vergunning kan de minister, via het CIBG, de Wet Bibob toepassen. Het is de tweede plek, naast de gemeente, waar zorgaanbieders de Bibob-toets tegenkomen, en de twee werken op elkaar in.",
    marge=marge([
        ("Meldplicht", "Art. 2 Wtza: alle nieuwe zorgaanbieders, ook Wmo en jeugdhulp"),
        ("Vergunningplicht", "Art. 4 Wtza: medisch-specialistische zorg; Zvw/Wlz-zorg met meer dan tien zorgverleners"),
        ("Bibob", "Art. 5 Wtza; Beleidsregels Wet Bibob Wtza (Stcrt. 2022, 202); uitvoering CIBG"),
        ("Rechtsbescherming", "Bestuursrecht: bezwaar bij de minister, beroep rechtbank, hoger beroep CBb"),
    ]),
    body='''
<h2>Meldplicht en vergunningplicht</h2>
<p>De Wtza (in werking sinds 1 januari 2022) kent twee instrumenten. De meldplicht (art. 2) geldt voor elke nieuwe zorgaanbieder die zorg levert als bedoeld in de Wkkgz of jeugdhulp, dus ook voor Wmo- en jeugdhulpaanbieders, ongeacht omvang of financiering. Zij dient om de IGJ zicht te geven op nieuwe aanbieders en is geen toets. De vergunningplicht (art. 4) geldt voor aanbieders van medisch-specialistische zorg en voor aanbieders van Zvw- of Wlz-zorg met meer dan tien zorgverleners. De vergunning stelt eisen aan de bestuursstructuur, waaronder een onafhankelijke interne toezichthouder, en aan de kwaliteit van zorg. Wmo- en jeugdhulpaanbieders hebben geen vergunning nodig.</p>

<h2>De Bibob-toets bij de vergunning</h2>
<p>Art. 5 Wtza geeft de minister de bevoegdheid de vergunning te weigeren of in te trekken op grond van de Wet Bibob. De Beleidsregels Wet Bibob Wtza (Stcrt. 2022, 202) beschrijven wanneer het CIBG een Bibob-onderzoek start: in elk geval bij signalen, bijvoorbeeld van de IGJ, de NZa, zorgverzekeraars of het IKZ, en risicogestuurd. Het CIBG doet dan eigen onderzoek (art. 7a Wet Bibob) en kan het Landelijk Bureau Bibob om advies vragen. De procedure, de termijnen en de rechten van de aanvrager zijn dezelfde als bij een gemeentelijke toets: vragenformulier, eventueel advies, voornemen, zienswijze (art. 33 Wet Bibob).</p>
<p>Anders dan bij een zorgcontract is de Wtza-vergunning een beschikking. Tegen weigering of intrekking staat bezwaar open bij de minister (zes weken, art. 6:7 Awb), daarna beroep bij de rechtbank en hoger beroep bij het College van Beroep voor het bedrijfsleven.</p>

<h2>De samenhang met gemeentelijke toetsen</h2>
<p>Het CIBG en de gemeenten raadplegen hetzelfde Bibob-register. Een gevaarsconclusie bij een gemeentelijke inkoop kan dus leiden tot een Bibob-onderzoek bij een latere Wtza-vergunningaanvraag en omgekeerd. Voor aanbieders die zowel Wmo- of jeugdhulp als Zvw- of Wlz-zorg leveren, in een of meer vennootschappen met dezelfde bestuurders, betekent dit dat een probleem in het ene domein doorwerkt in het andere. Een gezamenlijk Bibob-dossier voor de hele groep is dan geen luxe.</p>

<h2>Intrekking van een bestaande vergunning</h2>
<p>Ook een verleende vergunning kan na een Bibob-onderzoek worden ingetrokken. Dat is ingrijpend: zonder vergunning mag de zorg niet worden geleverd en vervallen contracten met zorgverzekeraars en zorgkantoren. Het CIBG moet de evenredigheid wegen (art. 3 lid 5 Wet Bibob) en kan bij een mindere mate van gevaar voorschriften verbinden aan de vergunning in plaats van haar in te trekken. Bij een voornemen tot intrekking is naast de zienswijze een voorlopige voorziening bij de rechtbank het aangewezen middel om de zorg te kunnen voortzetten hangende bezwaar.</p>

<h2>Wat u doet bij een vergunningaanvraag</h2>
<ul>
<li>Lever het Bibob-dossier mee, ook als er niet om wordt gevraagd: structuur, financiering, bestuurders, toezichthouders. Het versnelt de behandeling en toont transparantie.</li>
<li>Zorg dat de interne toezichthouder voldoet aan de onafhankelijkheidseisen van het Uitvoeringsbesluit Wtza; een toezichthouder met een zakelijke band met het bestuur is zowel een Wtza- als een Bibob-probleem.</li>
<li>Controleer of bestuurders of financiers in een eerder gemeentelijk Bibob-onderzoek zijn betrokken en bereid daarover een toelichting voor.</li>
</ul>
<p>Zie ook <a href="zorgaanbieder-worden-toetsen.html">Zorgaanbieder worden: welke toetsen u tegenkomt</a>.</p>
''',
    faq=[
        ("Ik heb alleen een meldplicht. Kan het CIBG mij toch Bibob-toetsen?", "Nee. De Bibob-bevoegdheid in de Wtza is gekoppeld aan de vergunning. Zonder vergunningplicht komt u de toets alleen bij de gemeente tegen."),
        ("Tellen zzp'ers mee voor de grens van tien zorgverleners?", "Ja. Het gaat om het aantal zorgverleners dat zorg verleent, ongeacht de arbeidsrelatie."),
        ("Hoe lang duurt een Wtza-vergunningaanvraag met Bibob-onderzoek?", "De reguliere beslistermijn is acht weken; een Bibob-onderzoek schort die op. Met LBB-advies kan het totaal oplopen tot een half jaar."),
        ("Kan ik zorg leveren terwijl de vergunningaanvraag loopt?", "Niet als de vergunningplicht al geldt. Bij een uitbreiding boven tien zorgverleners moet de vergunning er zijn vóórdat u de elfde zorgverlener inzet."),
    ],
    **CONTACT_STD)

add("wibz-zorgaanbieders.html", "Wibz: wat verandert er voor kleine aanbieders", "Winstuitkering, tegenstrijdige belangen en NZa-toezicht in het wetsvoorstel integere bedrijfsvoering.", "wetgeving",
    title="Wibz: Wet integere bedrijfsvoering zorg- en jeugdhulpaanbieders uitgelegd",
    desc="Wat het wetsvoorstel Wibz (36 686) regelt voor zorg- en jeugdhulpaanbieders: voorwaarden aan winstuitkering, tegenstrijdige belangen, weigeren of intrekken van de Wtza-vergunning wegens integriteit, NZa-toezicht; de koerswijziging van juli 2026 en de samenhang met de Wet Bibob.",
    h1="De Wibz: wat de Wet integere bedrijfsvoering voor zorgaanbieders betekent",
    intro="De Wet integere bedrijfsvoering zorg- en jeugdhulpaanbieders (Wibz) is het tweede grote integriteitsinstrument dat op zorgaanbieders afkomt, naast de Wet Bibob. Waar Bibob kijkt naar het netwerk achter de aanbieder, kijkt de Wibz naar de bedrijfsvoering zelf: hoe geld de onderneming verlaat, wie daarvan profiteert en of bestuurders en toezichthouders hun rol integer vervullen.",
    marge=marge([
        ("Wetsvoorstel", "Kamerstukken II 36 686, ingediend 29 januari 2025"),
        ("Koerswijziging", "Nota van wijziging aangekondigd 3 juli 2026: wettelijk maximumpercentage winstuitkering met voorwaarden in plaats van verbod"),
        ("Toezicht", "NZa (integere bedrijfsvoering), IGJ (kwaliteit), CIBG (vergunning)"),
        ("Status", "In behandeling; nog niet in werking. Volg de actuele stand."),
    ]),
    body='''
<h2>Waarom de Wibz er komt</h2>
<p>De Wtza regelde in 2022 de toetreding van zorgaanbieders, maar liet een lacune: eenmaal toegetreden, kon een aanbieder zijn winst vrijwel ongehinderd uitkeren en kon de overheid weinig doen tegen bestuurders die zichzelf of gelieerde partijen bevoordeelden, zolang de zorg niet aantoonbaar ondermaats was. De zorgfraudezaken en de discussie over excessieve winsten in de wijkverpleging, ggz en jeugdzorg leidden tot het voorstel voor de Wibz, dat de bedrijfsvoering zelf normeert en de NZa daarop laat toezien.</p>

<h2>Wat het voorstel regelt</h2>
<dl class="lijst">
<div class="item"><dt><h3>Winstuitkering<em>Van verbod naar voorwaarden</em></h3></dt><dd><p>Het oorspronkelijke voorstel verbood winstuitkering voor bepaalde sectoren. De nota van wijziging van juli 2026 kiest een andere route: een wettelijk maximumpercentage dat mag worden uitgekeerd, gekoppeld aan voorwaarden over financiële gezondheid, kwaliteit en het ontbreken van toezichtsmaatregelen. Hoe het percentage wordt vastgesteld en voor welke sectoren het geldt, wordt bij algemene maatregel van bestuur uitgewerkt.</p></dd></div>
<div class="item"><dt><h3>Tegenstrijdige belangen<em>Vastgoed, inkoop, gelieerde partijen</em></h3></dt><dd><p>Transacties met bestuurders, aandeelhouders of hun verwanten, zoals huur van vastgoed, inkoop van diensten of leningen, moeten marktconform zijn, worden gemeld en door de interne toezichthouder zijn goedgekeurd. Dit raakt direct de constructies die ook bij een Bibob-toets opvallen.</p></dd></div>
<div class="item"><dt><h3>Vergunning en integriteit<em>Aanvulling op de Wtza</em></h3></dt><dd><p>De Wtza-vergunning kan worden geweigerd of ingetrokken als de bedrijfsvoering niet integer is of bestuurders en toezichthouders niet aan integriteitseisen voldoen. Dit is een eigen grond, naast de Bibob-grond die al in art. 5 Wtza staat.</p></dd></div>
<div class="item"><dt><h3>NZa-toezicht<em>Normen en handhaving</em></h3></dt><dd><p>De NZa krijgt de bevoegdheid de integere bedrijfsvoering te toetsen, aanwijzingen te geven en boetes op te leggen. Zij kan daarbij informatie delen met het CIBG, de IGJ en, via de Wbsrz, met gemeenten en zorgverzekeraars.</p></dd></div>
</dl>

<h2>Wat dit betekent voor kleine aanbieders</h2>
<p>Het debat over de Wibz gaat vaak over grote concerns, maar de normen gelden voor elke zorg- en jeugdhulpaanbieder die onder de reikwijdte valt. Voor een kleine bv met één dga zijn drie punten van belang. Ten eerste de winstuitkering: een dga die zijn inkomen vooral als dividend ontvangt, moet dat straks toetsen aan het maximumpercentage en de voorwaarden. Ten tweede de gelieerde transacties: de bv die kantoor houdt in het pand van de dga, of diensten inkoopt bij de bv van zijn partner, moet dat marktconform en gedocumenteerd doen. Ten derde de samenloop met Bibob: dezelfde informatie over financiering, eigendom en gelieerde partijen die de NZa gaat vragen, vraagt de gemeente nu al in het Bibob-vragenformulier. Wie zijn Bibob-dossier op orde heeft, is voor een groot deel Wibz-klaar.</p>

<h2>Wat u nu al kunt doen</h2>
<ul>
<li>Breng alle transacties met gelieerde partijen in kaart (huur, leningen, inkoop, managementvergoedingen) en toets ze op marktconformiteit. Leg de toets vast.</li>
<li>Bekijk uw dividendbeleid: hoeveel keert u uit, hoe verhoudt zich dat tot omzet en resultaat, en kunt u dat verantwoorden?</li>
<li>Zorg dat een interne toezichthouder, als u die hebt of moet hebben, daadwerkelijk onafhankelijk is en gelieerde transacties goedkeurt.</li>
<li>Volg de behandeling van het wetsvoorstel; de uitwerking bij amvb bepaalt of en hoe het percentage u raakt.</li>
</ul>
<p>Zie ook <a href="wtza-bibob.html">Wtza-vergunning en Bibob</a> en <a href="bibob-financiering-zorgonderneming.html">Financiering en de Bibob-toets</a>.</p>
''',
    faq=[
        ("Geldt de Wibz al?", "Nee. Het wetsvoorstel is in behandeling en is in 2026 aangepast. De inwerkingtreding is nog niet bepaald. Deze pagina wordt bijgewerkt bij nieuwe stappen."),
        ("Geldt de Wibz ook voor Wmo- en jeugdhulpaanbieders?", "Jeugdhulpaanbieders vallen onder het voorstel. Voor Wmo-aanbieders hangt de reikwijdte af van de definitie van zorgaanbieder in de uiteindelijke wet; volg de behandeling."),
        ("Is de Wibz hetzelfde als de Wet Bibob?", "Nee. De Wet Bibob is een algemeen integriteitsinstrument voor de overheid als contractspartij of vergunningverlener; de Wibz normeert de bedrijfsvoering van zorgaanbieders zelf, met de NZa als toezichthouder. Zij overlappen in de informatie die zij vragen."),
        ("Mag ik straks nog winst uitkeren uit mijn zorg-bv?", "Volgens de koers van juli 2026 wel, tot een wettelijk maximumpercentage en onder voorwaarden. De details worden bij algemene maatregel van bestuur vastgesteld."),
    ],
    **CONTACT_STD)

add("vergewisplicht-vog-zorg.html", "Vergewisplicht, VOG en Bibob", "Drie toetsen op personen en hoe zij zich tot elkaar verhouden.", "wetgeving",
    title="Vergewisplicht, VOG en Bibob-toets: drie toetsen op personen in de zorg",
    desc="Het verschil tussen de vergewisplicht (art. 4 Wkkgz), de Verklaring Omtrent het Gedrag (Wkkgz, Jeugdwet) en de Bibob-toets: wie wordt getoetst, door wie, op welke gegevens en hoe de drie toetsen elkaar aanvullen bij zorgaanbieders.",
    h1="Vergewisplicht, VOG en Bibob-toets: drie toetsen op personen",
    intro="Zorgaanbieders kennen de vergewisplicht en de VOG als eisen bij het aannemen van personeel. De Bibob-toets wordt vaak in dezelfde adem genoemd, maar is iets anders: zij toetst niet de zorgverlener maar de onderneming en haar netwerk. Wie de drie uit elkaar houdt, begrijpt waarom een organisatie met uitsluitend VOG-gescreend personeel toch een Bibob-probleem kan hebben.",
    marge=marge([
        ("Vergewisplicht", "Art. 4 lid 1 onder a Wkkgz: nagaan of de zorgverlener geschikt is (arbeidsverleden, BIG, Waarschuwingsregister, referenties)"),
        ("VOG", "Art. 4 lid 1 onder b Wkkgz (Wlz, intramurale ggz); art. 4.1.6 Jeugdwet (alle jeugdhulpmedewerkers); gemeentelijke inkoopeisen Wmo"),
        ("Bibob", "Art. 3 Wet Bibob: de onderneming, bestuurders, financiers en samenwerkingsverband; door het bestuursorgaan"),
    ]),
    body='''
<h2>De vergewisplicht</h2>
<p>De Wkkgz verplicht de zorgaanbieder zich ervan te vergewissen dat de wijze waarop een nieuwe zorgverlener in het verleden heeft gefunctioneerd niet in de weg staat aan het inzetten van die zorgverlener (art. 4 lid 1 onder a Wkkgz). De aanbieder bepaalt zelf hoe: referenties opvragen, het BIG-register en het Waarschuwingsregister Zorg en Welzijn raadplegen, navraag doen bij de IGJ. De plicht rust op de aanbieder, geldt per zorgverlener en wordt door de IGJ gehandhaafd. Zij zegt niets over de aanbieder zelf.</p>

<h2>De VOG</h2>
<p>De Verklaring Omtrent het Gedrag wordt door Justis afgegeven voor één persoon en één functie, op basis van justitiële gegevens die relevant zijn voor die functie. Zij is verplicht voor zorgverleners in de Wlz en de intramurale ggz (art. 4 lid 1 onder b Wkkgz), voor alle medewerkers in de jeugdhulp (art. 4.1.6 Jeugdwet) en, via de inkoop, voor vrijwel alle Wmo-zorgverleners. Ook bestuurders moeten in veel inkoopdocumenten een VOG overleggen. De VOG kijkt alleen naar veroordelingen en sepots binnen een terugkijktermijn, niet naar vermoedens, fiscale informatie of bestuurlijke boetes, en zegt niets over financiers of zakenpartners.</p>

<h2>De Bibob-toets</h2>
<p>De Bibob-toets wordt niet door u maar door het bestuursorgaan uitgevoerd, richt zich op de onderneming als geheel en op iedereen die haar bestuurt, bezit, financiert of ermee samenwerkt (art. 3 lid 4 Wet Bibob), en mag gebruikmaken van justitiële, politiële en fiscale gegevens én van vermoedens. Zij beoordeelt geen geschiktheid voor een functie maar het risico dat een overheidscontract wordt misbruikt. Een bestuurder met een schone VOG kan in een Bibob-onderzoek toch een probleem zijn, bijvoorbeeld door een lopend onderzoek, een fiscale boete of een zakelijke relatie met iemand met antecedenten.</p>

<h2>Hoe de drie samenhangen</h2>
<dl class="lijst">
<div class="item"><dt><h3>Vergewisplicht<em>Door u, over uw zorgverleners</em></h3></dt><dd><p>Beschermt cliënten tegen ongeschikte hulpverleners. Bij een Bibob-toets laat een goed gedocumenteerde vergewisprocedure zien dat u uw organisatie beheerst; een gebrekkige is een kwaliteitssignaal dat een onderzoek kan uitlokken.</p></dd></div>
<div class="item"><dt><h3>VOG<em>Door Justis, over één persoon</em></h3></dt><dd><p>Verplicht voor zorgverleners en vaak voor bestuurders. Een VOG van bestuurders is nuttig in het Bibob-dossier, maar vervangt de toets niet: de Bibob-toets kijkt breder en dieper.</p></dd></div>
<div class="item"><dt><h3>Bibob<em>Door het bestuursorgaan, over het netwerk</em></h3></dt><dd><p>Het sluitstuk. Gebruikt de uitkomsten van de andere twee als signalen en voegt het onderzoek naar financiering en samenwerkingsverband toe.</p></dd></div>
</dl>

<h2>Praktisch</h2>
<ul>
<li>Vraag van alle bestuurders, toezichthouders en aandeelhouders met zeggenschap een VOG bij aantreden en leg die in het Bibob-dossier.</li>
<li>Leg de vergewisprocedure vast in een werkinstructie en bewaar per zorgverlener het bewijs dat zij is gevolgd.</li>
<li>Besef dat beide niets zeggen over financiers en onderaannemers; daarvoor is het <a href="bibob-proof-zorgonderneming.html">eigen Bibob-dossier</a> nodig.</li>
</ul>
''',
    faq=[
        ("Als al mijn medewerkers een VOG hebben, ben ik dan Bibob-proof?", "Nee. De VOG's dekken de zorgverleners. De Bibob-toets kijkt naar bestuurders, aandeelhouders, financiers en samenwerkingspartners, en naar meer dan alleen justitiële gegevens."),
        ("Moet een bestuurder een VOG hebben?", "De Wkkgz en Jeugdwet eisen dat voor zorgverleners; voor bestuurders volgt de eis meestal uit de inkoopdocumenten van de gemeente of uit de Wtza-vergunning. In de praktijk: ja."),
        ("Hoe ver kijkt een VOG terug?", "Standaard vier jaar, voor zedendelicten onbeperkt, voor bepaalde functies langer. De Bibob-toets kent geen vaste terugkijktermijn; tijdsverloop is een wegingsfactor."),
        ("Wat is het Waarschuwingsregister Zorg en Welzijn?", "Een register van werkgevers in de zorg over medewerkers die zijn ontslagen wegens ernstig grensoverschrijdend gedrag. Het is een hulpmiddel bij de vergewisplicht en staat los van het Bibob-register en het Waarschuwingsregister zorgfraude."),
    ],
    **CONTACT_STD)

add("zorgfraude-onderzoek-gemeente.html", "Zorgfraude-onderzoek door de gemeente", "Wmo-toezicht, rechtmatigheidsonderzoek, IKZ en Wbsrz: hoe zij samenhangen met de Bibob-toets.", "wetgeving",
    title="Zorgfraude-onderzoek door de gemeente: toezicht, rechtmatigheid en de weg naar Bibob",
    desc="Hoe gemeenten onderzoek doen naar zorgfraude: de Wmo-toezichthouder (art. 6.1 Wmo 2015), rechtmatigheidsonderzoek, het Informatie Knooppunt Zorgfraude, het Waarschuwingsregister zorgfraude (Wbsrz) en hoe toezichtsbevindingen uitmonden in een Bibob-toets. Uw rechten tijdens een onderzoek.",
    h1="Zorgfraude-onderzoek door de gemeente: van toezicht naar Bibob",
    intro="De Bibob-toets staat zelden op zichzelf. In de meeste gevallen gaat er een signaal aan vooraf: een toezichtsbezoek, een rechtmatigheidsonderzoek, een melding bij het Informatie Knooppunt Zorgfraude of een vermelding in het Waarschuwingsregister. Wie begrijpt hoe deze instrumenten samenhangen, ziet een Bibob-toets aankomen en kan erop reageren voordat hij er is.",
    marge=marge([
        ("Wmo-toezicht", "Art. 6.1 Wmo 2015: toezichthouder aangewezen door het college; vaak GGD"),
        ("Jeugdhulp", "Toezicht door IGJ (hoofdstuk 9 Jeugdwet); rechtmatigheid door gemeente"),
        ("Gegevensdeling", "Wet bevorderen samenwerking en rechtmatige zorg (Wbsrz), in werking 1 januari 2025: Waarschuwingsregister zorgfraude en IKZ"),
        ("Rechten", "Medewerkingsplicht art. 5:20 Awb; cautie bij punitief onderzoek; inzage in rapport; zienswijze"),
    ]),
    body='''
<h2>Vier instrumenten vóór de Bibob-toets</h2>
<dl class="lijst">
<div class="item"><dt><h3>Kwaliteitstoezicht<em>Wmo: gemeentelijke toezichthouder; Jeugdwet: IGJ</em></h3></dt><dd><p>De toezichthouder bezoekt locaties, spreekt cliënten en medewerkers en beoordeelt of de zorg voldoet aan de wet en het contract. Een kritisch rapport leidt tot een verbetertraject, en bij ernstige bevindingen tot een melding aan de inkoopafdeling. In veel gemeenten zijn rapporten openbaar.</p></dd></div>
<div class="item"><dt><h3>Rechtmatigheidsonderzoek<em>Klopt wat is gedeclareerd?</em></h3></dt><dd><p>De gemeente vergelijkt declaraties met geleverde zorg: uren, cliëntdossiers, roosters, kwalificaties van medewerkers. Bevindingen leiden tot terugvordering, opschorting van betalingen en, bij opzet, aangifte. Rotterdam publiceert sinds 2021 de uitkomsten van rechtmatigheidsonderzoeken naar pgb-aanbieders.</p></dd></div>
<div class="item"><dt><h3>Informatie Knooppunt Zorgfraude<em>Signalen bundelen</em></h3></dt><dd><p>Het IKZ verzamelt signalen van gemeenten, zorgverzekeraars, zorgkantoren, IGJ, NZa, Belastingdienst en opsporingsdiensten en koppelt ze aan elkaar. Een aanbieder die in meerdere gemeenten opvalt, wordt via het IKZ zichtbaar voor allemaal.</p></dd></div>
<div class="item"><dt><h3>Waarschuwingsregister zorgfraude<em>Wbsrz, sinds 2025</em></h3></dt><dd><p>Gemeenten, zorgverzekeraars en zorgkantoren kunnen een aanbieder registreren bij een gerechtvaardigde overtuiging van fraude, na een zorgvuldige procedure met hoor en wederhoor. Andere deelnemers zien de registratie en kunnen contracten weigeren. Het register staat los van het Bibob-register, maar een registratie is een signaal dat een Bibob-onderzoek uitlokt.</p></dd></div>
</dl>

<h2>Hoe een toezichtsbevinding een Bibob-toets wordt</h2>
<p>Een toezichtsrapport of rechtmatigheidsonderzoek gaat over de zorg en de declaraties. Op het moment dat de bevindingen wijzen op opzet, op het wegsluizen van geld of op personen in de achtergrond, meldt de inkoopafdeling het bij de Bibob-coördinator. Die beoordeelt of er grond is voor een eigen onderzoek (art. 7a Wet Bibob) en stuurt het vragenformulier. De toezichtsbevindingen zijn dan de aanleiding; het Bibob-onderzoek richt zich vervolgens op structuur, financiering en relaties. Een aanbieder die een rechtmatigheidsonderzoek achter de rug heeft, moet daarom rekening houden met een Bibob-vraag in de volgende inkoopronde, ook als het onderzoek met een schikking is afgesloten.</p>

<h2>Uw rechten tijdens een onderzoek</h2>
<ul>
<li><strong>Medewerking:</strong> u bent verplicht mee te werken aan toezicht (art. 5:20 Awb) en inlichtingen en dossiers te verstrekken, binnen de grenzen van het medisch beroepsgeheim en de AVG. Vraag altijd om de grondslag en het doel van het onderzoek.</li>
<li><strong>Cautie:</strong> zodra het onderzoek is gericht op het opleggen van een boete of een strafrechtelijke sanctie, hoeft u geen verklaring af te leggen (art. 5:10a Awb). Laat u informeren over het karakter van het onderzoek.</li>
<li><strong>Inzage en reactie:</strong> u krijgt het conceptrapport en kunt daarop reageren voordat het definitief wordt. Gebruik dat; het rapport volgt u bij een latere Bibob-toets.</li>
<li><strong>Bezwaar:</strong> tegen terugvordering, opschorting en registratie in het Waarschuwingsregister staan bezwaar of civiele procedures open. Laat termijnen niet lopen.</li>
</ul>

<h2>Wat u doet als een onderzoek loopt</h2>
<p>Documenteer alles, reageer schriftelijk en inhoudelijk op het conceptrapport, en begin tegelijk met het <a href="bibob-proof-zorgonderneming.html">Bibob-dossier</a>: structuur, financiering en relaties. Als het onderzoek uitmondt in een Bibob-toets, bent u dan voorbereid. En als het rechtmatigheidsonderzoek fouten aan het licht brengt, herstel ze dan zichtbaar: terugbetalen, procedures aanpassen, een externe controle. Bij de evenredigheidstoets van art. 3 lid 5 Wet Bibob weegt zelfreinigend vermogen mee.</p>
''',
    faq=[
        ("Is een rechtmatigheidsonderzoek hetzelfde als een Bibob-onderzoek?", "Nee. Rechtmatigheid gaat over declaraties en geleverde zorg; Bibob over integriteit van de onderneming en haar netwerk. Het eerste is vaak de aanleiding voor het tweede."),
        ("Mag de gemeente informatie uit een toezichtsonderzoek gebruiken in een Bibob-toets?", "Ja. Toezichtsbevindingen zijn signalen die het eigen onderzoek van art. 7a Wet Bibob kunnen onderbouwen, en de Wbsrz vergemakkelijkt het delen van fraudesignalen tussen instanties."),
        ("Kan ik registratie in het Waarschuwingsregister zorgfraude aanvechten?", "Ja. De Wbsrz schrijft een zorgvuldige procedure voor met kennisgeving en gelegenheid tot reactie, en registratie is een besluit waartegen rechtsmiddelen openstaan."),
        ("Moet ik een lopend onderzoek melden bij een inschrijving in een andere gemeente?", "Als het inschrijvingsformulier of het Bibob-vragenformulier ernaar vraagt, ja. Verzwijgen weegt zwaarder dan het onderzoek zelf."),
    ],
    **CONTACT_STD)

# =====================================================================
# D. REGIO'S
# =====================================================================

def regio(slug, naam, kop, intro_txt, kenmerken, body_txt):
    add(slug, f"Bibob-toets {naam}", kop, "regio",
        title=f"Bibob-toets {naam}: zorgaanbieders en gemeentelijke inkoop",
        desc=f"Hoe de gemeente {naam} de Wet Bibob toepast bij zorgaanbieders: inkoop Wmo en Jeugdwet, pgb-aanbieders en maatwerk, beleidsregel en praktijk. Wat zorgaanbieders in {naam} kunnen verwachten en hoe zij zich voorbereiden.",
        h1=f"Bibob-toets in {naam}: wat zorgaanbieders kunnen verwachten",
        intro=intro_txt,
        marge=marge(kenmerken),
        body=body_txt + f'''
<h2>Voorbereiden op de toets in {naam}</h2>
<p>De toets zelf verschilt niet per gemeente; de wet en het vragenformulier zijn landelijk. Wat verschilt is wanneer de gemeente toetst en hoe streng de contractbepaling is. Raadpleeg de actuele beleidsregel Wet Bibob van de gemeente (te vinden via overheid.nl, lokale wet- en regelgeving) en de Bibob-bepaling in de meest recente inkoopdocumenten. Breng daarna uw <a href="bibob-proof-zorgonderneming.html">Bibob-dossier</a> op orde: structuur, financiering, bestuurders en samenwerkingspartners.</p>
<p>Algemene uitleg: <a href="bibob-toets.html">De Bibob-toets</a>, <a href="bibob-onderzoek.html">Het Bibob-onderzoek</a> en <a href="bibob-vragenformulier.html">Het vragenformulier</a>.</p>
''',
        faq=[
            (f"Toetst {naam} alle zorgaanbieders bij inkoop?", f"Dat hangt af van de actuele beleidsregel en de inkoopdocumenten. Controleer de Bibob-bepaling in de laatste inkoopronde; daarin staat of alle inschrijvers, een steekproef of alleen aanbieders met signalen worden getoetst."),
            (f"Waar vind ik de beleidsregel Bibob van {naam}?", "Via overheid.nl onder lokale wet- en regelgeving, met als zoekterm \"Bibob\" en de gemeentenaam, of via de gemeentelijke website onder ondernemen of vergunningen."),
            ("Geldt een Bibob-uitkomst uit een andere gemeente ook hier?", "Een conclusie van ernstig gevaar of mindere mate van gevaar staat in het landelijke Bibob-register en wordt door elke gemeente gezien. Zij moet wel zelfstandig beoordelen of de situatie is veranderd."),
        ],
        **CONTACT_STD)

regio("bibob-rotterdam-zorg.html", "Rotterdam", "De gemeente met de meeste Bibob-aanvragen en een actief pgb-toezicht.",
    "Rotterdam is landelijk de gemeente die de Wet Bibob het meest inzet en heeft die ervaring vanaf 2022 ook naar het zorgdomein gebracht. Daarnaast is Rotterdam de gemeente die het verst gaat in het doorlichten van pgb-aanbieders, met openbaarmaking van rechtmatigheidsonderzoeken. Voor zorgaanbieders in de regio Rijnmond is de kans op een toets daarmee groter dan gemiddeld.",
    [("Bibob-praktijk", "Grootste aanvrager van LBB-adviezen; eigen Bibob-bureau binnen de gemeente"),
     ("Zorgdomein", "Bibob-bepaling in inkoop Wmo en jeugdhulp (regio Rijnmond); toetsing op signaal en risicogestuurd"),
     ("Pgb", "Doorlichten van pgb-aanbieders; openbaarmaking rechtmatigheidsonderzoeken sinds 2021"),
     ("Samenwerking", "RIEC Rotterdam; Informatie Knooppunt Zorgfraude")],
    '''
<h2>De Rotterdamse aanpak</h2>
<p>Rotterdam beschikt over een eigen Bibob-bureau met jarenlange ervaring in horeca, vastgoed en bouw, en heeft die infrastructuur na de wetswijziging van 2022 beschikbaar gemaakt voor de inkoop van zorg. De gemeente kiest voor risicogestuurde toetsing: niet elke inschrijver, maar aanbieders die op grond van signalen, toezichtsbevindingen of risico-indicatoren opvallen. Omdat Rotterdam tegelijk een intensief Wmo-toezicht en rechtmatigheidsbeleid voert, zijn er veel signalen en is de drempel naar een Bibob-onderzoek laag.</p>
<h2>Pgb-aanbieders in Rotterdam</h2>
<p>Rotterdam heeft sinds 2021 tientallen rechtmatigheidsonderzoeken naar pgb-aanbieders uitgevoerd en publiceert de uitkomsten. Een pgb-aanbieder die negatief uit zo'n onderzoek komt, ziet dat terug in de beoordeling van pgb-aanvragen van zijn cliënten en, bij een latere inschrijving op de inkoop, in een Bibob-toets. Zie <a href="bibob-pgb-zorgaanbieder.html">pgb-aanbieders en de Bibob-toets</a> en <a href="zorgfraude-onderzoek-gemeente.html">zorgfraude-onderzoek door de gemeente</a>.</p>
<h2>Regio Rijnmond</h2>
<p>De jeugdhulp wordt ingekocht via de Gemeenschappelijke Regeling Jeugdhulp Rijnmond, met Rotterdam als grootste deelnemer; de Bibob-bepaling in die inkoop geldt voor alle deelnemende gemeenten. Aanbieders die in meerdere Rijnmondgemeenten werken, hebben dus met één Bibob-regime te maken voor jeugdhulp en met de afzonderlijke gemeenten voor Wmo.</p>
''')

regio("bibob-amsterdam-zorg.html", "Amsterdam", "Groot inkoopvolume, eigen Bibob-beleid en toenemende aandacht voor zorgfraude.",
    "Amsterdam heeft een van de grootste inkoopvolumes voor Wmo en jeugdhulp van Nederland en een lange Bibob-traditie in horeca en vastgoed. De gemeente heeft de wet na 2022 opgenomen in haar beleidsregel en inkoopdocumenten voor het sociaal domein, en voert daarnaast een actief toezichts- en handhavingsbeleid tegen zorgfraude. Zorgaanbieders die in Amsterdam inschrijven, moeten op een Bibob-bepaling rekenen.",
    [("Bibob-praktijk", "Eigen Bibob-team (Bureau Integriteit / Bibob); beleidsregel Bibob gemeente Amsterdam"),
     ("Zorgdomein", "Bibob-bepaling in inkoop Wmo en jeugdhulp; toetsing risicogestuurd en op signaal"),
     ("Toezicht", "Afdeling Toezicht en Handhaving zorg; samenwerking met GGD, zorgverzekeraars en IKZ"),
     ("Samenwerking", "RIEC Amsterdam-Amstelland")],
    '''
<h2>De Amsterdamse aanpak</h2>
<p>Amsterdam past de Wet Bibob toe via een centraal team dat voor alle vergunningen, subsidies en opdrachten van de gemeente werkt. Voor het sociaal domein is de Bibob-bevoegdheid opgenomen in de inkoopdocumenten en de raamovereenkomsten voor Wmo-ondersteuning en jeugdhulp. De gemeente kiest voor een risicogestuurde inzet, met bijzondere aandacht voor aanbieders van beschermd wonen, begeleiding en dagbesteding en voor aanbieders die snel groeien of in korte tijd veel cliënten uit één doelgroep bedienen.</p>
<h2>Toezicht en signalen</h2>
<p>Amsterdam heeft een eigen afdeling voor toezicht en handhaving in de zorg, die kwaliteits- en rechtmatigheidsonderzoeken uitvoert en nauw samenwerkt met zorgverzekeraars en het Informatie Knooppunt Zorgfraude. Bevindingen uit die onderzoeken zijn de belangrijkste aanleiding voor Bibob-onderzoeken in de zorg. Een aanbieder die een toezichtstraject heeft doorlopen, doet er goed aan bij de volgende inkoop het Bibob-dossier gereed te hebben.</p>
<h2>Grootstedelijke bijzonderheden</h2>
<p>In Amsterdam speelt vastgoed een grote rol: aanbieders van beschermd en begeleid wonen huren of bezitten panden, en de verhuurder of de eigenaar van het pand komt daardoor in beeld als zakelijke relatie of financier. Leg huurovereenkomsten en de relatie met de verhuurder zorgvuldig vast; zie <a href="bibob-onderaannemer-zorg.html">het zakelijk samenwerkingsverband</a>.</p>
''')

regio("bibob-utrecht-zorg.html", "Utrecht", "Regionale inkoop met Bibob-bepaling en een actieve toezichthouder.",
    "Utrecht koopt Wmo-ondersteuning en jeugdhulp deels stedelijk en deels regionaal in, en heeft de Wet Bibob na 2022 in haar beleid en inkoopdocumenten voor het sociaal domein opgenomen. De gemeente en de regio hechten aan een beperkt aantal aanbieders met langdurige contracten, wat de toets bij toetreding zwaarder maakt dan in open-houseregio's met honderden aanbieders.",
    [("Bibob-praktijk", "Beleidsregel Wet Bibob gemeente Utrecht; toetsing bij vergunningen, subsidies en opdrachten"),
     ("Zorgdomein", "Bibob-bepaling in inkoop Wmo (stedelijk) en jeugdhulp (regio Utrecht Stad / Lekstroom / Zuidoost); selectieve inkoop met weinig aanbieders"),
     ("Toezicht", "Wmo-toezicht via GGD regio Utrecht; rechtmatigheid door gemeente"),
     ("Samenwerking", "RIEC Midden-Nederland")],
    '''
<h2>De Utrechtse aanpak</h2>
<p>Utrecht heeft, anders dan veel gemeenten, gekozen voor selectieve inkoop met een beperkt aantal aanbieders per zorgvorm en langlopende contracten. Dat betekent dat toetreding een echte aanbesteding is en dat de Bibob-toets deel uitmaakt van een selectie waarin ook kwaliteit, prijs en samenwerking worden gewogen. Voor de aanbieders die een contract krijgen, is de toets vooral relevant tijdens de looptijd: bij signalen, bij wijzigingen in bestuur of eigendom en bij de toetreding van onderaannemers.</p>
<h2>Onderaanneming in een selectief stelsel</h2>
<p>Omdat weinig aanbieders rechtstreeks zijn gecontracteerd, werken veel kleinere aanbieders in Utrecht als onderaannemer van een hoofdaannemer. De hoofdaannemer is verantwoordelijk voor het melden van onderaannemers en kan door de gemeente worden aangesproken op hun integriteit. Kleine aanbieders die in Utrecht willen werken, doen er goed aan hun Bibob-dossier op orde te hebben voordat zij zich bij een hoofdaannemer melden; zie <a href="bibob-onderaannemer-zorg.html">onderaannemers en het samenwerkingsverband</a>.</p>
<h2>Regionale inkoop</h2>
<p>Jeugdhulp wordt ingekocht in regionaal verband, met Utrecht als centrumgemeente voor een deel van de regio. De Bibob-bepaling in de regionale inkoopdocumenten geldt dan voor alle deelnemende gemeenten. Controleer per inkoop welke gemeente het Bibob-onderzoek uitvoert en bij wie u uw zienswijze indient.</p>
''')

regio("bibob-den-haag-zorg.html", "Den Haag", "Eigen Bibob-formulieren, een duidelijke zienswijzeprocedure en regionale inkoop via H10.",
    "Den Haag heeft een uitgewerkt Bibob-beleid met eigen vragenformulieren per toepassingsgebied en een beschreven procedure voor de zienswijze. De gemeente koopt jeugdhulp regionaal in via het samenwerkingsverband H10 en Wmo-ondersteuning stedelijk. Voor Haagse zorgaanbieders is het Bibob-proces daardoor relatief voorspelbaar, mits zij het beleid kennen.",
    [("Bibob-praktijk", "Eigen vragenformulieren (vergunningen, subsidies, overheidsopdrachten); zienswijzeprocedure beschreven op denhaag.nl"),
     ("Zorgdomein", "Bibob-bepaling in inkoop Wmo (stedelijk) en jeugdhulp (H10 Inkoopbureau)"),
     ("Zienswijze", "Twee weken na voornemen; schriftelijk of mondeling; inzage in het advies"),
     ("Samenwerking", "RIEC Den Haag; Haaglanden")],
    '''
<h2>De Haagse aanpak</h2>
<p>Den Haag publiceert haar Bibob-vragenformulieren en de bijbehorende toelichting zelf, met aparte formulieren voor vergunningen, subsidies en overheidsopdrachten. De gemeente beschrijft ook de zienswijzeprocedure: na een voornemen tot weigering of intrekking ontvangt u het advies en hebt u twee weken om schriftelijk of mondeling te reageren. Die transparantie maakt het proces voorspelbaar, maar ook strikt: de termijnen worden gehandhaafd en een onvolledig formulier wordt als zodanig behandeld.</p>
<h2>Inkoop en toezicht</h2>
<p>Wmo-ondersteuning koopt Den Haag stedelijk in, met een Bibob-bepaling in de inkoopdocumenten en raamovereenkomsten. Jeugdhulp wordt ingekocht via het H10 Inkoopbureau namens tien Haaglandengemeenten; de Bibob-bepaling in die inkoop geldt voor alle deelnemers. Het Wmo-toezicht is belegd bij de gemeente zelf en levert, samen met rechtmatigheidsonderzoek, de signalen voor Bibob-onderzoeken.</p>
<h2>Voor Haagse aanbieders</h2>
<p>Download het Haagse vragenformulier voor overheidsopdrachten en vul het bij wijze van oefening in; het is identiek aan wat u bij een toets krijgt. Waar u vastloopt, zit het werk. Als jurist in Den Haag ken ik de Haagse praktijk en de regionale inkoop van nabij; neem contact op als u het formulier of een voornemen hebt ontvangen.</p>
''')

regio("bibob-twente-zorg.html", "Twente", "De regio die als eerste alle inschrijvers structureel toetst.",
    "Twente is de regio waar de Bibob-toets in de zorg het verst is ontwikkeld. In de proeftuin Aanpak Zorgfraude ontwikkelden de veertien Twentse gemeenten een werkwijze om alle inschrijvers op de inkoop Wmo en Jeugd te screenen, en sinds de inkoopronde van 2024 wordt die structureel toegepast. Twente helpt inmiddels andere regio's hetzelfde te doen. Wat in Twente gebeurt, is de voorbode van wat elders komt.",
    [("Bibob-praktijk", "Structurele toetsing van alle inschrijvers sinds inkoop 2024 (meer dan 500 aanbieders); regionaal Bibob-team"),
     ("Instrument", "Kwaliteits- en Integriteitsinstrument Twente (KIT): kwaliteitstoets en Bibob-toets gecombineerd"),
     ("Inkoop", "Samen14 / OZJT: gezamenlijke inkoop Wmo en Jeugd voor veertien gemeenten"),
     ("Landelijk", "Proeftuin Aanpak Zorgfraude; ondersteunt een tiental andere regio's")],
    '''
<h2>De Twentse aanpak</h2>
<p>De Twentse gemeenten kopen Wmo-ondersteuning en jeugdhulp gezamenlijk in via Samen14 en het Organisatie voor Zorg en Jeugdhulp Twente. In de proeftuin Aanpak Zorgfraude ontwikkelden zij vanaf 2021 het Kwaliteits- en Integriteitsinstrument Twente, waarin de kwaliteitstoets uit de inkoop en de Bibob-toets zijn gecombineerd. Bij de inkoopronde van 2024 vulden meer dan vijfhonderd inschrijvers het Bibob-vragenformulier in, en een regionaal team beoordeelde die formulieren, met advies van het Landelijk Bureau Bibob in de gevallen die daarom vroegen. Een deel van de aanbieders trok de inschrijving in; een deel werd geweigerd; de overgrote meerderheid doorliep de toets zonder problemen.</p>
<h2>Wat Twente leert</h2>
<p>Drie lessen uit de Twentse praktijk zijn landelijk bruikbaar. Ten eerste: structurele toetsing is uitvoerbaar, ook bij honderden aanbieders, mits het formulier bij inschrijving wordt gevraagd en er een regionaal team is. Ten tweede: de meeste problemen zitten niet bij de aanbieders die de gemeente verwachtte, maar in financiering en samenwerkingsverbanden die op het eerste gezicht onopvallend waren. Ten derde: aanbieders die zich hadden voorbereid, merkten weinig van de toets; aanbieders die het formulier onderschatten, verloren weken en soms het contract.</p>
<h2>Voor aanbieders in Twente</h2>
<p>Reken erop dat elke inkoopronde en elke toetreding gepaard gaat met het volledige Bibob-vragenformulier, en dat de regio tijdens de looptijd toetst bij signalen. Houd het <a href="bibob-proof-zorgonderneming.html">Bibob-dossier</a> permanent bij; in Twente is het geen eenmalige exercitie.</p>
<h2>Voor aanbieders elders</h2>
<p>Twente ondersteunt via het landelijke programma Aanpak Zorgfraude een tiental andere regio's bij het invoeren van dezelfde werkwijze. Als uw regio daarbij hoort, is de volgende inkoopronde waarschijnlijk de eerste met structurele toetsing. Zie <a href="waarom-bibob-toets-zorg.html">Waarom de Bibob-toets in de zorg belangrijk is</a>.</p>
''')

# =====================================================================
# E. KENNISBANK-OVERZICHT
# =====================================================================
GROEPEN = [
    ("basis", "De basis", [
        ("wet-bibob.html", "Wat is de Wet Bibob", "Betekenis, bereik, Landelijk Bureau Bibob en toepassing in de zorg."),
        ("bibob-toets.html", "De Bibob-toets", "Wat de gemeente toetst, bij wie, en de drie uitkomsten."),
        ("bibob-onderzoek.html", "Het Bibob-onderzoek", "Het verloop in vijf stappen, met termijnen en artikelen."),
        ("bibob-vragenformulier.html", "Het vragenformulier", "De vier onderdelen en een printbare checklist bewijsstukken."),
        ("negatief-bibob-advies.html", "Negatief advies en zienswijze", "Opbouw van een zienswijze, bezwaar en kort geding."),
    ]),
    ("belang", "Het belang van de toets", [p for p in P if p[3] == "belang"]),
    ("situaties", "Situaties", [p for p in P if p[3] == "situaties"]),
    ("wetgeving", "Aanpalende wetgeving", [p for p in P if p[3] == "wetgeving"]),
    ("regio", "Regio's", [p for p in P if p[3] == "regio"]),
]

def groep_html(items):
    out = '<dl class="lijst">'
    for it in items:
        slug, kop, oms = it[0], it[1], it[2]
        out += f'<div class="item"><dt><h3><a href="{slug}">{kop}</a></h3></dt><dd><p>{oms}</p></dd></div>'
    return out + "</dl>"

kb_body = ""
for key, titel, items in GROEPEN:
    kb_body += f"<h2 id=\"{key}\">{titel}</h2>" + groep_html(items)

page(slug="kennisbank.html", breadcrumb="Kennisbank",
    title="Kennisbank Bibob en zorg — alle onderwerpen",
    desc="Alle uitlegpagina's over de Wet Bibob voor zorgaanbieders op één plek: de basis, het belang van de toets, situaties (inkoop, pgb, maatwerk, onderaanneming), aanpalende wetgeving (Wtza, Wibz, VOG, zorgfraude) en regio's.",
    h1="Kennisbank: de Wet Bibob voor zorgaanbieders",
    intro="Alle onderwerpen op één plek, geschreven voor bestuurders en kwaliteitsmedewerkers van zorgaanbieders, met de wetsartikelen erbij. Begin bij de basis als de Wet Bibob nieuw voor u is; ga direct naar de situatie of regio die op u van toepassing is als u een brief hebt ontvangen.",
    marge=marge([
        ("Onderdelen", [f'<a href="#{k}">{t}</a>' for k, t, _ in GROEPEN]),
        ("Auteur", "mr. J. Smit, jurist, Den Haag"),
    ]),
    body=kb_body, faq=[],
    **CONTACT_STD)

ALL = [p[0] for p in P] + ["kennisbank.html"]
print("\n".join(ALL))
