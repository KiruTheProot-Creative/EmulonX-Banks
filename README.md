# Emulon X banks

Sound banks (`.emxb`) for [Emulon X](https://github.com/KiruTheProot-Creative/EmulonX).

## Getting banks

Open the **Emulon X Hub**, go to **EMULON BANKS**, pick a bank and click **Download bank**. The Hub asks where it
should go (your banks folder from the Emulon X installer is filled in), and the bank shows up in Emulon X right away.

## How this repository works

Each bank has a folder in `banks/` with an `info.json` (and optionally a `cover.png`):

```json
{
  "name": "EMULON X BASE BANK",
  "author": "Kiru",
  "official": true,
  "soon": false,
  "description": "The official starter bank for Emulon X.",
  "presets": 64,
  "version": "1.0",
  "download": "https://github.com/KiruTheProot-Creative/EmulonX-Banks/releases/download/base-bank-v1.0/EmulonX-Base-Bank.emxb",
  "size": 251658240,
  "colour": 0
}
```

The bank file itself is too big for a normal repository file, so it's attached to a **release** of this repository:
**Releases > Draft a new release**, give it a tag like `base-bank-v1.0`, drop the `.emxb` file in, publish, then put the
file's download link into `download` in `info.json` and its size in bytes into `size`.

- `soon: true` shows the bank as "coming soon" (no download yet). The Hub notifies people when it changes to `false`.
- `colour` (0 to 360) colours the drawn cover when there's no `cover.png`.
- `index.json` (the list the Hub reads) is rebuilt automatically - don't edit it by hand.
