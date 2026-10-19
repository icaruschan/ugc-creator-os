# The twenty-seven blocks

Canonical. These are the block names the ReelStack Sequence Builder opens with, and no others exist.
Keys are ALL CAPS at the head of a line; values are lower-case prose. `SCENE CONTEXT` is always
present; the other twenty-six are added when the job needs them.

**Order in the delivered prompt is CONTEXT → BEATS → PROMPT SEGMENTS.** Within a tier, use the order
below. The model reads top to bottom and builds forward, so the world arriving before the shots and
the physics arriving after both matter.

Each entry: what it carries · how to fill it · a worked line · the failure it prevents.

---

# 01 · CONTEXT — one scene, written once

Everything in this tier is true from the first frame to the last. Written once, at the top, and
never restated. Budget for the whole tier: **35 words per block you load, +25 per bound reference
beyond two, +5 per beat, cap 480.** A block you did not load costs nothing and buys nothing.

---

## 1. `SCENE CONTEXT`

**Carries:** the scene itself, in a paragraph. Always present, in every preset, in every prompt.

The one block that is allowed to be prose. It answers *where, who and what kind of thing this is* in
three or four sentences, so that every block below it is read against something. If you delete every
other block, this one still has to produce a coherent render.

```
SCENE CONTEXT: two brothers sealed inside a low black car at night, forward-facing, side by side,
a raised console between them like a wall. The younger one drives; the older one came off a shift
and got in the way you get into a work van. Neither has looked at the other since the door came
down. Streetlight crosses both faces in slow bands as the car moves.
```

Rules:

- **Say what kind of scene it is, not what it means.** "Two brothers sealed inside a car" renders.
  "A meditation on estrangement" does not.
- **Consequence over adjective.** "a console between them like a wall" beats "tense, distant,
  uncomfortable".
- Three to five sentences. Past that you are writing blocks that already exist below.

**Prevents:** a prompt that is a pile of specifications with no scene under it, which renders as a
pile of specifications.

---

## 2. `FORMAT MODE`

**Carries:** duration, aspect, fps, cut budget. A single line, no prose.

```
FORMAT MODE: seedance 2.5 · 30s · 720p · 2.39:1 · audio on · 24fps · 6 beats, 5 hard cuts
```

Rules:

- Duration must be legal for the model. 1.0: 2–12 integer. 1.5: 4–12. 2.0: 4–15 or auto. 2.5: 4–30
  or auto.
- **fps is always 24 on every Seedance version and is not a parameter.** State it or omit it; never
  request another value.
- **Resolution and aspect are API parameters, not prompt text.** `FORMAT MODE` is a header for the
  human, and the compiler strips it before dispatch if the provider wants a clean body. Keep it in
  prompt-only deliveries so the user knows what to set.
- State the cut budget here and the beat count has to agree with it. That disagreement is the single
  most common structural error and the linter checks it.

**Prevents:** a 30-second prompt sent to a model capped at 15, and a six-cut sequence sent to a model
that holds two.

---

## 3. `ACTIVE REFERENCES`

**Carries:** the bound plates, and the exclusions on each. One line per reference, never combined.

```
ACTIVE REFERENCES:
@Image1 → the car interior: the cabin, the console, the seat backs, the dash geometry. NOT any person in it.
@Image2 → the younger brother, head: skin texture, the old jaw tattoo, eye colour, at close-up sharpness. NOT the pose, NOT the framing, NOT the background.
@Image3 → the older brother, head and shoulders: face, build, the work jacket. NOT the pose, NOT the lighting state.
@Video1 → camera behaviour ONLY: the drift and re-settle of a hand-held gimbal. NOT its subject, NOT its grade.
```

Every line takes the shape `@ImageN → <who or what>: <what to take>. NOT <what to leave>.`

The `NOT` clause is the load-bearing half. Without it the model blends every attribute of the
reference into the shot — which is how a close-up ref's framing overrides your wide blocking and a
location plate's time of day overrides your lighting.

In `text2video` **this block does not exist.** Identity moves into `CAST` and `OPEN` as description.

Syntax per provider, fidelity grades, per-beat subsetting and reference budgets:
[binding.md](binding.md).

**Prevents:** the single highest-frequency drift there is.

---

## 4. `LOCATION MAP`

**Carries:** what is where, and how far apart. Screen terms, not coordinates.

```
LOCATION MAP: the driver screen-left, the passenger screen-right, the console between them at
elbow height. The windscreen fills the upper third; the road runs away dead centre. Sodium poles
pass at roughly two-second intervals on the driver's side ONLY. Nothing behind the seats is
readable.
```

Rules:

- **Screen side and depth beat percentages.** "foreground screen-left, behind her in the mid-ground"
  is more reliable than "at 30% from the left edge". Use percentages only when matching an existing
  plate exactly.
- **Include the lights' positions**, not just their quality — where a source sits is geography, and
  `LIGHTING` will describe what it does.
- Distances matter when something has to close: `the straggler is forty feet ahead and losing it`.

**Prevents:** multi-subject staging that words alone cannot hold, and the shot that reads flat
because everything was arranged across frame instead of in depth.

---

## 5. `CAST`

**Carries:** who is in it, and what stays identical about each of them.

```
CAST: MARCUS, late twenties, lean, close-cropped, a faded line tattoo along the left jaw. RAY,
mid thirties, heavier, same jaw and same eyes — they read as blood at a glance. Two men, and NEVER
a third person in frame.
```

Rules:

- **One unrepeatable marker per character.** A scar through the eyebrow, a tape strip across the
  nose, one dark glove. Shared traits blur between characters; unique traits hold.
- **Never use pronouns across characters anywhere in the prompt.** "He looks at him" is unresolvable
  and produces the twins artefact. Use the name every time.
- Two characters is the comfortable limit in `text2video`; three or more simultaneous performers is
  the ID-drift cliff on every version.
- In `ref2video`, keep `CAST` short — the plates carry the likeness and this block only carries the
  names and the marker so the rest of the prompt has nouns to point at.

**Prevents:** the duplicate-subject artefact, and identity blending between characters who share a
description.

---

## 6. `STAGING`

**Carries:** where everyone stands, and how they move, relative to camera.

```
STAGING: both men forward-facing for the whole sequence, shoulders squared to the windscreen, the
camera on the dash between them. RAY turns fully in his seat exactly ONCE, on beat four, and does
NOT turn back. MARCUS never turns his head at all.
```

Rules:

- Staging is what holds across the scene; blocking that changes shot to shot belongs in `ACTION`.
- **Count the exceptions.** "turns exactly once, on beat four" is a rule the model can obey. "mostly
  faces forward" is not.
- If the scene has a line the camera must stay on one side of, say it here — that is staging, not
  camera.

**Prevents:** the coverage that flips across the axis between cuts and stops intercutting.

---

## 7. `WARDROBE`

**Carries:** what everyone wears, and what must not change.

```
WARDROBE: MARCUS in a plain black tee, no chain, no watch, nothing that catches light. RAY in a
grey work jacket over a faded tee, the jacket still zipped. Both EXACT in every beat.
```

Rules:

- Wardrobe belongs in `CONTEXT`, never in a beat. Stated in a beat, it re-rolls at every cut — this
  is the most common cause of a jacket changing colour mid-sequence.
- **Name what is absent when absence is the point.** "no chain, no watch, nothing that catches
  light" is doing real work on a character whose whole argument is that he is not flexing.
- Keep it to what the camera sees at the shot sizes you are actually using. Sock colour is words you
  are paying for.

**Prevents:** wardrobe drift across cuts, and jewellery the model adds because the character reads
as wealthy.

---

## 8. `GAZE AND EYELINES`

**Carries:** who looks at what, and where the lines cross.

```
GAZE AND EYELINES: an escalating ladder. Beats one and two, neither man looks at the other — both
eyelines out through the windscreen. Beat three, RAY finds MARCUS only in the reflection of the
side glass. Beat four, RAY turns and looks directly at him; MARCUS does NOT return it. Beat five,
MARCUS's eyes stay locked forward on the road. NOBODY looks at camera at any point.
```

Rules:

- **Build it as a ladder, beat by beat.** Who is *allowed* to look at whom. A ladder that runs
  "never looks up → finds him only in a reflection → first direct look → first and only returned
  look → asks for the look → does not get it" is a whole scene's dramaturgy expressed as blocking,
  and it reads with the sound off.
- **Say who never looks at camera.** Absent that, someone will.
- Let the camera run the same ladder — locked → creep → handheld → locked — via the per-beat
  `CAMERA` lines.

**Prevents:** the dead-eyed group shot. This is the cheapest fix for it there is.

---

## 9. `EVENT AND SHARED DIRECTION`

**Carries:** the one thing happening, and what everyone plays toward. A finish-register block; load it
when the scene has real acting in it.

```
EVENT AND SHARED DIRECTION
THE EVENT, containing both men and never spoken aloud: one brother refuses to be sold to, and the
other runs out of ways to sell.
The terrain is a car ride, and each pursues the event through a different physical channel: MARCUS
through the wheel and the pedals, RAY through stillness and the questions nobody has asked in years.
THE SHARED DIRECTION, played by both: keep it ordinary. Do not let this become a scene.
THE ESSENTIAL AXIS: performed ease against unperformed presence.
```

Rules: name the event from **how the scene ends**, not how it opens. The event must contain every
character including silent ones. Full method: [acting-task.md](acting-task.md).

**Prevents:** two characters playing two different scenes, and the performance that is technically
correct and emotionally inert.

---

## 10. `RULES`

**Carries:** the do-not-break list — continuity that holds for the whole clip.

```
RULES: the camera NEVER leaves the cabin. Both men stay in the SAME seats and the SAME clothes in
EVERY beat. The light state is night-for-night throughout — NEVER dusk, NEVER interior practicals.
Real-time, and the frame rate never changes.
```

Rules:

- `RULES` is continuity. `POSITIVE LOCKS` is anti-drift enforcement written as assertions. They are
  different blocks and the difference is: `RULES` states what is true, `POSITIVE LOCKS` states it
  again at the bottom because a render dropped it.
- Four to six clauses. This is where the closed capitals vocabulary earns its keep.
- **One light state per CONTEXT tier.** Day and dusk in the same scene is two prompts. The model
  picks one and ignores the other, or blends them into something incoherent.

**Prevents:** the continuity break that only shows up when you cut the clips together.

---

# 02 · BEATS — one shot each

Delta only. If the CONTEXT tier said it, do not say it again. Budget per beat:
**18 words per block you load, +8 × that beat's seconds, floor 80, cap 260.** Only `ACTION` and
`PERFORMANCE` genuinely scale with screen time; the rest is near-constant overhead. Capitals: 6 per
beat, from the closed vocabulary.

Label each one `BEAT n — <slug>`. `SHOT` and `SEGMENT` are accepted aliases; pick one and hold it.

---

## 11. `OPEN`

**Carries:** the first frame. The model builds forward from it, so it decides more than any other
block in the tier.

Four things, in order: **who · which screen side · which depth · already in motion.**

```
OPEN: dead-side profile on MARCUS, camera wedged in at the dash, medium-close. A slice of face lit
by the cluster from below, the rest falling to black. Already breathing hard, hands already on the
wheel.
```

Rules:

- **Nobody starts still.** A static first frame gives the model a photograph to animate out of, and
  the first half-second reads as exactly that. Everyone in frame is mid-something.
- **In image-to-video, do NOT describe the supplied first frame.** Write only what starts moving.
  Re-describing the plate is a top-three cause of drift.
- Only beat 1 needs a full `OPEN` in a continuous take. In a multi-beat clip every beat needs one,
  because every beat opens on a cut.

**Prevents:** the animated-photograph opening, and a first frame the model chose for you.

---

## 12. `ACTION`

**Carries:** what happens, in order. Clauses joined by `→`. The only block that scales with screen
time.

```
ACTION: MARCUS's foot goes down and stays down a beat too long → the rev needle sweeps and the
cluster light climbs his face → RAY's hand goes up flat against the roof, unhurried → the sodium
strips start strobing across the windscreen faster than they should → MARCUS's knuckles go pale on
the wheel and stay there.
```

Rules:

- **Arrows, not timecodes.** ByteDance flags strict timing markers as unstable and in practice they
  make the model rush or stall to hit them. Use `0–3s / 3–6s` only when syncing to a supplied audio
  reference, editing an existing clip, or cutting to an approved voice track.
- **One primary action per clause.** Two things at once become one blurred thing.
- **End on a held state, not mid-gesture.** The last clause is what the final frame looks like, and
  it is what an extension will continue from.
- For action work specifically — name the mass not the speed, one impact per beat, and say where the
  energy goes. [action.md](action.md).

**Prevents:** weightless motion, limb smearing, and an arbitrary final frame.

---

## 13. `CAMERA`

**Carries:** the shot's single move. Exactly one. This is law 2 and it has no exceptions.

```
CAMERA: a slow creep in on MARCUS, hand-felt rather than mechanical, settling when the sodium
strips start.
```

Or lock it:

```
CAMERA: locked off. The frame does NOT travel — ONLY the operator's breathing shows.
```

Rules:

- **A locked camera is a choice and must be stated**, or the model invents drift. If the provider
  exposes `camera_fixed` / `fixed_lens`, set it as well as writing it.
- Three parts, only the first mandatory: **the move · its quality · its ending.** The ending matters
  more than people expect — a move without a destination keeps going and lands the final frame
  somewhere arbitrary.
- **Handheld is a quality, not a move.** A handheld locked shot is legal and common: the frame
  trembles in place but does not travel. Write both halves.

Vocabulary the model actually recognises: [camera.md](camera.md).

**Prevents:** the jitter that stacked moves produce on every Seedance version.

---

## 14. `LENS`

**Carries:** framing for this beat only — shot size, focal family, focus behaviour.

```
LENS: medium close on MARCUS from the passenger side, 50mm, the near eye the sharpest thing in
frame, RAY soft and unreadable behind him.
```

Rules:

- `LENS` is per-beat framing. The capture medium, grain and grade live in `STYLE`, once, at the
  bottom. Do not restate the format here.
- **Say what the frame must not open to.** "stays medium-close and NEVER opens to a wide" is the fix
  for the move that widens on its own.
- Shot sizes the model reads: extreme close-up · facial close-up · medium close · medium · full body
  · wide / establishing.

**Prevents:** scale drift across cuts, and coverage that turns out to be four versions of the same
frame.

---

## 15. `PERFORMANCE`

**Carries:** the performance beat. Four lines, in this order. What separates a shot with acting in it
from a shot with movement in it.

```
PERFORMANCE: wants — to get the next sentence out without his voice going
             blocked by — the question was small enough to land
             plays — eyes fixed on the road, jaw working once, breath held a half-beat too long
             turns on — the second the name is said again; he stops answering and starts holding
```

Rules:

- `wants` is playable and physical. Not "to feel afraid" — fear is a *result*, not an objective.
- `blocked by` is present in the frame, not in the character's history.
- `plays` is visible behaviour: eyes, breath, hands, jaw, tempo. Never a state of mind. Give it the
  most words; it is the field that actually renders.
- `turns on` is the single moment the performance changes gear. One per beat.
- **One performer per beat.** Everyone else is present but not acting — sitting, watching, blurred by
  depth. Cut for the second performance.

For two-handers, dialogue with subtext, or a face that reads dead, use `EVENT AND SHARED DIRECTION`
plus per-character `ACTING TASK` blocks instead: [acting-task.md](acting-task.md). Micro-behaviour
vocabulary and the reason biography never renders: [performance.md](performance.md).

**Prevents:** the slack face. Nothing else fixes it — not lighting, not lens language.

---

## 16. `DIALOGUE`

**Carries:** the words spoken in this shot, in braces, after their delivery anchor.

```
DIALOGUE: RAY, plain and level, stating a fact rather than opening a subject, and NOT being kind:
{Ma asked about you.}
```

Rules:

- **Language, then voice, then intention, then the line.** The language anchor goes in `VOICE` once;
  the per-beat intention goes here. Never put emotion inside the braces — `{sadly} Don't.` speaks the
  word "sadly".
- **2 to 2.5 words per second is the ceiling.** A third of that when the pauses are the content. Over
  it, the model compresses delivery and lip-sync desyncs — the most common dialogue failure by a wide
  margin.
- **One speaker per beat.** Two people talking in one shot is where dialogue falls apart. Give each
  line its own beat and cut between them; this is what Seedance's shot-reverse handling is built for.
- **Direct the intention, never the emotion.** "Sad" returns a sad-voice cliché. "An inventory, the
  way you check a fuel gauge" returns the line.

Word ceilings by duration, voice locking and the full grammar: [sound.md](sound.md).

**Prevents:** rushed delivery, desynced lips, and a language that drifts mid-clip.

---

## 17. `SFX`

**Carries:** this beat's own sound, on top of the standing ambience in `AUDIO`.

```
SFX: <the engine note climbing and staying there> <a palm settling flat against a headliner> <one
sharp breath through the nose>
```

Rules:

- **One event per pair of angle brackets.** Object and action, never adjective. `<a metal latch
  clicks>` renders; `<intense dramatic impact sounds>` does not.
- **Order them the way they happen.** The model uses SFX order as a secondary timing signal, which is
  useful precisely because you have avoided timecodes.
- **Do not restate `AUDIO`.** The bed is already running.
- Breath is a sound effect and it is the cheapest realism in the whole rig.

**Prevents:** generic audio mush, and the beat whose sound has nothing to do with its picture.

---

## 18. `EDIT`

**Carries:** the out-point — cut, morph, dissolve or hold.

```
EDIT: hard cut.
EDIT: hold the last frame motionless for half a second.        ← for a clip you intend to extend
EDIT: match cut on the movement — the cut lands inside the turn, so the motion carries across it.
EDIT: no cut. This beat runs continuously into the next.
```

Rules:

- **Unlabelled multi-beat prompts render as one continuous take.** `EDIT` is what forces the cut.
  This is not optional in a multi-shot clip.
- **The last beat's `EDIT` is the final frame.** On any clip you intend to extend, write it locked
  and motionless — a clip that ends mid-move gives the extension nothing to hold and it invents a new
  scene.
- Stay inside the model's cut budget: 1.0 → 2 shots · 1.5 → 2–3 · 2.0 → 3–4 · 2.5 → 5–6. Past it,
  expect identity drift from the third or fourth cut onward. [scenes.md](scenes.md).

**Prevents:** the six-shot prompt that renders as one long unbroken take.

---

# 03 · PROMPT SEGMENTS — many projects

The parts that never change. The same on beat one and beat nine, and the same on the next project.
Write them once, save them, paste them. Budget for the whole tier: **38 words per block you load,
cap 360** — the most generous per-block allowance in the rig, because these are the only words you
buy once and spend forever.

This is the tier that makes the rig pay off. When you ask an AI to iterate a sequence, it rewrites
`CONTEXT` and `BEATS` and leaves this block alone — which is most of the token saving and all of the
consistency.

---

## 19. `PHYSICS`

**Carries:** how bodies and matter behave. Named objects with stated mass.

```
PHYSICS: real mass and inertia. The car is heavy and its weight transfers late — it settles onto
its outside springs through a turn and takes a beat to come back. Bodies inside it move with the
car and arrive after it. Hair and fabric lag a head turn, then catch up. Nothing floats and nothing
snaps back.
```

Rules:

- **Name the object, then its mass, then its behaviour.** This is worth more words than any adjective
  in `STYLE`, and it is what stops motion reading as weightless.
- Include the recovery, not just the impact. Landing without recovery is floating.
- This block is almost entirely reusable. A "real-world gravity" pack and a "stylised, weight
  exaggerated" pack cover most of what you will ever need.

**Prevents:** the single most recognisable AI-video tell there is.

---

## 20. `LIGHTING`

**Carries:** every source, named and placed, and what it does to the subject's face.

```
LIGHTING: the ONLY sources are sodium street poles passing outside on the driver's side, and the
instrument cluster below the windscreen. The poles rake across both faces in slow bands and leave
the cabin black between them. The cluster lights MARCUS from underneath, cold, and never reaches
RAY at all.
```

Rules:

- **One motivated source beats ten adjectives.** "Dim moody lighting" is a mood. "Daylight through
  the seams" is a source with a direction, and the model can render its falloff and its shadows.
- State three things: **where it comes from · what motivates it · what it does to the subject's
  face.** Everything else is decoration.
- **Colour arrives from the source, not from a grade.** Write "sodium street pole" and the orange
  comes out correct. Write "orange grade" and you get a filter.
- One light state per prompt. To change light state, generate the first state and feed it as a
  reference into the second.

**Prevents:** flat unmotivated light, and a catchlight you asked `PERFORMANCE` for that has no source
to come from.

---

## 21. `AUDIO`

**Carries:** the standing ambience, and what is banned from it.

```
AUDIO: <a sealed cabin, road noise arriving muffled through glass> <steady tyre hum on cold
asphalt> <the engine held at a low constant note>. Room sound ONLY.
```

Rules:

- Bracket grammar, one event per `< >` pair. Prose descriptions of sound get averaged into mush.
- **State silence explicitly.** "no music, room sound ONLY" is four words that stop the model
  inventing a score.
- Omit this block entirely on Seedance 1.0 — it produces silent video and the words are wasted.

**Prevents:** the generic cinematic soundbed the model adds when you leave audio unspecified.

---

## 22. `SCORE`

**Carries:** music — or plainly that there is none. Separate from `AUDIO` because most cinematic work
wants none, and "none" needs saying.

```
SCORE: none. NO music of any kind at any point. Everything in this clip is engine, tyre hum and
room tone.
```

With music:

```
SCORE: (a single low pulse under everything, no melody, no percussion, no swell)
```

Rules:

- **Describe function, not genre.** `(a single low pulse under everything)` outperforms `(epic
  cinematic soundtrack)` every time.
- Most cinematic work should carry `SCORE: none.` — score is added in post where it can be cut to
  picture. Leaving it unstated is how you get library music you have to fight.

**Prevents:** unrequested music, and a score that cannot be removed from the render.

---

## 23. `STYLE`

**Carries:** capture format, optics, grain, grade, palette.

```
STYLE: large-format film capture, 40mm spherical prime, real grain and halation, shallow falloff
with imperfect focus. Clean glass, soft contained glows, optics inherited from the plate. Palette
60 near-black asphalt and cabin, 25 sodium orange, 15 instrument-cluster cyan.
```

Rules:

- **Palette as a numeric split.** Three values summing to 100. It is the single most reliable colour
  instruction available — far stronger than naming a mood, and it is the answer to *not too much*:
  the accent never exceeds its number.
- **Name a capture medium, not an anti-CG rant.** One clause of "shot on film, real grain, imperfect
  focus" outperforms a paragraph refusing every synonym for computer graphics — and the long version
  seeds "3D", "render" and "engine" into the frame in the act of excluding them.
- **Anamorphic character does not hold from video text.** Bake it into the plate at the image stage
  and write only "clean glass, contained soft glows, optics inherited from the plate" here. The one
  loophole worth using: you may ask for **oval bokeh** as an image property.
  [finish.md](finish.md) §3.
- Two or three optical textures is a look. All seven is a list, and the model averages lists.

**Prevents:** grade drift between shots, and the palette that creeps until the accent is the film.

---

## 24. `STYLE LOCK`

**Carries:** the anti-drift clause for stylised work. **Non-photoreal only.**

```
STYLE LOCK: hand-drawn 2D animation on twos, visible ink line, flat cel fills, painted
backgrounds. NOT 3D, NOT photoreal, NO photobash, NO CGI smoothness, NO smooth interpolation, NO
motion blur, NO morphing.
```

Rules:

- **This is the one block where negations are load-bearing**, and the reason is specific: a stylised
  brief has to fight the model's gravity back toward photography, and there the negation is doing
  real work.
- **Never load `STYLE LOCK` in photoreal work.** In photoreal, naming an artefact summons it — use
  `POSITIVE LOCKS` instead.
- Keep it immutable across the whole project. This block and `PHYSICS` are the two that most reward
  never being retyped.

**Prevents:** the stylised sequence that drifts back to photoreal by shot four.

---

## 25. `TYPOGRAPHY`

**Carries:** type, weight, and how it enters and leaves.

**The default value of this block is a refusal.** On-screen text is the model's weakest area across
every Seedance version and corrupted lettering is close to unavoidable.

```
TYPOGRAPHY: none. The frame carries no text, no captions, no subtitles and no burned-in lettering
at any point. The final beat holds clean negative space at frame-right for a lockup composited in
post.
```

When a word genuinely must be in-frame, wrap the exact string in quotes to raise its weight and
accept the odds: `the sign reads "OPEN"`. Anything longer than a word or two: generate clean and add
type in post, which is what every real spot does anyway.

Load a real value for this block only in `MOTION GRAPHICS` work, where type *is* the subject — and
even there, expect to composite the final lockup.

**Prevents:** garbled lettering, and the subtitles the model burns in whenever there is speech.

---

## 26. `VOICE`

**Carries:** accent, register, delivery — the fixed identity of each speaker.

```
VOICE:
MARCUS — Southern California, Black American speech, late twenties. A light dry voice set fairly
high with no lift in it; he speaks on the tail of his breath and never pushes air. Faint touring
rasp at the edges. Clipped, unhurried, drops the ends of words. He NEVER raises his volume.
RAY — Southern California, Black American speech, mid thirties. Same placement and same vowels as
his brother, but heavier, slower, fully voiced. Ordinary conversational volume inside a very quiet
car. No tension anywhere in it.
```

Rules:

- **Paste it verbatim, every time. A synonym is a drift.** Rewriting a voice string re-rolls the
  voice, and that is why this block lives in `PROMPT SEGMENTS` and not in a beat.
- Four to six attributes per speaker: pitch height, weight, texture, pace, accent, one habit. More
  than that and the model averages them away.
- **Always anchor the language.** Dialogue language drifts if unstated. Officially supported
  lip-sync: Mandarin, English, Japanese, Korean, Spanish, Indonesian, plus Cantonese and Sichuanese.
- Better still, when the model supports it: bind an audio reference —
  `@Audio2 → voice identity for MARCUS: timbre and pace. NOT the words.`
- Per-beat delivery intention goes in `DIALOGUE`. Fixed identity goes here.

**Prevents:** a character whose voice changes between shots.

---

## 27. `POSITIVE LOCKS`

**Carries:** constraints written as assertions. Always the last block in the prompt.

**Seedance has no `negative_prompt` parameter on any endpoint.** Constraints live inside the prompt
body and compete with the description for attention, so every clause weakens the description. Worse,
in photoreal work the model does not reliably parse the negation — it parses the noun, and you get
the artefact you were trying to exclude.

So do not write bans. Restate every requirement as a positive assertion:

| Instead of | Write |
|---|---|
| `no extra people` | `Exactly two men are present for the whole clip.` |
| `no cuts` | `One continuous take from first frame to last.` |
| `no text or captions` | `The frame contains the two men, the windscreen and the road only.` |
| `no lens flares` | `Every light source renders as a soft, round, contained glow within its own source.` |
| `don't let him smile` | `His face stays level and closed in every frame.` |

```
POSITIVE LOCKS: exactly two men are present for the whole clip, and both stay in their seats. The
camera stays inside the cabin from first frame to last. MARCUS faces forward in every beat. RAY
turns exactly once. Every light source renders as a soft contained glow within its own source. The
frame contains the two men, the windscreen and the road only.
```

Rules:

- **Restate only what a render has actually dropped, or what is genuinely ambiguous.** This is not a
  summary of the prompt. If you find yourself locking something the beats already state clearly,
  delete it — you are paying words for nothing and diluting the locks that matter.
- Four to six clauses. Past that it is a negative wall wearing a different hat.
- **The exception is stylised work**, where the negations belong in `STYLE LOCK` and are load-bearing.

**Prevents:** exactly the artefact you were trying to exclude.

---

## Quick reference — one line each

```
01 CONTEXT ─ one scene
   SCENE CONTEXT              the scene itself, in a paragraph
   FORMAT MODE                duration, aspect, fps, cut budget
   ACTIVE REFERENCES          the bound plates, and the exclusions on each
   LOCATION MAP               the space and its distances
   CAST                       who is in it, and what stays identical about each
   STAGING                    blocking relative to camera
   WARDROBE                   what is worn, and what must not change
   GAZE AND EYELINES          attention and its direction
   EVENT AND SHARED DIRECTION the scene's single intent
   RULES                      the do-not-break list

02 BEATS ─ one shot each
   OPEN                       the first frame, already moving
   ACTION                     what happens, in order
   CAMERA                     the shot's single move
   LENS                       framing for this beat only
   PERFORMANCE                the performance beat
   DIALOGUE                   the words spoken in this shot
   SFX                        this beat's own sound
   EDIT                       the out-point — cut, morph, dissolve or hold

03 PROMPT SEGMENTS ─ many projects
   PHYSICS                    how bodies and matter behave
   LIGHTING                   every source, named and placed
   AUDIO                      ambience, and what is banned from it
   SCORE                      music — or plainly that there is none
   STYLE                      capture format, optics, palette
   STYLE LOCK                 the anti-drift clause for stylised work
   TYPOGRAPHY                 type, weight, and how it enters and leaves
   VOICE                      accent, register, delivery
   POSITIVE LOCKS             constraints written as assertions
```
