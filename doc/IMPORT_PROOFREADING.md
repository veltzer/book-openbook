# Imported Tune Proofreading Register

Status recorded on **2026-11-03**. The initial 328 imports were reviewed at
source snapshot `412ab688`; another 200 archive tunes were added on the same day.
Scope: the **528 MusicXML imports** in `src/openbook`, not the rest of the book.
No tune in this register has completed full musical proofreading.

This is a historical record of checks actually performed, not a claim that the
archived music or its copyright statements are authoritative. Recheck an entry
after changing its music. Keep the tune's own `Doc` TODOs until the corresponding
musical review is complete.

## Completed check methods

| Code | Check performed | Limits |
| --- | --- | --- |
| M | Compared the LilyPond melody's written-order pitched-note sequence with that tune's archived MusicXML: note count, note names, octaves, alterations, and metered durations as exact fractions. All 528 tunes matched, totaling 62,967 pitched-note events (36,961 initial and 26,006 new). | Grace-note pitches were included, but their unmetered performance durations were not compared. This did not compare rests, ties, articulation, note onset positions, or the unfolded performance order. Agreement with an import source does not prove that source is musically correct. |
| S | Ran `uv run python -m scripts.check_all --inputs src/openbook/*.ly.tera`. | Source conventions and UUID consistency, not musical correctness. |
| B | Regenerated the integrated book PDF, its index, and embedded bookmarks. | Successful engraving, not a manual inspection of every page or a playback review. |
| A | Checked the corrected altered-dominant chords against the archived `7alt` symbols, verified their actual LilyPond pitch-class sets, and confirmed altered-chord labels in rendered output. | Only the four corrected chords detailed below; other harmonies remain unreviewed. |
| V | Restored the specified repeat endings from the archived MusicXML and checked the unfolded lengths of both melody and chord streams. | Only the corrected volta structures, not D.C./D.S./coda/Fine playback routing. |
| E | Compiled the individual tune's PDF with `scripts.wrapper_lilypond_song`, directly or through rsconstruct. | The five initially corrected tunes and all 200 new tunes; compilation is not full visual proofreading. |
| P | Visually inspected the corrected ending brackets in the individual PDF; also inspected the integrated book page for September in the Rain. | Only the affected ending notation, not every symbol on the page. |
| I | Matched Bouncin' with Bud's source-page reference and printed copyright notice to the scanned page. | Transcription of the notice, not permission to redistribute or a legal determination. |

The full-cohort M comparison used a one-off MusicXML/LilyPond audit, not a
committed regression test. It read each source member identified in the tune's
`Doc` block from the local `real_books_archive.gi/Wikifonia.tar.xz`, extracted
LilyPond `NoteEvent` pitches and durations, and compared the written sequences.
The local archive is not required merely to read this register.

## Corrections and additional checks

| Tune | Correction and evidence |
| --- | --- |
| [Bouncin' with Bud](../src/openbook/bouncin_with_bud.ly.tera) | Restored F7alt at source measure 32 using the book's altered-dominant notation. Corrected the reference to `New Real Book 1.pdf`, PDF page 45 / printed page 37, and transcribed that page's 1947 Embassy Music copyright notice instead of the notice from the previously referenced, unrelated page. |
| [Detour Ahead](../src/openbook/detour_ahead.ly.tera) | Restored B7alt at source measures 11 and 15; verified both altered-dominant pitch-class sets and rendered labels. |
| [Lonnie's Lament](../src/openbook/lonnies_lament.ly.tera) | Restored G7alt at source measure 13; verified the altered-dominant pitch-class set. The archived MusicXML and reference scan use differing chord treatments, so this preserves the imported version rather than claiming the editions agree. |
| [I Wanna Be Loved by You](../src/openbook/i_wanna_be_loved_by_you.ly.tera) | Restored the first ending and the shared second/third ending. Melody and chords each unfold to 24 whole-note units before applying the printed D.C. al Fine instruction. Visually inspected the ending brackets. |
| [September in the Rain](../src/openbook/september_in_the_rain.ly.tera) | Restored the three-pass AABA form with separate first, second, and third endings, instead of two independent repeats. Melody and chords each unfold to 32 whole-note measures plus the quarter-note pickup (`129/4` whole-note units). Visually inspected the ending brackets. |

Measure references here and in the inventory are **one-based written MusicXML
measure positions, including any pickup**, not unfolded performance bar numbers.

## Checks still open for every listed tune

- [ ] Compare the complete melody with an independent historic/authoritative
      edition and check it by ear; the source itself can contain errors.
- [ ] Review all chord roots, qualities, alterations, slash basses, changes,
      durations, and placement. A does not sign off the rest of a tune's chords.
- [ ] Review rests and note onsets, ties/slurs, tuplets, grace-note placement,
      pickups, bar lengths, key signatures, and meter changes in context.
- [ ] Trace the complete performance form, including repeats, endings,
      D.C./D.S., segno, coda, and Fine; check actual playback where applicable.
- [ ] Verify tempo and stylistic instructions against an appropriate reference.
- [ ] Inspect the entire individual score and book page for readability,
      accidental placement, collisions, line breaks, and page turns.
- [ ] Review source attribution, copyright notices, edition differences, and
      applicable reuse terms. I verifies one printed notice, not reuse rights.

These pending checks apply to **every inventory row**, including the five
initially corrected tunes and all 200 new tunes. A, V, P, and I record narrowly scoped work; they do not close a
whole-tune review item.

## New 200-tune batch

The new batch uses notation from the local Wikifonia archive and references
tunes in the local real/fake-book PDF indexes, including the Real Books,
Standards Real Book, Firehouse Jazz Band, 557 Standards, and The Book.
It is not restricted to public-domain compositions. Source rights notices
are retained, lyrics are omitted, and no redistribution permission is asserted.
Book-index page numbers are not claimed to be verified PDF page numbers.
Each new entry has M, S, B, and E complete; full musical proofreading remains open.

## Tune inventory

Every tune below has completed M, S, and B. Extra codes identify additional
completed work. A dash in the last column means no *additional* specific flag was
recorded; it does not mean the tune is approved or has no outstanding checks.

Additional pending-review labels:

- **Spacing**: existing tune TODO; successive source chord symbols share an
  offset, so their editorial spacing must be checked at the listed measures.
  There are 174 tunes with this flag.
- **Notice**: the per-tune notice still needs comparison with the referenced
  scan. For the initial imports, a readable scan notice was not recovered;
  for the new batch, the archived MusicXML notice was retained without a scan
  comparison. There are 331 tunes with this flag.
- **Page**: the local PDF edition and exact page have not been verified;
  only the book-index reference is recorded. All 200 new tunes have this flag.
- **Route**: source navigation markers warrant a complete performance-order
  review. Listed markers are review prompts, not confirmed defects.
- **Endings**: unusual/unlabeled source ending markers need comparison with a
  scan, including confirmation of any normalization already made during import.

<!-- tune-inventory -->

| Tune | Batch | Completed checks | Additional pending review |
| --- | --- | --- | --- |
| ['S Wonderful](../src/openbook/s_wonderful.ly.tera) | Initial 328 | M, S, B | Spacing: 7, 20, 28 |
| [502 Blues](../src/openbook/502_blues.ly.tera) | Initial 328 | M, S, B | Notice |
| [A House Is Not A Home](../src/openbook/a_house_is_not_a_home.ly.tera) | New 200 | M, S, B, E | Spacing: 34; Notice; Page |
| [A Song For You](../src/openbook/a_song_for_you.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [A Time For Love](../src/openbook/a_time_for_love.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 16, 24 |
| [Ach, Du Lieber Augustin](../src/openbook/ach_du_lieber_augustin.ly.tera) | Initial 328 | M, S, B | - |
| [After the Ball](../src/openbook/after_the_ball.ly.tera) | Initial 328 | M, S, B | - |
| [After The Lovin'](../src/openbook/after_the_lovin.ly.tera) | New 200 | M, S, B, E | Spacing: 17, 21; Notice; Page |
| [Again](../src/openbook/again.ly.tera) | New 200 | M, S, B, E | Spacing: 17, 32, 34, 35; Notice; Page |
| [Ah! Sweet Mystery of Life](../src/openbook/ah_sweet_mystery_of_life.ly.tera) | Initial 328 | M, S, B | - |
| [Ain't She Sweet](../src/openbook/aint_she_sweet.ly.tera) | Initial 328 | M, S, B | - |
| [AL DI LA](../src/openbook/al_di_la.ly.tera) | New 200 | M, S, B, E | Spacing: 32; Notice; Page |
| [Alabama  Jubilee](../src/openbook/alabama_jubilee.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Alabamy Bound](../src/openbook/alabamy_bound.ly.tera) | Initial 328 | M, S, B | - |
| [Alexander's Ragtime Band](../src/openbook/alexanders_ragtime_band.ly.tera) | Initial 328 | M, S, B | - |
| [Alfie](../src/openbook/alfie.ly.tera) | Initial 328 | M, S, B | Notice; Endings: 40, 41 |
| [Alice Blue Gown](../src/openbook/alice_blue_gown.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [All Alone](../src/openbook/all_alone.ly.tera) | Initial 328 | M, S, B | Spacing: 32 |
| [All My Loving](../src/openbook/all_my_loving.ly.tera) | New 200 | M, S, B, E | Notice; Page; Route: to coda at 25, coda at 27 |
| [All The Way](../src/openbook/all_the_way.ly.tera) | New 200 | M, S, B, E | Spacing: 8, 12, 16, 24, 28, 31, 32; Notice; Page |
| [All Through The Night](../src/openbook/all_through_the_night.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Almost Like Being in Love](../src/openbook/almost_like_being_in_love.ly.tera) | Initial 328 | M, S, B | Spacing: 37 |
| [Always And Forever](../src/openbook/always_and_forever.ly.tera) | New 200 | M, S, B, E | Notice; Page; Route: segno at 9, to coda at 16, D.S. at 27, coda at 28 |
| [Am I Blue?](../src/openbook/am_i_blue.ly.tera) | Initial 328 | M, S, B | Spacing: 16 |
| [American Patrol](../src/openbook/american_patrol.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [AMOR](../src/openbook/amor.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [And I Love Her](../src/openbook/and_i_love_her.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [And The Angels Sing](../src/openbook/and_the_angels_sing.ly.tera) | New 200 | M, S, B, E | Spacing: 16, 32, 44, 48, 50; Notice; Page |
| [Angels We Have Heard on High](../src/openbook/angels_we_have_heard_on_high.ly.tera) | Initial 328 | M, S, B | - |
| [Angry](../src/openbook/angry.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Any Time](../src/openbook/any_time.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Anything Goes](../src/openbook/anything_goes.ly.tera) | New 200 | M, S, B, E | Spacing: 6, 8, 14, 30, 32; Notice; Page |
| [April Showers](../src/openbook/april_showers.ly.tera) | New 200 | M, S, B, E | Spacing: 47; Notice; Page |
| [Aquarius](../src/openbook/aquarius.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Around The World](../src/openbook/around_the_world.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [As Long As He Needs Me](../src/openbook/as_long_as_he_needs_me.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Ask Me Now](../src/openbook/ask_me_now.ly.tera) | Initial 328 | M, S, B | Notice |
| [At A Georgia Camp Meeting](../src/openbook/at_a_georgia_camp_meeting.ly.tera) | New 200 | M, S, B, E | Notice; Page; Route: segno at 22, Fine at 38, D.S. at 55 |
| [At Last](../src/openbook/at_last.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 18, 20, 24, 26, 28, 32, 42, 44, 48; Route: segno at 18, Fine at 48, D.S. at 49 |
| [At Long Last Love](../src/openbook/at_long_last_love.ly.tera) | New 200 | M, S, B, E | Spacing: 4, 16; Notice; Page |
| [At Sundown](../src/openbook/at_sundown.ly.tera) | Initial 328 | M, S, B | Spacing: 9, 25 |
| [Auld Lang Syne](../src/openbook/auld_lang_syne.ly.tera) | Initial 328 | M, S, B | - |
| [Autumn Nocturne](../src/openbook/autumn_nocturne.ly.tera) | Initial 328 | M, S, B | Notice |
| [Avalon](../src/openbook/avalon.ly.tera) | Initial 328 | M, S, B | - |
| [Ba-Lue Bolivar Ba-Lues Are](../src/openbook/ba_lue_bolivar_ba_lues_are.ly.tera) | Initial 328 | M, S, B | Notice |
| [Baby Face](../src/openbook/baby_face.ly.tera) | Initial 328 | M, S, B | Spacing: 31 |
| [Baby It's Cold Outside](../src/openbook/baby_its_cold_outside.ly.tera) | Initial 328 | M, S, B | - |
| [Back In Your Own Backyard](../src/openbook/back_in_your_own_backyard.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Ballad for Trane](../src/openbook/ballad_for_trane.ly.tera) | Initial 328 | M, S, B | Notice |
| [Baltimore Oriole](../src/openbook/baltimore_oriole.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Baubles, Bangles and Beads](../src/openbook/baubles_bangles_and_beads.ly.tera) | Initial 328 | M, S, B | Notice |
| [Be My Love](../src/openbook/be_my_love.ly.tera) | Initial 328 | M, S, B | Notice |
| [Beautiful Dreamer](../src/openbook/beautiful_dreamer.ly.tera) | Initial 328 | M, S, B | Route: D.C. at 27, coda at 28 |
| [Beer Barrel Polka](../src/openbook/beer_barrel_polka.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Begin The Beguine](../src/openbook/begin_the_beguine.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Bemsha Swing](../src/openbook/bemsha_swing.ly.tera) | Initial 328 | M, S, B | Notice |
| [Between The Devil And The Deep Blue Sea](../src/openbook/between_the_devil_and_the_deep_blue_sea.ly.tera) | Initial 328 | M, S, B | Spacing: 16, 24; Notice |
| [Bidin' My Time](../src/openbook/bidin_my_time.ly.tera) | Initial 328 | M, S, B | - |
| [Bird Food](../src/openbook/bird_food.ly.tera) | Initial 328 | M, S, B | Route: to coda at 32, coda at 35 |
| [Birk's Works](../src/openbook/birks_works.ly.tera) | Initial 328 | M, S, B | Notice |
| [Black and Blue](../src/openbook/black_and_blue.ly.tera) | Initial 328 | M, S, B | - |
| [Black And Tan Fantasy](../src/openbook/black_and_tan_fantasy.ly.tera) | Initial 328 | M, S, B | Notice |
| [Black Coffee](../src/openbook/black_coffee.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 9, 12, 20, 24, 40, 44; Notice |
| [Blame It On My Youth](../src/openbook/blame_it_on_my_youth.ly.tera) | Initial 328 | M, S, B | Spacing: 4, 8, 12, 20, 24, 28, 32 |
| [Blue Gardenia](../src/openbook/blue_gardenia.ly.tera) | Initial 328 | M, S, B | Notice |
| [Blue Moon](../src/openbook/blue_moon.ly.tera) | Initial 328 | M, S, B | - |
| [Blue Prelude](../src/openbook/blue_prelude.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Bluebird](../src/openbook/bluebird.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Blues By Five](../src/openbook/blues_by_five.ly.tera) | Initial 328 | M, S, B | Notice |
| [Blues My Naughty Sweetie Gives to Me](../src/openbook/blues_my_naughty_sweetie_gives_to_me.ly.tera) | Initial 328 | M, S, B | - |
| [Bohemia After Dark](../src/openbook/bohemia_after_dark.ly.tera) | Initial 328 | M, S, B | Spacing: 17; Notice; Route: D.C. at 21, Fine at 22 |
| [Bouncin' with Bud](../src/openbook/bouncin_with_bud.ly.tera) | Initial 328 | M, S, B, A, E, I | - |
| [Bourbon Street Parade](../src/openbook/bourbon_street_parade.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Brazil](../src/openbook/brazil.ly.tera) | New 200 | M, S, B, E | Spacing: 2, 3, 6, 7, 10, 11, 14, 48, 50, 52, 54, 56, 57, 58, 60; Notice; Page |
| [Brilliant Corners](../src/openbook/brilliant_corners.ly.tera) | Initial 328 | M, S, B | Notice |
| [Broadway](../src/openbook/broadway.ly.tera) | Initial 328 | M, S, B | Notice |
| [burgundystreet blues](../src/openbook/burgundystreet_blues.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Buster Rides Again](../src/openbook/buster_rides_again.ly.tera) | Initial 328 | M, S, B | Notice |
| [By Myself](../src/openbook/by_myself.ly.tera) | Initial 328 | M, S, B | Notice |
| [Bye Bye Baby](../src/openbook/bye_bye_baby.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 10, 15, 24, 26, 34; Notice |
| [C'est Magnifique](../src/openbook/cest_magnifique.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [C-Jam Blues](../src/openbook/c_jam_blues.ly.tera) | Initial 328 | M, S, B | Notice |
| [Can't Smile Without You](../src/openbook/cant_smile_without_you.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Can't We Be Friends?](../src/openbook/cant_we_be_friends.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 16, 23, 24, 32, 33; Notice |
| [Can't We Talk It Over](../src/openbook/cant_we_talk_it_over.ly.tera) | Initial 328 | M, S, B | Notice |
| [Careless Love](../src/openbook/careless_love.ly.tera) | Initial 328 | M, S, B | - |
| [Chameleon](../src/openbook/chameleon.ly.tera) | Initial 328 | M, S, B | Notice |
| [Charade](../src/openbook/charade.ly.tera) | Initial 328 | M, S, B | - |
| [Chattanooga Choo-Choo](../src/openbook/chattanooga_choo_choo.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Chicago](../src/openbook/chicago.ly.tera) | Initial 328 | M, S, B | - |
| [China Boy](../src/openbook/china_boy.ly.tera) | Initial 328 | M, S, B | - |
| [Chinatown, My Chinatown](../src/openbook/chinatown_my_chinatown.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Chloe](../src/openbook/chloe.ly.tera) | Initial 328 | M, S, B | Spacing: 10 |
| [Choucoune](../src/openbook/choucoune.ly.tera) | Initial 328 | M, S, B | - |
| [Ciao, ciao, bambino](../src/openbook/ciao_ciao_bambino.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Ciribiribin](../src/openbook/ciribiribin.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Clarinet polka](../src/openbook/clarinet_polka.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Close Enough For Love](../src/openbook/close_enough_for_love.ly.tera) | Initial 328 | M, S, B | Spacing: 11, 12 |
| [Close to You](../src/openbook/close_to_you.ly.tera) | New 200 | M, S, B, E | Spacing: 2, 18, 32; Notice; Page |
| [Cold Duck Time](../src/openbook/cold_duck_time.ly.tera) | Initial 328 | M, S, B | Notice |
| [Colonel Bogey](../src/openbook/colonel_bogey.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Colour My World](../src/openbook/colour_my_world.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Come Closer To Me](../src/openbook/come_closer_to_me.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Come Fly With Me](../src/openbook/come_fly_with_me.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Cool Blues](../src/openbook/cool_blues.ly.tera) | Initial 328 | M, S, B | Notice |
| [Coquette](../src/openbook/coquette.ly.tera) | Initial 328 | M, S, B | - |
| [Crazy He Calls Me](../src/openbook/crazy_he_calls_me.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Cuando Calienta el Sol](../src/openbook/cuando_calienta_el_sol.ly.tera) | New 200 | M, S, B, E | Spacing: 7, 8; Notice; Page |
| [Daisy Bell](../src/openbook/daisy_bell.ly.tera) | Initial 328 | M, S, B | - |
| [Dancing In The Dark](../src/openbook/dancing_in_the_dark.ly.tera) | New 200 | M, S, B, E | Spacing: 31; Notice; Page |
| [Danny Boy](../src/openbook/danny_boy.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Dardanella](../src/openbook/dardanella.ly.tera) | Initial 328 | M, S, B | - |
| [Dark Eyes](../src/openbook/dark_eyes.ly.tera) | Initial 328 | M, S, B | - |
| [Darktown Strutters' Ball](../src/openbook/darktown_strutters_ball.ly.tera) | Initial 328 | M, S, B | - |
| [Day by Day](../src/openbook/day_by_day.ly.tera) | Initial 328 | M, S, B | Notice |
| [Day Dream](../src/openbook/day_dream.ly.tera) | Initial 328 | M, S, B | - |
| [Day in, Day out](../src/openbook/day_in_day_out.ly.tera) | Initial 328 | M, S, B | Notice |
| [Deck the Halls](../src/openbook/deck_the_halls.ly.tera) | Initial 328 | M, S, B | - |
| [Dedicated To You](../src/openbook/dedicated_to_you.ly.tera) | New 200 | M, S, B, E | Spacing: 6, 14, 16, 20, 32; Notice; Page |
| [Deep Purple](../src/openbook/deep_purple.ly.tera) | Initial 328 | M, S, B | - |
| [Detour Ahead](../src/openbook/detour_ahead.ly.tera) | Initial 328 | M, S, B, A, E | Notice |
| [Diane](../src/openbook/diane.ly.tera) | Initial 328 | M, S, B | - |
| [Didn't We](../src/openbook/didnt_we.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Dig](../src/openbook/dig.ly.tera) | Initial 328 | M, S, B | Notice; Route: to coda at 30, coda at 33 |
| [Dippermouth Blues](../src/openbook/dippermouth_blues.ly.tera) | Initial 328 | M, S, B | - |
| [Dixie](../src/openbook/dixie.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Do-Re-Mi](../src/openbook/do_re_mi.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Don't Be That Way](../src/openbook/dont_be_that_way.ly.tera) | Initial 328 | M, S, B | Spacing: 2, 4, 6, 8, 10, 12, 14, 16, 26, 28, 30, 32 |
| [Don't Bring Lulu](../src/openbook/dont_bring_lulu.ly.tera) | Initial 328 | M, S, B | - |
| [Don't Go To Strangers](../src/openbook/dont_go_to_strangers.ly.tera) | Initial 328 | M, S, B | Spacing: 7, 15, 31; Notice |
| [Don't Worry 'Bout Me](../src/openbook/dont_worry_bout_me.ly.tera) | New 200 | M, S, B, E | Spacing: 34, 35; Notice; Page |
| [Doodle-Doo-Doo](../src/openbook/doodle_doo_doo.ly.tera) | Initial 328 | M, S, B | - |
| [Down Among The Sheltering Palms](../src/openbook/down_among_the_sheltering_palms.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Dream a Little Dream of Me](../src/openbook/dream_a_little_dream_of_me.ly.tera) | Initial 328 | M, S, B | - |
| [Dream Dancing](../src/openbook/dream_dancing.ly.tera) | Initial 328 | M, S, B | Spacing: 52; Notice |
| [Dreamsville](../src/openbook/dreamsville.ly.tera) | New 200 | M, S, B, E | Spacing: 6, 14, 30; Notice; Page |
| [Drink to Me Only with Thine Eyes](../src/openbook/drink_to_me_only_with_thine_eyes.ly.tera) | Initial 328 | M, S, B | - |
| [Easy Street](../src/openbook/easy_street.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Edelweiss](../src/openbook/edelweiss.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Eight Days A Week](../src/openbook/eight_days_a_week.ly.tera) | New 200 | M, S, B, E | Notice; Page; Route: to coda at 16, D.S. at 25, coda at 26 |
| [El Choclo](../src/openbook/el_choclo.ly.tera) | Initial 328 | M, S, B | Endings: 25, 34 |
| [El Relicario](../src/openbook/el_relicario.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Elvira](../src/openbook/elvira.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Embraceable You](../src/openbook/embraceable_you.ly.tera) | Initial 328 | M, S, B | Spacing: 4, 12, 16, 20, 24, 31, 32 |
| [Emily](../src/openbook/emily.ly.tera) | Initial 328 | M, S, B | - |
| [Endless Love](../src/openbook/endless_love.ly.tera) | New 200 | M, S, B, E | Notice; Page; Route: to coda at 22, D.S. at 38, coda at 39 |
| [Estate](../src/openbook/estate.ly.tera) | Initial 328 | M, S, B | Notice |
| [Evergreen](../src/openbook/evergreen.ly.tera) | New 200 | M, S, B, E | Spacing: 44; Notice; Page |
| [Everything I Have Is Yours](../src/openbook/everything_i_have_is_yours.ly.tera) | Initial 328 | M, S, B | Spacing: 16 |
| [Exodus](../src/openbook/exodus.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Fascinating Rhythm](../src/openbook/fascinating_rhythm.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 24 |
| [Fascination](../src/openbook/fascination.ly.tera) | New 200 | M, S, B, E | Spacing: 8, 24; Notice; Page |
| [Feel Like Makin' Love](../src/openbook/feel_like_makin_love.ly.tera) | Initial 328 | M, S, B | - |
| [Feelings](../src/openbook/feelings.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Fine And Dandy](../src/openbook/fine_and_dandy.ly.tera) | New 200 | M, S, B, E | Spacing: 32, 33; Notice; Page |
| [Five Foot Two, Eyes of Blue](../src/openbook/five_foot_two_eyes_of_blue.ly.tera) | Initial 328 | M, S, B | - |
| [Fools rush in](../src/openbook/fools_rush_in.ly.tera) | Initial 328 | M, S, B | Notice |
| [For Heaven's Sake](../src/openbook/for_heavens_sake.ly.tera) | Initial 328 | M, S, B | Spacing: 21; Notice |
| [For The Good Times](../src/openbook/for_the_good_times.ly.tera) | New 200 | M, S, B, E | Spacing: 34; Notice; Page |
| [Four on Six](../src/openbook/four_on_six.ly.tera) | Initial 328 | M, S, B | Notice |
| [Frenesi](../src/openbook/frenesi.ly.tera) | New 200 | M, S, B, E | Spacing: 32; Notice; Page |
| [Full Moon And Empty Arms](../src/openbook/full_moon_and_empty_arms.ly.tera) | Initial 328 | M, S, B | Spacing: 3, 7, 13, 19, 23, 31; Notice |
| [Fun To Be Fooled](../src/openbook/fun_to_be_fooled.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Get Happy](../src/openbook/get_happy.ly.tera) | Initial 328 | M, S, B | Spacing: 33 |
| [Give Me the Simple Life](../src/openbook/give_me_the_simple_life.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [God Rest Ye Merry, Gentlemen](../src/openbook/god_rest_ye_merry_gentlemen.ly.tera) | Initial 328 | M, S, B | - |
| [Golliwog's Cakewalk](../src/openbook/golliwog_s_cakewalk.ly.tera) | Initial 328 | M, S, B | - |
| [Good Morning Heartache](../src/openbook/good_morning_heartache.ly.tera) | Initial 328 | M, S, B | Spacing: 8 |
| [Goodbye](../src/openbook/goodbye.ly.tera) | Initial 328 | M, S, B | Spacing: 18; Notice |
| [Green Eyes](../src/openbook/green_eyes.ly.tera) | New 200 | M, S, B, E | Spacing: 24, 32; Notice; Page |
| [Groove Merchant](../src/openbook/groove_merchant.ly.tera) | Initial 328 | M, S, B | Notice |
| [Guantanamera](../src/openbook/guantanamera.ly.tera) | New 200 | M, S, B, E | Spacing: 4, 21; Notice; Page; Route: to coda at 7, coda at 21 |
| [Happiness Is A Thing Called Joe](../src/openbook/happiness_is_a_thing_called_joe.ly.tera) | New 200 | M, S, B, E | Spacing: 17; Notice; Page |
| [Happy Days Are Here Again](../src/openbook/happy_days_are_here_again.ly.tera) | Initial 328 | M, S, B | Route: segno at 3, Fine at 19 |
| [Hard Times Come Again No More](../src/openbook/hard_times_come_again_no_more.ly.tera) | Initial 328 | M, S, B | - |
| [Haunted Ballroom](../src/openbook/haunted_ballroom.ly.tera) | Initial 328 | M, S, B | Notice; Route: Fine at 8, D.C. at 24 |
| [He Was Too Good To Me](../src/openbook/he_was_too_good_to_me.ly.tera) | Initial 328 | M, S, B | Spacing: 6, 16, 20, 23, 25, 27, 32, 36, 39, 40, 45; Notice |
| [Heat Wave](../src/openbook/heat_wave.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Hello! Ma Baby](../src/openbook/hello_ma_baby.ly.tera) | Initial 328 | M, S, B | - |
| [Hey there](../src/openbook/hey_there.ly.tera) | Initial 328 | M, S, B | Route: to coda at 5, coda at 17 |
| [Hey, Look Me Over](../src/openbook/hey_look_me_over.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Hindustan](../src/openbook/hindustan.ly.tera) | Initial 328 | M, S, B | - |
| [Home](../src/openbook/home.ly.tera) | New 200 | M, S, B, E | Spacing: 1, 2, 3, 4, 30, 31, 32; Notice; Page; Route: segno at 13, to coda at 21, D.S. at 33, coda at 34 |
| [House of Jade](../src/openbook/house_of_jade.ly.tera) | Initial 328 | M, S, B | Notice |
| [How About You](../src/openbook/how_about_you.ly.tera) | Initial 328 | M, S, B | Notice; Endings: 50 |
| [How Come You Do Me Like You Do?](../src/openbook/how_come_you_do_me_like_you_do.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [How Do You Keep The Music Playing](../src/openbook/how_do_you_keep_the_music_playing.ly.tera) | New 200 | M, S, B, E | Spacing: 16; Notice; Page |
| [How Long Has This Been Going On?](../src/openbook/how_long_has_this_been_going_on.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 10, 14, 18 |
| [I Ain't Gonna Give Nobody None Of My Jelly Roll](../src/openbook/i_aint_gonna_give_nobody_none_of_my_jelly_roll.ly.tera) | Initial 328 | M, S, B | - |
| [I Apologise](../src/openbook/i_apologise.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [I Can't Believe That You're in Love with Me](../src/openbook/i_cant_believe_that_youre_in_love_with_me.ly.tera) | Initial 328 | M, S, B | - |
| [I Can't Help It](../src/openbook/i_cant_help_it.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [I Didn't Know About You](../src/openbook/i_didnt_know_about_you.ly.tera) | Initial 328 | M, S, B | Spacing: 7, 15, 16 |
| [I Double Dare You](../src/openbook/i_double_dare_you.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [I Get A Kick Out Of You](../src/openbook/i_get_a_kick_out_of_you.ly.tera) | Initial 328 | M, S, B | Spacing: 4, 15, 20, 27, 52; Notice |
| [I Get Along Without You Very Well](../src/openbook/i_get_along_without_you_very_well.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [I Guess I'll Have To Change My Plan](../src/openbook/i_guess_ill_have_to_change_my_plan.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [I Had The Craziest Dream](../src/openbook/i_had_the_craziest_dream.ly.tera) | New 200 | M, S, B, E | Spacing: 25; Notice; Page |
| [I Hadn't Anyone Till You](../src/openbook/i_hadnt_anyone_till_you.ly.tera) | Initial 328 | M, S, B | - |
| [I Hear a Rhapsody](../src/openbook/i_hear_a_rhapsody.ly.tera) | Initial 328 | M, S, B | Spacing: 21 |
| [I Hear Music](../src/openbook/i_hear_music.ly.tera) | Initial 328 | M, S, B | Notice |
| [I Know That You Know](../src/openbook/i_know_that_you_know.ly.tera) | Initial 328 | M, S, B | - |
| [I may be wrong](../src/openbook/i_may_be_wrong.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [I Only Have Eyes For You](../src/openbook/i_only_have_eyes_for_you.ly.tera) | Initial 328 | M, S, B | Spacing: 4, 8, 53; Notice |
| [I Remember You](../src/openbook/i_remember_you.ly.tera) | Initial 328 | M, S, B | Spacing: 23, 35, 36, 37, 38; Notice |
| [I Surrender, Dear](../src/openbook/i_surrender_dear.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 20, 24, 32; Notice |
| [I Thought About You](../src/openbook/i_thought_about_you.ly.tera) | Initial 328 | M, S, B | Spacing: 8; Notice |
| [I Wanna Be Loved by You](../src/openbook/i_wanna_be_loved_by_you.ly.tera) | Initial 328 | M, S, B, V, E, P | Route: Fine at 9, D.C. at 18 |
| [I Want A Little Girl](../src/openbook/i_want_a_little_girl.ly.tera) | Initial 328 | M, S, B | Notice |
| [I Want to Be Happy](../src/openbook/i_want_to_be_happy.ly.tera) | Initial 328 | M, S, B | Spacing: 23, 24, 31, 32 |
| [I Was Doing All Right](../src/openbook/i_was_doing_all_right.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [I Wish I Knew](../src/openbook/i_wish_i_knew.ly.tera) | New 200 | M, S, B, E | Spacing: 40; Notice; Page |
| [I Wish I Were In Love Again](../src/openbook/i_wish_i_were_in_love_again.ly.tera) | New 200 | M, S, B, E | Spacing: 17; Notice; Page |
| [I Wished On The Moon](../src/openbook/i_wished_on_the_moon.ly.tera) | New 200 | M, S, B, E | Spacing: 5, 21; Notice; Page |
| [I Wonder Where My Baby Is Tonight](../src/openbook/i_wonder_where_my_baby_is_tonight.ly.tera) | Initial 328 | M, S, B | - |
| [I'll Never Stop Loving You](../src/openbook/ill_never_stop_loving_you.ly.tera) | New 200 | M, S, B, E | Spacing: 5, 6, 24; Notice; Page |
| [I'll See You In My Dreams](../src/openbook/ill_see_you_in_my_dreams.ly.tera) | Initial 328 | M, S, B | - |
| [I'm A Fool To Want You](../src/openbook/im_a_fool_to_want_you.ly.tera) | Initial 328 | M, S, B | Spacing: 16; Notice |
| [I'm All Smiles](../src/openbook/im_all_smiles.ly.tera) | Initial 328 | M, S, B | - |
| [I'm an Old Cowhand](../src/openbook/im_an_old_cowhand.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [I'm confessin'](../src/openbook/im_confessin.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [I'm Getting Sentimental Over You](../src/openbook/im_getting_sentimental_over_you.ly.tera) | Initial 328 | M, S, B | - |
| [I'm In the Mood for Love](../src/openbook/im_in_the_mood_for_love.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 18, 24; Notice |
| [I'm Just A Lucky So And So](../src/openbook/im_just_a_lucky_so_and_so.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [I'm Through With Love](../src/openbook/im_through_with_love.ly.tera) | Initial 328 | M, S, B | Spacing: 9, 17 |
| [I've Found a New Baby](../src/openbook/ive_found_a_new_baby.ly.tera) | Initial 328 | M, S, B | - |
| [I've Got A Crush On You](../src/openbook/ive_got_a_crush_on_you.ly.tera) | Initial 328 | M, S, B | Spacing: 9, 18, 19 |
| [I've Got The World On  A String](../src/openbook/ive_got_the_world_on_a_string.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 16; Notice |
| [I've Never Been In Love Before](../src/openbook/ive_never_been_in_love_before.ly.tera) | Initial 328 | M, S, B | Spacing: 2, 3, 8, 9, 10, 18, 20, 21, 25, 26, 27; Notice |
| [I've Told Ev'ry Little Star](../src/openbook/ive_told_evry_little_star.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Ida (Sweet As Apple Cider)](../src/openbook/ida_sweet_as_apple_cider.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [If I Could Be With You (One Hour Tonight)](../src/openbook/if_i_could_be_with_you_one_hour_tonight.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [If I Had You](../src/openbook/if_i_had_you.ly.tera) | Initial 328 | M, S, B | Spacing: 7, 8, 16, 24, 31, 33 |
| [If I Love Again](../src/openbook/if_i_love_again.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [If I Loved You](../src/openbook/if_i_loved_you.ly.tera) | Initial 328 | M, S, B | Notice |
| [If I Should Lose You](../src/openbook/if_i_should_lose_you.ly.tera) | Initial 328 | M, S, B | Spacing: 16, 32; Notice |
| [If You Never Come To Me](../src/openbook/if_you_never_come_to_me.ly.tera) | Initial 328 | M, S, B | Notice |
| [If You Were The Only Girl In The World](../src/openbook/if_you_were_the_only_girl_in_the_world.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [In A Mellow Tone](../src/openbook/in_a_mellow_tone.ly.tera) | Initial 328 | M, S, B | - |
| [In Love in Vain](../src/openbook/in_love_in_vain.ly.tera) | Initial 328 | M, S, B | Notice |
| [In the Chapel In The Moonlight](../src/openbook/in_the_chapel_in_the_moonlight.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [In the Wee Small Hours of the Morning](../src/openbook/in_the_wee_small_hours_of_the_morning.ly.tera) | Initial 328 | M, S, B | Spacing: 9, 13, 15 |
| [Indian Love Call](../src/openbook/indian_love_call.ly.tera) | Initial 328 | M, S, B | - |
| [Indian Summer](../src/openbook/indian_summer.ly.tera) | Initial 328 | M, S, B | Notice |
| [Interplay](../src/openbook/interplay.ly.tera) | Initial 328 | M, S, B | Notice |
| [Is It True What They Say About Dixie](../src/openbook/is_it_true_what_they_say_about_dixie.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Isfahan](../src/openbook/isfahan.ly.tera) | Initial 328 | M, S, B | Notice |
| [Isle Of Capri](../src/openbook/isle_of_capri.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Isn't It A Pity](../src/openbook/isnt_it_a_pity.ly.tera) | New 200 | M, S, B, E | Spacing: 4, 6, 12, 30, 47, 48; Notice; Page |
| [Israel](../src/openbook/israel.ly.tera) | Initial 328 | M, S, B | Notice |
| [It Could Happen To You](../src/openbook/it_could_happen_to_you.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 12, 24, 28, 31, 33; Notice |
| [It Had To Be You](../src/openbook/it_had_to_be_you.ly.tera) | Initial 328 | M, S, B | Spacing: 2, 4, 8, 12, 18, 20, 24, 32, 34 |
| [It Was A Very Good Year](../src/openbook/it_was_a_very_good_year.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [It's Always You](../src/openbook/its_always_you.ly.tera) | New 200 | M, S, B, E | Spacing: 5, 13, 29; Notice; Page |
| [It's De-lovely](../src/openbook/its_de_lovely.ly.tera) | Initial 328 | M, S, B | - |
| [It's You Or No One](../src/openbook/its_you_or_no_one.ly.tera) | Initial 328 | M, S, B | Spacing: 31; Notice |
| [Ja-Da](../src/openbook/ja_da.ly.tera) | Initial 328 | M, S, B | Spacing: 4, 8, 16 |
| [Jazz Baby](../src/openbook/jazz_baby.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Jeanie with the Light Brown Hair](../src/openbook/jeanie_with_the_light_brown_hair.ly.tera) | Initial 328 | M, S, B | - |
| [Jeepers Creepers](../src/openbook/jeepers_creepers.ly.tera) | Initial 328 | M, S, B | Notice |
| [Jelly Roll](../src/openbook/jelly_roll.ly.tera) | Initial 328 | M, S, B | Notice |
| [Jive Samba](../src/openbook/jive_samba.ly.tera) | Initial 328 | M, S, B | Notice; Route: segno at 5, coda at 21, D.S. at 21, coda at 22 |
| [Joy Spring](../src/openbook/joy_spring.ly.tera) | Initial 328 | M, S, B | Notice |
| [Joy To The World](../src/openbook/joy_to_the_world.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Jump Monk](../src/openbook/jump_monk.ly.tera) | Initial 328 | M, S, B | Notice |
| [Just A Gigolo](../src/openbook/just_a_gigolo.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Just Squeeze Me](../src/openbook/just_squeeze_me.ly.tera) | Initial 328 | M, S, B | - |
| [Just You, Just Me](../src/openbook/just_you_just_me.ly.tera) | Initial 328 | M, S, B | Spacing: 18 |
| [La Comparsa](../src/openbook/la_comparsa.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Lady Sings The Blues](../src/openbook/lady_sings_the_blues.ly.tera) | New 200 | M, S, B, E | Spacing: 32; Notice; Page |
| [Lazybones](../src/openbook/lazybones.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Le Temps des Cerises](../src/openbook/le_temps_des_cerises.ly.tera) | Initial 328 | M, S, B | - |
| [Lester Leaps In](../src/openbook/lester_leaps_in.ly.tera) | Initial 328 | M, S, B | Notice |
| [Let's Do It (Let's Fall in Love)](../src/openbook/lets_do_it_lets_fall_in_love.ly.tera) | Initial 328 | M, S, B | - |
| [Like A Lover](../src/openbook/like_a_lover.ly.tera) | Initial 328 | M, S, B | Notice |
| [Limehouse Blues](../src/openbook/limehouse_blues.ly.tera) | Initial 328 | M, S, B | - |
| [Little B's Poem](../src/openbook/little_bs_poem.ly.tera) | Initial 328 | M, S, B | Notice |
| [Little Rootie Tootie](../src/openbook/little_rootie_tootie.ly.tera) | Initial 328 | M, S, B | Notice |
| [Little White Lies](../src/openbook/little_white_lies.ly.tera) | Initial 328 | M, S, B | Spacing: 33 |
| [Liza (All the Clouds'll Roll Away)](../src/openbook/liza_all_the_cloudsll_roll_away.ly.tera) | Initial 328 | M, S, B | Spacing: 15, 16, 18, 22, 26, 30, 34, 35, 38, 39, 46, 50 |
| [Lonnie's Lament](../src/openbook/lonnies_lament.ly.tera) | Initial 328 | M, S, B, A, E | Notice |
| [Lost](../src/openbook/lost.ly.tera) | New 200 | M, S, B, E | Notice; Page; Route: segno at 17, to coda at 24, D.S. at 39, coda at 40 |
| [Louise](../src/openbook/louise.ly.tera) | Initial 328 | M, S, B | Spacing: 16 |
| [Love Is A Many Splendored Thing](../src/openbook/love_is_a_many_splendored_thing.ly.tera) | Initial 328 | M, S, B | - |
| [Love Is Just Around The Corner](../src/openbook/love_is_just_around_the_corner.ly.tera) | Initial 328 | M, S, B | Spacing: 6, 14, 32; Notice |
| [Love Letters](../src/openbook/love_letters.ly.tera) | New 200 | M, S, B, E | Spacing: 12, 16, 24, 31; Notice; Page |
| [Love Me Or Leave Me](../src/openbook/love_me_or_leave_me.ly.tera) | Initial 328 | M, S, B | Spacing: 15, 24, 32, 33 |
| [Lover, Come Back To Me](../src/openbook/lover_come_back_to_me.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Lucky to Be Me](../src/openbook/lucky_to_be_me.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Lulu's Back in Town](../src/openbook/lulus_back_in_town.ly.tera) | Initial 328 | M, S, B | Spacing: 17; Notice |
| [Ma he's making eyes at me](../src/openbook/ma_hes_making_eyes_at_me.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Makin' Whoopee](../src/openbook/makin_whoopee.ly.tera) | Initial 328 | M, S, B | Spacing: 19; Route: segno at 2 |
| [Mamacita](../src/openbook/mamacita.ly.tera) | Initial 328 | M, S, B | - |
| [Mambo Inn](../src/openbook/mambo_inn.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Marie](../src/openbook/marie.ly.tera) | Initial 328 | M, S, B | - |
| [Mas Que Nada](../src/openbook/mas_que_nada.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Memphis Blues](../src/openbook/memphis_blues.ly.tera) | Initial 328 | M, S, B | - |
| [Michelle](../src/openbook/michelle.ly.tera) | New 200 | M, S, B, E | Spacing: 38; Notice; Page; Route: segno at 13, to coda at 22, coda at 28 |
| [Midnight Mood](../src/openbook/midnight_mood.ly.tera) | Initial 328 | M, S, B | Notice; Route: Fine at 23 |
| [Minnie the Moocher](../src/openbook/minnie_the_moocher.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Minority](../src/openbook/minority.ly.tera) | Initial 328 | M, S, B | Notice |
| [Monk's Dream](../src/openbook/monks_dream.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Moon and Sand](../src/openbook/moon_and_sand.ly.tera) | Initial 328 | M, S, B | Spacing: 1, 5, 7, 8, 15, 19, 29, 31, 32, 39, 40 |
| [Moondance](../src/openbook/moondance.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Moonlight Serenade](../src/openbook/moonlight_serenade.ly.tera) | New 200 | M, S, B, E | Spacing: 6, 7, 14, 18, 27, 28, 34; Notice; Page |
| [Morning](../src/openbook/morning.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Mountain Greenery](../src/openbook/mountain_greenery.ly.tera) | Initial 328 | M, S, B | - |
| [Mr. Lucky](../src/openbook/mr_lucky.ly.tera) | Initial 328 | M, S, B | - |
| [Muskrat Ramble](../src/openbook/muskrat_ramble.ly.tera) | Initial 328 | M, S, B | - |
| [My Baby Just Cares For Me](../src/openbook/my_baby_just_cares_for_me.ly.tera) | Initial 328 | M, S, B | Spacing: 7, 23, 28, 31 |
| [My Blue Heaven](../src/openbook/my_blue_heaven.ly.tera) | Initial 328 | M, S, B | - |
| [My Bonnie Lies over the Ocean](../src/openbook/my_bonnie_lies_over_the_ocean.ly.tera) | Initial 328 | M, S, B | - |
| [My Buddy](../src/openbook/my_buddy.ly.tera) | Initial 328 | M, S, B | - |
| [My Girl](../src/openbook/my_girl.ly.tera) | New 200 | M, S, B, E | Spacing: 45; Notice; Page |
| [My Heart Stood Still](../src/openbook/my_heart_stood_still.ly.tera) | Initial 328 | M, S, B | Spacing: 7, 15, 24, 31, 32 |
| [My Ideal](../src/openbook/my_ideal.ly.tera) | Initial 328 | M, S, B | Spacing: 6, 12, 28 |
| [My Old Flame](../src/openbook/my_old_flame.ly.tera) | Initial 328 | M, S, B | Notice |
| [My Silent Love](../src/openbook/my_silent_love.ly.tera) | New 200 | M, S, B, E | Spacing: 7, 8, 16, 20, 24, 31, 32, 33; Notice; Page |
| [Nagasaki](../src/openbook/nagasaki.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Nancy](../src/openbook/nancy.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Never Let Me Go](../src/openbook/never_let_me_go.ly.tera) | Initial 328 | M, S, B | Spacing: 27; Notice |
| [Nice 'N' Easy](../src/openbook/nice_n_easy.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 15, 16, 24, 31, 35, 36, 37; Notice |
| [Night Train](../src/openbook/night_train.ly.tera) | Initial 328 | M, S, B | Notice; Route: D.C. at 32, Fine at 44 |
| [No Me Esqueca](../src/openbook/no_me_esqueca.ly.tera) | Initial 328 | M, S, B | - |
| [No Moe](../src/openbook/no_moe.ly.tera) | Initial 328 | M, S, B | Notice |
| [Nobody Else but Me](../src/openbook/nobody_else_but_me.ly.tera) | Initial 328 | M, S, B | Notice |
| [Nobody Knows You When You're Down and Out](../src/openbook/nobody_knows_you_when_youre_down_and_out.ly.tera) | Initial 328 | M, S, B | - |
| [Nobody's Sweetheart](../src/openbook/nobodys_sweetheart.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Nostalgia in Times Square](../src/openbook/nostalgia_in_times_square.ly.tera) | Initial 328 | M, S, B | Notice; Endings: 13 |
| [Nuages](../src/openbook/nuages.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [O Christmas Tree](../src/openbook/o_christmas_tree.ly.tera) | Initial 328 | M, S, B | - |
| [Oh My Darling, Clementine](../src/openbook/oh_my_darling_clementine.ly.tera) | Initial 328 | M, S, B | - |
| [Oh, Lady Be Good!](../src/openbook/oh_lady_be_good.ly.tera) | Initial 328 | M, S, B | Spacing: 31, 33 |
| [Oh, You Crazy Moon](../src/openbook/oh_you_crazy_moon.ly.tera) | New 200 | M, S, B, E | Spacing: 4, 12, 28; Notice; Page |
| [On the Alamo](../src/openbook/on_the_alamo.ly.tera) | Initial 328 | M, S, B | - |
| [Once In A While](../src/openbook/once_in_a_while.ly.tera) | Initial 328 | M, S, B | Spacing: 4, 7, 8, 12, 15, 24, 28, 31; Notice |
| [One For My Baby](../src/openbook/one_for_my_baby.ly.tera) | Initial 328 | M, S, B | Spacing: 5, 13, 21, 25, 29, 37, 45, 49, 53, 56, 59; Notice |
| [Our Delight](../src/openbook/our_delight.ly.tera) | Initial 328 | M, S, B | Notice |
| [Out of This World](../src/openbook/out_of_this_world.ly.tera) | Initial 328 | M, S, B | - |
| [Pagan Love Song](../src/openbook/pagan_love_song.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Pent-Up House](../src/openbook/pent_up_house.ly.tera) | Initial 328 | M, S, B | Notice |
| [Petite Fleur](../src/openbook/petite_fleur.ly.tera) | New 200 | M, S, B, E | Spacing: 17, 33, 35, 37, 39; Notice; Page |
| [Phase Dance](../src/openbook/phase_dance.ly.tera) | Initial 328 | M, S, B | Notice |
| [Play A Simple Melody](../src/openbook/play_a_simple_melody.ly.tera) | Initial 328 | M, S, B | - |
| [Please Don't Talk About Me When I'm Gone](../src/openbook/please_dont_talk_about_me_when_im_gone.ly.tera) | New 200 | M, S, B, E | Spacing: 15, 31, 33; Notice; Page |
| [Pretty Baby](../src/openbook/pretty_baby.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Pussy Cat Dues](../src/openbook/pussy_cat_dues.ly.tera) | Initial 328 | M, S, B | Notice |
| [Puttin' on the Ritz](../src/openbook/puttin_on_the_ritz.ly.tera) | Initial 328 | M, S, B | Spacing: 16, 23, 31, 48, 49 |
| [Question Mark](../src/openbook/question_mark.ly.tera) | New 200 | M, S, B, E | Notice; Page; Route: segno at 2, Fine at 5, D.S. at 14 |
| [Recado Bossa](../src/openbook/recado_bossa.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Recorda-Me](../src/openbook/recorda_me.ly.tera) | Initial 328 | M, S, B | Notice |
| [Remember](../src/openbook/remember.ly.tera) | Initial 328 | M, S, B | - |
| [Reverie](../src/openbook/reverie.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Rhythm-a-Ning](../src/openbook/rhythm_a_ning.ly.tera) | Initial 328 | M, S, B | Notice |
| [Rico Vacilon](../src/openbook/rico_vacilon.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Rose of Washington Square](../src/openbook/rose_of_washington_square.ly.tera) | Initial 328 | M, S, B | - |
| [Roses Of Picardy](../src/openbook/roses_of_picardy.ly.tera) | New 200 | M, S, B, E | Spacing: 21; Notice; Page |
| [Ruby](../src/openbook/ruby.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Runnin' Wild](../src/openbook/runnin_wild.ly.tera) | Initial 328 | M, S, B | - |
| [Russian Lullaby](../src/openbook/russian_lullaby.ly.tera) | Initial 328 | M, S, B | - |
| [San Francisco Bay Blues](../src/openbook/san_francisco_bay_blues.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Sandu](../src/openbook/sandu.ly.tera) | Initial 328 | M, S, B | Notice; Route: to coda at 10, coda at 28 |
| [Save Your Love For Me](../src/openbook/save_your_love_for_me.ly.tera) | Initial 328 | M, S, B | - |
| [Secret Love](../src/openbook/secret_love.ly.tera) | Initial 328 | M, S, B | Notice |
| [See See Rider](../src/openbook/see_see_rider.ly.tera) | New 200 | M, S, B, E | Spacing: 19, 20, 23, 24, 25, 26; Notice; Page |
| [Seems Like Old Times](../src/openbook/seems_like_old_times.ly.tera) | New 200 | M, S, B, E | Spacing: 9, 16, 48, 50; Notice; Page |
| [September in the Rain](../src/openbook/september_in_the_rain.ly.tera) | Initial 328 | M, S, B, V, E, P | Spacing: 8, 20 |
| [Serenade In Blue](../src/openbook/serenade_in_blue.ly.tera) | New 200 | M, S, B, E | Spacing: 7, 8, 15, 30; Notice; Page |
| [Serenata](../src/openbook/serenata.ly.tera) | Initial 328 | M, S, B | - |
| [Shchedryk](../src/openbook/shchedryk.ly.tera) | Initial 328 | M, S, B | - |
| [Silver Dollar](../src/openbook/silver_dollar.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Simone](../src/openbook/simone.ly.tera) | Initial 328 | M, S, B | Notice |
| [Since I Fell For You](../src/openbook/since_i_fell_for_you.ly.tera) | Initial 328 | M, S, B | Spacing: 1, 3, 5, 7, 9, 11, 13, 26, 28, 30, 33 |
| [Sing You Sinners](../src/openbook/sing_you_sinners.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Sleepy Time Gal](../src/openbook/sleepy_time_gal.ly.tera) | Initial 328 | M, S, B | Spacing: 32 |
| [Slow Hot Wind](../src/openbook/slow_hot_wind.ly.tera) | Initial 328 | M, S, B | Notice |
| [Small Fry](../src/openbook/small_fry.ly.tera) | Initial 328 | M, S, B | Notice |
| [Smile](../src/openbook/smile.ly.tera) | New 200 | M, S, B, E | Spacing: 16, 33; Notice; Page |
| [So Danco Samba](../src/openbook/so_danco_samba.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [So In Love](../src/openbook/so_in_love.ly.tera) | Initial 328 | M, S, B | - |
| [So Many Stars](../src/openbook/so_many_stars.ly.tera) | Initial 328 | M, S, B | Spacing: 36; Notice |
| [Social Call](../src/openbook/social_call.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Solamente una Vez](../src/openbook/solamente_una_vez.ly.tera) | New 200 | M, S, B, E | Spacing: 9; Notice; Page; Route: coda at 29, coda at 34 |
| [Some Other Blues](../src/openbook/some_other_blues.ly.tera) | Initial 328 | M, S, B | Notice |
| [Some Other Time](../src/openbook/some_other_time.ly.tera) | Initial 328 | M, S, B | Spacing: 32, 40 |
| [Some Sunny Day](../src/openbook/some_sunny_day.ly.tera) | Initial 328 | M, S, B | - |
| [Somebody Loves Me](../src/openbook/somebody_loves_me.ly.tera) | Initial 328 | M, S, B | Spacing: 29 |
| [Somebody Stole My Gal](../src/openbook/somebody_stole_my_gal.ly.tera) | Initial 328 | M, S, B | - |
| [Someone to Light up My Life](../src/openbook/someone_to_light_up_my_life.ly.tera) | Initial 328 | M, S, B | - |
| [Sonnymoon for Two](../src/openbook/sonnymoon_for_two.ly.tera) | Initial 328 | M, S, B | Notice |
| [Soon](../src/openbook/soon.ly.tera) | Initial 328 | M, S, B | - |
| [Speak No Evil](../src/openbook/speak_no_evil.ly.tera) | Initial 328 | M, S, B | Notice |
| [Spring Is Here](../src/openbook/spring_is_here.ly.tera) | Initial 328 | M, S, B | Spacing: 33 |
| [St. Louis Blues](../src/openbook/st_louis_blues.ly.tera) | Initial 328 | M, S, B | Spacing: 52, 53, 56, 57 |
| [Stairway To The Stars](../src/openbook/stairway_to_the_stars.ly.tera) | Initial 328 | M, S, B | Spacing: 7, 8, 16, 20, 24 |
| [Stars Fell On Alabama](../src/openbook/stars_fell_on_alabama.ly.tera) | Initial 328 | M, S, B | Spacing: 7, 8, 9, 32 |
| [Sticks](../src/openbook/sticks.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Straight, No Chaser](../src/openbook/straight_no_chaser.ly.tera) | Initial 328 | M, S, B | Notice |
| [Streets of Laredo](../src/openbook/streets_of_laredo.ly.tera) | Initial 328 | M, S, B | - |
| [Strode Rode](../src/openbook/strode_rode.ly.tera) | Initial 328 | M, S, B | Notice |
| [Stumbling](../src/openbook/stumbling.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Sugar Blues](../src/openbook/sugar_blues.ly.tera) | Initial 328 | M, S, B | - |
| [Sunday](../src/openbook/sunday.ly.tera) | Initial 328 | M, S, B | - |
| [Sunny](../src/openbook/sunny.ly.tera) | New 200 | M, S, B, E | Spacing: 4, 8; Notice; Page |
| [Swanee](../src/openbook/swanee.ly.tera) | Initial 328 | M, S, B | - |
| [Sweet Lorraine](../src/openbook/sweet_lorraine.ly.tera) | Initial 328 | M, S, B | - |
| [Taking A Chance On Love](../src/openbook/taking_a_chance_on_love.ly.tera) | Initial 328 | M, S, B | Spacing: 8 |
| [Tangerine](../src/openbook/tangerine.ly.tera) | Initial 328 | M, S, B | Notice |
| [Tea for Two](../src/openbook/tea_for_two.ly.tera) | Initial 328 | M, S, B | - |
| [Teach Me Tonight](../src/openbook/teach_me_tonight.ly.tera) | Initial 328 | M, S, B | Spacing: 16, 32, 34 |
| [Thanks For The Memory](../src/openbook/thanks_for_the_memory.ly.tera) | New 200 | M, S, B, E | Spacing: 16, 32, 37; Notice; Page |
| [That Certain Feeling](../src/openbook/that_certain_feeling.ly.tera) | Initial 328 | M, S, B | - |
| [That Old Black Magic](../src/openbook/that_old_black_magic.ly.tera) | Initial 328 | M, S, B | Notice |
| [That Old Feeling](../src/openbook/that_old_feeling.ly.tera) | Initial 328 | M, S, B | Spacing: 16, 28, 32 |
| [That Sunday (That Summer)](../src/openbook/that_sunday_that_summer.ly.tera) | New 200 | M, S, B, E | Spacing: 9; Notice; Page |
| [That's a Plenty](../src/openbook/thats_a_plenty.ly.tera) | Initial 328 | M, S, B | Route: Fine at 10, D.C. at 26 |
| [That's My Weakness Now](../src/openbook/thats_my_weakness_now.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [That's What Friends Are For](../src/openbook/thats_what_friends_are_for.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [The Anniversary Song](../src/openbook/the_anniversary_song.ly.tera) | New 200 | M, S, B, E | Spacing: 48; Notice; Page; Route: Fine at 33, D.C. at 50 |
| [The Anniversary Waltz](../src/openbook/the_anniversary_waltz.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [The Best Thing For You](../src/openbook/the_best_thing_for_you.ly.tera) | New 200 | M, S, B, E | Spacing: 7, 35; Notice; Page |
| [The Birth of the Blues](../src/openbook/the_birth_of_the_blues.ly.tera) | Initial 328 | M, S, B | Spacing: 20, 34 |
| [The Boy Next Door](../src/openbook/the_boy_next_door.ly.tera) | Initial 328 | M, S, B | Spacing: 32, 33; Notice |
| [The Christmas Waltz](../src/openbook/the_christmas_waltz.ly.tera) | New 200 | M, S, B, E | Spacing: 40; Notice; Page |
| [The Continental](../src/openbook/the_continental.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [The Flat Foot Floogie](../src/openbook/the_flat_foot_floogie.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [The Hawaiian Wedding Song](../src/openbook/the_hawaiian_wedding_song.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [The Inch Worm](../src/openbook/the_inch_worm.ly.tera) | Initial 328 | M, S, B | Notice; Route: Fine at 10 |
| [The Japanese Sandman](../src/openbook/the_japanese_sandman.ly.tera) | Initial 328 | M, S, B | - |
| [The Loco-motion](../src/openbook/the_loco_motion.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [The Love Nest](../src/openbook/the_love_nest.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [The Lullaby Of Broadway](../src/openbook/the_lullaby_of_broadway.ly.tera) | New 200 | M, S, B, E | Spacing: 29, 30, 37, 38; Notice; Page |
| [The Man on the Flying Trapeze](../src/openbook/the_man_on_the_flying_trapeze.ly.tera) | Initial 328 | M, S, B | - |
| [The Midnight Sun Will Never Set](../src/openbook/the_midnight_sun_will_never_set.ly.tera) | Initial 328 | M, S, B | Spacing: 2, 4, 19, 21; Notice |
| [The Moontrane](../src/openbook/the_moontrane.ly.tera) | Initial 328 | M, S, B | Notice |
| [The Night Has A Thousand Eyes](../src/openbook/the_night_has_a_thousand_eyes.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [The Night We Called It A Day](../src/openbook/the_night_we_called_it_a_day.ly.tera) | Initial 328 | M, S, B | Spacing: 17, 21; Notice |
| [The Old Rugged Cross](../src/openbook/the_old_rugged_cross.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [The Second Time Around](../src/openbook/the_second_time_around.ly.tera) | Initial 328 | M, S, B | - |
| [The Summer Knows](../src/openbook/the_summer_knows.ly.tera) | Initial 328 | M, S, B | - |
| [The Sweetest Sounds](../src/openbook/the_sweetest_sounds.ly.tera) | Initial 328 | M, S, B | Spacing: 16; Notice |
| [The Sweetheart Of Sigma Chi](../src/openbook/the_sweetheart_of_sigma_chi.ly.tera) | New 200 | M, S, B, E | Spacing: 8, 13, 16, 17, 23, 24, 31, 34; Notice; Page |
| [The Very Thought Of You](../src/openbook/the_very_thought_of_you.ly.tera) | Initial 328 | M, S, B | Spacing: 13; Notice |
| [The Whiffenpoof Song](../src/openbook/the_whiffenpoof_song.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Them There Eyes](../src/openbook/them_there_eyes.ly.tera) | Initial 328 | M, S, B | - |
| [There Goes My Heart](../src/openbook/there_goes_my_heart.ly.tera) | Initial 328 | M, S, B | Spacing: 12, 32, 34; Notice |
| [There's No You](../src/openbook/theres_no_you.ly.tera) | New 200 | M, S, B, E | Spacing: 4, 24; Notice; Page |
| [They Say It's Wonderful](../src/openbook/they_say_its_wonderful.ly.tera) | Initial 328 | M, S, B | Spacing: 31; Notice |
| [Things Ain't What They Used to Be](../src/openbook/things_aint_what_they_used_to_be.ly.tera) | Initial 328 | M, S, B | Notice; Route: to coda at 10, D.C. at 24, coda at 25 |
| [Thinking Of You](../src/openbook/thinking_of_you.ly.tera) | New 200 | M, S, B, E | Spacing: 1, 9, 16, 23, 25; Notice; Page |
| [This Heart of Mine](../src/openbook/this_heart_of_mine.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Thou Swell](../src/openbook/thou_swell.ly.tera) | Initial 328 | M, S, B | - |
| [Three Little Words](../src/openbook/three_little_words.ly.tera) | Initial 328 | M, S, B | - |
| [Tiger Rag](../src/openbook/tiger_rag.ly.tera) | Initial 328 | M, S, B | - |
| [Till There Was You](../src/openbook/till_there_was_you.ly.tera) | Initial 328 | M, S, B | Notice |
| [Till We Meet Again](../src/openbook/till_we_meet_again.ly.tera) | Initial 328 | M, S, B | - |
| [Time after time](../src/openbook/time_after_time.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Time on My Hands](../src/openbook/time_on_my_hands.ly.tera) | Initial 328 | M, S, B | Spacing: 31, 33 |
| [Time Was](../src/openbook/time_was.ly.tera) | Initial 328 | M, S, B | Spacing: 7, 15, 31; Notice |
| [Too Close For Comfort](../src/openbook/too_close_for_comfort.ly.tera) | Initial 328 | M, S, B | Notice |
| [Too Marvelous For Words](../src/openbook/too_marvelous_for_words.ly.tera) | Initial 328 | M, S, B | Notice |
| [Toot, Toot, Tootsie](../src/openbook/toot_toot_tootsie.ly.tera) | New 200 | M, S, B, E | Spacing: 3, 5, 7, 20, 36, 48, 52; Notice; Page |
| [Topsy](../src/openbook/topsy.ly.tera) | New 200 | M, S, B, E | Spacing: 4, 8, 28; Notice; Page |
| [Tricotism](../src/openbook/tricotism.ly.tera) | Initial 328 | M, S, B | Notice |
| [Trouble In Mind](../src/openbook/trouble_in_mind.ly.tera) | Initial 328 | M, S, B | - |
| [Trouble Is A Man](../src/openbook/trouble_is_a_man.ly.tera) | Initial 328 | M, S, B | Spacing: 9 |
| [Turn Out the Stars](../src/openbook/turn_out_the_stars.ly.tera) | Initial 328 | M, S, B | - |
| [Two for the Road](../src/openbook/two_for_the_road.ly.tera) | Initial 328 | M, S, B | - |
| [Two Guitars](../src/openbook/two_guitars.ly.tera) | Initial 328 | M, S, B | - |
| [Two Sleepy People](../src/openbook/two_sleepy_people.ly.tera) | New 200 | M, S, B, E | Spacing: 32; Notice; Page |
| [Unless It's You](../src/openbook/unless_its_you.ly.tera) | Initial 328 | M, S, B | - |
| [Until It's Time For You To Go](../src/openbook/until_its_time_for_you_to_go.ly.tera) | New 200 | M, S, B, E | Notice; Page; Route: Fine at 16, D.C. at 49 |
| [Up Jumped Spring](../src/openbook/up_jumped_spring.ly.tera) | Initial 328 | M, S, B | Notice |
| [Virgo](../src/openbook/virgo.ly.tera) | Initial 328 | M, S, B | Notice |
| [Wabash Blues](../src/openbook/wabash_blues.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Walk On By](../src/openbook/walk_on_by.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Waltz New](../src/openbook/waltz_new.ly.tera) | Initial 328 | M, S, B | Route: to coda at 31, D.C. at 32, coda at 33 |
| [Waltzing Matilda](../src/openbook/waltzing_matilda.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Warm Valley](../src/openbook/warm_valley.ly.tera) | Initial 328 | M, S, B | - |
| [We Wish You a Merry Christmas](../src/openbook/we_wish_you_a_merry_christmas.ly.tera) | Initial 328 | M, S, B | - |
| [We'll Be Together Again](../src/openbook/well_be_together_again.ly.tera) | Initial 328 | M, S, B | Spacing: 9, 33; Notice |
| [What A Little Moonlight Can Do](../src/openbook/what_a_little_moonlight_can_do.ly.tera) | Initial 328 | M, S, B | Spacing: 10, 58; Notice |
| [What Am I Here For](../src/openbook/what_am_i_here_for.ly.tera) | Initial 328 | M, S, B | - |
| [What Are You Doing the Rest of Your Life?](../src/openbook/what_are_you_doing_the_rest_of_your_life.ly.tera) | Initial 328 | M, S, B | Spacing: 43 |
| [What is There to Say](../src/openbook/what_is_there_to_say.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [What Is This Thing Called Love?](../src/openbook/what_is_this_thing_called_love.ly.tera) | Initial 328 | M, S, B | Spacing: 4, 12 |
| [What The World Needs Now Is Love](../src/openbook/what_the_world_needs_now_is_love.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [When Day Is Done](../src/openbook/when_day_is_done.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [When I Look In Your Eyes](../src/openbook/when_i_look_in_your_eyes.ly.tera) | Initial 328 | M, S, B | Spacing: 7, 8, 15, 23 |
| [When Irish Eyes Are Smiling](../src/openbook/when_irish_eyes_are_smiling.ly.tera) | Initial 328 | M, S, B | - |
| [When It's Sleepy Time Down South](../src/openbook/when_its_sleepy_time_down_south.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [When Sunny Gets Blue](../src/openbook/when_sunny_gets_blue.ly.tera) | Initial 328 | M, S, B | Spacing: 5, 9, 13, 17, 29, 33, 34; Notice |
| [When the Saints Go Marching In](../src/openbook/when_the_saints_go_marching_in.ly.tera) | Initial 328 | M, S, B | - |
| [When The Sun Comes Out](../src/openbook/when_the_sun_comes_out.ly.tera) | Initial 328 | M, S, B | Spacing: 36; Notice |
| [When the World Was Young](../src/openbook/when_the_world_was_young.ly.tera) | New 200 | M, S, B, E | Spacing: 34, 36; Notice; Page |
| [When You Wore a Tulip](../src/openbook/when_you_wore_a_tulip.ly.tera) | Initial 328 | M, S, B | - |
| [Where Are You?](../src/openbook/where_are_you.ly.tera) | Initial 328 | M, S, B | - |
| [Whispering](../src/openbook/whispering.ly.tera) | Initial 328 | M, S, B | - |
| [Who Cares](../src/openbook/who_cares.ly.tera) | Initial 328 | M, S, B | - |
| [Who's Sorry Now](../src/openbook/whos_sorry_now.ly.tera) | Initial 328 | M, S, B | - |
| [Why Try To Change Me Now](../src/openbook/why_try_to_change_me_now.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [With a Song in My Heart](../src/openbook/with_a_song_in_my_heart.ly.tera) | Initial 328 | M, S, B | Spacing: 15, 16, 26, 31 |
| [With Every Breath I Take](../src/openbook/with_every_breath_i_take.ly.tera) | Initial 328 | M, S, B | Notice |
| [Without a Song](../src/openbook/without_a_song.ly.tera) | Initial 328 | M, S, B | Spacing: 16, 21 |
| [Woody 'n' You](../src/openbook/woody_n_you.ly.tera) | Initial 328 | M, S, B | - |
| [Words](../src/openbook/words.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Yes Sir, That's My Baby](../src/openbook/yes_sir_thats_my_baby.ly.tera) | Initial 328 | M, S, B | - |
| [Yes We Have No Bananas](../src/openbook/yes_we_have_no_bananas.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [Yesterday](../src/openbook/yesterday.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [You](../src/openbook/you.ly.tera) | New 200 | M, S, B, E | Spacing: 7, 15, 16, 41; Notice; Page |
| [You And The Night And The Music](../src/openbook/you_and_the_night_and_the_music.ly.tera) | New 200 | M, S, B, E | Spacing: 4, 12, 21, 25, 29; Notice; Page |
| [You Are My Sunshine](../src/openbook/you_are_my_sunshine.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [You Are So Beautiful](../src/openbook/you_are_so_beautiful.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [You are the sunshine of my life](../src/openbook/you_are_the_sunshine_of_my_life.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [You Are Too Beautiful](../src/openbook/you_are_too_beautiful.ly.tera) | Initial 328 | M, S, B | Spacing: 4, 8, 12, 15, 16, 24, 28, 31, 32 |
| [You Can Depend On Me](../src/openbook/you_can_depend_on_me.ly.tera) | New 200 | M, S, B, E | Spacing: 16; Notice; Page |
| [You Do Something to Me](../src/openbook/you_do_something_to_me.ly.tera) | Initial 328 | M, S, B | Spacing: 17, 31, 32 |
| [You Make Me Feel Brand New](../src/openbook/you_make_me_feel_brand_new.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [You Make Me Feel So Young](../src/openbook/you_make_me_feel_so_young.ly.tera) | Initial 328 | M, S, B | Spacing: 2, 10, 20, 31, 33 |
| [You Must Believe In Spring](../src/openbook/you_must_believe_in_spring.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 16 |
| [You Say You Care](../src/openbook/you_say_you_care.ly.tera) | Initial 328 | M, S, B | Notice |
| [You Stepped Out Of A Dream](../src/openbook/you_stepped_out_of_a_dream.ly.tera) | Initial 328 | M, S, B | - |
| [You Took Advantage Of Me](../src/openbook/you_took_advantage_of_me.ly.tera) | Initial 328 | M, S, B | Spacing: 8, 24, 32 |
| [You'll Never Know](../src/openbook/youll_never_know.ly.tera) | Initial 328 | M, S, B | - |
| [You're Driving Me Crazy](../src/openbook/youre_driving_me_crazy.ly.tera) | Initial 328 | M, S, B | Spacing: 31, 33 |
| [You're My Thrill](../src/openbook/youre_my_thrill.ly.tera) | New 200 | M, S, B, E | Notice; Page |
| [You're The Top](../src/openbook/youre_the_top.ly.tera) | Initial 328 | M, S, B | Spacing: 16, 32, 34 |
| [Yours Is My Heart Alone](../src/openbook/yours_is_my_heart_alone.ly.tera) | Initial 328 | M, S, B | Spacing: 7; Notice |
