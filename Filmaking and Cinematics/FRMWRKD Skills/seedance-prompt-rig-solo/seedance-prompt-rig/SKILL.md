---
name: seedance-prompt-rig
description: "Writes ByteDance Seedance video prompts (1.0, 1.5 pro, 2.0, 2.5) on the Prompt Rig — three tiers sorted by lifespan: CONTEXT once per scene, BEATS one per shot, PROMPT SEGMENTS saved and reused across projects. 27 named blocks in an ALL-CAPS key grammar that round-trips through the ReelStack Sequence Builder. Enforces per-block word budgets, one camera move per beat, reference role lines with explicit exclusions, the bracket audio grammar, dialogue timed to clip length, and POSITIVE LOCKS instead of a negative wall. Owns video-to-video from a 3D blockout or previz: the reference governs camera, spacing and timing, the prompt governs the performance. Keeps cuts inside each model's real budget. Includes a linter and a post-render verification checklist. Use for fights, chases, stunts, crowds, dialogue coverage, reference-to-video, video-to-video, 30-second sequences, compressing a bloated prompt, or any request naming Seedance. Formerly shot-builder-cinematic-action. Triggers: seedance, seedance 2.5, prompt rig, scene context, beats, prompt segments, sequence builder, reference-to-video, video-to-video, v2v, blockout, 3D blockout, previz, animatic, motion reference, staging reference, action scene, fight scene, chase, stunt, hard cut, multi-shot, video prompt, shot list, acting, performance, two-hander, dead eyes, video extension, verify the render. A Claude skill made by FRMWRKD."
---

# Seedance Prompt Rig

*A Claude skill made by [FRMWRKD](https://www.youtube.com/@FRMWRKD). Formerly shipped as
`shot-builder-cinematic-action`; the grammar is unchanged, so prompts and saved `PROMPT SEGMENTS`
packs written under the old name still work.*

A compiler, not a describer. In: a beat, some locked tokens, a target model. Out: a Seedance prompt sorted by lifespan, where every word is spent on something the camera can see.

Companion to `shot-builder`, never a replacement. `shot-builder` locks identity, locations and looks and runs the generation. This skill turns those locks into Seedance-shaped prompts and owns the action and performance grammar. If `shot-builder` is installed, reuse its tokens rather than inventing new ones — see §9.

**The grammar here is the same grammar the ReelStack Sequence Builder opens with**
(`reel-stack.com/lab/prompt-rig/`). Same three parts, same block names, same key casing. A prompt
this skill writes pastes into that tool and comes back out unbroken. Do not invent block names.

---

## 0 — The rig, in one screen

A video prompt is not a paragraph. It is three tiers, sorted by **how long each fact stays true**.

```
01  CONTEXT           ← one scene.      Written once, at the top. Never restated.
02  BEATS             ← one shot each.  Only what changes. The only part you write again.
03  PROMPT SEGMENTS   ← many projects.  Physics, light, sound, style. Saved, pasted, reused.
```

Most prompts collapse all three into one block and restate the world in every shot. The model then
**re-decides the world in every shot** — and that is where wardrobe drifts, geography moves and a
sixth dancer appears. Every restatement is a fresh decision point, and nothing forces the answers
to match.

### The lifespan test

One question sorts every fact you are about to write:

> **"Would I have to write this again in beat four?"**

| Answer | Where it goes |
|---|---|
| Yes — and it is true of this project only | **CONTEXT** |
| Yes — and it will still be true on the next project | **PROMPT SEGMENTS** |
| No | **BEATS** |

Misfiling costs measurable words. A constant parked in BEATS is paid for once per beat: put the
grade in five beats and you have bought it five times and given the model five chances to render it
differently. The linter prices this for you — `lint` reports every fact it finds in more than one
beat and what hoisting it would save.

---

## 1 — The five laws

Break these and the render drifts. They outrank everything below.

1. **Every fact appears exactly once, in the tier that owns its lifespan.** Restating a fact in five
   blocks is not emphasis, it is noise the model averages — and it dilutes the four facts that were
   stated once. `POSITIVE LOCKS` restates only what a previous render actually dropped.
2. **One camera move per BEAT.** Stacked moves produce jitter on every Seedance version. Want a
   second move? That is a second BEAT and a cut.
3. **Capitals are a closed vocabulary, budget six per BEAT.** Only
   `ONE · ONLY · NEVER · NOT · NO · NOBODY · SAME · EXACT · EVERY` may be capitalised inside a value,
   and the six-per-beat budget covers all of them together. Block keys are always caps; that is the
   grammar, not shouting. Everything else is sentence case — shouting a whole paragraph flattens the
   weighting of the words that actually matter.
4. **Never bind a reference without an exclusion.** `@Image2 → Naomi's face` is a coin flip.
   `@Image2 → Naomi's face, skin and glasses. NOT the pose, NOT the framing.` is an instruction.
   Details in [references/binding.md](references/binding.md).
5. **A reference video governs staging, never performance.** A blockout, previz or animatic gets
   **one compact role line** — camera, spacing, timing, and what it does not own — and then the
   prompt spends everything on positive physical description of the performance. Shouting
   `IGNORE THE MOVEMENT` in capitals makes the actors copy the boxes; heavy negation focuses the
   model on what is negated, and a model given nothing positive to perform falls back on the only
   motion it can see. [references/blockout.md](references/blockout.md).

---

## 2 — Flat vs tiered, on the same eight seconds

**Flat — the world restated per shot.** The set is declared four times, the optics three:

```
A wet container dock at midnight, sodium floods from behind, one blue work lamp, a broad man
swings at a hooded figure, 35mm anamorphic, real grain, then the hooded figure stumbles back on
the wet dock at midnight with sodium floods, water sprays, shot on 35mm anamorphic, then he
catches himself on a container, midnight, sodium, blue lamp, anamorphic…
```

**Tiered — declared once, then only deltas:**

```
SCENE CONTEXT: a wet container dock at midnight. Four sodium floods behind the action, one blue
work lamp at the near stack. A broad man and a hooded figure, alone.

BEAT 1
ACTION: the swing lands high on the chest.

BEAT 2
ACTION: he folds over it, two stumbling steps.

BEAT 3
ACTION: heels plough water, he stays up.

PHYSICS: weight arrives before the limb that carries it.
STYLE: 35mm anamorphic, 40mm, real grain, halation.
```

The scene is stated once and cannot disagree with itself. The beats carry only what changes. The
style and physics sit at the bottom, where they can be lifted whole into the next project.

---

## 3 — The twenty-seven blocks

`SCENE CONTEXT` is always present. The other twenty-six are blocks you add when the job needs them —
never all at once. Keys are ALL CAPS at the head of a line; values are lower-case prose.

### 01 · CONTEXT — one scene

| Block | Carries |
|---|---|
| `SCENE CONTEXT` | the scene itself, in a paragraph |
| `FORMAT MODE` | duration, aspect, fps, cut budget |
| `ACTIVE REFERENCES` | the bound plates, and the exclusions on each |
| `LOCATION MAP` | the space and its distances |
| `CAST` | who is in it, and what stays identical about each |
| `STAGING` | blocking relative to camera |
| `WARDROBE` | what is worn, and what must not change |
| `GAZE AND EYELINES` | attention and its direction |
| `EVENT AND SHARED DIRECTION` | the scene's single intent |
| `RULES` | the do-not-break list |

### 02 · BEATS — one shot each

| Block | Carries |
|---|---|
| `OPEN` | the first frame, already moving |
| `ACTION` | what happens, in order |
| `CAMERA` | the shot's single move |
| `LENS` | framing for this beat only |
| `PERFORMANCE` | the performance beat |
| `DIALOGUE` | the words spoken in this shot |
| `SFX` | this beat's own sound |
| `EDIT` | the out-point — cut, morph, dissolve or hold |

### 03 · PROMPT SEGMENTS — many projects

| Block | Carries |
|---|---|
| `PHYSICS` | how bodies and matter behave |
| `LIGHTING` | every source, named and placed |
| `AUDIO` | ambience, and what is banned from it |
| `SCORE` | music — or plainly that there is none |
| `STYLE` | capture format, optics, palette |
| `STYLE LOCK` | the anti-drift clause for stylised work |
| `TYPOGRAPHY` | type, weight, and how it enters and leaves |
| `VOICE` | accent, register, delivery |
| `POSITIVE LOCKS` | constraints written as assertions |

Fill rules, budgets and a worked line for every single block:
[references/blocks.md](references/blocks.md). Read it before composing anything you have not
composed before.

### The assembled shape

```
SCENE CONTEXT: …
FORMAT MODE: …
ACTIVE REFERENCES: …
LOCATION MAP: …
CAST: …
GAZE AND EYELINES: …
RULES: …

BEAT 1 — <slug>
OPEN: …
CAMERA: …
LENS: …
ACTION: …
PERFORMANCE: …
DIALOGUE: …
SFX: …
EDIT: hard cut.

BEAT 2 — <slug>
…

PHYSICS: …
LIGHTING: …
AUDIO: …
SCORE: …
STYLE: …
VOICE: …
POSITIVE LOCKS: …
```

`BEAT` is the house label. `SHOT` and `SEGMENT` read identically to the model and the linter accepts
all three — but pick one and hold it for the whole project.

---

## 4 — Start from a preset

Never load all twenty-seven blocks. Start from the preset that matches the job and add only what the
beat actually needs. Full block lists and paste-ready starters:
[references/presets.md](references/presets.md).

| Preset | For | Blocks |
|---|---|---|
| **CINEMATIC** | direction and acting | 15 |
| **ACTION** | weight, contact, consequence | 14 |
| **MOTION GRAPHICS** | type and flat colour | 12 |
| **COMMERCIAL** | product and surface | 14 |
| **STYLISED** | anime, painterly, abstract | 13 |
| **EVERYTHING** | the full rig, for stripping down | 27 |

An empty block costs a line and buys nothing. If you cannot write a real value for it, it is not in
this prompt.

---

## 5 — Pick the model first

Duration, audio and reference budget all change what the rig may contain, so resolve the model
before composing a single line.

| Need | Model | Ceiling |
|---|---|---|
| Longest take, most references, in-clip editing | **2.5** | 30 s · 720p max · 50 refs |
| Extending or editing a clip you already have | **2.5 only** | `video_extension` (`forward`/`backward`), `video_edit` |
| 4K, or 15 s at 1080p | **2.0** | 15 s · 4K · 12 refs |
| Cheap dialogue at 1080p | **1.5 pro** | 12 s · 1080p · first+last frame only |
| Silent coverage, lowest cost | **1.0 pro / lite** | 12 s · 1080p · no audio at all |

**Seedance 1.0 generates no audio.** If the beat has a line of dialogue and the user is on 1.0, say
so before composing, not after the render. Full matrix, model IDs per provider, parameters,
per-second pricing and the resolution traps: [references/models.md](references/models.md).

---

## 6 — Budgets

Seedance 2.5 accepts **20,000 characters** — roughly 3,000 words. That is the API cap, not the
target. Adherence, not the parser, is what limits you, and adherence scales with duration: a 30-second
six-beat sequence legitimately needs three pages, and a 5-second single shot legitimately does not.

| Unit | Budget | Notes |
|---|---|---|
| `CONTEXT` tier | 35 × blocks loaded, +25 per reference beyond two, +5 per beat | Role lines are real work. Cap 480. Amortised across every beat |
| One `BEAT` | 18 × blocks loaded, +8 × **that beat's** seconds | Floor 80, cap 260. In a multi-beat clip the seconds are shared out |
| `PROMPT SEGMENTS` tier | 38 × blocks loaded | Cap 360. Written once and pasted forever, so it is the cheapest tier you own |
| **Working ceiling** | **400 + 45 × duration** | 5 s ≈ 625 w · 12 s ≈ 940 w · 30 s ≈ 1,750 w |
| Hard ceiling | 3,000 words / 20,000 chars | The 2.5 API cap. Past the working ceiling, adherence falls before the parser does |
| Capitals | 6 per BEAT | From the closed vocabulary only |

**The rig prices what you loaded.** A block you did not load costs nothing and buys nothing; a block
you did load gets a real allowance. That is why the budgets are per-block rather than flat — a
five-block ACTION beat and a nine-block CINEMATIC beat are not the same shot and should not have the
same budget. The linter computes all of it; do not do the arithmetic by hand.

Worked, for the two shapes you will hit most:

| Shape | CONTEXT | BEATS | SEGMENTS | Total | Ceiling |
|---|---|---|---|---|---|
| 8 s, one beat, 7 blocks a tier | 250 | 190 | 266 | ~700 | 760 |
| 30 s, six beats, 7 blocks a tier | 275 | 6 × 166 | 266 | ~1,540 | 1,750 |

A 1,400-word prompt for one 8-second shot is not thorough, it is three copies of a 460-word prompt.
The saving compounds on the second shot: it costs one BEAT, not another full prompt. Compression
method and before/after rewrites: [references/density.md](references/density.md).

---

## 7 — The workflow

```
model gate → preset → token pull → CONTEXT → BEATS → SEGMENTS → lint → pre-flight → hand off or generate → verify
```

**Model gate.** Ask, or read it from the project. Never assume 2.5 — it is capped at 720p and that
disqualifies it for a lot of work.

**Preset.** Pick one from §4 and name it in the pre-flight. It is the shortest possible statement of
what kind of prompt this is.

**Token pull.** If `shot-builder` is present, resolve every named token before composing (§9). A
token that does not exist is an identity the model will invent.

**CONTEXT.** Write it once. If the scene already has a CONTEXT tier from an earlier session, reuse
it **verbatim** — a re-typed CONTEXT is a continuity break.

**BEATS.** One per shot. Check the cut budget in [references/scenes.md](references/scenes.md) before
putting two shots in one clip.

**PROMPT SEGMENTS.** Load the saved pack if the project has one. If the project does not have one
yet, write it and offer to save it — that is the block set that will still be true on the next film.

**Lint.** Mechanical, so let the script do it:

```bash
python3 "$SKILL_DIR/scripts/seedance.py" lint prompt.txt --model 2.5 --duration 30
```

It checks per-tier word budgets, the capitals vocabulary, one-move-per-beat, unexcluded reference
bindings, unbalanced audio brackets, dialogue that will not fit the clip, cut budget, timecodes on
models where they destabilise, negative walls, **constants misfiled into BEATS**, video role lines
that shout or run long, `identity ONLY` cast bindings, excluded room proportions, and timestamps
that fall past the end of the clip. Fix what it flags before showing the user. Thirty free seconds
of linting has caught invented blocks, misfiled tiers and budget overruns that had already been paid
for in credits.

**Pre-flight.** Bullets, never prose:

```
Pre-flight:
- Preset: <CINEMATIC>
- Model: <seedance 2.5 · 30s · 720p · 2.39:1 · audio on>
- Refs: <@Image1 hero face · @Image2 corridor · @Video1 camera move>
- Beats: <6 beats, 5 hard cuts — at 2.5's ceiling>
- Budget: <CONTEXT 238/245w · BEATS 6×118w · SEGMENTS 186/200w · total 1,132/1,750w · lint clean>
- Dialogue: <42 words over 30s — fits, 1.4 w/s>
Run it?
```

Skip pre-flight only for a minor iteration on an already-approved prompt. Always show it when the
model, beat count, cast or reference set changes.

**Hand off or generate.** This skill's default output is the prompt itself, in one fenced block,
clean, no preamble inside the fence. If `shot-builder` is configured with a provider, dispatch
through its `fal_gen.py` / `kie_gen.py`.

**Verify.** Editing the source is not verifying the output. Before writing *fixed*, *done* or any
note about a render, open the rendered file and look at one full-size frame at the open, the middle
and the close. Test the property you care about (do the frames differ, is the duration right, is
the room the room), never a proxy for it. Checklist: [references/verify.md](references/verify.md).

---

## 8 — What this skill is for

### Action

Action is where generic prompt templates fail. The model does not fail at "man punches man" — it
fails at weight, contact and consequence. Four rules, expanded in
[references/action.md](references/action.md):

- **Name the mass, not the speed.** "Fast punch" renders as a blur. "His weight arrives before his
  fist, and the impact folds the other man over it" renders as a punch.
- **One impact per BEAT.** Seedance smears limbs when several collisions compete for the same second.
- **Say where the energy goes.** Every force needs a destination: heels plough, dust bursts, the body
  tumbles with him. Unresolved force is what makes AI action look weightless.
- **Three or more simultaneous fighters is the ID-drift cliff.** Push extras into motion blur, depth,
  or a separate BEAT.

Fast camera + fast cut + busy frame in the same shot is a documented failure combination on every
Seedance version. Pick one.

### Acting

Action fails on weight; acting fails on *aliveness*. A face with nothing to do goes slack, and no
amount of lighting or lens language rescues it.

- **`PERFORMANCE` — the beat-level unit.** One character, one shot, four lines.
  [references/performance.md](references/performance.md).
- **`EVENT AND SHARED DIRECTION` + `ACTING TASK` — the scene-level unit.** Two or more characters,
  dialogue with subtext, the scene where the performance *is* the shot.
  [references/acting-task.md](references/acting-task.md).

The one rule that governs both: **direct the tactic, never the expression.** No emotion adjectives,
no facial choreography. Externals belong only in the `MICRO-BEHAVIOUR` safety block, which exists
because models render glassy unblinking eyes without it.

Two staging notes that carry more weight than any adjective: build the escalation as an **eyeline
ladder** in `GAZE AND EYELINES` (who is allowed to look at whom, beat by beat) and let the **camera
run the same ladder** (locked → creep → handheld → locked). Both read with the sound off.

Restraint outperforms emphasis. Tears, sweat, a trembling chin, flaring nostrils and a working jaw
written together make the model play every tell at once, at full volume — which reads as soulless,
not moving. Breath and eye contact do more than every tell combined. Externals stay in one
`MICRO-BEHAVIOUR` line and nowhere else.

### Video-to-video from a blockout

A 3D blockout, previz or animatic attached as `@VideoN` is the strongest staging control the model
has. It owns **where the camera sits and moves, where the bodies stand, how the space lays out, and
where the cuts fall**. It never owns the performance — the figures are boxes, and any motion the
boxes carry is a placeholder that must not reach the render.

Four rules, expanded in [references/blockout.md](references/blockout.md):

- **One compact role line, then stop talking about the video.** Say what it governs, say what it
  does not, and spend the rest of the prompt on the performance in concrete physical verbs.
- **Name the room by its contents, not its materials.** *Aqua tile, brass pendants, timber counter,
  concrete floor* is satisfied perfectly by a subway tunnel. *The curved-glass pastry case, the
  speaker cabinets, the bentwood chairs, the rug* is the café.
- **Never exclude the room's proportions.** When the blockout bends the space, write it as *this
  room extending, carrying its own furniture* — and only in the shot where the transform happens.
- **Bind the cast face and whole outfit**, never `identity ONLY`. Cuts are labelled `BEAT`s with
  `EDIT: hard cut.` — prose shot changes render as one drifting take.

### Sound, and the bracket grammar

Seedance 1.5 and up read a delimiter grammar. Use it; prose descriptions of audio get averaged into
mush.

| Content | Wrap in | Lives in | Example |
|---|---|---|---|
| Music / score | `( )` | `SCORE` | `(low sustained strings, no percussion)` |
| Sound effects | `< >` | `AUDIO` / `SFX` | `<a metal latch clicks>` |
| Dialogue | `{ }` | `DIALOGUE` | `{I thought you weren't coming.}` |
| On-screen text | `【 】` | `TYPOGRAPHY` | Avoid entirely — see §10 |

**Dialogue must fit the clip: 2 to 2.5 words per second**, and a third of that when the pauses are
the content. Over the ceiling, the model speeds up delivery and lip-sync desyncs. Thirty seconds
buys about 75 words, and that is a ceiling, not a target. Always state the language in `VOICE`
before the braces or it drifts. Full grammar, voice-identity locking and the SFX writing rules:
[references/sound.md](references/sound.md).

---

## 9 — Interop

### shot-builder

If `shot-builder` is installed, it owns the tokens and this skill consumes them. Do not duplicate a
character sheet here.

```bash
SB="$HOME/.claude/skills/shot-builder"
python3 "$SB/scripts/token_resolver.py" --token <HERO> --token <CORRIDOR>
```

| shot-builder token | Compiles into |
|---|---|
| Cast token | `CAST` + `ACTIVE REFERENCES` role lines, wardrobe into `WARDROBE` |
| Location token | `SCENE CONTEXT` + `LOCATION MAP` |
| Style token / cinema mode | `STYLE` |
| `workflow_mode: ref2video` | `ACTIVE REFERENCES` is mandatory; write the `NOT` clauses |
| `workflow_mode: text2video` | No `ACTIVE REFERENCES` block; identity carried by `CAST` description and `OPEN` |

If `shot-builder` is absent, this skill still runs standalone — write the CONTEXT tier from the
user's description and offer to save it as a reusable scene file.

### The Sequence Builder

`reel-stack.com/lab/prompt-rig/` opens with these exact three parts and these exact block names. A
prompt written here pastes in and edits without translation, and a saved `PROMPT SEGMENTS` pack in
that tool pastes back out into this skill. Where they disagree, **the tool's block names win** —
this file follows the tool, not the other way round.

---

## 10 — What this skill will not do

- **No negative wall.** Seedance has no `negative_prompt` parameter on any endpoint. Thirty "no X"
  clauses steal weight from the description, and naming an artefact summons it. Write
  `POSITIVE LOCKS` instead — constraints as assertions. `no extra people` becomes `exactly two men
  are present for the whole clip`. See [references/blocks.md](references/blocks.md) §27.
- **No hard timecodes by default.** ByteDance's own guidance flags strict timing markers as unstable.
  Order beats with `→` inside `ACTION`. Use timecodes only when syncing to supplied audio, editing an
  existing clip, or cutting to an approved voice track.
- **No emblems, logos, on-screen type or anamorphic optics asked for in video text.** They drift or
  corrupt. Bake them into the reference image at the image stage, or composite in post. See
  [references/finish.md](references/finish.md) §3.
- **No re-describing the first frame in image-to-video.** The image is already there. Describe only
  what moves. Re-describing it is a top cause of drift.
- **No moving last frame on a clip you intend to extend.** `video_extension` (2.5 only) holds
  whatever the source ends on. Write the last beat locked and motionless, or the extension invents a
  new scene.
- **No overwriting `shot-builder`.** Different skill, different folder, shared tokens.
- **No real names or brands in prompt bodies.** Describe by build, wardrobe and marker. Consumer
  Seedance channels also reject photoreal real-person face references.
- **No inventing block names.** Twenty-seven keys, listed in §3. If a fact does not fit one of them,
  it belongs in `SCENE CONTEXT` or it does not belong in the prompt.
- **No negation wall around a reference video.** `THERE IS NO DANCING IN THIS VIDEO — IGNORE THE
  MOVEMENT COMPLETELY` produced four clips of actors copying the blocks. One role line, then positive
  description. See [references/blockout.md](references/blockout.md).
- **No "fixed" without opening the render.** A claim about a file is made after looking at the
  file, at full size, not after editing the script that made it. See
  [references/verify.md](references/verify.md).

---

## 11 — References, load on demand

Load only what the job needs. Pairings matter: reading one half of a pair produces drift.

| File | Load when | Pair with |
|---|---|---|
| [references/blocks.md](references/blocks.md) | Composing anything | — |
| [references/presets.md](references/presets.md) | Starting a new prompt or a new project | `blocks.md` |
| [references/models.md](references/models.md) | Choosing a model, setting duration or resolution | — |
| [references/binding.md](references/binding.md) | Any reference image, video or audio is attached | `blocks.md` |
| [references/camera.md](references/camera.md) | Writing `CAMERA`, `LENS` or `LIGHTING` | — |
| [references/sound.md](references/sound.md) | Writing `AUDIO`, `SCORE`, `SFX`, `DIALOGUE` or `VOICE` | `models.md` for the audio flag |
| [references/performance.md](references/performance.md) | Writing `PERFORMANCE`, a single-character beat | `sound.md` if the character speaks |
| [references/acting-task.md](references/acting-task.md) | Two or more characters, dialogue with subtext, a face that reads dead | `finish.md` + `sound.md` |
| [references/action.md](references/action.md) | Fights, chases, impacts, stunts, crowds | `camera.md` |
| [references/scenes.md](references/scenes.md) | More than one beat, or a whole sequence | `binding.md` |
| [references/density.md](references/density.md) | Over budget, or converting someone else's prompt | — |
| [references/finish.md](references/finish.md) | Finish-grade work, multi-character staging, brand or emblem work, anything you are paying to complete | `scenes.md` |
| [references/blockout.md](references/blockout.md) | A 3D blockout, previz, animatic or any video reference whose motion is not the wanted motion | `binding.md` + `performance.md` |
| [references/verify.md](references/verify.md) | After every render, before writing anything about it; before any status or ledger doc | `fixes.md` |
| [references/fixes.md](references/fixes.md) | A render came back wrong | — |
| [references/examples.md](references/examples.md) | You want a full worked prompt to pattern-match | `blocks.md` |

---

## 12 — Script

One script, four subcommands. Set `SKILL_DIR` to this folder once per session.

```bash
python3 "$SKILL_DIR/scripts/seedance.py" models                      # capability matrix, plain text
python3 "$SKILL_DIR/scripts/seedance.py" models --model 2.5          # one model's limits
python3 "$SKILL_DIR/scripts/seedance.py" blocks                      # the 27 blocks and their tiers
python3 "$SKILL_DIR/scripts/seedance.py" budget --duration 30        # word and dialogue budgets
python3 "$SKILL_DIR/scripts/seedance.py" lint prompt.txt --model 2.5 --duration 30
```

When you are unsure whether a prompt is legal, run the linter. It is faster than reasoning about it
and it does not drift.

---

## 13 — Session close

When the job is done, ask once: *anything worth keeping for next time?*

- A `PROMPT SEGMENTS` pack that worked → offer to save it to the project. That is the whole point of
  the third tier.
- Scene-level learnings → the scene file's own notes.
- Model quirks → [references/fixes.md](references/fixes.md). Offer the edit, never make it silently.
- A verification failure that cost a render → [references/verify.md](references/verify.md), as a
  numbered rule with the check that would have caught it.

---

*Made by FRMWRKD — the YouTube channel about making film with AI tools. Every prompt we publish is
one we paid to render. Updates ship free to everyone who has the skill.*
