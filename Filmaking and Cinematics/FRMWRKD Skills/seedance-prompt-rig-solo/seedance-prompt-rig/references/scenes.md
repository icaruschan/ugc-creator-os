# Scaling to sequences

One `CONTEXT` tier, many `BEATS`. This is what makes the rig worth its setup cost: the second shot
in a scene costs one BEAT, not another prompt.

This file owns everything past a single shot — the scene file, the ledger, the in-clip cut budget,
the `EDIT` block, the thirty-second sequence, and what to do when the work is longer than one clip.
Pair it with [binding.md](binding.md); a sequence that does not hold together is almost always a
sequence whose references were re-bound differently on the second clip.

---

## The scene file

Keep a scene as one file. It survives sessions and it is the continuity record — the place the
`CONTEXT` tier lives between the day you write it and the day you shoot the rest of the coverage.

```
scenes/<scene-slug>.md

# <scene name>
model:  seedance 2.5 · 30s · 720p · 2.39:1
pool:   @Image1 hero · @Image2 hero head · @Image3 corridor · @Video1 gimbal drift
preset: CINEMATIC

## CONTEXT
SCENE CONTEXT: …
FORMAT MODE: …
ACTIVE REFERENCES: …
LOCATION MAP: …
CAST: …
STAGING: …
WARDROBE: …
GAZE AND EYELINES: …
RULES: …

## LEDGER
| Holds across | Value |
|---|---|
| wardrobe | maroon jacket, olive bodysuit, black boots |
| markers | rimless glasses, lower-lip ring |
| light state | overcast daylight through seams, no practicals |
| camera side | interior only, never exterior |

## BEATS
BEAT 1 — <slug>
OPEN: …
CAMERA: …
ACTION: …
EDIT: hard cut.

BEAT 2 — <slug>
…

## PROMPT SEGMENTS
PHYSICS: …
LIGHTING: …
AUDIO: …
SCORE: …
STYLE: …
VOICE: …
POSITIVE LOCKS: …
```

**Reuse the `CONTEXT` tier verbatim.** A re-typed `CONTEXT` is a continuity break — one changed
adjective in `STYLE` and the grade shifts between shots, one re-phrased role line and the face
does. Copy, never retype. The same applies to the `PROMPT SEGMENTS` tier, and more strongly: it is
the tier that is meant to be pasted.

The `pool` line is there so that the reference numbering is decided once. `@Image2` meaning the hero
head in clip one and the corridor in clip four is the quietest way to break a sequence.

---

## The ledger

Four to eight rows. Only things that must not change. Check every new BEAT against it before
delivering.

Rows worth having: wardrobe · unrepeatable markers · light state · time of day · which side of the
action the camera stays on · props and who owns them · voice identity per speaker.

Rows not worth having: anything the `CONTEXT` tier already states unambiguously. The ledger is a
checklist for *you*, not text that ships in the prompt. If a row starts wanting to be in the render,
it is a `RULES` clause or a `POSITIVE LOCKS` clause and it belongs in the prompt body instead.

---

## Cuts inside one clip

Seedance handles in-clip cuts natively. It is genuinely good at shot-reverse, match cuts and action
cuts. But there is a ceiling.

| Model | Practical cut budget | Note |
|---|---|---|
| 1.0 | 2 shots, 1 cut | Silent. Wide → close is the reliable pair |
| 1.5 pro | 2–3 shots | Audio carries across the cut |
| 2.0 | 3–4 shots | Reference binding is what holds identity across cuts |
| 2.5 | 5–6 shots | Built for it — setup / develop / turn / resolve in one pass |

Past the budget, expect identity drift from the third or fourth cut onward. The drift is not gradual;
it arrives at a particular cut and everything after it is a different film. State the budget in
`FORMAT MODE` and keep the beat count in agreement with it — the linter checks that they match,
because a `FORMAT MODE` claiming three cuts over a prompt carrying six is the most common structural
error there is.

### Forcing the cut

Unlabelled multi-beat prompts render as one continuous take. The `BEAT` label plus the `EDIT` block
is what forces the edit:

```
BEAT 1 — <slug>
CAMERA: <one move>
ACTION: <one primary action>
SFX: <its sound>
EDIT: hard cut.

BEAT 2 — <slug>
CAMERA: <one move>
ACTION: <one primary action>
SFX: <its sound>
```

Keep each beat to one move and one primary action. This is the same one-move law, applied per beat
rather than per clip. A beat with a push and a whip in it does not become two shots; it becomes one
shot with jitter in it.

---

## The `EDIT` block, in full

`EDIT` is the out-point. Five values cover everything, and picking the wrong one is more expensive
than leaving it out.

| Value | Right when |
|---|---|
| `hard cut` | the default, and the only one that is free |
| `match cut on the movement` | a gesture spans the cut and you want the motion carried across it |
| `dissolve` | almost never — Seedance is poor at it |
| `morph` | a continuous graphic element exists on both sides of the change |
| `hold` | the clip is going to be extended |

**Hard cut.** `EDIT: hard cut.` Nothing is cheaper and nothing is more reliable. Every coverage
pattern below is built out of hard cuts, and a sequence made entirely of them reads as an edit
rather than as a model transitioning. When in doubt, this one.

**Match cut on the movement.** `EDIT: match cut on the movement — the cut lands inside the turn, so
the motion carries across it.` The cut falls *inside* a gesture that is already running, and the
gesture completes on the other side of it at a different size. Say which movement carries it; a
match cut with no named movement to match on is a hard cut with extra words. This is the pattern
that makes coverage read as coverage instead of as four separate renders.

**Dissolve.** Rare, and worth being blunt about: Seedance renders dissolves poorly on every version
— it tends to produce a soft blend that reads as a glitch rather than as an optical transition.
Cut hard and dissolve in post, where the transition can be timed to picture and where undoing it
costs nothing.

**Morph.** `EDIT: morph — the wheel of the car becomes the face of the clock, held dead centre
throughout.` 2.5 handles a graphic match better than it handles a dissolve, but only when there is
a **continuous graphic element to match on** — a shape, a mass, a line that occupies the same part
of frame before and after. Without one, morph degrades into the same soft blend as a dissolve. Name
the element and say where it sits in frame.

**Hold.** `EDIT: hold the last frame motionless for half a second.` The last beat of any clip you
intend to extend must be written locked and motionless. `video_extension` holds whatever the source
ends on and continues from it; a clip that ends mid-move gives the extension a moving frame to
guess about, and it invents a new scene rather than continuing yours. This is the single highest-cost
mistake in sequence work, because it is not visible until the extension comes back.

---

## Timecodes

Default to `→` ordering inside `ACTION`, not clocks. ByteDance's own guidance flags strict timing
markers as unstable, and in practice they cause the model to rush or stall to hit them.

Use timecodes only when:

- syncing to a supplied audio reference,
- editing a specific range of an existing clip (2.5 supports this),
- the user has an edit already cut and the render must slot into it.

When you do use them, keep to whole seconds and no more than four segments. The linter flags
timecodes on the models where they destabilise.

---

## Coverage patterns

Reliable shapes for common beats. Each fits inside one clip on 2.0 or 2.5.

**Establish → land** (2 beats) — a silent wide that sets the geography, hard cut to the close where
the beat actually happens. The wide is doing spatial work, not dramatic work, so it wants to be the
short one — ask for about two and a half seconds and trim it to one in the edit.

**Shot–reverse** (2–4 beats) — one speaker per beat. The best-supported multi-shot pattern there is,
and the only reliable way to render a two-hander. `STAGING` carries the axis; the beats carry the
lines.

**Action cut** (2 beats) — a move begins wide and completes in close. The cut lands *inside* the
movement, so the motion carries across it. This is what `EDIT: match cut on the movement` is for;
say which frame the cut falls on.

**Push triplet** (3 beats) — wide, medium, close on the same subject, each a hard cut, no camera
move in any of them. Cheap, clean, and it reads as coverage rather than as AI. Vary `LENS` and
nothing else.

**Reveal** (2 beats) — a detail so tight it is unreadable, then the pull that explains it. The second
beat carries all the information; the first carries all the tension.

---

## The thirty-second sequence

2.5's 30-second ceiling changes the unit of work. At 30 seconds you are not writing a shot, you are
writing a scene, and the whole rig is built for exactly this case.

**The cut budget is the constraint, not the duration.** Five to six shots is the ceiling, and it is
the same ceiling at 12 seconds as at 30. What the extra seconds buy is not more cuts, it is longer
ones — beats with room to play rather than beats that have to state themselves and get out.

**Thirty seconds across six beats is five seconds a beat, and that is a real edit rhythm.** It is
close to how a dialogue scene actually cuts. A six-beat 30-second clip is a complete unit of
storytelling — setup, develop, turn, resolve — and it comes back as one file that is already cut.

**The `CONTEXT` tier is amortised across all six beats, so its cost per beat collapses.** A 240-word
`CONTEXT` over one beat is most of the prompt; over six beats it is forty words a beat. The tier that
looks expensive on a single shot is the cheapest thing in a sequence, which is why loading more
`CONTEXT` blocks gets *more* attractive as the clip gets longer, not less. Worked, at 30 seconds:

```
CONTEXT   238 w        one scene
BEATS     6 × 118 w    = 708
SEGMENTS  186 w        pasted from the pack
total     1,132 w      against a working ceiling of 1,750
```

**Generate long and cut short.** The model needs run-up to stabilise — the first fraction of a
second of any beat is where it settles into the shot. A one-second beat is not a thing you should
ask for; it is a request for the unstable part with none of the stable part attached. Ask for about
**2.5 seconds minimum per beat** and trim in the edit, where trimming is free. Six beats at five
seconds gives you thirty seconds of material and about eighteen usable.

**Past 30 seconds, plan as 30 s + extension, not as separate clips.** Two 30-second clips built from
the same `CONTEXT` will be close, but close does not intercut — the grade lands slightly apart, the
face lands slightly apart, and you notice at the join. `video_extension` carries subject, scene,
style and sound forward, and two rounds are supported. Write the last beat of the first clip as a
`hold` and the extension has something to continue from.

---

## Sequences past one clip

Beyond the cut budget, or past what extension can carry, you are cutting clips together in post.
Three things make them match:

1. **The `CONTEXT` tier is identical across every clip.** Not similar. Identical. Paste it.
2. **The `PROMPT SEGMENTS` tier is identical across every clip.** See below.
3. **Chain the frames.** Take the last frame of clip A and pass it as the first-frame reference of
   clip B. Every model supports first-frame conditioning; 1.5 and up also take a last frame, so you
   can pin both ends.

On 2.5 specifically, prefer **extension** over a new clip: it carries subject, scene, style and
sound forward. A new clip carries nothing but what you re-bind.

### `PROMPT SEGMENTS` is what makes clips intercut

The third tier is the strongest continuity device in the rig, and almost nobody uses it that way.
`PHYSICS`, `LIGHTING`, `STYLE`, `VOICE` and `POSITIVE LOCKS` pasted **byte-identical** across every
clip in a sequence is a stronger guarantee than any per-clip lock you can write, because there is no
re-decision anywhere for the model to make differently. A lock says *keep doing this*; an identical
segment gives it nothing else to do.

And it is free. You are not writing it again, you are pasting it. The only way to lose the guarantee
is to retype the tier, or to let a well-meaning iteration pass rewrite it — so when you hand a
sequence to anything that will edit it, say the segments are locked and only the first two tiers are
in play.

---

## Converting a shot list

When the user arrives with a shot list rather than a beat:

1. Read the whole list before writing anything. The `CONTEXT` tier is derived from what is *common*
   to every shot — that is the only way to know what to hoist.
2. Write the `CONTEXT` tier from the intersection.
3. Write one BEAT per line of the list, delta only.
4. Group BEATS into clips by cut budget, not by scene logic. Four shots on 2.0 is one clip; eight
   shots is two.
5. Flag any shot that changes light state, location or time of day — that is a **new prompt**, not a
   new BEAT.

Step 5 is the one that gets missed, and it is the one that produces a sequence that will not
intercut. One light state per prompt is not a style preference; the model picks one of the two states
and ignores the other, or blends them into something that is neither. Day and dusk in the same brief
is two `CONTEXT` tiers, two prompts, and a hard cut between them in post — or, better, generate the
first state and feed its last frame in as the reference for the second.
