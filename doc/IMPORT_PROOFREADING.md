# Imported Tune Proofreading Register

Status recorded on **2026-11-03**, against source snapshot `412ab688`.
Scope: the **328 MusicXML imports** in `src/openbook`, not the rest of the book.
No tune in this register has completed full musical proofreading.

This is a historical record of checks actually performed, not a claim that the
archived music or its copyright statements are authoritative. Recheck an entry
after changing its music. Keep the tune's own `Doc` TODOs until the corresponding
musical review is complete.

## Completed check methods

| Code | Check performed | Limits |
| --- | --- | --- |
| M | Compared the LilyPond melody's written-order pitched-note sequence with that tune's archived MusicXML: note count, note names, octaves, alterations, and metered durations as exact fractions. All 328 tunes matched, totaling 36,961 pitched-note events. | Grace-note pitches were included, but their unmetered performance durations were not compared. This did not compare rests, ties, articulation, note onset positions, or the unfolded performance order. Agreement with an import source does not prove that source is musically correct. |
| S | Ran `uv run python -m scripts.check_all --inputs src/openbook/*.ly.tera`. | Source conventions and UUID consistency, not musical correctness. |
| B | Regenerated the integrated book PDF, its index, and embedded bookmarks. | Successful engraving, not a manual inspection of every page or a playback review. |
| A | Checked the corrected altered-dominant chords against the archived `7alt` symbols, verified their actual LilyPond pitch-class sets, and confirmed altered-chord labels in rendered output. | Only the four corrected chords detailed below; other harmonies remain unreviewed. |
| V | Restored the specified repeat endings from the archived MusicXML and checked the unfolded lengths of both melody and chord streams. | Only the corrected volta structures, not D.C./D.S./coda/Fine playback routing. |
| E | Rebuilt the individual tune's PDF through the repository's song build. | Only the five corrected tunes; compilation is not full visual proofreading. |
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
corrected tunes. A, V, P, and I record narrowly scoped work; they do not close a
whole-tune review item.

## Tune inventory

Every tune below has completed M, S, and B. Extra codes identify additional
completed work. A dash in the last column means no *additional* specific flag was
recorded; it does not mean the tune is approved or has no outstanding checks.

Additional pending-review labels:

- **Spacing**: existing tune TODO; successive source chord symbols share an
  offset, so their editorial spacing must be checked at the listed measures.
  There are 109 tunes with this flag.
- **Notice**: existing tune TODO; no readable per-tune notice was recovered from
  the referenced scan, and the notice still needs comparison. There are 131
  tunes with this flag.
- **Route**: source navigation markers warrant a complete performance-order
  review. Listed markers are review prompts, not confirmed defects.
- **Endings**: unusual/unlabeled source ending markers need comparison with a
  scan, including confirmation of any normalization already made during import.

<!-- tune-inventory -->

| Tune | Completed checks | Additional pending review |
| --- | --- | --- |
| ['S Wonderful](../src/openbook/s_wonderful.ly.tera) | M, S, B | Spacing: 7, 20, 28 |
| [502 Blues](../src/openbook/502_blues.ly.tera) | M, S, B | Notice |
| [A Time For Love](../src/openbook/a_time_for_love.ly.tera) | M, S, B | Spacing: 8, 16, 24 |
| [Ach, Du Lieber Augustin](../src/openbook/ach_du_lieber_augustin.ly.tera) | M, S, B | - |
| [After the Ball](../src/openbook/after_the_ball.ly.tera) | M, S, B | - |
| [Ah! Sweet Mystery of Life](../src/openbook/ah_sweet_mystery_of_life.ly.tera) | M, S, B | - |
| [Ain't She Sweet](../src/openbook/aint_she_sweet.ly.tera) | M, S, B | - |
| [Alabamy Bound](../src/openbook/alabamy_bound.ly.tera) | M, S, B | - |
| [Alexander's Ragtime Band](../src/openbook/alexanders_ragtime_band.ly.tera) | M, S, B | - |
| [Alfie](../src/openbook/alfie.ly.tera) | M, S, B | Notice; Endings: 40, 41 |
| [All Alone](../src/openbook/all_alone.ly.tera) | M, S, B | Spacing: 32 |
| [Almost Like Being in Love](../src/openbook/almost_like_being_in_love.ly.tera) | M, S, B | Spacing: 37 |
| [Am I Blue?](../src/openbook/am_i_blue.ly.tera) | M, S, B | Spacing: 16 |
| [Angels We Have Heard on High](../src/openbook/angels_we_have_heard_on_high.ly.tera) | M, S, B | - |
| [Ask Me Now](../src/openbook/ask_me_now.ly.tera) | M, S, B | Notice |
| [At Last](../src/openbook/at_last.ly.tera) | M, S, B | Spacing: 8, 18, 20, 24, 26, 28, 32, 42, 44, 48; Route: segno at 18, Fine at 48, D.S. at 49 |
| [At Sundown](../src/openbook/at_sundown.ly.tera) | M, S, B | Spacing: 9, 25 |
| [Auld Lang Syne](../src/openbook/auld_lang_syne.ly.tera) | M, S, B | - |
| [Autumn Nocturne](../src/openbook/autumn_nocturne.ly.tera) | M, S, B | Notice |
| [Avalon](../src/openbook/avalon.ly.tera) | M, S, B | - |
| [Ba-Lue Bolivar Ba-Lues Are](../src/openbook/ba_lue_bolivar_ba_lues_are.ly.tera) | M, S, B | Notice |
| [Baby Face](../src/openbook/baby_face.ly.tera) | M, S, B | Spacing: 31 |
| [Baby It's Cold Outside](../src/openbook/baby_its_cold_outside.ly.tera) | M, S, B | - |
| [Ballad for Trane](../src/openbook/ballad_for_trane.ly.tera) | M, S, B | Notice |
| [Baubles, Bangles and Beads](../src/openbook/baubles_bangles_and_beads.ly.tera) | M, S, B | Notice |
| [Be My Love](../src/openbook/be_my_love.ly.tera) | M, S, B | Notice |
| [Beautiful Dreamer](../src/openbook/beautiful_dreamer.ly.tera) | M, S, B | Route: D.C. at 27, coda at 28 |
| [Bemsha Swing](../src/openbook/bemsha_swing.ly.tera) | M, S, B | Notice |
| [Between The Devil And The Deep Blue Sea](../src/openbook/between_the_devil_and_the_deep_blue_sea.ly.tera) | M, S, B | Spacing: 16, 24; Notice |
| [Bidin' My Time](../src/openbook/bidin_my_time.ly.tera) | M, S, B | - |
| [Bird Food](../src/openbook/bird_food.ly.tera) | M, S, B | Route: to coda at 32, coda at 35 |
| [Birk's Works](../src/openbook/birks_works.ly.tera) | M, S, B | Notice |
| [Black and Blue](../src/openbook/black_and_blue.ly.tera) | M, S, B | - |
| [Black And Tan Fantasy](../src/openbook/black_and_tan_fantasy.ly.tera) | M, S, B | Notice |
| [Black Coffee](../src/openbook/black_coffee.ly.tera) | M, S, B | Spacing: 8, 9, 12, 20, 24, 40, 44; Notice |
| [Blame It On My Youth](../src/openbook/blame_it_on_my_youth.ly.tera) | M, S, B | Spacing: 4, 8, 12, 20, 24, 28, 32 |
| [Blue Gardenia](../src/openbook/blue_gardenia.ly.tera) | M, S, B | Notice |
| [Blue Moon](../src/openbook/blue_moon.ly.tera) | M, S, B | - |
| [Blues By Five](../src/openbook/blues_by_five.ly.tera) | M, S, B | Notice |
| [Blues My Naughty Sweetie Gives to Me](../src/openbook/blues_my_naughty_sweetie_gives_to_me.ly.tera) | M, S, B | - |
| [Bohemia After Dark](../src/openbook/bohemia_after_dark.ly.tera) | M, S, B | Spacing: 17; Notice; Route: D.C. at 21, Fine at 22 |
| [Bouncin' with Bud](../src/openbook/bouncin_with_bud.ly.tera) | M, S, B, A, E, I | - |
| [Brilliant Corners](../src/openbook/brilliant_corners.ly.tera) | M, S, B | Notice |
| [Broadway](../src/openbook/broadway.ly.tera) | M, S, B | Notice |
| [Buster Rides Again](../src/openbook/buster_rides_again.ly.tera) | M, S, B | Notice |
| [By Myself](../src/openbook/by_myself.ly.tera) | M, S, B | Notice |
| [Bye Bye Baby](../src/openbook/bye_bye_baby.ly.tera) | M, S, B | Spacing: 8, 10, 15, 24, 26, 34; Notice |
| [C-Jam Blues](../src/openbook/c_jam_blues.ly.tera) | M, S, B | Notice |
| [Can't We Be Friends?](../src/openbook/cant_we_be_friends.ly.tera) | M, S, B | Spacing: 8, 16, 23, 24, 32, 33; Notice |
| [Can't We Talk It Over](../src/openbook/cant_we_talk_it_over.ly.tera) | M, S, B | Notice |
| [Careless Love](../src/openbook/careless_love.ly.tera) | M, S, B | - |
| [Chameleon](../src/openbook/chameleon.ly.tera) | M, S, B | Notice |
| [Charade](../src/openbook/charade.ly.tera) | M, S, B | - |
| [Chicago](../src/openbook/chicago.ly.tera) | M, S, B | - |
| [China Boy](../src/openbook/china_boy.ly.tera) | M, S, B | - |
| [Chloe](../src/openbook/chloe.ly.tera) | M, S, B | Spacing: 10 |
| [Choucoune](../src/openbook/choucoune.ly.tera) | M, S, B | - |
| [Close Enough For Love](../src/openbook/close_enough_for_love.ly.tera) | M, S, B | Spacing: 11, 12 |
| [Cold Duck Time](../src/openbook/cold_duck_time.ly.tera) | M, S, B | Notice |
| [Cool Blues](../src/openbook/cool_blues.ly.tera) | M, S, B | Notice |
| [Coquette](../src/openbook/coquette.ly.tera) | M, S, B | - |
| [Daisy Bell](../src/openbook/daisy_bell.ly.tera) | M, S, B | - |
| [Dardanella](../src/openbook/dardanella.ly.tera) | M, S, B | - |
| [Dark Eyes](../src/openbook/dark_eyes.ly.tera) | M, S, B | - |
| [Darktown Strutters' Ball](../src/openbook/darktown_strutters_ball.ly.tera) | M, S, B | - |
| [Day by Day](../src/openbook/day_by_day.ly.tera) | M, S, B | Notice |
| [Day Dream](../src/openbook/day_dream.ly.tera) | M, S, B | - |
| [Day in, Day out](../src/openbook/day_in_day_out.ly.tera) | M, S, B | Notice |
| [Deck the Halls](../src/openbook/deck_the_halls.ly.tera) | M, S, B | - |
| [Deep Purple](../src/openbook/deep_purple.ly.tera) | M, S, B | - |
| [Detour Ahead](../src/openbook/detour_ahead.ly.tera) | M, S, B, A, E | Notice |
| [Diane](../src/openbook/diane.ly.tera) | M, S, B | - |
| [Dig](../src/openbook/dig.ly.tera) | M, S, B | Notice; Route: to coda at 30, coda at 33 |
| [Dippermouth Blues](../src/openbook/dippermouth_blues.ly.tera) | M, S, B | - |
| [Don't Be That Way](../src/openbook/dont_be_that_way.ly.tera) | M, S, B | Spacing: 2, 4, 6, 8, 10, 12, 14, 16, 26, 28, 30, 32 |
| [Don't Bring Lulu](../src/openbook/dont_bring_lulu.ly.tera) | M, S, B | - |
| [Don't Go To Strangers](../src/openbook/dont_go_to_strangers.ly.tera) | M, S, B | Spacing: 7, 15, 31; Notice |
| [Doodle-Doo-Doo](../src/openbook/doodle_doo_doo.ly.tera) | M, S, B | - |
| [Dream a Little Dream of Me](../src/openbook/dream_a_little_dream_of_me.ly.tera) | M, S, B | - |
| [Dream Dancing](../src/openbook/dream_dancing.ly.tera) | M, S, B | Spacing: 52; Notice |
| [Drink to Me Only with Thine Eyes](../src/openbook/drink_to_me_only_with_thine_eyes.ly.tera) | M, S, B | - |
| [El Choclo](../src/openbook/el_choclo.ly.tera) | M, S, B | Endings: 25, 34 |
| [Embraceable You](../src/openbook/embraceable_you.ly.tera) | M, S, B | Spacing: 4, 12, 16, 20, 24, 31, 32 |
| [Emily](../src/openbook/emily.ly.tera) | M, S, B | - |
| [Estate](../src/openbook/estate.ly.tera) | M, S, B | Notice |
| [Everything I Have Is Yours](../src/openbook/everything_i_have_is_yours.ly.tera) | M, S, B | Spacing: 16 |
| [Fascinating Rhythm](../src/openbook/fascinating_rhythm.ly.tera) | M, S, B | Spacing: 8, 24 |
| [Feel Like Makin' Love](../src/openbook/feel_like_makin_love.ly.tera) | M, S, B | - |
| [Five Foot Two, Eyes of Blue](../src/openbook/five_foot_two_eyes_of_blue.ly.tera) | M, S, B | - |
| [Fools rush in](../src/openbook/fools_rush_in.ly.tera) | M, S, B | Notice |
| [For Heaven's Sake](../src/openbook/for_heavens_sake.ly.tera) | M, S, B | Spacing: 21; Notice |
| [Four on Six](../src/openbook/four_on_six.ly.tera) | M, S, B | Notice |
| [Full Moon And Empty Arms](../src/openbook/full_moon_and_empty_arms.ly.tera) | M, S, B | Spacing: 3, 7, 13, 19, 23, 31; Notice |
| [Get Happy](../src/openbook/get_happy.ly.tera) | M, S, B | Spacing: 33 |
| [God Rest Ye Merry, Gentlemen](../src/openbook/god_rest_ye_merry_gentlemen.ly.tera) | M, S, B | - |
| [Golliwog's Cakewalk](../src/openbook/golliwog_s_cakewalk.ly.tera) | M, S, B | - |
| [Good Morning Heartache](../src/openbook/good_morning_heartache.ly.tera) | M, S, B | Spacing: 8 |
| [Goodbye](../src/openbook/goodbye.ly.tera) | M, S, B | Spacing: 18; Notice |
| [Groove Merchant](../src/openbook/groove_merchant.ly.tera) | M, S, B | Notice |
| [Happy Days Are Here Again](../src/openbook/happy_days_are_here_again.ly.tera) | M, S, B | Route: segno at 3, Fine at 19 |
| [Hard Times Come Again No More](../src/openbook/hard_times_come_again_no_more.ly.tera) | M, S, B | - |
| [Haunted Ballroom](../src/openbook/haunted_ballroom.ly.tera) | M, S, B | Notice; Route: Fine at 8, D.C. at 24 |
| [He Was Too Good To Me](../src/openbook/he_was_too_good_to_me.ly.tera) | M, S, B | Spacing: 6, 16, 20, 23, 25, 27, 32, 36, 39, 40, 45; Notice |
| [Hello! Ma Baby](../src/openbook/hello_ma_baby.ly.tera) | M, S, B | - |
| [Hey there](../src/openbook/hey_there.ly.tera) | M, S, B | Route: to coda at 5, coda at 17 |
| [Hindustan](../src/openbook/hindustan.ly.tera) | M, S, B | - |
| [House of Jade](../src/openbook/house_of_jade.ly.tera) | M, S, B | Notice |
| [How About You](../src/openbook/how_about_you.ly.tera) | M, S, B | Notice; Endings: 50 |
| [How Long Has This Been Going On?](../src/openbook/how_long_has_this_been_going_on.ly.tera) | M, S, B | Spacing: 8, 10, 14, 18 |
| [I Ain't Gonna Give Nobody None Of My Jelly Roll](../src/openbook/i_aint_gonna_give_nobody_none_of_my_jelly_roll.ly.tera) | M, S, B | - |
| [I Can't Believe That You're in Love with Me](../src/openbook/i_cant_believe_that_youre_in_love_with_me.ly.tera) | M, S, B | - |
| [I Didn't Know About You](../src/openbook/i_didnt_know_about_you.ly.tera) | M, S, B | Spacing: 7, 15, 16 |
| [I Get A Kick Out Of You](../src/openbook/i_get_a_kick_out_of_you.ly.tera) | M, S, B | Spacing: 4, 15, 20, 27, 52; Notice |
| [I Hadn't Anyone Till You](../src/openbook/i_hadnt_anyone_till_you.ly.tera) | M, S, B | - |
| [I Hear a Rhapsody](../src/openbook/i_hear_a_rhapsody.ly.tera) | M, S, B | Spacing: 21 |
| [I Hear Music](../src/openbook/i_hear_music.ly.tera) | M, S, B | Notice |
| [I Know That You Know](../src/openbook/i_know_that_you_know.ly.tera) | M, S, B | - |
| [I Only Have Eyes For You](../src/openbook/i_only_have_eyes_for_you.ly.tera) | M, S, B | Spacing: 4, 8, 53; Notice |
| [I Remember You](../src/openbook/i_remember_you.ly.tera) | M, S, B | Spacing: 23, 35, 36, 37, 38; Notice |
| [I Surrender, Dear](../src/openbook/i_surrender_dear.ly.tera) | M, S, B | Spacing: 8, 20, 24, 32; Notice |
| [I Thought About You](../src/openbook/i_thought_about_you.ly.tera) | M, S, B | Spacing: 8; Notice |
| [I Wanna Be Loved by You](../src/openbook/i_wanna_be_loved_by_you.ly.tera) | M, S, B, V, E, P | Route: Fine at 9, D.C. at 18 |
| [I Want A Little Girl](../src/openbook/i_want_a_little_girl.ly.tera) | M, S, B | Notice |
| [I Want to Be Happy](../src/openbook/i_want_to_be_happy.ly.tera) | M, S, B | Spacing: 23, 24, 31, 32 |
| [I Wonder Where My Baby Is Tonight](../src/openbook/i_wonder_where_my_baby_is_tonight.ly.tera) | M, S, B | - |
| [I'll See You In My Dreams](../src/openbook/ill_see_you_in_my_dreams.ly.tera) | M, S, B | - |
| [I'm A Fool To Want You](../src/openbook/im_a_fool_to_want_you.ly.tera) | M, S, B | Spacing: 16; Notice |
| [I'm All Smiles](../src/openbook/im_all_smiles.ly.tera) | M, S, B | - |
| [I'm Getting Sentimental Over You](../src/openbook/im_getting_sentimental_over_you.ly.tera) | M, S, B | - |
| [I'm In the Mood for Love](../src/openbook/im_in_the_mood_for_love.ly.tera) | M, S, B | Spacing: 8, 18, 24; Notice |
| [I'm Through With Love](../src/openbook/im_through_with_love.ly.tera) | M, S, B | Spacing: 9, 17 |
| [I've Found a New Baby](../src/openbook/ive_found_a_new_baby.ly.tera) | M, S, B | - |
| [I've Got A Crush On You](../src/openbook/ive_got_a_crush_on_you.ly.tera) | M, S, B | Spacing: 9, 18, 19 |
| [I've Got The World On  A String](../src/openbook/ive_got_the_world_on_a_string.ly.tera) | M, S, B | Spacing: 8, 16; Notice |
| [I've Never Been In Love Before](../src/openbook/ive_never_been_in_love_before.ly.tera) | M, S, B | Spacing: 2, 3, 8, 9, 10, 18, 20, 21, 25, 26, 27; Notice |
| [If I Had You](../src/openbook/if_i_had_you.ly.tera) | M, S, B | Spacing: 7, 8, 16, 24, 31, 33 |
| [If I Loved You](../src/openbook/if_i_loved_you.ly.tera) | M, S, B | Notice |
| [If I Should Lose You](../src/openbook/if_i_should_lose_you.ly.tera) | M, S, B | Spacing: 16, 32; Notice |
| [If You Never Come To Me](../src/openbook/if_you_never_come_to_me.ly.tera) | M, S, B | Notice |
| [In A Mellow Tone](../src/openbook/in_a_mellow_tone.ly.tera) | M, S, B | - |
| [In Love in Vain](../src/openbook/in_love_in_vain.ly.tera) | M, S, B | Notice |
| [In the Wee Small Hours of the Morning](../src/openbook/in_the_wee_small_hours_of_the_morning.ly.tera) | M, S, B | Spacing: 9, 13, 15 |
| [Indian Love Call](../src/openbook/indian_love_call.ly.tera) | M, S, B | - |
| [Indian Summer](../src/openbook/indian_summer.ly.tera) | M, S, B | Notice |
| [Interplay](../src/openbook/interplay.ly.tera) | M, S, B | Notice |
| [Isfahan](../src/openbook/isfahan.ly.tera) | M, S, B | Notice |
| [Israel](../src/openbook/israel.ly.tera) | M, S, B | Notice |
| [It Could Happen To You](../src/openbook/it_could_happen_to_you.ly.tera) | M, S, B | Spacing: 8, 12, 24, 28, 31, 33; Notice |
| [It Had To Be You](../src/openbook/it_had_to_be_you.ly.tera) | M, S, B | Spacing: 2, 4, 8, 12, 18, 20, 24, 32, 34 |
| [It's De-lovely](../src/openbook/its_de_lovely.ly.tera) | M, S, B | - |
| [It's You Or No One](../src/openbook/its_you_or_no_one.ly.tera) | M, S, B | Spacing: 31; Notice |
| [Ja-Da](../src/openbook/ja_da.ly.tera) | M, S, B | Spacing: 4, 8, 16 |
| [Jeanie with the Light Brown Hair](../src/openbook/jeanie_with_the_light_brown_hair.ly.tera) | M, S, B | - |
| [Jeepers Creepers](../src/openbook/jeepers_creepers.ly.tera) | M, S, B | Notice |
| [Jelly Roll](../src/openbook/jelly_roll.ly.tera) | M, S, B | Notice |
| [Jive Samba](../src/openbook/jive_samba.ly.tera) | M, S, B | Notice; Route: segno at 5, coda at 21, D.S. at 21, coda at 22 |
| [Joy Spring](../src/openbook/joy_spring.ly.tera) | M, S, B | Notice |
| [Jump Monk](../src/openbook/jump_monk.ly.tera) | M, S, B | Notice |
| [Just Squeeze Me](../src/openbook/just_squeeze_me.ly.tera) | M, S, B | - |
| [Just You, Just Me](../src/openbook/just_you_just_me.ly.tera) | M, S, B | Spacing: 18 |
| [Le Temps des Cerises](../src/openbook/le_temps_des_cerises.ly.tera) | M, S, B | - |
| [Lester Leaps In](../src/openbook/lester_leaps_in.ly.tera) | M, S, B | Notice |
| [Let's Do It (Let's Fall in Love)](../src/openbook/lets_do_it_lets_fall_in_love.ly.tera) | M, S, B | - |
| [Like A Lover](../src/openbook/like_a_lover.ly.tera) | M, S, B | Notice |
| [Limehouse Blues](../src/openbook/limehouse_blues.ly.tera) | M, S, B | - |
| [Little B's Poem](../src/openbook/little_bs_poem.ly.tera) | M, S, B | Notice |
| [Little Rootie Tootie](../src/openbook/little_rootie_tootie.ly.tera) | M, S, B | Notice |
| [Little White Lies](../src/openbook/little_white_lies.ly.tera) | M, S, B | Spacing: 33 |
| [Liza (All the Clouds'll Roll Away)](../src/openbook/liza_all_the_cloudsll_roll_away.ly.tera) | M, S, B | Spacing: 15, 16, 18, 22, 26, 30, 34, 35, 38, 39, 46, 50 |
| [Lonnie's Lament](../src/openbook/lonnies_lament.ly.tera) | M, S, B, A, E | Notice |
| [Louise](../src/openbook/louise.ly.tera) | M, S, B | Spacing: 16 |
| [Love Is A Many Splendored Thing](../src/openbook/love_is_a_many_splendored_thing.ly.tera) | M, S, B | - |
| [Love Is Just Around The Corner](../src/openbook/love_is_just_around_the_corner.ly.tera) | M, S, B | Spacing: 6, 14, 32; Notice |
| [Love Me Or Leave Me](../src/openbook/love_me_or_leave_me.ly.tera) | M, S, B | Spacing: 15, 24, 32, 33 |
| [Lulu's Back in Town](../src/openbook/lulus_back_in_town.ly.tera) | M, S, B | Spacing: 17; Notice |
| [Makin' Whoopee](../src/openbook/makin_whoopee.ly.tera) | M, S, B | Spacing: 19; Route: segno at 2 |
| [Mamacita](../src/openbook/mamacita.ly.tera) | M, S, B | - |
| [Marie](../src/openbook/marie.ly.tera) | M, S, B | - |
| [Memphis Blues](../src/openbook/memphis_blues.ly.tera) | M, S, B | - |
| [Midnight Mood](../src/openbook/midnight_mood.ly.tera) | M, S, B | Notice; Route: Fine at 23 |
| [Minority](../src/openbook/minority.ly.tera) | M, S, B | Notice |
| [Moon and Sand](../src/openbook/moon_and_sand.ly.tera) | M, S, B | Spacing: 1, 5, 7, 8, 15, 19, 29, 31, 32, 39, 40 |
| [Mountain Greenery](../src/openbook/mountain_greenery.ly.tera) | M, S, B | - |
| [Mr. Lucky](../src/openbook/mr_lucky.ly.tera) | M, S, B | - |
| [Muskrat Ramble](../src/openbook/muskrat_ramble.ly.tera) | M, S, B | - |
| [My Baby Just Cares For Me](../src/openbook/my_baby_just_cares_for_me.ly.tera) | M, S, B | Spacing: 7, 23, 28, 31 |
| [My Blue Heaven](../src/openbook/my_blue_heaven.ly.tera) | M, S, B | - |
| [My Bonnie Lies over the Ocean](../src/openbook/my_bonnie_lies_over_the_ocean.ly.tera) | M, S, B | - |
| [My Buddy](../src/openbook/my_buddy.ly.tera) | M, S, B | - |
| [My Heart Stood Still](../src/openbook/my_heart_stood_still.ly.tera) | M, S, B | Spacing: 7, 15, 24, 31, 32 |
| [My Ideal](../src/openbook/my_ideal.ly.tera) | M, S, B | Spacing: 6, 12, 28 |
| [My Old Flame](../src/openbook/my_old_flame.ly.tera) | M, S, B | Notice |
| [Never Let Me Go](../src/openbook/never_let_me_go.ly.tera) | M, S, B | Spacing: 27; Notice |
| [Nice 'N' Easy](../src/openbook/nice_n_easy.ly.tera) | M, S, B | Spacing: 8, 15, 16, 24, 31, 35, 36, 37; Notice |
| [Night Train](../src/openbook/night_train.ly.tera) | M, S, B | Notice; Route: D.C. at 32, Fine at 44 |
| [No Me Esqueca](../src/openbook/no_me_esqueca.ly.tera) | M, S, B | - |
| [No Moe](../src/openbook/no_moe.ly.tera) | M, S, B | Notice |
| [Nobody Else but Me](../src/openbook/nobody_else_but_me.ly.tera) | M, S, B | Notice |
| [Nobody Knows You When You're Down and Out](../src/openbook/nobody_knows_you_when_youre_down_and_out.ly.tera) | M, S, B | - |
| [Nostalgia in Times Square](../src/openbook/nostalgia_in_times_square.ly.tera) | M, S, B | Notice; Endings: 13 |
| [O Christmas Tree](../src/openbook/o_christmas_tree.ly.tera) | M, S, B | - |
| [Oh My Darling, Clementine](../src/openbook/oh_my_darling_clementine.ly.tera) | M, S, B | - |
| [Oh, Lady Be Good!](../src/openbook/oh_lady_be_good.ly.tera) | M, S, B | Spacing: 31, 33 |
| [On the Alamo](../src/openbook/on_the_alamo.ly.tera) | M, S, B | - |
| [Once In A While](../src/openbook/once_in_a_while.ly.tera) | M, S, B | Spacing: 4, 7, 8, 12, 15, 24, 28, 31; Notice |
| [One For My Baby](../src/openbook/one_for_my_baby.ly.tera) | M, S, B | Spacing: 5, 13, 21, 25, 29, 37, 45, 49, 53, 56, 59; Notice |
| [Our Delight](../src/openbook/our_delight.ly.tera) | M, S, B | Notice |
| [Out of This World](../src/openbook/out_of_this_world.ly.tera) | M, S, B | - |
| [Pent-Up House](../src/openbook/pent_up_house.ly.tera) | M, S, B | Notice |
| [Phase Dance](../src/openbook/phase_dance.ly.tera) | M, S, B | Notice |
| [Play A Simple Melody](../src/openbook/play_a_simple_melody.ly.tera) | M, S, B | - |
| [Pussy Cat Dues](../src/openbook/pussy_cat_dues.ly.tera) | M, S, B | Notice |
| [Puttin' on the Ritz](../src/openbook/puttin_on_the_ritz.ly.tera) | M, S, B | Spacing: 16, 23, 31, 48, 49 |
| [Recorda-Me](../src/openbook/recorda_me.ly.tera) | M, S, B | Notice |
| [Remember](../src/openbook/remember.ly.tera) | M, S, B | - |
| [Rhythm-a-Ning](../src/openbook/rhythm_a_ning.ly.tera) | M, S, B | Notice |
| [Rose of Washington Square](../src/openbook/rose_of_washington_square.ly.tera) | M, S, B | - |
| [Runnin' Wild](../src/openbook/runnin_wild.ly.tera) | M, S, B | - |
| [Russian Lullaby](../src/openbook/russian_lullaby.ly.tera) | M, S, B | - |
| [Sandu](../src/openbook/sandu.ly.tera) | M, S, B | Notice; Route: to coda at 10, coda at 28 |
| [Save Your Love For Me](../src/openbook/save_your_love_for_me.ly.tera) | M, S, B | - |
| [Secret Love](../src/openbook/secret_love.ly.tera) | M, S, B | Notice |
| [September in the Rain](../src/openbook/september_in_the_rain.ly.tera) | M, S, B, V, E, P | Spacing: 8, 20 |
| [Serenata](../src/openbook/serenata.ly.tera) | M, S, B | - |
| [Shchedryk](../src/openbook/shchedryk.ly.tera) | M, S, B | - |
| [Simone](../src/openbook/simone.ly.tera) | M, S, B | Notice |
| [Since I Fell For You](../src/openbook/since_i_fell_for_you.ly.tera) | M, S, B | Spacing: 1, 3, 5, 7, 9, 11, 13, 26, 28, 30, 33 |
| [Sleepy Time Gal](../src/openbook/sleepy_time_gal.ly.tera) | M, S, B | Spacing: 32 |
| [Slow Hot Wind](../src/openbook/slow_hot_wind.ly.tera) | M, S, B | Notice |
| [Small Fry](../src/openbook/small_fry.ly.tera) | M, S, B | Notice |
| [So In Love](../src/openbook/so_in_love.ly.tera) | M, S, B | - |
| [So Many Stars](../src/openbook/so_many_stars.ly.tera) | M, S, B | Spacing: 36; Notice |
| [Some Other Blues](../src/openbook/some_other_blues.ly.tera) | M, S, B | Notice |
| [Some Other Time](../src/openbook/some_other_time.ly.tera) | M, S, B | Spacing: 32, 40 |
| [Some Sunny Day](../src/openbook/some_sunny_day.ly.tera) | M, S, B | - |
| [Somebody Loves Me](../src/openbook/somebody_loves_me.ly.tera) | M, S, B | Spacing: 29 |
| [Somebody Stole My Gal](../src/openbook/somebody_stole_my_gal.ly.tera) | M, S, B | - |
| [Someone to Light up My Life](../src/openbook/someone_to_light_up_my_life.ly.tera) | M, S, B | - |
| [Sonnymoon for Two](../src/openbook/sonnymoon_for_two.ly.tera) | M, S, B | Notice |
| [Soon](../src/openbook/soon.ly.tera) | M, S, B | - |
| [Speak No Evil](../src/openbook/speak_no_evil.ly.tera) | M, S, B | Notice |
| [Spring Is Here](../src/openbook/spring_is_here.ly.tera) | M, S, B | Spacing: 33 |
| [St. Louis Blues](../src/openbook/st_louis_blues.ly.tera) | M, S, B | Spacing: 52, 53, 56, 57 |
| [Stairway To The Stars](../src/openbook/stairway_to_the_stars.ly.tera) | M, S, B | Spacing: 7, 8, 16, 20, 24 |
| [Stars Fell On Alabama](../src/openbook/stars_fell_on_alabama.ly.tera) | M, S, B | Spacing: 7, 8, 9, 32 |
| [Straight, No Chaser](../src/openbook/straight_no_chaser.ly.tera) | M, S, B | Notice |
| [Streets of Laredo](../src/openbook/streets_of_laredo.ly.tera) | M, S, B | - |
| [Strode Rode](../src/openbook/strode_rode.ly.tera) | M, S, B | Notice |
| [Sugar Blues](../src/openbook/sugar_blues.ly.tera) | M, S, B | - |
| [Sunday](../src/openbook/sunday.ly.tera) | M, S, B | - |
| [Swanee](../src/openbook/swanee.ly.tera) | M, S, B | - |
| [Sweet Lorraine](../src/openbook/sweet_lorraine.ly.tera) | M, S, B | - |
| [Taking A Chance On Love](../src/openbook/taking_a_chance_on_love.ly.tera) | M, S, B | Spacing: 8 |
| [Tangerine](../src/openbook/tangerine.ly.tera) | M, S, B | Notice |
| [Tea for Two](../src/openbook/tea_for_two.ly.tera) | M, S, B | - |
| [Teach Me Tonight](../src/openbook/teach_me_tonight.ly.tera) | M, S, B | Spacing: 16, 32, 34 |
| [That Certain Feeling](../src/openbook/that_certain_feeling.ly.tera) | M, S, B | - |
| [That Old Black Magic](../src/openbook/that_old_black_magic.ly.tera) | M, S, B | Notice |
| [That Old Feeling](../src/openbook/that_old_feeling.ly.tera) | M, S, B | Spacing: 16, 28, 32 |
| [That's a Plenty](../src/openbook/thats_a_plenty.ly.tera) | M, S, B | Route: Fine at 10, D.C. at 26 |
| [The Birth of the Blues](../src/openbook/the_birth_of_the_blues.ly.tera) | M, S, B | Spacing: 20, 34 |
| [The Boy Next Door](../src/openbook/the_boy_next_door.ly.tera) | M, S, B | Spacing: 32, 33; Notice |
| [The Inch Worm](../src/openbook/the_inch_worm.ly.tera) | M, S, B | Notice; Route: Fine at 10 |
| [The Japanese Sandman](../src/openbook/the_japanese_sandman.ly.tera) | M, S, B | - |
| [The Man on the Flying Trapeze](../src/openbook/the_man_on_the_flying_trapeze.ly.tera) | M, S, B | - |
| [The Midnight Sun Will Never Set](../src/openbook/the_midnight_sun_will_never_set.ly.tera) | M, S, B | Spacing: 2, 4, 19, 21; Notice |
| [The Moontrane](../src/openbook/the_moontrane.ly.tera) | M, S, B | Notice |
| [The Night We Called It A Day](../src/openbook/the_night_we_called_it_a_day.ly.tera) | M, S, B | Spacing: 17, 21; Notice |
| [The Second Time Around](../src/openbook/the_second_time_around.ly.tera) | M, S, B | - |
| [The Summer Knows](../src/openbook/the_summer_knows.ly.tera) | M, S, B | - |
| [The Sweetest Sounds](../src/openbook/the_sweetest_sounds.ly.tera) | M, S, B | Spacing: 16; Notice |
| [The Very Thought Of You](../src/openbook/the_very_thought_of_you.ly.tera) | M, S, B | Spacing: 13; Notice |
| [Them There Eyes](../src/openbook/them_there_eyes.ly.tera) | M, S, B | - |
| [There Goes My Heart](../src/openbook/there_goes_my_heart.ly.tera) | M, S, B | Spacing: 12, 32, 34; Notice |
| [They Say It's Wonderful](../src/openbook/they_say_its_wonderful.ly.tera) | M, S, B | Spacing: 31; Notice |
| [Things Ain't What They Used to Be](../src/openbook/things_aint_what_they_used_to_be.ly.tera) | M, S, B | Notice; Route: to coda at 10, D.C. at 24, coda at 25 |
| [Thou Swell](../src/openbook/thou_swell.ly.tera) | M, S, B | - |
| [Three Little Words](../src/openbook/three_little_words.ly.tera) | M, S, B | - |
| [Tiger Rag](../src/openbook/tiger_rag.ly.tera) | M, S, B | - |
| [Till There Was You](../src/openbook/till_there_was_you.ly.tera) | M, S, B | Notice |
| [Till We Meet Again](../src/openbook/till_we_meet_again.ly.tera) | M, S, B | - |
| [Time on My Hands](../src/openbook/time_on_my_hands.ly.tera) | M, S, B | Spacing: 31, 33 |
| [Time Was](../src/openbook/time_was.ly.tera) | M, S, B | Spacing: 7, 15, 31; Notice |
| [Too Close For Comfort](../src/openbook/too_close_for_comfort.ly.tera) | M, S, B | Notice |
| [Too Marvelous For Words](../src/openbook/too_marvelous_for_words.ly.tera) | M, S, B | Notice |
| [Tricotism](../src/openbook/tricotism.ly.tera) | M, S, B | Notice |
| [Trouble In Mind](../src/openbook/trouble_in_mind.ly.tera) | M, S, B | - |
| [Trouble Is A Man](../src/openbook/trouble_is_a_man.ly.tera) | M, S, B | Spacing: 9 |
| [Turn Out the Stars](../src/openbook/turn_out_the_stars.ly.tera) | M, S, B | - |
| [Two for the Road](../src/openbook/two_for_the_road.ly.tera) | M, S, B | - |
| [Two Guitars](../src/openbook/two_guitars.ly.tera) | M, S, B | - |
| [Unless It's You](../src/openbook/unless_its_you.ly.tera) | M, S, B | - |
| [Up Jumped Spring](../src/openbook/up_jumped_spring.ly.tera) | M, S, B | Notice |
| [Virgo](../src/openbook/virgo.ly.tera) | M, S, B | Notice |
| [Waltz New](../src/openbook/waltz_new.ly.tera) | M, S, B | Route: to coda at 31, D.C. at 32, coda at 33 |
| [Warm Valley](../src/openbook/warm_valley.ly.tera) | M, S, B | - |
| [We Wish You a Merry Christmas](../src/openbook/we_wish_you_a_merry_christmas.ly.tera) | M, S, B | - |
| [We'll Be Together Again](../src/openbook/well_be_together_again.ly.tera) | M, S, B | Spacing: 9, 33; Notice |
| [What A Little Moonlight Can Do](../src/openbook/what_a_little_moonlight_can_do.ly.tera) | M, S, B | Spacing: 10, 58; Notice |
| [What Am I Here For](../src/openbook/what_am_i_here_for.ly.tera) | M, S, B | - |
| [What Are You Doing the Rest of Your Life?](../src/openbook/what_are_you_doing_the_rest_of_your_life.ly.tera) | M, S, B | Spacing: 43 |
| [What Is This Thing Called Love?](../src/openbook/what_is_this_thing_called_love.ly.tera) | M, S, B | Spacing: 4, 12 |
| [When I Look In Your Eyes](../src/openbook/when_i_look_in_your_eyes.ly.tera) | M, S, B | Spacing: 7, 8, 15, 23 |
| [When Irish Eyes Are Smiling](../src/openbook/when_irish_eyes_are_smiling.ly.tera) | M, S, B | - |
| [When Sunny Gets Blue](../src/openbook/when_sunny_gets_blue.ly.tera) | M, S, B | Spacing: 5, 9, 13, 17, 29, 33, 34; Notice |
| [When the Saints Go Marching In](../src/openbook/when_the_saints_go_marching_in.ly.tera) | M, S, B | - |
| [When The Sun Comes Out](../src/openbook/when_the_sun_comes_out.ly.tera) | M, S, B | Spacing: 36; Notice |
| [When You Wore a Tulip](../src/openbook/when_you_wore_a_tulip.ly.tera) | M, S, B | - |
| [Where Are You?](../src/openbook/where_are_you.ly.tera) | M, S, B | - |
| [Whispering](../src/openbook/whispering.ly.tera) | M, S, B | - |
| [Who Cares](../src/openbook/who_cares.ly.tera) | M, S, B | - |
| [Who's Sorry Now](../src/openbook/whos_sorry_now.ly.tera) | M, S, B | - |
| [With a Song in My Heart](../src/openbook/with_a_song_in_my_heart.ly.tera) | M, S, B | Spacing: 15, 16, 26, 31 |
| [With Every Breath I Take](../src/openbook/with_every_breath_i_take.ly.tera) | M, S, B | Notice |
| [Without a Song](../src/openbook/without_a_song.ly.tera) | M, S, B | Spacing: 16, 21 |
| [Woody 'n' You](../src/openbook/woody_n_you.ly.tera) | M, S, B | - |
| [Yes Sir, That's My Baby](../src/openbook/yes_sir_thats_my_baby.ly.tera) | M, S, B | - |
| [You Are Too Beautiful](../src/openbook/you_are_too_beautiful.ly.tera) | M, S, B | Spacing: 4, 8, 12, 15, 16, 24, 28, 31, 32 |
| [You Do Something to Me](../src/openbook/you_do_something_to_me.ly.tera) | M, S, B | Spacing: 17, 31, 32 |
| [You Make Me Feel So Young](../src/openbook/you_make_me_feel_so_young.ly.tera) | M, S, B | Spacing: 2, 10, 20, 31, 33 |
| [You Must Believe In Spring](../src/openbook/you_must_believe_in_spring.ly.tera) | M, S, B | Spacing: 8, 16 |
| [You Say You Care](../src/openbook/you_say_you_care.ly.tera) | M, S, B | Notice |
| [You Stepped Out Of A Dream](../src/openbook/you_stepped_out_of_a_dream.ly.tera) | M, S, B | - |
| [You Took Advantage Of Me](../src/openbook/you_took_advantage_of_me.ly.tera) | M, S, B | Spacing: 8, 24, 32 |
| [You'll Never Know](../src/openbook/youll_never_know.ly.tera) | M, S, B | - |
| [You're Driving Me Crazy](../src/openbook/youre_driving_me_crazy.ly.tera) | M, S, B | Spacing: 31, 33 |
| [You're The Top](../src/openbook/youre_the_top.ly.tera) | M, S, B | Spacing: 16, 32, 34 |
| [Yours Is My Heart Alone](../src/openbook/yours_is_my_heart_alone.ly.tera) | M, S, B | Spacing: 7; Notice |
