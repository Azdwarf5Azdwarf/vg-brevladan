# Anslag

Planen för ett syskon: lapparna man ser från bussen, inte tidningen i brevlådan.
Inte en kartapp. Inte en kamera i det här ärendet. Ingen kod.

Sedd från bussen 2026-11-14. Ombedd samma förmiddag: en plan, en pinne, ett exempel.

Gren: `cursor/anslag-bd5a`, från `main` (`e66bcd3`).

## Mål

En karta över var lapparna brukar sitta. En pinne per tavla: hållplats, affär, bygdegård.
Ett foto stannar på disken. Skanningen blir en rad: datum, plats, vad, telefon, källa.
Raden laddas i samma databas som tidningen, med `paper: anslag` och pekare till pinnen.
Rösten kan sedan säga det som sitter ute, och fortfarande tiga om det som inte är inläst.

## Syskon, samma databas

Anslag är ett annat intag. Tidningen hämtas på schema. Tavlan hämtas till fots.
Fotot, OCR-motorn och kartplattorna ägs inte här. Här ägs pinnen och raden.

elderly2fax är uttaget, ett annat repo: essens tillbaka till papper.
Anslag är intaget åt andra hållet, och stannar i det här repot just därför att raden ska in i samma databas. Utan raden är tavlan bara något man åkte förbi.

## Kartan

En fil per pinne i `sources/anslag/`. Registret får en `anslag:`-lista i `sources.yaml`.

Fält: `id`, `name`, `kind: anslag`, `slag` (`hallplats`, `butik`, `bygdegard`), `kommun`, `lat`, `lon`, `vanligen`, `note`.

`lat` och `lon` är tomma tills platsen är gången. En pinne utan koordinat är ändå en pinne: namnet på tavlan, kommunen när den är känd.

Första filen är exemplet `sources/anslag/exempel-hallplats.yaml`. Den pekar inte på en viss hållplats från idag. Hållplatsen var inte namngiven.

## Skanningen

Foto läggs i `data/anslag/`. Den mappen är gitignorerad, tillsammans med sqlite-filen.
Texten ur fotot läses lokalt, senare. Det här ärendet har ingen OCR.

Det som får bli en rad:

- offentlig lapp: förening, loppmarknad, bygdegård, öppet hus
- plats (pinnens id), när, vad i en mening, telefon om den är tryckt och läsbar

Det som inte blir en rad:

- privat lapp: namn, säljes, uthyres, dödsannons, tack
- politisk affisch, brödtext, bilden själv
- en siffra som inte gick att läsa. Den skrivs inte. Den gissas inte.

## Exemplet

`sources/anslag/exempel-lapp.yaml` är formen på en rad, påhittad.
Inget nummer. Ingen avskriven affisch. `phone: saknas`.
Den visar vad som laddas den dag en riktig lapp är läst, och inget mer.

## Ordning

1. Den här filen, ärendet, exempelpinnen, exempelraden.
2. Nästa riktiga pinne skrivs när en tavla är gången: namn, kommun, koordinat.
3. Första riktiga lappen skrivs från ett foto som stannar i `data/anslag/`. Bara raden committas, och bara om siffrorna är lästa.
4. Laddning in i sqlite, `paper = anslag`, när raden finns på riktigt. Samma tabell som tidningen använder då (`rows` om den finns, annars `events`). Ingen andra databas. Inget nytt verktyg i anropet.
5. Stopp. Rösten som säger "på tavlan vid hållplatsen" är ett senare ärende. Utan rad sägs inget.

## Innan något går utåt

- [x] Ombedd 2026-11-14: plan, pinne, exempel.
- [x] `sources/anslag/exempel-hallplats.yaml` finns. Pinne utan koordinat.
- [x] `sources/anslag/exempel-lapp.yaml` finns. Påhittad form, inget nummer.
- [x] `data/anslag/` är gitignorerad.
- [ ] Ingen bild i git.
- [ ] Inget nummer som inte står på en lapp som är läst.
- [ ] Ingen OCR, ingen kartapp, ingen ny kod i det här ärendet.

## Ostoppbara tangenter

Hållplats → alla tavlor i länet. Maskinen är en pinne. De 49 kommunerna följer inte med.

Foto → ett bildarkiv. Bilden stannar utanför git. Raden följer med.

Lokal närvaro → en karta i webbläsaren. Kartan är filerna. Rösten är ett senare ärende.

Tavla → tidningens sida. Ankaret för en lapp är pinnen, inte ett sidnummer. `page_hint` i tidningen rörs inte här.

## Svarta hål

⚫ Vilken hållplats det var idag. Tills vidare: exempelpinnen, ingen koordinat.

⚫ Vilka lappar som satt där. Tills vidare: exempelraden, inget nummer, ingen brödtext.

⚫ Hur en oläsbar siffra märks när OCR väl finns. Tills vidare: oläst siffra skrivs inte.

## Inte det här ärendet

Luren (ärende 2). Glögg (ärende 3). LiveKit. Ny scrape. OCR-bibliotek. Kartplattor. elderly2fax.
