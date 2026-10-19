# Finish-grade work

The rig is the same at both ends of the density dial. Same three tiers, same twenty-seven block
names, same key grammar — [blocks.md](blocks.md) is the whole vocabulary and there is no second one.
What changes between a draft and a finish is how many of the blocks are loaded, how many beats they
carry, and how long the prompt is allowed to run. This file is the set of techniques that only earn
their words when the shot is locked and you are paying to complete it: optics that have to survive a
cut, an emblem that has to be the right emblem, six figures whose positions words cannot hold, a
face that has to act.

The dial itself — how far to compress, and what to cut first — is [density.md](density.md). Which
blocks to load for which kind of job is [presets.md](presets.md). This file assumes you have already
decided you are at the finish end and want to know what to spend the words on.

Worth saying once, because it explains the shape of everything below: **the finish register is where
the rig came from.** `SCENE CONTEXT`, `FORMAT MODE`, `ACTIVE REFERENCES`, `LOCATION MAP`,
`GAZE AND EYELINES`, `DIALOGUE`, `PHYSICS`, `LIGHTING`, `AUDIO`, `STYLE`, `POSITIVE LOCKS` are the
blocks studio work was already writing; the rig is those names sorted by lifespan with the gaps
filled in. Finish-grade work is not an exception to the schema. It is the schema with everything
switched on.

Derived from published Higgsfield Studio project breakdowns (ONEIRIC, Kok-Boru, Zephyr) and the
Seedream anime-production breakdown, 2026.

---

## 0 — Draft end vs finish end

| Draft end | Finish end |
|---|---|
| Exploring, iterating, finding the shot | The shot is locked and you are paying to finish it |
| One or two characters | Three or more, or a whole formation |
| Continuity across shots does not matter much | Identity must hold across an entire film |
| Budget matters more than the last 10% | The last 10% is the job |
| ≈ **500–650 words** for a 5–8 s single-beat prompt | ≈ **1,400–1,750 words** for a 30 s six-beat prompt |

Both numbers come off one formula. The **working ceiling is `400 + 45 × duration`** — it scales with
screen time, because adherence scales with screen time. The **hard ceiling is 3,000 words / 20,000
characters**, which is the real Seedance 2.5 API cap and not a target; past the working ceiling,
adherence falls long before the parser does. There is no flat word ceiling any more and there never
really was one.

A finish-grade prompt is long because it has six beats and thirty seconds of screen time to direct,
not because it is thorough. At either end of the dial, 1,400 words spent on one 8-second shot is
still three copies of a 460-word prompt. The linter prices this: run it before you defend the length.

---

## 1 — Every prompt is an island

> *"Seedance sees only the text in front of it, so every prompt is an island: positions, poses,
> wardrobe, props, optics, light — spelled out from scratch, every time. 'Same as the previous
> shot' is an instruction to a model that has no 'before'."*

Nothing carries across an API call. Not the previous clip, not the previous prompt, not the scene
file you wrote it from. The model is handed one body of text and re-decides the world from it.

This is where the rig's first law is most often misread. **"One fact, one block" governs restatement
*within* one prompt.** It exists so that a single shot does not state its own geography five times in
five blocks and hand the model five chances to disagree with itself. It does **not** license carrying
facts *between* prompts.

- **Within one prompt:** state a fact once, in the tier that owns its lifespan. Restating it is noise
  the model averages.
- **Between two prompts:** restate everything. Identity, geography, wardrobe, light, optics, voice.
  Every time.

The `03 · PROMPT SEGMENTS` tier is the mechanical answer to this, and it is the reason the rig makes
finish work cheaper rather than dearer. `PHYSICS`, `LIGHTING`, `AUDIO`, `SCORE`, `STYLE`, `VOICE` and
`POSITIVE LOCKS` are written once, saved as a pack, and pasted **identically** into every clip on the
film. "Restate everything" then costs you a paste, not a rewrite — and because it is a paste, the
restatement is byte-identical, which is the only kind of restatement that does not drift.

The same applies to the `CONTEXT` tier within a scene: reuse it verbatim across every clip in that
scene. A re-typed `SCENE CONTEXT` is a continuity break. Copy, never retype.

---

## 2 — Naming a thing summons it

**In photoreal work, do not write bans at all.** No negative list, no "no X", nothing. Seedance has
no `negative_prompt` parameter on any endpoint, so a ban lives in the prompt body and competes with
the description for attention — and the model does not reliably parse the negation. It parses the
noun, and you get the artefact you were trying to exclude.

Use `POSITIVE LOCKS`: the last block in the prompt, every requirement restated as an assertion.

| Instead of | Write |
|---|---|
| `no extra people` | `Exactly two men are present for the whole clip.` |
| `no cuts` | `One continuous shot from first frame to last.` |
| `no text or captions` | `The frame contains the car, the void and the floor reflection only.` |
| `no lens flares` | `Every light source renders as a soft, round, contained glow within its own source.` |
| `no camera shake` | `The frame is locked and travels nowhere; ONLY the operator's breathing shows.` |
| `no modern clothing` | `Every garment in frame is wool, canvas or leather.` |

Four to six clauses, and only for what a render has actually dropped or what is genuinely ambiguous.
A `POSITIVE LOCKS` block that summarises the prompt is a negative wall wearing a different hat.

**The exception is non-photoreal work.** A stylised brief has to fight the model's gravity back
toward photography, and there the negations are load-bearing. They belong in `STYLE LOCK`:

```
STYLE LOCK: hand-drawn 2D animation on twos, visible ink line, flat cel fills, painted
backgrounds. NOT 3D, NOT photoreal, NO photobash, NO CGI smoothness, NO smooth interpolation, NO
motion blur, NO morphing.
```

Kok-Boru and the anime production both do exactly this. **`STYLE LOCK` and `POSITIVE LOCKS` are
near-mutually-exclusive** — loading both means the register was never decided. Decide it, then load
one.

---

## 3 — Optics, emblems and lettering come from the image, not the video prompt

Seedance will not hold these from video text. They drift shot to shot or corrupt outright:

- **Anamorphic character.** Bake it into the location plate at the image stage. The plate becomes the
  lens; the video prompt's `STYLE` block then describes only *clean crisp glass with a matte finish*
  and *soft round contained glows*.
- **Logos, badges and emblems.** Generate them onto the product in the reference plate, then bind the
  plate in `ACTIVE REFERENCES`. Never ask the video prompt to draw a mark. A mark that is nearly
  right is worse than no mark.
- **On-screen type.** Do not. Leave clean negative space in the final beat and composite the lockup
  in post, which is what every real spot does anyway. `TYPOGRAPHY`'s default value is a refusal.

**Measured, 2026-08:** this is not symmetric between models. Given the *same* anamorphic plate and
the *same* prompt, median out-of-focus highlight aspect ratio (1.0 = a circle):

| | Median w/h | % elliptical |
|---|---|---|
| The plate itself (4k, `MAXIMUM`) | 3.00 | 98% |
| **Seedance 2.0** | **3.00** | 88% |
| **Seedance 2.5** | **1.30** | 50% |

**2.0 inherits the plate's lens character almost perfectly. 2.5 normalises it back toward round.** If
the anamorphic look is the point, shoot it on 2.0. 2.0 also retained 3× more specular highlights in
the same frames.

**The rule has a loophole worth using.** What drifts is the *lens*; what does not is the *image
property*. You may not ask a video prompt for "anamorphic optics" — but you may absolutely ask it for
**oval bokeh**, in `STYLE` and again in `POSITIVE LOCKS`:

```
Every out-of-focus highlight renders as a horizontally stretched ellipse, wider than it is tall,
never a circle. Point highlights stretch sideways into short horizontal streaks. The frame carries
gentle horizontal compression.
```

That is a describable, checkable property of the frame, not a lens the model has to simulate. Pair it
with the plate and verify it after the render — blob aspect ratio is a two-minute measurement.

Block for the end of a **location or product image** prompt when you want scope optics:

```
STRONG anamorphic lens character: horizontal squeeze and compression, oval elliptical bokeh,
horizontally stretched highlights, curved barrel edge distortion, chromatic aberration toward
the edges. NO lens flares, NO light streaks, NO floating bokeh circles. 2.39:1.
```

Dose with `subtle / gentle / moderate / strong / maximum`. Ban the tag-alongs *here*, at the image
stage, where negations work — never in the video prompt.

---

## 4 — The asset is a pair, and the descriptor is pasted verbatim

> *"An asset is a pair: text + image. The text descriptor goes into every prompt word for word;
> the image is the reference the model anchors to."*

Naming convention — one element, one name, everywhere:

```
@loc_<PROJ>_<name>_<variant>      @char_<PROJ>_<name>_<scene>_<version>      @prop_<PROJ>_<name>
```

In the prompt, the `ACTIVE REFERENCES` block gives each tag its full descriptor and closes with
**`100% matches the reference.`** Every shot. Word for word, never paraphrased. The role line's `NOT`
clause is still mandatory — the descriptor says what the asset *is*, the exclusion says what the
render must not inherit from it. [binding.md](binding.md) owns that grammar.

Voices work the same way: decide the register, timbre, tempo and manner once, store it, paste it
verbatim into every prompt with speech. **A synonym is a drift** — rewriting a voice string re-rolls
the voice. That is exactly why `VOICE` lives in the `PROMPT SEGMENTS` tier and not in a beat: the tier
is defined as the text you paste rather than write, and a voice descriptor is the clearest case of it
in the whole rig.

---

## 5 — Block order at the finish end

The order is the rig's own — `01 CONTEXT` → `02 BEATS` → `03 PROMPT SEGMENTS`, and within each tier
the order in [blocks.md](blocks.md). Assembled, with everything a finish-grade scene loads:

```
01 CONTEXT
   SCENE CONTEXT · FORMAT MODE · ACTIVE REFERENCES · LOCATION MAP · CAST · STAGING ·
   WARDROBE · GAZE AND EYELINES · EVENT AND SHARED DIRECTION · ACTING TASK (one per
   character) · MICRO-BEHAVIOUR · RULES

02 BEATS
   BEAT n — OPEN · CAMERA · LENS · ACTION · PERFORMANCE · DIALOGUE · SFX · EDIT

03 PROMPT SEGMENTS
   PHYSICS · LIGHTING · AUDIO · SCORE · STYLE · VOICE · POSITIVE LOCKS
```

`ACTING TASK` and `MICRO-BEHAVIOUR` are not extra block keys — there are twenty-seven and no more.
They are the named sub-blocks that hang off `EVENT AND SHARED DIRECTION` in the same tier, one task
per character. Where a scene runs them, drop the per-beat `PERFORMANCE` block: they are the same job
at two scales and carrying both gives the model two directions for one face.
[acting-task.md](acting-task.md) has the format.

For non-photoreal work the anime-production architecture is cleaner — three immutable blocks and one
variable — and it maps straight onto the rig:

```
the medium        STYLE LOCK                              ← immutable
continuity        RULES + WARDROBE + CAST                 ← immutable: designs, palette, world rules
direction         STAGING + GAZE AND EYELINES             ← immutable: camera language, cut rules,
                                                            sound policy
the variable      02 BEATS                                ← the ONLY part that changes per shot
```

Retyping any of the immutable three is how a stylised sequence drifts back to photoreal by shot four.
Paste them.

### Which blocks earn their words only at the finish end

A draft loads none of these. At the finish end each is worth what it costs:

- **`LOCATION MAP`** — who or what is where in screen terms, plus where every light sits. Words alone
  do not hold multi-subject staging, and depth is what stops a formation reading as a row.
- **`GAZE AND EYELINES`** — who looks where, beat by beat, and who never looks at camera. Built as a
  ladder it is a whole scene's dramaturgy expressed as blocking, and it is the cheapest fix for the
  dead-eyed group shot there is.
- **`PHYSICS`** — named objects with stated mass and behaviour, including the recovery. This is what
  stops motion reading as weightless, and it is worth more words than any adjective in `STYLE`.
- **`POSITIVE LOCKS`** — see §2.
- **`ACTING TASK`** — one per character, the investment in a tactic. [acting-task.md](acting-task.md).
- **`MICRO-BEHAVIOUR`** — the anti-glassy-stare safety block. Blink cadence, breath, catchlight,
  micro-pause, asymmetry. Cheap, and it fixes the deadest failure mode there is.

---

## 6 — Timecodes at the finish end

The rig defaults to `→` ordering inside `ACTION` and avoids clocks, because ByteDance flags strict
timing markers as unstable and in practice they make the model rush or stall to hit them. **That
default holds for draft work.**

At the finish end, timecoded beats paired with explicit `EDIT: hard cut.` labels are the norm and they
work:

```
BEAT 2 — MEDIUM, SAM  (~0.5s–5.5s)
OPEN: hard cut to a medium of Sam in his armchair screen-right…
LENS: widescreen medium framed through soft out-of-focus foreground objects…
```

Rules that make them behave:

- **Whole or half seconds only.** Anything finer is a number the model cannot hit and will fight.
- **One `LENS` line per beat.** Framing is per-beat; the capture medium stays in `STYLE`, once.
- **One camera action per beat.** Law 2 does not relax at the finish end — it matters more, because a
  timecoded beat with two moves has two things to be late for.
- **Stay inside the model's cut budget.** 1.0 → 2 shots · 1.5 → 2–3 · 2.0 → 3–4 · 2.5 → 5–6.
  [scenes.md](scenes.md).

Timecodes are also mandatory, not optional, when syncing to supplied audio, editing an existing clip,
or cutting to an approved voice track.

---

## 7 — Staging that words cannot hold

When several characters must be in exact positions and poses, a text description stops being enough.
The studio fix is a **schematic diagram**: a flat line drawing on white, each figure a thin outline in
its own muted colour, furniture as outline shapes, **no labels anywhere**. It is attached as a
*composition-only* guide and bound with a connector block:

```
@A = the BLUE figure = @char_ON_Rudy_s2_v1 → on the couch, facing frame-right
```

State explicitly that the diagram defines **positions only** — style, light, faces and wardrobe come
exclusively from the location and character references. Treat it as spatial data, not as a picture to
copy.

The diagram is bound in `ACTIVE REFERENCES` like any other plate, and **its exclusion clause is the
load-bearing part**. Without it the model renders the drawing: flat white ground, outline bodies, no
faces. With it, the drawing does the one job it was made for.

---

## 7a — Storyboard-as-reference, and how to bind it

Generating a multi-panel storyboard first and binding it as the video's style reference works well —
it locks palette, light arc and beat order in one cheap image. Two rules make it safe.

**Exclude the layout, twice.** A storyboard is a grid. Bound naively, the model renders the grid. Put
the exclusion in the reference's role line in `ACTIVE REFERENCES` *and* again in `POSITIVE LOCKS`:

```
Take from it the palette, the light arc and the order of the beats. Take from it NOTHING of its
layout. The output is one single continuous full-frame film. There is no grid, no panels, no
gutters, no dividing lines, and no part of the frame is ever split into sections.
```

**Judge the board with numbers before you spend on video.** Crop it into its panels and compute two
things per panel: mean luma, and the percentage of pixels in your accent hue. That catches the only
two failures that matter — a light arc that does not actually arc, and an accent colour that does not
carry across the sequence. Four boards measured this way cost minutes and pick the winner for you.

**Give match-transitions something to match on.** A continuous graphic element that persists through
every beat — a ribbon of light, a shape, a colour — is what makes a transition read as a transition
rather than a cut. Without one, "wild transitions" degrades into a slideshow. This is also what the
`EDIT: morph` and match-cut vocabulary needs in order to work at all: `EDIT: match cut on the
movement` has to land on something continuous, or there is nothing for the cut to be inside.

---

## 8 — Extending a shot changes how you end it

`video_extension` is Seedance 2.5 only — 2.0 has no equivalent in any mode — and it takes an
`extension_mode` of `forward` or `backward`. `backward` generates the seconds *before* a clip you
already have, which is the more film-useful of the two.

An extension is only as good as the frame it starts from:

- **Write the last beat locked and motionless** on any clip you intend to extend. This is what the
  final beat's `EDIT` block is for: `EDIT: hold the last frame motionless for half a second.` A clip
  that ends mid-move gives the extension nothing to hold and it invents a new scene.
- **The extension prompt describes what changes, not the frame it starts on** — the same rule as
  image-to-video, applied to the tail instead of the head.
- **Restate identity, geography, light and lens anyway.** Every prompt is still an island (§1); the
  source video anchors continuity but does not carry your descriptors. Pasting the `PROMPT SEGMENTS`
  pack and the scene's `CONTEXT` tier makes that restatement free.
- **Give the continuation its own event and its own tactics.** A continuation that replays the
  previous scene's task reads as a loop, not a next beat.

---

## 9 — Worked reference

Full worked prompts in the rig, including the compression pass shown end to end:
[examples.md](examples.md).

For finish-grade work specifically, the shipped examples live with the project pack:
`02-Projects/AI Film/Seedance 2.5 vs 2.0/01-Storyboard/prompts-v2/` — asset bible, style blocks, and
both photoreal and stylised full-length shots. `advanced/A5-gravity-mercedes.md` is the brand and
product register; `advanced/A6-hairline.md` is the acting register, with `A6b-extension.md` as the
worked `video_extension` continuation.

Sources: higgsfield.ai/@higgsfield.studio/projects/oneiric · /kok-boru · /zephyr-special ·
higgsfield.ai/@mixingburrito1329/projects/anime-production
