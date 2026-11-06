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

## Lyrics - in progress

Started 2026-11-04. Tunes whose front matter names a poet but whose file has
no lyrics part. The Jazz Fake Book prints the lyrics under the melody, so the
tunes located only in it (`jfb:`) are done from that page; the rest need
another source.

Helper scripts for this work live outside the repo (scratchpad of the session):
`page.sh <book page>` renders the fake book page, `compile.sh <tune>` renders the
tera tree, compiles the single tune and prints lilypond's syllable-to-note
alignment bar by bar.

Conventions used: lyrics go in a `Lyrics<Version>` part right after the
`Voice<Version>` part, `doLyrics = true` in that version; a second verse
printed under the first goes in `Lyricsmore<Version>` with `doLyricsmore =
true` and only runs as far as the book prints it; `_` skips an untied note
that has no syllable (tied and slurred continuations never take a syllable
and need no skip); `__` draws the extender after a held syllable; double
quotes are not allowed in lyrics, use single quotes; a lyric that starts with
a digit or contains special characters is written in double quotes as a
lilypond string (`"500"`).

Status 2026-11-07: the fake book pass is complete. 378 of the 396 fake
book tunes with a poet carry lyrics; every one was compiled and its
syllable-to-note alignment compared with the page bar by bar (except
`twisted`, whose file has a TODO to do that check).

Pages that print no lyrics (instrumental heads, nothing to add):
`down_by_the_riverside`, `its_sand_man`, `johnnys_theme`, `king_porter_stomp`,
`maple_leaf_rag`, `salt_peanuts`, `shiny_stockings`, `swinging_shepherd_blues`,
`tickle_toe`.

Not done because the assistant's output filter refuses to reproduce these
particular lyrics (type them by hand from the page): `arent_you_glad_youre_you`
(48), `god_bless_the_child` (131), `i_wont_dance` (166),
`is_you_is_or_is_you_aint` (188), `lullaby_of_the_leaves` (231), `lush_life`
(232), `sonny_boy` (354), `you_better_go_now` (439), `you_made_me_love_you`
(440).

Melody edits made while adding lyrics (the book prints no tie/slur there):
`boplicity` bars 2-3 and 27. Bars where the book's ties and the typed melody
disagree are listed as TODO lines in the files (`fever`,
`a_lot_of_livin_to_do`, `frosty_the_snow_man`, `im_glad_there_is_you`,
`lets_get_away_from_it_all`, `do_you_know_what_it_means_to_miss_new_orleans`,
`put_your_little_foot_right_out`, `van_lingle_mungo`, `new_york_afternoon`).

Fake book tunes missing lyrics at the start (353):

a_beautiful_friendship, a_cottage_for_sale, a_felicidade,
a_ghost_of_a_chance, a_good_man_is_hard_to_find, a_lot_of_livin_to_do,
a_string_of_pearls, a_sunday_kind_of_love, a_taste_of_honey,
across_the_alley_from_the_alamo, after_hours, after_youve_gone,
aint_misbehavin, all_about_ronnie, all_of_you, alright_okay_you_win, amapola,
and_all_that_jazz, arent_you_glad_youre_you, baby_wont_you_please_come_home,
ballin_the_jack, basin_street_blues, bernies_tune, bess_you_is_my_woman,
blue_and_sentimental, blue_champagne, blueberry_hill, blues_in_the_night,
boplicity, born_to_be_blue, button_up_your_overcoat, bye_bye_blues, caldonia,
candy, carioca, carolina_moon, cc_rider, charmaine, cherokee,
choo_choo_ch_boogie, close_as_pages_in_a_book, come_sunday, comes_love,
count_every_star, crazy_rhythm, cute, dc_farewell, dearly_beloved, deed_i_do,
dinah, do_nothin_till_you_hear_from_me,
do_you_know_what_it_means_to_miss_new_orleans,
dont_let_the_sun_catch_you_cryin, dont_take_your_love_from_me,
down_by_the_riverside, east_of_the_sun, everybody_loves_my_baby,
everythings_coming_up_roses, evry_time_we_say_goodbye, exactly_like_you,
falling_in_love_with_love, fever, fine_and_mellow, fool_that_i_am,
for_all_we_know, for_every_man_theres_a_woman, for_sentimental_reasons,
for_you_for_me_for_evermore, from_this_moment_on, frosty_the_snow_man,
gee_baby_aint_i_good_to_you, getting_to_know_you, god_bless_the_child,
goin_out_of_my_head, gone_with_the_wind, guess_who_i_saw_today, happy_talk,
harlem_nocturne, harolds_house_of_jazz, haunted_heart, hello_dolly,
hello_young_lovers, high_society, hooray_for_love, i_cant_get_started,
i_cover_the_waterfront, i_cried_for_you, i_didnt_know_what_time_it_was,
i_dont_know_why_i_just_do, i_love_lucy, i_love_paris, i_loves_you_porgy,
i_see_your_face_before_me, i_should_care, i_will_wait_for_you,
i_wish_you_love, i_wont_dance, if_ever_i_would_leave_you, if_i_were_a_bell,
ill_always_be_in_love_with_you, ill_be_around, ill_get_by, ill_take_romance,
ill_walk_alone, ill_wind, im_confessin_that_i_love_you, im_glad_there_is_you,
im_gonna_sit_right_down_and_write_myself_a_letter, im_old_fashioned,
in_a_little_spanish_town, in_a_shanty_in_old_shanty_town,
in_the_blue_of_evening, in_the_mood, in_the_still_of_the_night, indiana,
intermission_riff, is_you_is_or_is_you_aint, it_aint_necessarily_so,
its_a_blue_world, its_magic, its_not_for_me_to_say, its_only_a_paper_moon,
its_sand_man, its_the_talk_of_the_town, ive_got_you_under_my_skin,
ive_grown_accustomed_to_her_face, ive_heard_that_song_before, jersey_bounce,
jim, jingle_bell_rock, johnny_one_note, johnnys_theme, johnson_rag,
juke_box_saturday_night, jumpin_with_symphony_sid,
june_is_bustin_out_all_over, june_night, just_in_time, king_porter_stomp,
laugh_clown_laugh, lazy_afternoon, let_it_snow_let_it_snow_let_it_snow,
let_the_good_times_roll, let_there_be_love, let_there_be_you, lets_dance,
lets_fall_in_love, lets_get_away_from_it_all,
life_is_just_a_bowl_of_cherries, linger_awhile, little_girl,
little_girl_blue, lonely_woman, long_ago_and_far_away,
look_for_the_silver_lining, louisiana, love_is_a_simple_thing,
love_walked_in, lullaby_of_the_leaves, lush_life,
mad_about_him_sad_without_him_how_can_i_be_glad_without_him_blues,
mad_about_the_boy, make_someone_happy, malaguena, manhattan, maple_leaf_rag,
margie, memories_of_you, memphis_in_june, merry_christmas_baby,
midnight_blue, milenberg_joys, moon_love, moonglow, moonlight_and_roses,
moonlight_bay, moonlight_cocktail, moonlight_on_the_ganges, more,
more_than_you_know, my_heart_belongs_to_daddy, my_melancholy_baby,
my_monday_date, my_prayer, my_shining_hour, nevertheless_im_in_love_with_you,
new_york_afternoon, no_moon_at_all, none_but_the_lonely_heart,
oh_look_at_me_now, oh_what_a_beautiful_mornin, oh_what_it_seemed_to_be,
oh_you_beautiful_doll, on_a_clear_day_you_can_see_forever,
on_a_little_street_in_singapore, on_a_slow_boat_to_china,
on_the_street_where_you_live, on_the_sunny_side_of_the_street,
once_upon_a_summertime, one_mint_julep, open_country, paper_doll,
peel_me_a_grape, pennies_from_heaven, people, people_will_say_were_in_love,
pick_yourself_up, poinciana, pompton_turnpike, put_on_a_happy_face,
put_your_little_foot_right_out, red_top, river_stay_way_from_my_door,
rock_a_bye_your_baby_with_a_dixie_melody, rockin_chair, rosetta, route_66,
royal_garden_blues, salt_peanuts, samba_de_orfeu, saturday_night_fish_fry,
second_hand_rose, senor_blues, sentimental_journey, sermonette,
shake_rattle_and_roll, shes_funny_that_way, shine, shiny_stockings,
shoo_fly_pie_and_apple_pan_dowdy, side_by_side, skylark, small_world,
smoke_gets_in_your_eyes, smoke_rings, so_nice, solitude,
some_enchanted_evening, some_of_these_days, sometimes_im_happy,
song_of_the_islands, songbird_thank_you_for_your_lovely_song, sonny_boy,
south_of_the_border, spring_can_really_hang_you_up_the_most,
spring_will_be_a_little_late_this_year, squeeze_me, stay_as_sweet_as_you_are,
stompin_at_the_savoy, struttin_with_some_barbeque, sugar, sugar_foot_stomp,
sunny_side_up, sunrise_serenade, sweet_and_lovely, sweet_eloise,
sweet_sue_just_you, swingin_the_blues, swinging_shepherd_blues,
taint_nobodys_biz_ness_if_i_do, taint_what_you_do, thats_entertainment,
thats_life, the_best_is_yet_to_come, the_best_things_in_life_are_free,
the_breeze_and_i, the_christmas_song, the_glory_of_love, the_glow_worm,
the_good_life, the_gypsy, the_jazz_me_blues, the_joint_is_jumpin,
the_lady_is_a_tramp, the_last_time_i_saw_paris, the_man_that_got_away,
the_new_frankie_and_johnnie_song, the_partys_over, the_peacock,
the_peanut_vendor, the_preacher, the_rain_in_spain, the_sheik_of_araby,
the_song_is_you, the_surrey_with_the_fringe_on_top, the_tailgate_ramble,
the_thrill_is_gone, the_touch_of_your_lips,
the_world_is_waiting_for_the_sunrise, there_are_such_things,
there_is_no_greater_love, therell_be_some_changes_made,
theres_a_boat_dats_leavin_soon_for_new_york, theres_a_small_hotel,
these_foolish_things, they_didnt_believe_me, this_love_of_mine, tickle_toe,
tin_roof_blues, tis_autumn, tishomingo_blues, together, too_darn_hot,
travlin_light, tuxedo_junction, twisted, undecided, under_a_blanket_of_blue,
until_the_real_thing_comes_along, van_lingle_mungo, very_early,
violets_for_your_furs, wagon_wheels, wait_till_you_see_her,
walkin_my_baby_back_home, watch_what_happens, way_down_yonder_in_new_orleans,
we_kiss_in_a_shadow, weary_blues, well_you_neednt, west_end_blues,
what_kind_of_fool_am_i, whats_new, when_my_sugar_walks_down_the_street,
when_your_lover_has_gone, where_flamingos_fly, where_is_love, where_or_when,
while_were_young, who, who_can_i_turn_to, why_do_i_love_you,
will_you_still_be_mine, willow_weep_for_me, witchcraft,
with_a_little_bit_of_luck, work_song, wouldnt_it_be_loverly,
wrap_your_troubles_in_dreams, yes_indeed, yesterdays, you_better_go_now,
you_call_it_madness, you_came_a_long_way_from_st_louis, you_made_me_love_you,
you_turned_the_tables_on_me, youd_be_so_nice_to_come_home_to,
youll_never_walk_alone, young_and_foolish, young_at_heart,
younger_than_springtime, youre_my_everything, youre_the_cream_in_my_coffee.

Tunes with a poet but located elsewhere (need another lyric source): all_my_tomorrows (rbk1), april_in_paris (rbk1), besame_mucho, days_of_wine_and_roses, georgia_on_my_mind, in_a_sentimental_mood, invitation, it_dont_mean_a_thing, moon_river, out_of_nowhere, peace, softly_as_in_a_morning_sunrise, sophisticated_lady, star_dust, triste, wave, you_dont_know_what_love_is (hlrjb), i_fall_in_love_too_easily, star_eyes, when_you_wish_upon_a_star (557), my_mans_gone_now (rbk3), someday_youll_be_sorry (dfb), the_more_i_see_you (srb), and without any location: early_autumn, i_got_rhythm, its_all_right_with_me, just_one_of_those_things, laura, love_is_here_to_stay, mack_the_knife, mean_to_me, o_grande_amor, old_devil_moon, pure_imagination, retrato_em_branco_e_preto, september_song, speak_low, strike_up_the_band.
