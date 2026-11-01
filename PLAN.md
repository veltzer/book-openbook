# PLAN

Progress notes for adding tunes to the openbook (`src/openbook/`) from the
scanned books in `real_books_archive.gi/`. Last updated 2026-11-01.

## Status

- `src/openbook/` holds 807 tunes.
- Tunes with a Jazz Fake Book location (`jfb:`): 583.
- Tunes with a Real Book vol 1 location (`rbk1:`): 110.
- Duplicate uuids were removed, and `scripts/check_all.py` now fails the build
  on any duplicate uuid (test in `tests/test_check_all.py`).

## Jazz Fake Book (`jfb`) - done

Source: `real_books_archive.gi/Jazz Fake Book.pdf`, PDF page = book page - 1.
Index: `real_books_archive.gi/index/Jazz_Fakebook.csv` (its page column is the
PDF page).

Every title in the index has been handled: either added or found to be in the
book already (sometimes under another spelling, e.g. "What A Diff'rence A Day
Made", "Strange Fruit" whose title was misspelled "Strang Fruit").

Tunes still at completion 3 (doubtful bars listed in each file's TODO):
`close_as_pages_in_a_book`, `fiesta_in_blue`, `inner_space`,
`lennies_pennies`, `now_he_sings_now_he_sobs`, `out_to_lunch`,
`parkers_mood`, `spain`, `thermo`.

Known book quirks kept as printed:

- The Thrill Is Gone: the page prints copyright 1922 (the song is from 1931).

Credits corrected against the page:

- Sonny Boy: composer "B.G. DeSylva" (the book prints "B.D.").

## Real Book vol 1 (`rbk1`) - in progress

Source: `real_books_archive.gi/Real Book Vol 1.pdf` (the old handwritten Real
Book), PDF page = book page + 8. The book's own printed index is on PDF pages
2-7. Do not use `index/Real_Book_1.csv`: it belongs to a different edition.

Helper source for unclear notes: `real_books_archive.gi/Real Book Vol 1 in
Bb.pdf`, the same book transposed for Bb instruments (sounding pitch = written
pitch a major second lower), PDF page = book page + 10, scanned at a higher
resolution. The New Real Book volumes also have some of these tunes.

### Done

Every index title from "A Call For All Demons" (page 1) through
"12-4 2-4/Duplicities" (page 128) has been handled: 50 tunes added in the last
batch, the rest were already in the book.

The handwriting makes many readings doubtful, so most of the new tunes are at
completion 3; each file's TODO lists the doubtful bars:
`12_4_2_4_duplicities`, `a_call_for_all_demons`, `a_child_is_born`,
`african_flower`, `ana_maria`, `arise_her_eyes`, `armageddon`, `ballet`,
`beauty_and_the_beast`, `bitter_suite_in_the_ozone`, `black_nile`,
`blessed_relief`, `blue_comedy`, `boston_marathon`, `brainville`,
`bright_size_life`, `broadway_blues`, `brownout`, `butterfly`,
`captain_marvel`, `central_park_west`, `ceora`, `childrens_song`,
`como_en_vietnam`, `conception`, `crescent`, `deluge`, `doin_the_pig`,
`domino_biscuit`, `the_dolphin`.

Needing the most work:

- `the_dolphin`: the melody is mostly guesswork (very crowded handwriting).
- `country_roads`: chords only (completion 1), the melody staff is empty; the
  page is a piano arrangement whose top line did not add up.
- `domino_biscuit`: the voice part is the bass line (the page prints only solo
  slashes, voicings and a bass line).
- No chords in the book: `childrens_song`, `broadway_blues`,
  `a_call_for_all_demons` (doChords = false).

Credits that differ from the page:

- Afro Blue: Mongo Santamaria (the book says John Coltrane).
- Dexterity: Charlie Parker (the book says Dexter Gordon).
- April In Paris: poet E.Y. Harburg added (not printed).
- Dear Old Stockholm: composer "Traditional" (the page prints the folk song
  name "Varmland").

### Skipped (not lead sheets, or illegible)

These pages are dense piano or ensemble arrangements, free-time pieces, or
have runs that cannot be read in the scan. A later attempt could try the Bb
edition or another book:

- A Family Joy (4), And Now, The Queen (22), Around Again (22),
  And On The Third Day (23), April Joy (27), Ay, Arriba! (34),
  Batterie (38), Chelsea Bells (76), Colors Of Chloe (82),
  Canyon Song (72, time signatures change almost every bar and cannot be
  read).

Already in the book under another title: Black Orpheus (=
`a_day_in_the_life_of_a_fool`), Blue Train (= "Blue Trane"), Five Hundred
Miles High (= `500_miles_high`), Corcovado (=
`quiet_nights_of_quiet_stars`), Freddie The Freeloader (=
`freddie_freeloader`).

### Next

Index titles from page 129 on that are not in the book yet (checked through
the H section; I-Z of the index has not been checked against the book):

Ecclusiastics (131), Eiderdown (132), Eighty One (134), El Gaucho (135),
Elizete (136), Empathy (137), Equipoise (140), E.S.P. (141),
Exercise #3 (142), Exercise #6 (143), Fables Of Faubus (144), Fall (146),
Falling Grace (147), Fee-Fi-Fo-Fum (149), Feelings And Things (150),
The Fields We Know (151), 502 Blues (153), Follow Your Heart (154),
Flags (156), Forest Flower (158), For Heaven's Sake (159),
Fortune Smiles (160), Four On Six (162), Four Winds (163),
Freedom Jazz Dance (165), Gary's Waltz (166), Gemini (167),
General Mojo's Well Laid Plan (168), Golden Lady (174),
Good Evening Mr. And Mrs. America (176), Grand Central (178),
Green Mountains (180), Grow Your Own (182), Hassan's Dream (185),
Heaven (187), Henninger Flats (190), Herzog (192), Hey There (194),
Hold Out Your Hand (195), Hotel Overture (196), Hotel Vamp (197),
Hotel Hello (198), House Of Jade (201), How My Heart Sings (204),
Hullo, Bolinas (205).

Before each batch, check titles against the book loosely (titles and file
names, alternate titles like Black Orpheus / Manha de Carnaval): exact title
matching missed several duplicates.

After the Real Book vol 1: Real Book vol 2/3, the New Real Book volumes and
the other books in `real_books_archive.gi/`.

## How a tune is added

Conventions (see `four.ly.tera`, `god_bless_the_child.ly.tera`,
`all_blues.ly.tera`, and for Real Book tunes `round_midnight.ly.tera`):

- One file `src/openbook/<snake_name>.ly.tera`: TOML front matter, Doc
  DONE/TODO, `Chords<Ver>` / `Voice<Ver>` parts. Version "Fake" for the fake
  book, "Real" for the real book. The voice part is `{ ... }` without
  `\relative` (the driver adds it).
- Front matter: title, style, composer, poet (if any), piece (tempo/style
  word on the page), copyright (only if printed), typesetter, completion
  ("5" when chords and tune match the scan bar by bar, "3" when parts are
  doubtful), uuid (`python -c 'import uuid;print(uuid.uuid1())'`), structure,
  location (`jfb:<page>` / `rbk1:<page>`, a range when a tune spans two
  pages).
- Multiple names comma separated, never "and"; no double quote inside a
  front matter value (use single quotes for nicknames).
- Transcribe from the scan only, never from memory. No lyric text (add
  "- add the lyrics." to TODO for songs with words).
- `\tempo "Name" 4 = N`, then `\time`, then `\key` on consecutive lines;
  `\myMark` only with accepted names (A, B, C, D, Intro, End, Instr, ...)
  and an empty line before it; no `\bar`, `\include`, `\break`; Dutch note
  names; tabs; `\tuplet` not `\times`.
- Two `[[youtube]]` entries (the original or the recording the page cites,
  plus one more), each verified with
  `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=ID&format=json`.
- Verify with `python -m scripts.check_all --inputs <file>`, a render
  compared with the scan bar by bar, and finally `rsconstruct build` and
  `rsmultigit check same --terse --no-stop` (from `~/git`).

The batches were run as parallel helpers (5 tunes each) following written
briefs. The briefs and the helper scripts (page rendering, single-tune render,
staff-line pitch finder) lived in a temporary scratchpad under `/tmp` and are
not kept; this section holds what they said.
