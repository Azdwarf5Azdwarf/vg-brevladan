# Luren

Planen för att hämta de tre nycklarna så att en lokal CLI sedan kan prata.
Inte CLI:n. Inte LiveKit. Inget bygge förrän rutorna under "Innan något går utåt" är avbockade.

Ärende: https://github.com/Azdwarf5Azdwarf/vg-brevladan/issues/2

## Mål

Tre nycklar, var och en bevisad med ett anrop, sparade utanför git. Sedan stopp.
Nästa ärende, inte det här, är push-to-talk som läser `data/veckovis-2026-v46.tsv`.

🔴 Gissat: den befintliga Deepgram-nyckeln och den befintliga Claude-nyckeln provas först. En ny skapas bara om anropet nekas. Du sade "hämta från plattformarna" och gick och la dig.

## Var nyckeln hämtas

De ligger inte på samma ställe. `platform.claude.com` är bara Claude.

| | Konsol | På maskinen nu |
|---|---|---|
| Deepgram, örat | https://console.deepgram.com/ | `~/.config/deepgram/.env`, variabeln `DEEPGRAM_API_KEY` är satt |
| Claude, hjärnan | https://platform.claude.com/settings/keys | `~/.nullclaw/anthropic.env`, namnet `ANTHROPIC_API_KEY` |
| Cartesia, munnen | https://play.cartesia.ai/keys | ingen nyckel, `~/dev/above5below5/cartesia.toml` är tom |

Claude-konsolen är skild från Claude-chatten och från `claude` i terminalen. En prenumeration där räcker inte som API-nyckel.

## Var de sparas

Utanför repot. Rättigheter `600`. Aldrig i git, aldrig i ärendet, aldrig i den här filen.

- Deepgram stannar i `~/.config/deepgram/.env`.
- Cartesia blir `~/.config/cartesia/.env` med `CARTESIA_API_KEY` och `CARTESIA_VOICE_ID`.
- Claude stannar i `~/.nullclaw/anthropic.env` om den nyckeln svarar. Annars samma fil, nytt värde, den gamla raden kvar som kommentar utan att skrivas ut någonstans.

Repot är publikt. Den här filen också.

## Bevisa, utan att skriva ut nyckeln

Varje bevis skriver bara statuskod. Nyckeln rör inte stdout.

- Deepgram: `GET https://api.deepgram.com/v1/projects` med headern `Authorization: Token`. `200` räcker.
- Claude: `POST https://api.anthropic.com/v1/messages` med `x-api-key`, `anthropic-version: 2023-06-01`, en mening, `max_tokens` lågt. `200` räcker. Modellen väljs när anropet görs, den som konsolen visar som vanlig.
- Cartesia: `POST https://api.cartesia.ai/tts/bytes` med `X-API-Key` och `Cartesia-Version: 2026-08-14`, en svensk mening, `model_id` `sonic-3`, språk `sv`. Rösten väljs i playground, en som talar svenska. Svaret spelas med `afplay`. Engelsk demo-röst används inte.

## Innan något går utåt

- [ ] Dennis har läst den här filen.
- [ ] Ingen nyckel i git, ärende eller chatt.
- [ ] Inget kort dras och ingen kredit köps förrän Dennis sagt beloppet. Deepgram används redan. Claude-konsolen och Cartesia kan be om kort.

## Ostoppbara tangenter

De tre nycklarna → samma öra, hjärna och mun kan läsa en annan lokal tabell. Veckovis-raderna, sidpekaren och släktingen följer inte med.

⚫ Svart hål: vilket hushåll, om pappret ligger på bordet, vilken kommun de bor i. Tills vidare: bara vecka 46, och bara om de frågar.

## Inte det här ärendet

Mikrofon, `mcp_server.py`, sqlite, LiveKit, AlingsåsKuriren. `ROADMAP.md` säger fortfarande LiveKit. Det här ärendet följer ordet från 2026-11-13: lokal CLI, nycklarna först.
