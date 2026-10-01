# Roadmap

Målet är diskret samla små tidningar i Västra Götaland.

Målet är uppnått när en modell, via MCP, kan förklara för en gamling med ren TTS — och gubben eller kärringen har pappret framför sig.

Modellen har kontexten digitalt. Människan har tidningen. TTS pekar på pappret, den ersätter det inte.

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

Då är målet nått. Fler tidningar är bara fler rader.

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
