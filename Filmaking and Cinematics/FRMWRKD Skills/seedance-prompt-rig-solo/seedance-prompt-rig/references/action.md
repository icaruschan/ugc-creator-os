# ACTION — weight, contact, consequence

This file drives the `ACTION` block in the BEATS tier, and it is what the ACTION preset is built
around ([presets.md](presets.md)). Load it with [camera.md](camera.md) — half of an action beat is
the rig.

Why generic prompt templates fail here: the model does not struggle with "man punches man". It
struggles with weight, contact and consequence. Action that looks fake looks fake because nothing
has mass and no force goes anywhere.

---

## Where an action beat's facts live

An action beat is not one block. It is eight facts with three different lifespans, and most bad
action prompts are a single paragraph carrying all eight — which means the mass, the geography and
the rig all get re-decided at every cut. File them:

| The fact | Block | Tier | Written as |
|---|---|---|---|
| mass and inertia — how bodies and matter behave at all | `PHYSICS` | segments | `real mass and inertia. A heavy body arrives after the limb that swings it and takes a full beat to settle. Nothing floats and nothing snaps back.` |
| geography and distance — what is where, and what is closing | `LOCATION MAP` | context | `the straggler is forty feet ahead on the same road, screen-right, and losing it. The rank recedes toward the hills behind him.` |
| the rig, and its ONE move | `CAMERA` | beat | `tracking alongside him at shoulder height, the frame shaking with the ground under his feet, settling as he comes level.` |
| readable shape, and the framing floor | `LENS` | beat | `full body, 35mm, the whole shape of the swing stays in frame and NEVER opens to a wide.` |
| what happens, in order | `ACTION` | beat | `he plants → the shoulder drops into it → the other man folds over the arm → both go down together` |
| impact and consequence sound | `SFX` | beat | `<the flat crack of a shield> <a body arriving on ground> <grit sliding under two heels>` |
| the cut, and where inside the movement it lands | `EDIT` | beat | `match cut on the movement — the cut lands inside the fall, so the motion carries across it.` |
| what must stay true after a render dropped it | `POSITIVE LOCKS` | segments | `exactly two fighters are in frame for the whole clip. Every hit lands at the frame edge or below it.` |

Two misfiles account for most bloated action prompts. **Mass written into `ACTION`** is bought once
per beat and re-rolled at every cut, when one `PHYSICS` block at the bottom covers the whole
sequence and the next project as well. **Geography written into `ACTION`** turns every beat into a
re-establishing shot; `LOCATION MAP` states the distances once and the beats only close them.

---

## The four rules

### 1. Name the mass, not the speed

"Fast" is the least useful word in an action prompt. The model renders speed as blur, and blur is
what makes AI action look cheap.

| Weak | Strong |
|---|---|
| he punches him very fast and hard | his weight arrives before his fist, and the impact folds the other man over it |
| she runs quickly across the plain | she runs heavy, armour bouncing, each stride landing flat and costing her something |
| the rocket flies fast | the rocket rips past low enough to snatch the dust up behind it |

Speed is the *result* of mass moving. Describe the mass and the speed comes free — with weight
attached.

The general rule — that bodies have inertia, that fabric lags a turn, that nothing snaps back —
belongs in `PHYSICS`, once, at the bottom, where it is reusable across the whole project.
The beat's `ACTION` names only the mass that is moving in *this* shot.

### 2. One impact per BEAT

Seedance smears limbs when several collisions compete for the same second. One contact, and give it
room.

**`EDIT` is how you split a combo.** A three-hit combination is three beats and two hard cuts — or
one beat in which two hits happen off-frame and one lands on camera. Both read as a combination;
neither asks the model to resolve three collisions inside one second. Stay inside the model's cut
budget while you do it: 1.0 → 2 shots · 1.5 → 2–3 · 2.0 → 3–4 · 2.5 → 5–6.
[scenes.md](scenes.md).

### 3. Say where the energy goes

Every force needs a destination. Unresolved force is the tell of synthetic action.

```
… and the momentum slams him backwards, heels ploughing two grooves into the floor, the arm
shuddering as it holds.
… they go down together, the dust bursting up around them, the line collapsing on both sides of the
hit.
… the blade keeps going past the block, tracking down and out of frame, never stopping, never
bouncing back.
```

That last one matters: **a weapon or limb that stops dead at contact reads as a collision with an
invisible wall.** Follow-through is what sells the strike. If the strike is a glancing blow, say the
tip continues past.

This is also why `ACTION` ends on a held state rather than mid-gesture — the last clause is the
final frame, and on a clip you intend to extend it is the only thing the extension has to hold.

### 4. Three or more simultaneous fighters is the drift cliff

Identities cross-contaminate. Options: push extras into motion blur and depth, cut them into their
own BEAT, or make the crowd a condition of the environment rather than a cast of characters.

---

## The failure combination

**Fast camera + fast cut + busy frame in the same shot.** Documented across every Seedance version.
Pick one:

| Keep | Give up |
|---|---|
| Fast camera move | Hold the cut, simplify the frame |
| Fast cutting | Lock or slow the camera |
| Busy frame | Slow the camera, hold the cut |

The best AI action shots are usually a **locked or simple camera on a violent event**. The violence
carries the energy; the camera does not have to. A locked camera is a choice and has to be stated in
`CAMERA` — say nothing and the model invents drift on top of the action, which is the busy frame and
the fast camera arriving together by accident.

---

## Impact vocabulary that renders

**Weight transfer** — plants, whirls, pivots like a hammer-thrower, drives off the back foot, drops
his shoulder into it.

**Contact** — the meaty clamp of a hand on metal, the flat crack of a shield, the dull thud of a
body arriving on ground.

**Consequence** — heels plough, dust bursts, ranks buckle, the body tumbles under and with him,
sparks crack off the surface.

**Strain** — the arm shuddering, teeth gritted, the strap creaking under load, breath forced out on
the effort.

**Recovery** — knees absorbing the landing, the stagger before the balance returns, the half-second
before he moves again.

That last category is the one people skip, and it is the one that separates a stunt from a cartoon.
Landing without recovery is floating. Contact and consequence get a second pass in `SFX` — the same
event, heard: one `< >` pair per sound, in the order they happen, object and action, never an
adjective.

---

## Crowds and armies

Never a cast. Always a condition, with three properties:

```
… a marching rank that thins away toward the hills, varied and never repeated, shields and
spear-tips picking up the low sun.
```

- **Varied, not cloned.** Say it. The default is a copy-paste army.
- **Depth, not width.** Ranks that recede into distance read as scale. A line laid across frame
  reads as a wall. That recession is geography, so it belongs in `LOCATION MAP`.
- **One thing they are collectively doing.** Advancing, breaking, going flat, clearing out of the
  way. **That single collective action is a clause in `ACTION`** — it is what changes this beat, and
  it is the only thing the crowd is permitted to be doing in it. A crowd with individual intentions
  becomes noise.

Individuals inside a crowd get a single distinguishing behaviour and nothing else — `one of them
lets go of his weapon and drops` — never a description. A named individual with a face is a member
of `CAST`, and then the drift cliff in rule 4 applies to him.

---

## Chases and vehicle work

- **The camera is rigged to something.** Say what, in `CAMERA`: behind the object, alongside the
  runner, on the hood. A free-floating chase camera drifts. It is still one move — the rig is the
  move.
- **The subject stays fully readable.** If a prop's shape is the point, pull the rig wider in `LENS`
  so the whole shape stays in frame. Half a shape at speed is an unrecognisable smear.
- **The world does the moving.** Subject sharp, world in motion blur. That is the entire grammar of
  a chase shot.
- **Closing distance is the story.** State the starting gap in `LOCATION MAP` — `forty feet ahead
  and losing it` — and close it in the beats: `he fills more of the frame with every second` is a
  plot beat expressed as blocking.

---

## Violence, safety and the content filters

Consumer Seedance channels reject violence keywords, real-person face references, celebrity names
and brands. This is a hard gate, not a soft preference.

Practical translation, which is also better writing:

| Blocked | Renders, and reads better |
|---|---|
| blood, gore, wounds | sparks where things collide, nothing wet |
| stabbing, killing | the blade tracks past and out of frame |
| a named celebrity | build, wardrobe and one unrepeatable marker |
| graphic injury | black on the last frame before contact |

**Cutting away before the contact is almost always the stronger choice anyway.** The frame before is
more violent than the frame after, and it passes the filter.

Where that is a standing rule for the sequence rather than one beat's staging, write it into
`POSITIVE LOCKS` as an assertion, never as a ban: `every hit lands at the frame edge or below it,
and the shot cuts on the swing` — not `no violence on camera`. Seedance has no negative prompt
parameter, and a ban naming the thing you are trying to avoid is the most reliable way to summon it.
[blocks.md](blocks.md) §27.
