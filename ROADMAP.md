# Roadmap

Riktning 2026-11-14, Dennis: lokaltidning och lokala marknader. Vi skrapar webbplatser som har PDF:erna, och webbplatser för det andra. Fallens dagar är en webbplats. Brevlådan nedan är mallen vi började med. Se `README.md` och `docs/features/glogg.md`.

Målet är diskret samla små tidningar i Västra Götaland.

Målet är uppnått när en modell, via MCP, kan förklara för en gamling med ren TTS — och gubben eller kärringen har pappret framför sig.

Modellen har kontexten digitalt. Människan har tidningen. TTS pekar på pappret, den ersätter det inte.
Den kommer innehålla STT och LLM också för de lilla reasoning lagret ovanpå den talar frågor i paradoxer och låter den äldre bestämma de poi-vägen alltid där hemma. Den är neutral i lagret nedan detta handlar om lokala fina nyheter ingen politik direkt

## Bilden

```
brevlåda  →  papper på bordet
                ↑
MCP läser essens (vecka, sida, vad, nummer)
                ↓
ren TTS: "På sidan du har framför dig, lördag, bygdegården. Numret står under rubriken."
```

Inte en app. Inte ett flöde. En röst som kan tidningen de redan håller i.

## Klart när

Ett test, en tisdag, ett hushåll:

1. Veckovis ligger på bordet.
2. Modellen vet vilken vecka och vilka essensrader som finns.
3. Gamlingen frågar högt: vad händer på lördag, och vilket nummer.
4. TTS svarar i korta meningar, pekar på pappret, läser inte om världen.
5. Ingen skärm behövs för svaret.
6. Ett snabbt test; på bibloteken sitter alla gamlingar i ett hörn och läser tidningarna som samlas där dem pratar inte men det är något där jag inte vill ersätta. Bara om jag kan ordna något så andra gamlingar vet att de finns och dem kan lära sig om marknader, nyheter och butiker. För dem sprider det mun till mun bäst.
7. Frågan är bara svarad tills de får se det. Arketypen finns de barnbarnet som hjälper med tekniken - och alltid svarar mormor och morfars samtal och dyker upp (detta är för mig att simulera känslan.)

Då är målet nått. Fler tidningar är bara fler rader.

## MVP, nu

Ett test för hela projektet, innan riktiga hushåll:

1. Tre veckors Veckovis, skannade (eller PDF om de finns på nätet). Rader extraheras och sparas. Skanningarna stannar utanför git.
2. En lokal LiveKit-agent i terminalen: tal till text, en LLM via API, text till tal.
3. Ett samtal: någon spelar en gamling som pratar igenom veckans tidning med agenten.

Klart när samtalet går igenom utan skärm, och agenten bara säger det som står i raderna.

## Steg

### 0. Länet, inte landet
Gjort. `sources.yaml` är bara Västra Götaland. Veckovis är mallen. AlingsåsKuriren är tvåan. BoråsKuriren är okollad.

### 1. Diskret insamling
Cron, en gång i veckan, efter utdelningsdagen.
Spara vecka, URL, kommun, händelse, telefon, sidhint.
Inte hela artikeln. Inte annonstexten i git.

### 2. Pappret som ankare
Varje rad får `week` + `page_hint` ("höger spalt, under loppmarknad").
TTS får bara prata om rader som har en ankarpunkt. Annars: "det står inte i tidningen jag ser."

### 3. MCP, tre verktyg
`vad_hander(kommun)` — denna vecka, max sju rader.
`ring(namn)` — nummer plus var på pappret det står.
`las_sidan(paper, week)` — essens i den ordning man bläddrar.
Inget scrape i anropet.

### 4. Ren TTS
Kort mening. Ett faktum. Nummer sagda långsamt.
Inga "enligt källan", inga länkar, inget engelskt.
Om det är osäkert: tystnad, inte gissning.
Röstkontraktet ligger i `tts/contract.md`.

### 5. Syskon, inte den här kontexten
När rösten inte räcker ska samma essens kunna gå tillbaka till papper.
Det är ett annat projekt: **elderly2fax**.
Hint only. Eget repo, troligen privat, egen kontext. Brevladan exporterar en rad (vem, nummer, en mening, vecka). Fax-projektet äger tonval, försättssida och sändning. Blanda inte ihop dem.

### 6. Andra tidningen
Först när Veckovis klarar testet ovan. Sen AlingsåsKuriren, samma schema.

## Inte målet

Alla 49 kommuner. Paywall (GP, TTELA, Bohusläningen). En chatt. En tidning på skärmen i stället för i handen.