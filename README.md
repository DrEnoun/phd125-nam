# PHD125 · Chemistry with Dr. NAM · Study Hub

Self-instructional materials for PHD125 Pharmaceutical Organic Chemistry (Faculty of Pharmacy, UiTM Bertam, Penang). Sister site of the [PHD115 Study Hub](https://github.com/DrEnoun/phd115-nam), built on the same engines.

**Status: draft.** Chapter 1 is built. Sign-in, tracking and the leaderboard are switched off (`ENDPOINT` is empty in `js/track.js`) until the Apps Script backend accepts PHD125 records.

## Layout

- `index.html` · the hub, grouped by AIMS chapter (Chapters 1–8), then "Beyond the syllabus" (x1 Nucleic Acids, x2 Lipid Metabolism, x3 VSEPR Theory)
- `ch1/` … `ch8/` · one folder per AIMS chapter: `pre/`, `slides/`, `post/`, `tutorial/`, `game/`
- `x1/` … `x3/` · extras: `slides/`, `tutorial/`, `game/` only
- `downloads/` · printable PDFs (student pages followed by the answer key)
- `js/`, `img/`, `leaderboard/` · shared with PHD115, renamed for PHD125 (storage keys use `phd125:` and `nam125:` so the two hubs never mix on the same browser)
- `_src/` · content and build scripts (not published: GitHub Pages skips folders starting with `_`)

## Slides

One long deck per AIMS chapter, in the Dr. NAM Science Decks style. The AIMS chapter title is on every slide; each subchapter has a divider and a chip (1.1, 1.2 …). Link to a subchapter with `#s3` (for example `ch1/slides/#s3`).

## Building a chapter

Content lives in `_src/<ch>/slides.py`, `_src/<ch>/activities.py` and `_src/<ch>/game.py`. Structures are drawn from SMILES with RDKit, so every figure is exact and works offline.

```
pip install rdkit playwright pypdf && python3 -m playwright install chromium
python3 -I _src/build_hub.py            # hub (chapter list in _src/hub_chapters.js)
python3 -I _src/build_deck.py ch1       # slides
python3 -I _src/build_acts.py ch1       # before class, after class, tutorial, game
python3 -m http.server 8125 &           # then:
python3 -I _src/build_pdfs.py ch1       # printable PDFs
```

To switch on a chapter in the hub, give its activities paths in `_src/hub_chapters.js` and rebuild the hub.

## Sources and licence

Core references: Dr. NAM's NAM-INTRO and NAM-ALKANE notes (LibreTexts, Sharpe Elles remix), *The Basics of General, Organic, and Biological Chemistry* (Ball, Hill & Scott) and *Fundamentals of General Organic and Biological Chemistry* (LibreTexts), all CC BY-NC-SA 3.0; Soderberg, *Organic Chemistry with a Biological Emphasis*, CC BY-NC-SA 4.0. Each page credits its own sources. Shared under CC BY-NC-SA for non-commercial teaching.
