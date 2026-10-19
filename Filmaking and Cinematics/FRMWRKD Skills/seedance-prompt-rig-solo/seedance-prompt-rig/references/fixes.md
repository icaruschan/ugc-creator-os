# Fixes

Symptom → cause → fix. Read the symptom column, not the whole file.

---

## Read this first

Three causes account for most of what ends up in this table. Check them before scanning anything
below.

1. **A reference bound without a `NOT` clause.** Everything in the plate arrives — pose, framing,
   grade, time of day — and it overrides what you wrote. Every role line in `ACTIVE REFERENCES`
   needs its exclusions. [binding.md](binding.md).
2. **Two camera moves in one beat.** Stacked moves jitter on every Seedance version. One move per
   beat; the second move is a second beat and a cut.
3. **A fact restated in more than one block.** Restatement is not emphasis — the model re-decides
   the fact at every copy, and the copies do not have to agree. One fact, one tier, one block.

---

## Identity and references

| Symptom | Cause | Fix |
|---|---|---|
| Face resembles the reference but is subtly wrong | reference bound without exclusions, so pose and framing bled in | add the `NOT` clause to that role line: `@Image2 → head: skin, glasses, eyes. NOT the pose, NOT the framing.` |
| Two copies of the same character in frame ("twins") | ambiguous pronouns, or too many simultaneous subjects | name every character in `CAST` and use the name every time, never "he/him" across characters. State it positively in `POSITIVE LOCKS` — `exactly one <character> is present in every frame`. Drop to two performers |
| A close-up reference overrode the wide blocking | the reference took its framing as an instruction | `NOT the framing` on that role line |
| Wardrobe changes between shots | wardrobe stated in a beat instead of the CONTEXT tier | hoist it into `WARDROBE`, reuse the CONTEXT tier verbatim |
| Location looks generic, not like the plate | location reference unbound, or bound loosely | `@ImageN → the set: architecture, materials, light through the seams. NOT any person in it.` |
| An attribute migrated from one character to another | too many references live in one shot | subset per beat. Send each beat only the plates it needs |
| Faces flat and expressionless | no reference attached; prompt-only identity | documented weakness of text2video. Attach a face reference, or accept it. `PERFORMANCE` and a `GAZE AND EYELINES` ladder recover some of it |
| Face drifts toward a familiar screen actor | same cause | same fix. Add one unrepeatable marker to `CAST` |

---

## Camera

| Symptom | Cause | Fix |
|---|---|---|
| Camera jitters and wanders | more than one move in `CAMERA` | keep one. The second move becomes a second beat and a cut |
| Camera drifts when it should be locked | the lock was never stated | write `locked off, the frame does NOT travel` in `CAMERA` **and** set `camera_fixed` |
| The move opens out to a wide you did not ask for | no framing floor stated | add "stays medium-close and NEVER opens to a wide" to that beat's `LENS` |
| Scale drifts across cuts, coverage reads as four versions of the same frame | no `LENS` line per beat | give every beat its own shot size and framing floor |
| Blue streak flares you did not want | "anamorphic" drags them in | `oval bokeh and horizontal stretch, NOT flares, NOT streaks`, and bake the anamorphic character into the plate at the image stage — [finish.md](finish.md) §3 |
| The final frame lands somewhere arbitrary | `CAMERA` has no ending | give the move a destination — "settling when her eyes find the lens" |
| Shot reads flat, no depth | subjects arranged across frame instead of in depth | stage foreground / mid / background explicitly in `LOCATION MAP`. Name a long lens in `LENS` |

---

## Motion and action

| Symptom | Cause | Fix |
|---|---|---|
| Action looks weightless | no consequence written | say where the energy goes in `ACTION` — heels plough, dust bursts, the line buckles |
| Limbs stretch or ghost | fast motion, or several impacts competing for the same second | one impact per beat. Slow the camera. Simplify the frame |
| A strike stops dead at contact | no follow-through | "the blade tracks past and out of frame, never stopping, never bouncing back" |
| A landing floats | no recovery written | add the knees absorbing and the stagger, and state recovery as a rule in `PHYSICS` |
| Crowd is visibly cloned | default behaviour | say "varied, not repeated". Stage them in depth in `LOCATION MAP` and give them one collective action |
| Whole shot is a blur | fast camera + fast cut + busy frame together | pick one. Usually: lock the camera and let the event carry it |
| Two characters play two different scenes; the performance is technically correct and inert | no `EVENT AND SHARED DIRECTION` | name the event from how the scene ends, and give every character in frame a task — including the silent listeners. [acting-task.md](acting-task.md) |

---

## Cuts and sequence

| Symptom | Cause | Fix |
|---|---|---|
| Multi-shot prompt rendered as one continuous take | the shots were never labelled and no out-point was written | label them `BEAT 1` / `EDIT: hard cut.` / `BEAT 2` |
| Identity drifts from the third cut onward | over the model's cut budget | 1.0: 2 shots · 1.5: 2–3 · 2.0: 3–4 · 2.5: 5–6. Split into two clips |
| Coverage flips sides between cuts and stops intercutting | the axis was never stated | say which side of the line the camera stays on in `STAGING` — it is staging, not camera |
| Model rushes or stalls to hit timings | hard timecodes | order the clauses with `→` inside `ACTION`. Timecodes only for audio sync or range edits |
| Two clips will not intercut | the CONTEXT tier was retyped instead of pasted | paste it verbatim into both. Chain the last frame of A into the first frame of B |
| Sequence stops intercutting between clips | the `PROMPT SEGMENTS` tier was retyped rather than pasted | paste it identically into every clip. A reworded `VOICE`, `STYLE` or `PHYSICS` re-rolls what it describes |
| An extension does not match | a new clip instead of a real extension | on 2.5 use the extension path; it carries subject, scene, style and sound. Write the last beat's `EDIT` locked and motionless |

---

## Audio and dialogue

| Symptom | Cause | Fix |
|---|---|---|
| Video is silent | the model is Seedance 1.0, which has no audio at all | move to 1.5 pro or above. On 1.0, drop `AUDIO`, `SCORE`, `SFX` and `DIALOGUE` — the words are wasted |
| Lips move but delivery is rushed, sync slips | the line is longer than duration × 2.5 words | cut the line, or lengthen the clip |
| Dialogue came out in the wrong language | language not anchored | anchor it in `VOICE`, once, before any braces appear |
| Voice changes between shots | no voice identity locked | fix a 4–6 attribute string per speaker in `VOICE` and paste it unchanged — a synonym is a drift. Or bind an audio reference |
| Music appeared and you did not want it | silence was never stated | `SCORE: none. NO music of any kind at any point.` |
| Sound is generic mush | audio described in prose | bracket grammar. One event per `< >` pair, in the order they happen |
| A direction was spoken aloud | the direction went inside the braces | `{sadly} Don't.` says the word "sadly". Intention goes before the braces in `DIALOGUE`; only the words go inside them |
| Everything crossed into the dialogue track | an unbalanced brace | check the bracket pairs. The linter catches this |
| Both characters talk and it falls apart | two speakers in one shot | one speaker per beat, cut between them |

---

## Text

| Symptom | Cause | Fix |
|---|---|---|
| On-screen text is garbled | the model's worst area, near-unavoidable on every version | generate clean, add type in post. This is not fixable by prompting |
| Subtitles burned in uninvited | speech invites them | `TYPOGRAPHY: none.` plus a positive lock naming what the frame does contain — `the frame contains the two men, the windscreen and the road only` |
| A required word came out wrong | its weight was too low | wrap the exact string in quotes: `the sign reads "OPEN"`. Accept the odds |
| A logo or emblem came back corrupted | it was asked for in video text | bake it into the reference plate at the image stage, or composite it in post — [finish.md](finish.md) §3 |

---

## Prompt-level

| Symptom | Cause | Fix |
|---|---|---|
| Model ignored something you said five times | repetition dilutes rather than emphasises | one fact, one tier, one block. [density.md](density.md) |
| The model rendered a constant differently in different beats | the constant is sitting in BEATS instead of CONTEXT or PROMPT SEGMENTS | apply the lifespan test — "would I have to write this again in beat four?" — and hoist it. `seedance.py lint` reports every fact it finds in more than one beat and prices the hoist |
| Prompt is over its working ceiling | restatement | the ceiling scales with duration: 400 + 45 × duration. Run the seven cuts in [density.md](density.md). Expect 4:1 |
| Something in `POSITIVE LOCKS` still drifted | the lock restates something the beats already say clearly, so it is diluting the locks that matter | cut it back to 4–6 clauses that name only what a render actually dropped |
| Something you banned turned up in the frame | negations seed their own terms — the model parses the noun, not the refusal | state the positive instead, in `POSITIVE LOCKS`. `no extra people` becomes `exactly two men are present for the whole clip` |
| The stylised look drifts back to photoreal by shot four | `STYLE LOCK` missing, or written once and then paraphrased | keep it immutable and paste it verbatim into every clip of the project |
| Both `STYLE LOCK` and `POSITIVE LOCKS` are loaded and the render is muddy | the register was never decided | photoreal takes `POSITIVE LOCKS` and no negations; stylised takes `STYLE LOCK`, where the negations are load-bearing. One or the other, never both |
| Render was rejected by the platform | violence keyword, real-person face reference, brand or celebrity name | describe by build and wardrobe. Cut away before contact. Sparks, no blood |
| Aspect ratio ignored | the ratio was written into the prompt body | it is an API parameter. Keep it in `FORMAT MODE` for the human and out of the body |
| Requested 30 s at 1080p and it failed | Seedance 2.5 is capped at 720p | 15 s on 2.0 for 1080p, or accept 720p |
| Bill much higher than estimated | reference videos bill for their own duration | trim the reference videos. Note the ×0.6 rate offset — [models.md](models.md) |

---

## Video-to-video and blockouts

| Symptom | Cause | Fix |
|---|---|---|
| The actors copy the reference video's motion — flat hinged arms, a glide, a torso that never bends | the role line shouted `IGNORE THE MOVEMENT` in capitals and the performance got two lines; the model was handed nothing positive to perform | one compact role line for the video, then spend everything on concrete physical verbs in `ACTION`, `PHYSICS`, `PERFORMANCE`. [blockout.md](blockout.md) §1–3 |
| The location came back as a bare tiled tunnel | `SCENE CONTEXT` described materials only — tile, brass, timber, concrete — which a tunnel satisfies perfectly | name the fixtures: the pastry case, the speaker cabinets, the bentwood chairs, the rug. Contents identify a room; materials do not |
| The room was thrown away entirely | `NOT its ordinary room proportions`, or *stretched into a corridor*, inherited from a transform shot into a shot that does not transform | never exclude proportions. Write the bend as *this room extending, carrying its own furniture*, and only in the shot where the transform is the point |
| Wardrobe drifted from the turnaround | the cast plate was bound `identity ONLY` | bind face **and** whole outfit; restate garments once in `WARDROBE` with `EXACT throughout` |
| One continuous drifting take instead of the cuts | shot changes described in prose | labelled `BEAT`s with `EDIT: hard cut.` between them |
| Room reads less like the plate after adding atmosphere | steam, dust beams and haze compete with the facts that identify the room | strip the atmospherics. Restraint outperforms emphasis |
| Hours spent animating the blocks, no improvement in the render | the blockout's job is staging, camera and timing; the acting belongs to the model | leave the blocks stiff, spend the time on the words |
| Status polling returns *pending* forever (Artlist) | the `assetId` from a share URL was polled as a `generationId` | two namespaces: uploads bind as `{assetId}`, generations as `{generationId}`. [binding.md](binding.md) |

---

## Verification

| Symptom | Cause | Fix |
|---|---|---|
| Notes say *fixed*, the shot still opens on black | the script was edited and the edit assumed to have landed; the file was never opened | open the rendered file and look at frame 0 at full size before writing *fixed*. [verify.md](verify.md) |
| Two rounds of exposure correction, both wrong | exposure judged from a contact sheet | one full-size frame, delivery resolution |
| A good near-black shot rejected as broken | a file-size floor standing in for *frames differ* | test the property: frame difference, duration — never bytes |
| Half the beat events never fire | events authored past the end of the clip; nothing failed loudly | check every timestamp against duration. `seedance.py lint` errors on `timing.range` |
| Files pass every check but were built by the wrong code | two render queues running at once; provenance is not integrity | one job at a time, enforced by a lock or `pgrep`, not a sentence |
| A process looks dead, keeps producing files | its log was pipe-buffered | `pgrep`, and run long jobs unbuffered |
| The wrong location plate was bound, credits spent | guessed from history instead of asking for the file the user said existed | a stated constraint binds every later step. Ask once rather than guess twice |

---

## When nothing here fits

Change one thing and re-render. Not three. The most common debugging failure is editing five fields at once and learning nothing from the result.

If a fix generalises, offer to add it to this file — never edit it silently.
