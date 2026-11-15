# vg-brevladan

Personligt verktyg för lokala tidningar och lokala marknader i **Västra Götaland**.

Mallen vi började med är [Veckovis](https://veckovis.com/): tisdag i brevlådan, annonser, telefonnummer, vad som händer. Inga världshändelser.

Nästa lager är marknader. Vi skrapar webbplatser som har PDF:erna, och webbplatser för det andra. Första tillagda: Trollhättans Fallens dagar, en webbplats.

Allt utanför länet är borttaget. Skåne, Norrbotten, Gävleborg, Halland ingår inte.

## Vad det känner av

Lokal ekonomi som den faktiskt syns: vem som annonserar, vilket nummer man ringer, vilken loppmarknad, vilken bygdegård. Och marknaden när den dyker upp, med källa. Inte en världsnyhetsfeed.

## Källor

`sources.yaml` är registret. Ett papper per fil i `sources/`. En marknad per fil i `sources/markets/`.

Bara sådant som hör till länet. Fallens dagar: `sources/markets/fallens-dagar.yaml`. Den hör till webbplatserna, inte till PDF:erna.

## Kör

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/extract.py --demo
python src/mcp_server.py
```

Demo läser `fixtures/` så du kan känna flödet utan att scrapa någon live.

## Helg

Se `WEEKEND.md`.

## Bok

Utkast: `bok/jag-alskar-tidningar.md`.

## Regler

- Scrapa på schema, aldrig i frågan.
- Spara datum, plats, vad, telefon, källa. Inte hela artikeln.
- Respektera robots.txt. Publicera inte om annonsörens text.
- Personligt bruk. Ingen vidarepublicering.
