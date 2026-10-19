# Worked examples

Six complete prompts on the rig, spanning the cases that come up most: a two-beat dialogue cut, a
rigged chase, a crowd charge, a dual-reference character shot, a full thirty-second six-beat
sequence, and one compression pass shown end to end.

Names are generic on purpose. Substitute tokens. Every prompt here lints clean.

---

## 1 — Dialogue with one cut · CINEMATIC · 2.5 · 6 s

Two beats in one clip: a silent wide that sets the geography, hard cut to the close where the line
lands. The wide is doing spatial work only, so it gets one second. Six seconds buys about 14 words
of dialogue; the line below is 9.

```
SCENE CONTEXT: a shared common room gone comfortably to seed. Four people spread through it at
mixed distances, late in an argument nobody is treating as an argument. One of them is about to
take the floor.
FORMAT MODE: seedance 2.5 · 6s · 720p · 16:9 · audio on · 24fps · 2 beats, 1 hard cut
ACTIVE REFERENCES:
@Image1 → the room: the couch under the window, the two armchairs, the low table, the clutter. NOT any person in it.
@Image2 → the speaker: face, hair, the rimless glasses, the raglan tee. NOT the framing, NOT the background.
CAST: the speaker, thirties, rimless glasses, a raglan tee. Three others, present but not acting.
STAGING: everyone stays in the SAME seat across both beats. Nobody stands.
GAZE AND EYELINES: in beat one nobody looks at anybody. In beat two the speaker's eyes go
screen-left and down first, then move between the three off-screen listeners. NOBODY looks at
camera.
RULES: the SAME four people in the SAME clothes in EVERY frame. One light state throughout.

BEAT 1 — the room, one second
OPEN: four of them spread through the room at mixed distances, none of them in a line — one low on
the couch, one either side, one nearest the lens turned away from it. Nobody is talking.
CAMERA: locked off. The frame does NOT travel.
LENS: wide, the whole room in one, deep focus.
ACTION: nobody speaks → the room just sits there for a beat.
SFX: room tone ONLY.
EDIT: hard cut.

BEAT 2 — the close, held to the end
OPEN: the speaker fills the frame, turned screen-left toward the others, who are off-screen.
Already mid-thought.
CAMERA: locked off, the SAME as before.
LENS: tight close-up, the near eye sharpest.
ACTION: he lets the question hang a beat, taking the floor → then he answers, working the line at
them → on the last two words he stops selling and just holds their eyes.
PERFORMANCE: wants — to make the other three drop their answers and take his
             blocked by — they already like their own
             plays — eyes moving between them, landing each beat AT them, checking whether it
             lands before pressing on
             turns on — the last two words, where the pitch stops and the daring starts
DIALOGUE: the speaker, bright and fast, pitching something he already knows will win:
{No brainer. Deep future — space future.}
EDIT: hold.

LIGHTING: the ONLY source is late daylight through the window behind the couch. It lands warm and
low across the room and the corners stay dark.
AUDIO: <a quiet warm room> <fabric and frame creaking under people who are sitting badly>
SCORE: none.
STYLE: soft photoreal capture, natural grain, gentle contrast. Palette 60 warm brown and beige, 30
shadow, 10 cold window light.
VOICE: American English, bright and fast with a nasal edge, set high, no weight behind it.
TYPOGRAPHY: none.
POSITIVE LOCKS: exactly four people are present in both beats. The speaker is the ONLY one who
speaks. Both beats are locked off. There is EXACTLY one cut.
```

**Why it works:** the wide costs almost nothing and buys the geography the close-up cannot show. The
line fits the clip. One speaker, one cut, one locked camera — every constraint the model is good at.
Note that `LIGHTING`, `STYLE` and `AUDIO` are written once at the bottom and would be identical in
the next twelve shots of this scene.

---

## 2 — Rigged chase, continuous take · ACTION · 2.0 · 15 s

Camera bolted to a moving object. The subject is sharp, the world is blur, and the whole shot is one
closing distance. No cuts — the whip *is* the transition.

```
SCENE CONTEXT: a vast pale hall aboard a ship, mid-battle. A projectile is in flight down the
length of it, and one man at the rear of a running group is about to be the only one who turns
around.
FORMAT MODE: seedance 2.0 · 15s · 1080p · 21:9 · audio on · 24fps · 1 beat, no cuts
ACTIVE REFERENCES:
@Image1 → the projectile: its full silhouette — chrome head, ribbed body, swept tail fins. NOT its background.
@Image2 → the hall: the pale ribbed architecture, the tiered central platform, the corridor mouth in the far wall. NOT its lighting state.
@Image3 → the runner at the rear: build, coat, the pompadour. NOT his pose.
@Image4 → the guards: uniform and rifle ONLY, as a repeating type. NOT one fixed face, NOT one fixed body.
LOCATION MAP: the corridor mouth is in the far wall, dead centre, and the raised platform sits
between it and camera. The runner is at the rear of a group of three, forty feet short of the
corridor and losing ground. Guards are scattered across the floor at every depth.
CAST: the runner, heavy through the shoulders, long coat, a high pompadour. The guards are a type,
varied and NEVER repeated, not a cast.
RULES: nobody is struck on camera. Guards stay varied. The camera NEVER leaves the rig.

BEAT 1 — the flight
OPEN: rigged behind the projectile, pulled wide enough that its whole shape stays readable —
filling the lower third and sharp while everything else smears. Already at speed, smoke tearing
away beneath.
CAMERA: the rig holds behind the object throughout — the world does the moving. The frame turns
ONLY when the object turns.
LENS: wide, the projectile's full silhouette in frame at all times, everything past it in motion
blur.
ACTION: guards streak past underneath as blurred shapes, breaking in all directions → the
straggler fills more of the frame with every second → he looks back, sets his feet and takes it
one-handed → the load drives him backward, heels tearing two furrows, the arm juddering as it
holds → he turns on the spot like a hammer-thrower and sends it back → the frame snaps through a
half-turn and the hall is pouring past the other way → a figure on the raised platform registers
it and runs → the projectile leans into each change of direction, that face turned back over the
shoulder filling more of the frame → black on the last frame before it arrives.
SFX: <a whistle rising to a shriek> <the meaty clamp of a hand on metal> <heels ploughing a hard
floor> <a roar on the pivot> <torn air on the half-turn> <rifles clattering as bodies flatten> →
silence.
EDIT: hold. Black.

PHYSICS: real ballistic weight. The projectile has mass and the catch is a genuine momentum
transfer, not a stop — the man absorbs it through his heels and his shoulder and it costs him.
Sparks where things collide, nothing wet. Bodies that go down go down under and with the force.
LIGHTING: bright even artificial ship light from overhead panels, flat and white. No daylight, no
shadow pools, no practicals.
AUDIO: <a battle streaking past underneath, muffled by speed> <the rig rattling with the flight>
SCORE: none.
STYLE: anamorphic character inherited from the plate — clean glass, contained soft glows, oval
bokeh. Palette 70 white and pale grey, 20 chrome, 10 hot pink from the uniforms.
TYPOGRAPHY: none.
POSITIVE LOCKS: the projectile's full shape stays readable in EVERY frame. One continuous take
from first frame to last. The frame goes black before contact. Exactly one man turns around.
```

**Why it works:** one rig, one continuous move, one closing distance. The `ACTION` chain is long but
each clause is a single action, and the whole thing resolves into black before the model has to
render an impact it would fail at anyway. `PHYSICS` is doing the work that makes the catch read as a
catch rather than a stop.

---

## 3 — Crowd charge, single beat · ACTION · 2.0 · 8 s

Crowd as condition, not cast. One hero, one impact, one consequence.

```
SCENE CONTEXT: a battlefield on a dry golden plain, two lines about to meet. One heavy soldier is
running ahead of his own side and enjoying it more than anyone else is.
FORMAT MODE: seedance 2.0 · 8s · 1080p · 2.39:1 · audio on · 24fps · 1 beat, no cuts
ACTIVE REFERENCES:
@Image1 → the charging soldier: face, the too-small bronze armour, the raised sword. NOT the background of the reference.
@Image2 → the allied soldiers: armour and shields ONLY, as a varied type. NOT one repeated face.
@Image3 → the enemy column: shields and spears in a marching rank ONLY. NOT one repeated face.
LOCATION MAP: he charges screen-left to screen-right. Allies close around him in the near
foreground; the enemy column stretches from mid-frame deep into the distance on the right, thinning
toward hazy hills. One large gold banner in the near foreground.
CAST: the charging soldier, heavy, bronze armour a size too small. Everyone else is a condition of
the field — varied, NEVER repeated, and NEVER an individual.
RULES: nobody bleeds. Real-time, and NEVER slow motion. One impact only.

BEAT 1 — the charge
OPEN: on him mid-run, screen-left, sword already high, charging left to right. Allied soldiers
close around him in the near foreground. Nobody in frame is still.
CAMERA: tracking alongside him at a run, hand-held, shaking with the ground under his feet.
LENS: full body, long lens, he stays sharp and everything else melts to bokeh.
ACTION: he runs hard across the plain, sword up, soldiers charging with him → he yells as they
close on the ranks → he leaves the ground and lands bodily into the column → they go down together
in a burst of dust, the line buckling on both sides of the hit.
PERFORMANCE: wants — to hit the line first, ahead of everyone
             blocked by — his own weight, which he is ignoring
             plays — open-mouthed delight the whole way, no fear anywhere in it, eyes fixed on the
             point of contact
             turns on — the moment his feet leave the ground and he commits to it
DIALOGUE: English, one shouted word as he leaves the ground, lips synced to it ONLY:
{Cannonball!}
SFX: <pounding feet> <metal and shields> <the thud of bodies arriving on hard ground>
EDIT: hold.

PHYSICS: real mass. He is heavy, so the run is laboured and gleeful at once, belly and armour
bouncing. The charge arrives with weight; bodies that go down go down under and with him. Dust
bursts and drifts. Nothing floats and nothing snaps back.
LIGHTING: bright day, the sun low enough to throw long shadows across bare ground. Dust hanging in
the air catches it and softens the distance.
AUDIO: <a wall of battlefield sound — feet, metal, shields, shouting, wind>
SCORE: none.
STYLE: anamorphic character inherited from the plate — clean glass, oval bokeh, contained glows.
Palette 60 dry gold ground, 30 bronze and shadow, 10 hazy blue distance.
VOICE: English, a big open shout from a big open man, no strain in it.
TYPOGRAPHY: none.
POSITIVE LOCKS: exactly ONE impact, and it lands. He stays sharp and everything else goes soft.
Real-time throughout. The ranks are varied in every frame.
```

---

## 4 — Dual-reference character shot · CINEMATIC · 2.5 · 8 s

Two references on one character: body and rig from a wide, face at close-up fidelity from a head
shot. The `NOT` clauses are doing all the work.

```
SCENE CONTEXT: a pilot hangs inverted inside a sealed metal cockpit she cannot straighten in, the
machine swaying under her. She has been trying to get out for some time and is about to run out of
things to try.
FORMAT MODE: seedance 2.5 · 8s · 720p · 21:9 · audio on · 24fps · 1 beat, no cuts
ACTIVE REFERENCES:
@Image1 → the pilot, body and rig: her inverted pose, the five-point harness, the exact cabin around her. NOT the face resolution.
@Image2 → the pilot, head: pore-level skin, the rimless glasses, the lip ring, brown eyes. NOT the pose, NOT the framing.
@Video1 → camera behaviour ONLY: the drift and re-settle of a hand-carried gimbal. NOT its subject, NOT its grade.
LOCATION MAP: two joystick grips at her hands, scuffed panels pressing close on every side, a
sealed metal ceiling below her inverted head. Nothing outside the shell is visible at any point.
CAST: the pilot, alone. NEVER a second person.
WARDROBE: maroon jacket, olive bodysuit, black boots, rimless glasses, a lower-lip ring. EXACT
throughout.
RULES: she is inverted in EVERY frame. The camera stays inside the cabin.

BEAT 1 — the last thing she tries
OPEN: dead-side profile on her, camera wedged in at her inverted head height, medium-close — the
near eye is the sharpest thing in frame. She reads upside-down instantly, already breathing hard.
CAMERA: one slow arc from this profile around to the other, hand-felt, drifting off-axis and
re-settling when her eyes stop moving.
LENS: medium-close throughout, and it NEVER opens to a wide.
ACTION: she scans the cabin, eyes darting, looking for a way out → one hand goes up and tests the
shoulder strap twice → the hand drops to a joystick and pulls once, hard → it does NOT move, a dead
clunk → she gives up on it and keeps thinking, jaw tight.
PERFORMANCE: wants — out of the harness before the cabin swings again
             blocked by — her own weight holding everything shut
             plays — testing, checking, refusing to panic out loud; it shows in the breath and the
             eyes, with natural blink cadence throughout
             turns on — the joystick failing, where she stops solving and starts listening
SFX: <webbing creaking as she tests the strap> <a dead clunk as the joystick refuses> <a strained
grunt on the pull> <one sharp breath after it>
EDIT: hold.

PHYSICS: she hangs inverted, curled like an embryo, her whole weight on the straps — webbing
compressing her shoulders and creaking under load. Hair falls straight down, lags her head turns,
sticks where her face is damp. The cabin sways and she swings after it. Nothing floats.
LIGHTING: the ONLY light is cold overcast daylight through the shell's seams. It lands unevenly —
a slice of her face lit, the rest near-black — and it is what puts the catchlight in the near eye.
AUDIO: <a steel cable groaning> <the shell creaking as it sways> <her breathing, heavy and loud in
a small space>
SCORE: none.
STYLE: large-format film capture, 40mm spherical prime, real grain and halation, imperfect focus,
matte fingerprinted surfaces. Palette 70 dark steel and near-black, 20 maroon from jacket and
hydraulic line, 10 cold grey-blue from the seams.
TYPOGRAPHY: none.
POSITIVE LOCKS: profile the whole way — NEVER frontal, NEVER three-quarter. The camera stays
inside the cabin from first frame to last. She is inverted in EVERY frame. Exactly ONE pull on the
joystick, and it fails. One continuous take.
```

**Note the split:** identity facts live in `ACTIVE REFERENCES` with exclusions. Wardrobe lives in
`WARDROBE` because it holds across the scene. Physical behaviour lives in `PHYSICS` because it will
still be true on the next film with a harness in it. Only what changes lives in the beat. Add a
second beat and it costs 150 words, not another 900.

---

## 5 — A thirty-second, six-beat sequence · CINEMATIC · 2.5 · 30 s

This is what 2.5 actually unlocked, and it is a different unit of work: you are writing a scene, not
a shot. Six beats at five seconds each is a real edit rhythm. Notice what the tiers cost — the
`CONTEXT` and `PROMPT SEGMENTS` tiers are written once and amortised across all six beats, so the
sixth beat costs about 120 words instead of another whole prompt.

`text2video` — no plates, so `ACTIVE REFERENCES` is absent and identity has to survive on `CAST`
alone. Expect flatter faces than a reference-bound render. That is the documented trade, not a
prompting mistake.

```
SCENE CONTEXT: a night bus, nearly empty, running a long straight road out of a city. A woman in
her fifties sits three rows back with a cardboard box on her lap. A younger man boards at a stop in
the middle of nowhere and sits opposite her, and neither of them says anything for a long time.
FORMAT MODE: seedance 2.5 · 30s · 720p · 2.39:1 · audio on · 24fps · 6 beats, 5 hard cuts
LOCATION MAP: the woman screen-left, three rows back, window side. The man screen-right across the
aisle, one row forward of her, from beat three onward. The driver is a silhouette at the far end of
the aisle and NEVER turns around. The road runs away behind through the rear window.
CAST: the woman, fifties, grey hair pinned badly, a deep vertical crease between her brows. The
man, late twenties, a healing split through the right eyebrow, one earbud in. Two passengers and
the driver's silhouette, and NEVER anyone else.
STAGING: both stay seated from beat three to the end. Neither stands. The woman keeps both hands on
the box in EVERY beat.
WARDROBE: the woman in a buttoned brown coat she has not taken off. The man in a thin black jacket
over a work shirt. EXACT throughout.
GAZE AND EYELINES: a ladder. Beats one and two, the woman looks only out of the window. Beat three,
the man looks at the box, NOT at her. Beat four, she catches him at it in the reflection. Beat five,
she looks straight at him and he does NOT look back. Beat six, he looks at her and by then she is
back at the window. NOBODY looks at camera.
RULES: night-for-night throughout, NEVER dusk. The bus never stops after beat three. The SAME four
people in EVERY frame.

BEAT 1 — the window
OPEN: the woman screen-left in profile, lit only by what passes outside, the box already square on
her knees and her hands already on it. The bus is already moving.
CAMERA: locked off. The frame does NOT travel.
LENS: medium, from across the aisle, the empty seats behind her soft.
ACTION: light from outside crosses her face and goes → she does not follow it → her thumb moves
once on the corner of the box and stops.
PERFORMANCE: wants — to get to the end of the ride without thinking about it
             blocked by — the box, which she cannot put down
             plays — eyes fixed out of the window, breath shallow and regular, one thumb doing all
             the moving
             turns on — nothing yet; this beat holds
EDIT: hard cut.

BEAT 2 — the aisle
OPEN: down the length of the aisle from behind, the driver a silhouette at the far end, the woman
small and screen-left in the middle distance. Already rolling.
CAMERA: locked off, the SAME as before.
LENS: wide, deep focus, the whole aisle readable.
ACTION: the bus slows → the doors fold open on nothing but dark road → a man climbs in and stands
a moment too long deciding where to sit.
SFX: <air brakes letting go> <doors folding> <one pair of boots on a rubber floor>
EDIT: hard cut.

BEAT 3 — he sits
OPEN: the man screen-right, dropping into the seat across the aisle and one row forward, earbud
already in, already looking at the box and NOT at her.
CAMERA: a slow creep in, hand-felt, settling when he stops moving.
LENS: medium two-shot, both of them in frame, her soft.
ACTION: he settles → his eyes go to the box and stay there a second too long → he looks away and
out of his own window.
PERFORMANCE: wants — to work out what is in the box without asking
             blocked by — the fact that asking is the only way to find out
             plays — a flick of the eyes back to it, then away, then back; the jaw completely still
             turns on — the second look, where he stops pretending he did not see it
EDIT: hard cut.

BEAT 4 — the reflection
OPEN: tight on the woman's window, her face in it and his shoulder behind hers in the same glass,
the road running through both. Already moving.
CAMERA: locked off but hand-held — organic jitter in place, NEVER a pan, NEVER a push.
LENS: extreme close, the reflection sharper than the glass.
ACTION: she finds him in the reflection → her thumb stops → she does not turn her head.
PERFORMANCE: wants — to know whether he is going to say something
             blocked by — that turning around would be saying something herself
             plays — the eyes doing all of it, the rest of the face level and closed
             turns on — the moment she decides he is not going to
EDIT: hard cut.

BEAT 5 — she looks
OPEN: on the woman, turned screen-right toward him for the first time, box still square on her
knees. Already turned when the frame opens.
CAMERA: locked off.
LENS: medium close, him soft and out of focus over her shoulder.
ACTION: she looks straight at him and holds it → he does NOT look back → she stays there a beat
longer than is comfortable → then she turns to the window again.
PERFORMANCE: wants — to be asked
             blocked by — that he has decided to be polite
             plays — the look held flat and open, then the small mechanical turn away; breath out
             through the nose on the turn
             turns on — the half-second where she gives up on it
DIALOGUE: none.
EDIT: hard cut.

BEAT 6 — the earbud
OPEN: on the man screen-right, one hand already moving toward his ear. Behind him the road runs
away through the rear window.
CAMERA: a slow pull back off him, revealing the empty seats between them, settling wide.
LENS: opens from medium close to a two-shot with the aisle between them.
ACTION: he takes the earbud out → he turns and looks at her → she is looking at the window → he
does not say it → he faces forward and the bus keeps going.
PERFORMANCE: wants — to ask her now
             blocked by — that the moment for it was thirty seconds ago
             plays — the earbud held in the hand and not put back, eyes on her then forward, the
             mouth opening about a centimetre and closing
             turns on — the moment he sees she has stopped waiting
SFX: <a thin tinny leak of music as the earbud comes out> <tyres on a joint in the road>
EDIT: hold the last frame motionless for half a second.

PHYSICS: real mass. The bus is heavy and its movements are slow and late — it leans into a curve
and takes a beat to come back, and everyone in it moves with the bus and arrives after it. The box
stays exactly where it is on her knees. Nothing floats.
LIGHTING: the ONLY sources are the road lights passing outside and one strip of dim service light
running the length of the ceiling. The road lights cross both faces in bands and leave the bus
black between them. The ceiling strip is too weak to model a face and only separates shoulders from
the dark.
AUDIO: <a diesel engine held at a constant note> <tyre roar coming up through the floor> <one loose
panel rattling somewhere behind> <no other passengers, no conversation>
SCORE: none. NO music of any kind, at any point.
STYLE: 35mm film capture, 40mm spherical prime, real grain, halation on the passing lights,
imperfect focus. Clean glass, contained soft glows, optics inherited from the plate. Palette 65
near-black interior, 25 cold sodium from outside, 10 dull green from the ceiling strip.
TYPOGRAPHY: none.
POSITIVE LOCKS: exactly four people are on the bus for the whole clip — the woman, the man, one
other passenger and the driver. Both principals stay seated from beat three to the end. The box
stays on her knees in EVERY frame. Every light source renders as a soft contained glow within its
own source. The frame contains the bus interior, the windows and the road only.
```

**What to notice.** Six beats, five cuts — exactly at 2.5's ceiling, and the linter will say so. The
`GAZE AND EYELINES` ladder is the whole dramaturgy and it reads with the sound off; the camera runs
the same ladder underneath it (locked → locked → creep → hand-held → locked → pull back). There is
no dialogue at all, and the scene still has a turn in it. And the entire `PROMPT SEGMENTS` tier
would be pasted unchanged into the next clip of this film.

---

## 6 — A compression pass, shown

Source: a circulating single-shot prompt for example 4. **1,412 words.** Rewritten above:
**461 words** across all three tiers. 3.1:1 on this shot — and a second beat in the same cockpit now
costs about 150 words instead of another 1,412, which is 9.4:1.

Where the 951 words went:

| Cut | Words recovered |
|---|---|
| "camera inside the cabin, never outside" stated in 5 places → once in `CAMERA`, once as an assertion in `POSITIVE LOCKS` | ~110 |
| Anti-CG rant across 3 paragraphs → `STYLE: large-format film capture, real grain and halation, imperfect focus` | ~175 |
| Sealed ceiling as `NO glass, NO windows, NO canopy` repeated in 4 blocks → `a sealed metal ceiling below her inverted head` in `LOCATION MAP` | ~85 |
| Meta-commentary — purpose, what-we-read, OVER-CINEMATIC, claustrophobic awe-inducing dread | ~140 |
| Full re-description of both reference images → two role lines with `NOT` clauses in `ACTIVE REFERENCES` | ~195 |
| Camera described across 4 blocks with 5 stacked moves → one `CAMERA` line, one move, plus one `LENS` line | ~150 |
| A locks block restating the entire prompt → 5 assertions in `POSITIVE LOCKS` | ~96 |

The rewrite is not just shorter. The one-move `CAMERA` fixes the jitter the five stacked moves were
causing, and the two role lines fix the close-up reference overriding the blocking. **The compression
and the quality fix are the same edit** — which is the whole argument for the rig.

And the second saving is larger than the first. Everything in the `PROMPT SEGMENTS` tier — 148 words
of `PHYSICS`, `LIGHTING`, `AUDIO`, `STYLE` — is now a file you paste. It cost you once and it will
be correct on every shot of this film and on the next film with a harness in it.

---

## 7 — Video-to-video from a 3D blockout · CINEMATIC · 2.5 · 8 s

The blockout owns the camera and the spacing; the prompt owns the performance. The verified prompt,
the failure it replaced, and the checklist live in [blockout.md](blockout.md) §8 — it is kept there
rather than duplicated here so it cannot drift between two copies.

---

## Linting them

```bash
python3 scripts/seedance.py lint ex4.txt --model 2.5 --duration 8
python3 scripts/seedance.py lint ex5.txt --model 2.5 --duration 30
```

Example 5 will report `cuts.budget  6 shots, 5 cut(s), within budget` — at the ceiling, not over it.
Add a seventh beat and it becomes an ERROR, which is the correct answer: that is a second clip.
