# ACTIVE REFERENCES — reference binding

This file owns exactly one block: `ACTIVE REFERENCES`, in the `01 · CONTEXT` tier, written once at
the top of the prompt and never restated in a beat.

Attaching a reference does not tell the model what to do with it. Binding does. This is the
highest-leverage block in the rig and the one most often written wrong — law 4 in `SKILL.md` exists
because of it.

Role lines are the reason the CONTEXT budget scales with references: **35 words per block loaded,
+25 for every bound reference beyond the second, +5 per beat, cap 480.** A reference you did not pay words for is a reference the model interprets for you.

Fill rules and the block's place in the order: [blocks.md](blocks.md) §3.

---

## The role line

Every reference gets exactly one line, and every line has three parts:

```
@ImageN → <who or what>: <what to take>. NOT <what to leave>.
```

| Part | Job |
|---|---|
| The alias | Ties the tag to a noun the rest of the prompt can refer to |
| What to take | The attributes you are actually harvesting |
| The `NOT` clause | The attributes you are refusing |

**Without the `NOT` clause, the model blends everything in the image into the shot.** That is how a
close-up face reference ends up overriding your wide blocking, and how a location plate's time of
day overrides your lighting.

### Right

```
ACTIVE REFERENCES:
@Image1 → the pilot, body and rig: her pose in the seat, the strap tension, the cabin around her. NOT the face detail.
@Image2 → the pilot, head: skin texture, glasses, lip ring, eye colour, at close-up sharpness. NOT the pose, NOT the framing, NOT the background.
@Image3 → the corridor: architecture, materials, the light through the seams. NOT any person in it.
@Video1 → camera behaviour ONLY: the drift and re-settle of a hand-held gimbal. NOT its subject, NOT its grade, NOT its cutting.
@Audio1 → room tone bed ONLY. NOT its music, NOT any speech in it.
```

### Wrong

```
@Image1 and @Image2 are the first and last frames        ← two roles in one line, model picks one
@Image1 is the character reference                       ← no exclusions, everything bleeds
follow the references closely                            ← binds nothing
@Image2 position, mood, everything                       ← "everything" is not a role
```

---

## One role per line, one owner per thing

- **One line per reference.** Never combine.
- **Each prop belongs to exactly one character.** If two characters both "have the bass guitar", the
  model gives it to both or neither.
- **Never leave a reference unassigned.** An attached image with no role line still influences the
  render, uncontrolled. Either bind it or detach it.
- **Name the alias, then use the alias.** `@Image1 (the pilot)` once, then "the pilot" everywhere
  else. Repeating the tag inside `ACTION` or `OPEN` reads as a new instruction.

---

## ACTIVE REFERENCES and CAST are different blocks

They are adjacent in the CONTEXT tier and they are routinely collapsed into one. They do not do the
same job.

| | `ACTIVE REFERENCES` | `CAST` |
|---|---|---|
| Binds | plates — images, video, audio | nothing; it is description |
| Says | what to take from each file, and what to refuse | who is in the scene, and what stays identical about them |
| Exists in `text2video` | no | yes, and it carries the whole identity |
| Shape | one `@tag →` line per file | a sentence or two of prose |

`ACTIVE REFERENCES` is the harvest instruction. `CAST` gives the rest of the prompt **nouns to point
at** — names, builds, and one unrepeatable marker each — so that `ACTION`, `PERFORMANCE` and
`GAZE AND EYELINES` can address a person rather than a file. Nothing else in the rig can write "RAY
turns exactly once" if `CAST` never named RAY.

Both can be present, and in `ref2video` both usually are. Neither replaces the other:

- `CAST` with no `ACTIVE REFERENCES` is `text2video` — legal, weaker on identity.
- `ACTIVE REFERENCES` with no `CAST` is a prompt full of `@Image2` where the character's name should
  be, which reads to the model as a fresh binding instruction every time it appears.

In `ref2video`, keep `CAST` short. The plates carry the likeness; `CAST` carries the names and the
markers only, and every adjective it repeats from the plate is a word competing with the plate.

---

## Fidelity grades

When a plain take/exclude split is not precise enough, grade it:

| Grade | Means | Use for |
|---|---|---|
| `full-preserve` | Reproduce exactly, pixel-faithful | Faces, logos, a specific prop's design |
| `partial-preserve` | Keep the identity, allow re-pose and re-light | Characters in new blocking |
| `attribute-transfer` | Take one property only | A palette, a material, a fabric |
| `loose-guide` | Direction only | Mood boards, composition hints |

```
@Image2 → the pilot's head: full-preserve on skin, glasses and lip ring; partial-preserve on expression. NOT the pose.
```

---

## The finish-grade convention — the asset is a pair

On work you are paying to complete rather than exploring, references stop being files and become
named assets, and the convention tightens:

> *An asset is a pair: text + image. The text descriptor goes into every prompt word for word; the
> image is the reference the model anchors to.*

One element, one name, everywhere:

```
@loc_<PROJ>_<name>_<variant>        @char_<PROJ>_<name>_<scene>_<version>        @prop_<PROJ>_<name>
```

In the prompt, each tag gets its full stored descriptor — **pasted verbatim, never paraphrased, in
every shot** — and the block closes with:

```
100% matches the reference.
```

A synonym is a drift. Rewriting a descriptor because it read a little stiff re-rolls the asset, and
the whole point of the pair is that the words and the pixels arrive together saying the same thing
in every prompt they appear in. `VOICE` works identically for the same reason.

This register is longer and more repetitive than the compressed rig on purpose. Full treatment,
including block order and staging that words alone cannot hold: [finish.md](finish.md).

---

## Tag syntax per platform

The tag itself is platform-specific. Compose in one dialect and convert on delivery.

| Platform | Image | Video | Audio |
|---|---|---|---|
| fal.ai | `@Image1` | `@Video1` | `@Audio1` |
| Replicate | `[Image1]` | `[Video1]` | `[Audio1]` |
| BytePlus ModelArk | `[Image 1]` | `[Video 1]` | `[Audio 1]` |
| Volcengine (CN) | `@图片1` | `@视频1` | `@音频1` |
| Dreamina / Jimeng | `@Image 1` | `@Video 1` | `@Audio 1` |
| Artlist (MCP) | `{assetId}` for an upload · `{generationId}` for a prior generation | same | same |

**Artlist has two ID namespaces.** An uploaded file binds by its `assetId`; something the platform
generated binds by its `generationId`. The `assetId` inside a share URL is **not** a `generationId`
— polling it for status returns *pending* forever. Uploading the platform's own output back to it as
a reference is normal and is not contamination.

**House default is the fal form** (`@Image1`, no space). Convert at hand-off, and say which dialect
you converted to.

Some third-party front-ends use a UUID form — `<<<a6b968e1-…>>>` — where the platform substitutes
the asset. Those are a UI convention, not a model feature; the role line and its `NOT` clause matter
exactly as much there.

---

## Budgets

| Model | Images | Videos | Audio | Total files |
|---|---|---|---|---|
| 1.0 lite | 1–4 | — | — | 4 |
| 1.0 pro / 1.5 pro | first + last frame only | — | — | 2 |
| 2.0 | 9 | 3 | 3 | 12 |
| 2.5 | 30 | 10 | 10 | 50 |

**The ceiling is not the target.** Official guidance puts stable quality at 1–8 image subjects and
1–5 video/audio references. Past that, attributes start crossing between subjects. Thirty images is
a scene-wide pool to draw from, not a per-shot payload.

Seedance 2.5 file limits: images ≤30 MB each; videos 1.8–30.2 s, ≤200 MB, combined ≤30.2 s,
300–6000 px per side, 24–60 fps source; audio 1.8–30.2 s, ≤15 MB, combined ≤30.2 s. **Audio
references require at least one image or video reference** alongside them.

---

## Per-BEAT subsetting — the rule that makes sequences work

Do not attach the whole pool to every shot. Build the pool once at scene level, then send each BEAT
only what it needs.

```
Scene pool (once):
  characters : hero, second, three extras
  props      : the rifle, the pendant
  sets       : corridor, hall
  motion     : one gimbal-drift reference video

BEAT 1 (wide, three people)  → hero, second, corridor
BEAT 2 (close on hero)       → hero head ref, pendant
BEAT 3 (hall, hero alone)    → hero, hall, gimbal video
```

Every unnecessary reference is a chance for the wrong attribute to migrate. It also costs money —
reference videos bill for their own duration.

The pool is scene-level, so it is described once in the CONTEXT tier. The subset is per-shot, so it
is a dispatch decision, not a second `ACTIVE REFERENCES` block written inside the beat. Beats carry
deltas only, and a reference list is not a delta.

---

## Video and audio references

Video references are the strongest control the model has, and the least used. Bind them to a
**behaviour**, never to content:

```
@Video1 → camera move ONLY: the whip and re-settle of a fast pan. NOT the subject, NOT the location, NOT the grade.
@Video2 → choreography ONLY: the timing and footwork of the sequence. NOT the wardrobe, NOT the framing.
@Video3 → transition and effect treatment ONLY.
```

They are also the one case where the one-camera-move-per-beat rule bends: if a reference video
*demonstrates* a compound move, the model can follow it, because it is copying a trajectory rather
than composing one. Only then. [camera.md](camera.md).

### When the video's motion is NOT the motion you want

A 3D blockout, previz or animatic carries camera, spacing and timing — and placeholder motion on
grey boxes that must never reach the render. The role line is **one compact line**: what it
governs, then what it does not. Then the prompt stops mentioning the video and spends everything on
positive description of the performance.

```
@Video1 → the blockout, and it governs ONLY the camera and the spacing: where the camera sits and how it moves, how the room lays out into depth, roughly where she stands. NOT her movement, NOT her posture, NOT its grey untextured surfaces, NOT its flat unlit look.
```

Never `IGNORE THE MOVEMENT COMPLETELY`, never a second paragraph about the video. Heavy negation
focuses the model on the thing negated, and the actors copy the boxes. Full treatment, the failure
it comes from, and a verified prompt: [blockout.md](blockout.md).

### The `identity ONLY` trap

Never bind a cast plate as *identity ONLY* or *face ONLY* when the plate is a turnaround that also
shows the wardrobe. The model reads it as *take the face, ignore the clothes*, and the outfit drifts
on the first render. Bind face **and** whole outfit, then restate the garments once in `WARDROBE`:

```
@Image2 → Yuna, for her face, hair, ear jewellery and her whole outfit. NOT the pose, NOT the framing, NOT the studio light, NOT the grey background.
```

Audio references bind to a bed or a voice:

```
@Audio1 → ambient bed ONLY. NOT any speech.
@Audio2 → voice identity for the pilot: timbre and pace. NOT the words.
```

A bound voice identity is stronger than any `VOICE` description and outlasts it across shots. When
the model supports it, bind the voice and keep `VOICE` for delivery attributes the plate cannot
carry.

---

## When there are no references

In `text2video` there is no `ACTIVE REFERENCES` block at all — it is simply absent from the prompt,
not present and empty. Identity has to survive on description alone, so:

- **`CAST` carries the whole identity.** Full physical description, build, age, hair, face — the
  work the plates would have done. This is the one mode where `CAST` is allowed to be long.
- **`WARDROBE` carries what is worn**, in the CONTEXT tier, where it is decided once. Written in a
  beat it re-rolls at every cut.
- **`OPEN` carries the first frame**: who, which screen side, which depth, already in motion. It
  does not repeat `CAST` — it places what `CAST` described.
- Give each character **one unrepeatable marker** — a scar through the eyebrow, a tape strip across
  the nose, one dark glove. Shared traits blur; unique traits hold.
- **Never use pronouns across characters.** "He looks at him" is unresolvable without plates and
  produces the twins artefact. Use the name every time.
- Expect flatter expressions and some drift toward familiar screen faces. This is a documented
  weakness of prompt-only identity, not a prompting mistake.
- Two characters maximum before drift becomes the dominant problem.
