# Presets

Never load all twenty-seven blocks. Start from the preset that matches the job, then add or drop
blocks against the actual beat. **An empty block costs a line and buys nothing** — if you cannot
write a real value for it, it is not in this prompt.

These are the same six starters the ReelStack Sequence Builder opens with
(`reel-stack.com/lab/prompt-rig/`), so a preset picked there and a preset picked here produce the
same block list.

---

## At a glance

| | CINEMATIC | ACTION | MOTION GRAPHICS | COMMERCIAL | STYLISED | EVERYTHING |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| **Blocks** | 15 | 14 | 12 | 14 | 13 | 27 |
| SCENE CONTEXT | ● | ● | ● | ● | ● | ● |
| FORMAT MODE | ● | ● | ● | ● | ● | ● |
| ACTIVE REFERENCES | ● | ● | | ● | ● | ● |
| LOCATION MAP | | ● | | ● | | ● |
| CAST | ● | ● | | | ● | ● |
| STAGING | ● | ● | | ● | | ● |
| WARDROBE | ● | ● | | | ● | ● |
| GAZE AND EYELINES | ● | | | | | ● |
| EVENT AND SHARED DIRECTION | ● | | | | | ● |
| RULES | ● | ● | ● | ● | ● | ● |
| OPEN | ● | ● | ● | ● | ● | ● |
| ACTION | ● | ● | ● | ● | ● | ● |
| CAMERA | ● | ● | ● | ● | ● | ● |
| LENS | ● | ● | | ● | ● | ● |
| PERFORMANCE | ● | ● | | | ● | ● |
| DIALOGUE | ● | | | | | ● |
| SFX | ● | ● | ● | ● | ● | ● |
| EDIT | ● | ● | ● | ● | ● | ● |
| PHYSICS | | ● | | ● | ● | ● |
| LIGHTING | ● | ● | | ● | | ● |
| AUDIO | ● | ● | ● | ● | ● | ● |
| SCORE | | | ● | ● | | ● |
| STYLE | ● | ● | ● | ● | ● | ● |
| STYLE LOCK | | | ● | | ● | ● |
| TYPOGRAPHY | | | ● | | | ● |
| VOICE | ● | | | ● | | ● |
| POSITIVE LOCKS | ● | ● | ● | ● | | ● |

**`STYLE LOCK` and `POSITIVE LOCKS` are near-mutually-exclusive.** Photoreal work takes
`POSITIVE LOCKS` and no negations. Stylised work takes `STYLE LOCK`, where the negations are
load-bearing because the brief has to fight the model's gravity back toward photography. Loading
both is usually a sign the register has not been decided.

---

## CINEMATIC — direction and acting

For scenes where the performance is the point: two-handers, dialogue with subtext, a face carrying a
turn. The heaviest `CONTEXT` tier of any preset, because acting is staged and staging is context.

```
SCENE CONTEXT:
FORMAT MODE:
ACTIVE REFERENCES:
CAST:
STAGING:
WARDROBE:
GAZE AND EYELINES:
EVENT AND SHARED DIRECTION:
RULES:

BEAT 1 —
OPEN:
CAMERA:
LENS:
ACTION:
PERFORMANCE:
DIALOGUE:
SFX:
EDIT:

LIGHTING:
AUDIO:
STYLE:
VOICE:
POSITIVE LOCKS:
```

Notes:

- `GAZE AND EYELINES` is the block people skip and it is the one that fixes the dead group shot.
  Build it as a ladder, beat by beat.
- `PHYSICS` is deliberately absent — in a dialogue scene nothing has enough mass for it to earn its
  words. Add it back the moment somebody moves.
- One speaker per beat. Cut for the second performance.
- For a real two-hander, swap `PERFORMANCE` for per-character `ACTING TASK` blocks plus
  `MICRO-BEHAVIOUR`. [acting-task.md](acting-task.md).

---

## ACTION — weight, contact, consequence

Fights, chases, stunts, impacts, crowds. `PHYSICS` and `LOCATION MAP` come in; the acting apparatus
goes out, because a fight beat has one performer and no subtext.

```
SCENE CONTEXT:
FORMAT MODE:
ACTIVE REFERENCES:
LOCATION MAP:
CAST:
STAGING:
WARDROBE:
RULES:

BEAT 1 —
OPEN:
CAMERA:
LENS:
ACTION:
PERFORMANCE:
SFX:
EDIT:

PHYSICS:
LIGHTING:
AUDIO:
STYLE:
POSITIVE LOCKS:
```

Notes:

- `PHYSICS` is the highest-value block in this preset. Name the mass, say where the energy goes,
  include the recovery.
- `LOCATION MAP` carries closing distance, which is the whole grammar of a chase.
- One impact per beat. Fast camera + fast cut + busy frame in one shot is a documented failure
  combination — pick one. [action.md](action.md).
- `PERFORMANCE` stays, cut down to `wants` and `plays`. A stunt with a face doing nothing reads as a
  crash-test dummy.

---

## MOTION GRAPHICS — type and flat colour

Kinetic type, animated diagrams, flat-colour explainer B-roll. No cast, no location, no lens — there
is no camera in the physical sense, so the blocks that describe one are noise.

```
SCENE CONTEXT:
FORMAT MODE:
RULES:

BEAT 1 —
OPEN:
CAMERA:
ACTION:
SFX:
EDIT:

AUDIO:
SCORE:
STYLE:
STYLE LOCK:
TYPOGRAPHY:
POSITIVE LOCKS:
```

Notes:

- **This is the one preset where `TYPOGRAPHY` carries a real value** — and even here, expect to
  composite the final lockup in post. Seedance corrupts lettering on every version. Ask for shape,
  motion and negative space; add the words yourself.
- `STYLE LOCK` is doing the heaviest lifting: flat colour has to be defended against the model's pull
  toward photography and depth.
- `CAMERA` becomes a 2D move — push, pan across the board, hold. Still one per beat.
- `SCORE` matters more here than anywhere: motion graphics cut to music and the timing has to come
  from somewhere.

---

## COMMERCIAL — product and surface

Product films, spec spots, anything where a specific object has to stay a specific object. Identity
moves from faces to a thing, and surface behaviour under light becomes the whole job.

```
SCENE CONTEXT:
FORMAT MODE:
ACTIVE REFERENCES:
LOCATION MAP:
STAGING:
RULES:

BEAT 1 —
OPEN:
CAMERA:
LENS:
ACTION:
SFX:
EDIT:

PHYSICS:
LIGHTING:
AUDIO:
SCORE:
STYLE:
VOICE:
POSITIVE LOCKS:
```

Notes:

- **The product's badge, logo or lettering never comes from the video prompt.** Generate it onto the
  product in the reference plate and bind the plate. Asking a video model to draw a mark is how you
  get a mark that is nearly right, which is worse than absent. [finish.md](finish.md) §3.
- `LIGHTING` is the preset's centre of gravity. A product film is a lighting exercise; the camera is
  usually simple and the action is usually one move.
- `PHYSICS` covers how the surface behaves — reflections travelling across a panel, liquid finding
  its level, fabric settling.
- `VOICE` is present for VO. If the spot has none, drop it and say `SCORE:` explicitly instead.
- `CAST` is absent by default. Add it the moment a person's face is in frame.

---

## STYLISED — anime, painterly, abstract

Non-photoreal work of any kind. The negation blocks come in, the photoreal enforcement goes out, and
the architecture flattens to three immutable blocks and one variable.

```
SCENE CONTEXT:
FORMAT MODE:
ACTIVE REFERENCES:
CAST:
WARDROBE:
RULES:

BEAT 1 —
OPEN:
CAMERA:
LENS:
ACTION:
PERFORMANCE:
SFX:
EDIT:

PHYSICS:
AUDIO:
STYLE:
STYLE LOCK:
```

Notes:

- **`POSITIVE LOCKS` is absent on purpose.** In stylised work the negations belong in `STYLE LOCK`
  and they are load-bearing. Loading both blocks means the register has not been decided.
- `LIGHTING` is absent because in a stylised medium light is a drawing decision, not a physical one —
  it belongs inside `STYLE`.
- Treat `STYLE LOCK`, `PHYSICS` and `RULES` as **immutable across the whole project**. Retyping any
  of them is how a stylised sequence drifts back to photoreal by shot four.
- `PHYSICS` here describes the medium's physics, not the world's: animation on twos, held frames,
  no motion blur, no interpolation.

---

## EVERYTHING — all 27 blocks

Not a preset to write in. Load it to **strip down** from — when the job is unusual enough that none
of the five fit, start here and delete every block you cannot write a real value for. What survives
is the preset that job needed.

Also the right starting point for building a project-specific preset you intend to reuse. Strip once,
save the result to the project, and every prompt on that film starts from the same block list.

---

## Building your own

The five presets above are starting points, not a taxonomy. The rig is the taxonomy; the presets are
opinions about which blocks a kind of job usually needs.

To build one:

1. **Write one prompt for the job in EVERYTHING**, honestly, filling only the blocks you can fill.
2. **Delete every block you left empty.** That is your preset.
3. **Run a second prompt for a different beat of the same job through it.** Whatever you had to add
   back belongs in the preset; whatever you deleted again does not.
4. **Save the `PROMPT SEGMENTS` tier with it.** The block list is half a preset; the filled segment
   values are the other half, and they are the half that saves you time.

Two prompts is enough. A preset derived from one prompt is a description of that prompt.

---

## Saving a PROMPT SEGMENTS pack

The third tier is the reusable one, so it is worth storing separately from any single prompt:

```
segments/<pack-name>.md

# <pack name>
for: <what kind of work this is for>

PHYSICS: …
LIGHTING: …
AUDIO: …
SCORE: …
STYLE: …
VOICE: …
POSITIVE LOCKS: …
```

Load the pack, write `CONTEXT` and `BEATS`, concatenate. When you ask an AI to iterate a sequence,
tell it the segments are locked and it rewrites only the first two tiers — which is most of the token
saving and all of the consistency.

A project usually ends up with two or three packs: one per register. A film with a present-tense
register, a flashback register and an archive register has three, and **they never blend** — every cut
between them is hard.
