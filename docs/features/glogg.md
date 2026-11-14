# Glögg

Planen för ett eget spår: lokala marknader i tidningen, och marknader som dyker upp.
Inte en ny app. Inte TTS. Ingen kod förrän rutorna under "Innan något går utåt" är avbockade.

Ärende: https://github.com/Azdwarf5Azdwarf/vg-brevladan/issues/3
Gren: `glogg`, från `main` (`e66bcd3`).
Namnet glögg står. Dennis, 2026-11-14.

Riktning samma dag: lokaltidning och lokal marknad. Vi skrapar webbplatser som har PDF:erna, och webbplatser för det andra. Fallens dagar är en webbplats.

## Mål

Ur raderna som redan finns, plocka marknader: julmarknad, loppis, och det som står i samma spalt.
Ett anrop, `marknad(kommun)`, ger högst sju rader: namn, vad, när, sida, telefon om den finns.
Första beviset mot brevlådan är vecka 46, Tanum och Munkedal, `data/veckovis-2026-v46.tsv`. Ingen ny scrape.

Första marknaden utanför den tabellen är Fallens dagar. Kortet är `sources/markets/fallens-dagar.yaml`.

## Källor, en fil per papper

`sources.yaml` är registret: regeln "bara Västra Götaland", id:n, och pekare till filen.

```
sources/veckovis.yaml
sources/alingsaskuriren.yaml
sources/boraskuriren.yaml
sources/tidningen-vastsverige.yaml
sources/markets/fallens-dagar.yaml
```

Fallens dagar är inte ett femte papper. TTELA är fortfarande utanför.

## Fallens dagar

- Kommun: Trollhättan.
- När: tredje fredagen i juli sedan 1959. Senast 17–19 juli 2026. Nästa: juli 2027.
- Vad: stadsfestival, marknad i centrum, foodtrucks och karuseller längs Strandgatan.
- Källa: https://www.fallensdagar.se/ och https://www.vastsverige.com/visittrollhattanvanersborg/fallens-dagar/
- Hämtning: webbplats. 2027 års fallpåsläppstider är inte ute.
- Telefon: saknas. Inget nummer är hittat på de sidorna.

Inget artistprogram är kopierat hit.

## Vad som redan ligger i vecka 46

- Tanums Bygdegård, julmarknad med cafeteria, lör 21 nov kl 10-15, sidan 7. Inget nummer.
- Julmarknad och loppis i Kville, 14 november kl 10-14, sidan 30, 070-535 75 90.
- Pop-up loppis, Munkedal, Västra Åtorpsvägen 2, 14/11 10-14, sidan 30. Inget nummer.

Julbord, julkonsert och julerbjudanden i butik är inte marknader. De stannar i de vanliga raderna.

## Ordning

1. Dennis läser den här filen.
2. Ett ärende, den här grenen. Ärendet är nummer 3 och pekar hit.
3. Dela `sources.yaml`. Marknaderna ligger i `sources/markets/`.
4. Lägg Fallens dagar som marknadskort, en webbplats.
5. Ett filter på befintliga rader. Marknad känns igen på orden julmarknad och loppis i `what` eller `name`.
6. Bevis: de tre raderna ovan kommer med. Julbord kommer inte med. Fallens dagar kommer med från sitt kort, inte från vecka 46.
7. Stopp. MCP-verktyget och rösten är ett senare ärende.

## Innan något går utåt

- [x] Dennis har läst den här filen och bett om commit, push och PR (2026-11-14).
- [x] `sources/` har de fyra papper som redan fanns.
- [x] `sources/markets/fallens-dagar.yaml` finns. Webbplats, inget kopierat program.
- [ ] Ingen ny scrape.
- [ ] Inget nummer som inte redan står i en källa.
- [ ] Julbord och konserter följer inte med.

## Ostoppbara tangenter

Julmarknad → loppis och bygdegård året runt. Maskinen är raden: vecka, sida, vad, när, telefon. Ordet jul följer inte med.

Brevlådetidning → en webbplats som bär PDF:en, och en webbplats för det andra. Maskinen är en fil per källa, plus raden. Kravet "delas ut i brevlådan" följer inte med.

Trollhättan-marknad → Fallens dagar är första kortet, en webbplats. Nästa marknad blir en ny fil i `sources/markets/`. TTELA följer inte med.

⚫ Svart hål: vilket gratispapper som täcker Trollhättan till vardags. Tills vidare: ingen tidningsfil för stan.

⚫ Svart hål: vilka marknader folk faktiskt åker till, och om klockslaget stämmer när de står där. Tills vidare: bara vecka 46 och Fallens dagar-kortet.

## Inte det här ärendet

Nycklarna (ärende 2, Luren, grenen `claude/session-planning-verification-x23q8z`). LiveKit. Ny scrape. AlingsåsKuriren som innehåll. TTELA.
