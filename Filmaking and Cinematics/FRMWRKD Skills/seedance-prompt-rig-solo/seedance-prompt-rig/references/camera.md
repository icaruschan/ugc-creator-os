# Camera, lens and light

Three blocks draw on this file, across two tiers:

| Block | Tier | Carries |
|---|---|---|
| `CAMERA` | 02 · BEATS | the shot's single move |
| `LENS` | 02 · BEATS | framing for this beat only |
| `LIGHTING` | 03 · PROMPT SEGMENTS | every source, named and placed |

They are three blocks and not one because they have three different lifespans. The move is new in
every beat. The framing is new in every beat for a different reason. The light is not new at all —
it is written once, at the bottom, and lifted whole into the next project. Collapsing them into a
single stretch of camera prose is how a light state ends up being re-decided at every cut.

Fill rules and worked lines for all three: [blocks.md](blocks.md) §13, §14, §20. This file is the
vocabulary underneath them.

---

# 1 · CAMERA — the move

## The one-move rule

**One primary camera action per BEAT. No exceptions without a reference video.**

Stacking a pan with a tilt with a dolly with an orbit produces jitter on every Seedance version —
the model tries to satisfy all of them and satisfies none. This is the most consistently reported
camera failure across all four generations, and it is law 2 in `SKILL.md` for that reason.

Exception: if a reference video *demonstrates* the compound move, bind it
(`@Video1 → camera behaviour ONLY: …`) and the model can follow it, because it is copying a
trajectory rather than composing one. Role-line shape: [binding.md](binding.md).

Want a second move? That is a second BEAT and a cut.

---

## Moves the model recognises

**Core eight** — these are the best-supported, use them by default:

| Move | Write it as |
|---|---|
| Push in | `a slow push in on her face` |
| Pull out | `pulling back off him to reveal the room` |
| Pan | `a pan left across the ranks` |
| Track / follow | `tracking alongside him as he runs` |
| Orbit | `an arc around him, staying at his eye height` |
| Aerial / drone | `dropping from above the treeline` |
| Handheld | `hand-held, breathing with the operator` |
| Locked | `locked off, the frame does NOT travel` |

**Also recognised:** dolly in/out, crane up, whip pan, rack focus, dolly zoom, low-angle upshot,
overhead top-down, first-person POV, gimbal drift, one-shot continuous.

Anything outside these two lists is a gamble. A move the model does not recognise is not ignored —
it is approximated, usually by drifting.

---

## Writing CAMERA

Three parts, and only the first is mandatory: **the move · its quality · its ending.**

```
CAMERA: a slow push in, hand-felt rather than mechanical, settling when her eyes find the camera.
CAMERA: locked off. The frame does NOT travel — ONLY the operator's breathing shows.
CAMERA: tracking beside him at a run, the frame shaking with the ground under his feet.
```

The **ending** matters more than people expect. A move without a destination keeps going and lands
the final frame somewhere arbitrary — which then becomes the starting point for any extension, and
`video_extension` holds whatever the source ends on.

### A locked camera must be stated

Say nothing about the camera and the model invents drift. If the shot is static, write it, and set
`camera_fixed` / `fixed_lens` in the API call as well. Belt and braces, because the parameter alone
is sometimes ignored on complex prompts.

### Handheld is a quality, not a move

"Handheld" describes *how* the camera behaves, not where it goes. A handheld locked shot is legal
and common: the frame trembles in place but does not travel. Write both halves:

```
CAMERA: locked off but hand-held — organic jitter and small weight shifts, NEVER a pan, NEVER a push.
```

### Let the camera run the eyeline ladder

In scenes with real acting in them, the per-beat `CAMERA` lines are a second dramaturgy running
alongside `GAZE AND EYELINES`: locked → creep → handheld → locked. The camera getting closer and
less stable as the scene escalates reads with the sound off, and it costs one clause per beat.

---

# 2 · LENS — the frame

`LENS` is per-beat framing and nothing else. Three things, and only three: **shot size · focal
family · focus behaviour.**

```
LENS: medium close on MARCUS from the passenger side, 50mm, the near eye the sharpest thing in
frame, RAY soft and unreadable behind him.
```

## The capture format lives in STYLE, and is written once

The medium, the grain, the halation, the grade and the palette are `STYLE`, at the bottom of the
prompt, written once for the whole sequence. **Do not restate them in a beat.** "shot on 35mm
anamorphic, real grain" carried in five `LENS` lines is the same fact bought five times, and it
gives the model five chances to render it differently — which is precisely how a grade stops
matching across cuts.

What `LENS` may take from the optics department is the focal family and what it does to depth. What
it may never take is the medium. If you find a capture format in a `LENS` line, it is misfiled;
hoist it.

## Shot sizes the model reads

extreme close-up · facial close-up · medium close · medium · full body · wide / establishing.

Name exactly one per beat. Two sizes in one `LENS` line is a request for a zoom you did not write in
`CAMERA`.

## Lens families

The model responds to lens *family* and its consequences, not to a focal number alone. Give it both.

| Family | Say this | Renders as |
|---|---|---|
| Long / telephoto | `a long lens, narrow field, background compressed and thrown soft, one face sharp at a time` | Stacked depth, isolated subject |
| Wide | `a wide lens close in, edges stretching, deep focus into the room` | Immersion, geography |
| Anamorphic | `anamorphic character — oval bokeh and horizontal stretch, clean glass with no streaks` | Scope look — **image stage only**, see below |
| Large format | `large-format capture, creamy falloff, shallow at any distance` | Portrait separation |
| Spherical prime | `spherical prime, natural rendering, no distortion` | Neutral |

Focus behaviour is the third part and the one most often dropped: say what is sharp, and what is
allowed to go soft behind it. "the near eye the sharpest thing in frame" is a rack the model can
hold; "shallow depth of field" is a preference it can average away.

## Say what the frame must not open to

```
LENS: stays medium-close and NEVER opens to a wide.
```

A move that widens on its own is the commonest `LENS` failure there is, and it is a two-word fix.
The ending clause in `CAMERA` governs where the camera stops travelling; this clause governs how
much world it is allowed to show on the way. Both, in a push-in, or the push arrives somewhere you
did not ask for at a size you did not ask for.

## How CAMERA and LENS divide the work

**`CAMERA` is the move. `LENS` is the frame it moves within.** When a fact could plausibly sit in
either, this table settles it:

| The question | The block |
|---|---|
| Where does the camera go, and how does it behave getting there | `CAMERA` |
| Where does the move stop | `CAMERA` |
| Handheld, gimbal, crane, locked | `CAMERA` |
| How big is the subject in the frame | `LENS` |
| From which side, at what height, on what focal family | `LENS` |
| What is sharp and what falls soft | `LENS` |
| What the frame must NOT open to | `LENS` |
| Grain, grade, halation, palette, capture medium | `STYLE`, once, at the bottom |

A `CAMERA` line that names a shot size and a `LENS` line that names a move are the two halves of the
same mistake, and the linter will not catch either — the model just picks one and drops the other.

## Scale drift across cuts

Leave `LENS` out and the model chooses the size itself, beat by beat. It chooses badly in two
directions and both are recognisable:

- **Everything settles to the same mid-shot.** Six beats of coverage come back as six versions of
  one frame, and there is nothing to cut. This is the more common failure and the more expensive
  one, because the prompt is not wrong, it is just flat.
- **The subject jumps size between cuts.** A face fills the frame in beat two and is a full body in
  beat three with no move that got it there, so the sequence reads as three unrelated clips.

A `LENS` line per beat fixes both, because it is the only place in the rig where the sizes of every
beat are written near enough to each other to be read as a run. Write the run before you write the
beats — wide → medium → medium close → facial close-up is a ladder, and a ladder is what makes the
cuts feel motivated rather than arbitrary.

## Anamorphic belongs at the image stage

**Say what you do not want from anamorphic** — but say it in the *image* prompt. Ask for anamorphic
and you usually get blue streak flares thrown in, so name them as exclusions:
`oval bokeh and horizontal stretch, NOT flares, NOT streaks`. That is one of the few places a
negation earns its words, because the artefact is strongly associated with the term and image
prompts parse the refusal.

A video prompt does not. Seedance 2.5 normalises lens character back toward round, and in a video
body the negation tends to summon the noun it names. So bake the anamorphic into the plate at the
image stage, and write only this in `STYLE`:

```
STYLE: … clean glass, contained soft glows, optics inherited from the plate.
```

The measured 2.0-vs-2.5 numbers, the block to paste at the end of a location or product image
prompt, and the one loophole that does hold from video text — oval bokeh as a describable image
property — are in [finish.md](finish.md) §3.

## Optical texture that reads

Worth including, in roughly this order of impact: shallow focus falloff · real grain · halation on
highlights · 180° shutter motion blur · gentle vignette · edge chromatic aberration · lens
breathing.

Two or three of these is a look. All seven is a list, and the model averages lists.

This list lives here because it is a camera-department decision, and it is written into `STYLE`,
once, because it is true of every beat.

---

# 3 · LIGHTING — the sources

`LIGHTING` is a `PROMPT SEGMENTS` block: written once, at the bottom, true from the first frame to
the last, and reusable on the next project. It sits in this file because lighting is a camera
decision, not because it is ever written in a beat.

**One motivated source beats ten adjectives.** ByteDance's own guidance says as much, and it holds
in practice.

| Weak | Strong |
|---|---|
| dim moody atmospheric lighting | the only light is a window behind her, so her face is edge-lit and the room falls away |
| dramatic cinematic lighting | a single hard source from screen-left; the other half of his face is black |
| warm cozy lighting | late sun through a west window, low enough to throw long shadows across the floor |

State three things: **where it comes from · what motivates it · what it does to the subject's face.**
Everything else is decoration.

```
LIGHTING: the ONLY sources are sodium street poles passing outside on the driver's side, and the
instrument cluster below the windscreen. The poles rake across both faces in slow bands and leave
the cabin black between them. The cluster lights MARCUS from underneath, cold, and NEVER reaches
RAY at all.
```

Where a source physically sits is geography and belongs in `LOCATION MAP`. What it does when it gets
there belongs here. Written in both places, the two descriptions disagree eventually.

## Colour arrives from the source, not from a grade

Write **`sodium street pole`** and the orange comes out correct — right hue, right falloff, right
shadow, and it stops at the edge of what the pole can reach. Write **`orange grade`** and you get a
filter laid over a neutrally lit scene, with the orange in the shadows where no light is.

Every colour in the frame should be traceable to a named object that emits it: a sodium pole, an
instrument cluster, a phone screen, a fluorescent tube two rooms away, a fire out of frame. The
numeric palette split belongs in `STYLE`; the reason each of those colours is in the frame at all
belongs here.

## LIGHTING must motivate the catchlight

`PERFORMANCE` buys its aliveness in the eyes, and eyes read because something is reflected in them.
If a beat's `plays` line says "the near eye catches the cluster and holds it", then `LIGHTING` has
to have put a cluster below the windscreen on that side. Asked for and never lit, the model does one
of two things, and both are worse than the alternative: it invents a source that then contradicts
the rest of the scene, or it renders the flat dead eye the beat was written to avoid.

Read the two blocks against each other before you ship. It is the cheapest pass in the rig —
`PERFORMANCE` names the light in the eye, `LIGHTING` names the thing making it.

## One light state per prompt

Day and dusk in the same scene is two prompts. The model picks one and ignores the other, or blends
them into something that is neither.

To change light state while keeping the architecture identical, generate the first state, then feed
that render back in as a plate for the second:

```
@Image1 → the corridor: architecture, materials and geometry. NOT the light state, NOT the time of day.
```

The `NOT` clause is doing all the work in that line — without it the plate's own light comes with it
and you have generated the first state twice. [binding.md](binding.md).
