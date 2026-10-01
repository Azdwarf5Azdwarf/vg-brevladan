# vg-brevladan

Personligt verktyg för gratistidningar i **Västra Götaland**.

Mallen är [Veckovis](https://veckovis.com/): tisdag i brevlådan, annonser, telefonnummer, vad som händer. Inga världshändelser.

Allt utanför länet är borttaget. Skåne, Norrbotten, Gävleborg, Halland ingår inte.

## Vad det känner av

Lokal ekonomi som den faktiskt syns: vem som annonserar, vilket nummer man ringer, vilken loppmarknad, vilken bygdegård. Det är essensen, inte en nyhetsfeed.

## Källor

Se `sources.yaml`. Bara papper som delas ut i länet.

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
