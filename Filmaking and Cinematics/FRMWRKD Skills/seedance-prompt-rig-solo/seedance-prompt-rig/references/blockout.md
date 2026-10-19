# Video-to-video from a blockout

A blockout is a 3D previz pass: grey blocks standing where the actors will stand, a camera doing
what the camera will do, a room laid out at the right distances. It is the cheapest way to lock
staging, camera and timing before spending a credit on a video model. Attached to Seedance as a
`@VideoN` reference, it works — the model follows the camera and the spacing faithfully.

It also fails in one specific, expensive way, and this file exists because of it. Everything below
was proven on paid renders. Read it before binding any previz, animatic, mocap stand-in, or any
other video whose *motion* is not the motion you want in the finished shot.

---

## 0 — The division of labour

| The blockout owns | The prompt owns |
|---|---|
| where the camera sits and how it moves | every gesture, every step, every glance |
| where the bodies stand relative to camera and each other | posture, weight, how a body arrives and settles |
| how the space is laid out and how far things are | what the room actually is — named fixtures, materials, light |
| the timing of the cut points (labelled `BEAT`s) | the performance inside each beat |

**The blockout's job is staging, camera and timing. The acting belongs to the video model.** Hours
spent animating the blocks' hip pivots and arm swings are wasted: the figures still read as boxes,
and the only thing that survives into the render is the trajectory. Leave the blocks stiff. Spend the
time on the words.

---

## 1 — The failure that costs the most

Four clips came back with the actors performing the blocks' motion: flat panel arms tilting on a
hinge, a glide with no footfall, a torso that never bent. The choreography in the prompt did not
appear at all.

The cause was not the reference. The cause was the prompt's shape:

- **Over-negation.** The role line shouted `THERE IS NO DANCING IN THIS VIDEO — IGNORE THE MOVEMENT
  COMPLETELY`, in capitals, three times per prompt.
- **Under-description.** The dance itself got two thin lines.

Heavy negation focuses the model on exactly what is being negated. A model handed nothing positive
to perform falls back on the only motion it can see, and the only motion it could see was the blocks.
Both halves were the same bug: forty competing instructions, none carrying weight.

**The rule: one compact role line, then pure positive description.**

---

## 2 — The role line

One line. State what the video governs, then what it does not, and stop talking about the video.

```
@Video1 → the blockout, and it governs ONLY the camera and the spacing: where the camera sits and how it moves, how the room lays out into depth, roughly where she stands relative to camera. NOT her movement, NOT her posture, NOT its grey untextured surfaces, NOT its flat unlit look.
```

That is the whole budget the video gets. The linter warns past sixty words on a video role line and
flags any shouting inside it. After the line, the word *blockout* should not appear again except in
`CAMERA` (*the blockout's move, nothing added*) and, if needed, once in `RULES`.

What not to write, ever:

| Written | Why it fails |
|---|---|
| `IGNORE THE MOVEMENT COMPLETELY` | names the movement, at full volume, and gives nothing to do instead |
| `THERE IS NO DANCING IN THIS VIDEO` | the model parses *dancing*, not *no* |
| a second paragraph explaining the blockout | every sentence about the video is a sentence not spent on the performance |
| `@Video1 → follow this closely` | binds everything, including the boxes |

---

## 3 — Spend everything on the positive

After the role line, the performance is described the way you would describe it to a dancer who
cannot see the reference. Concrete physical verbs, carried by the body:

> arms carried by her spine rather than waved · sinking into the floor and rising out of it ·
> turning under her own arm · reaching out and drawing it back to her chest · weight arriving before
> the limb that carries it · a shoulder settling · a hand that lifts and lowers

Not: *she dances expressively*. Not: *fluid contemporary movement*. Those are categories; the model
needs verbs. `ACTION` carries the sequence in order, `PHYSICS` carries how mass behaves, and
`PERFORMANCE` carries why — wants, blocked by, plays, turns on. [performance.md](performance.md).

Restraint outperforms emphasis here too. Stripping steam, dust beams and haze from a café prompt made
the room read *more* like the café, not less. Every atmospheric you add is a fact competing with the
ones that identify the place.

---

## 4 — The location: contents, not materials

The second failure on the same day. The location plate was bound, the materials were listed
faithfully — *aqua gloss tile, brass pendants, timber counter, concrete floor* — and every render
came back as a bare tiled tunnel.

**Materials do not identify a room. Its contents do.** That materials list is satisfied perfectly by
a subway corridor. The moment the prompt named the curved-glass pastry case, the wooden speaker
cabinets, the bentwood chairs and the rug, the café appeared on the first render.

So `SCENE CONTEXT` names the fixtures, positively, every time:

```
SCENE CONTEXT: a coffee shop at the quiet hour. A long reclaimed-timber counter down the right with a curved-glass pastry case, a chrome espresso machine and kraft cup stacks, vintage wooden speaker cabinets above it, a glassware shelf behind. Round tables and bentwood chairs down the left against a banquette, a rug on polished concrete, pale aqua gloss tile floor to ceiling, brass dome pendants on black cords, a steel shopfront at the far end with a low sunrise through it.
```

A shot that shows none of those is not in the café, however correct the tile is.

### When the blockout's geometry differs from the plate

Blockouts often stretch, bend or rake a space for the camera. The plate shows a room; the blockout
shows a corridor. Two ways to write this, one of which throws the room away:

| Wrong | Right |
|---|---|
| `NOT its ordinary room proportions` | *(never exclude the proportions — that excludes the room)* |
| `a coffee shop that has stretched into a long corridor` | `this same room lengthens: the counter runs on, the tables recede, the pendants multiply away into depth. It is this café getting longer, not another place.` |

The right-hand version carries the room's own furniture into the transformation. The left-hand
version tells the model to discard the room, and it does. **The transform phrasing belongs only in
the shot where the transform is the point.** Pasted into a close-up or a static two-shot it returns a
tunnel every time — check every prompt in the sequence for inherited phrasing that was correct in one
shot and wrong in this one.

---

## 5 — Cast: the turnaround, garment for garment

Never bind a cast plate as *identity ONLY*. The model reads that as *take the face, ignore the
clothes*, and the wardrobe drifts to whatever the blockout's grey suggests.

```
@Image2 → Yuna, for her face, hair, ear jewellery and her whole outfit. NOT the pose, NOT the framing, NOT the studio light, NOT the grey background.
```

Then `WARDROBE` restates the garments once, in the CONTEXT tier, closing with `EXACT throughout`.
The plate and the words arrive together saying the same thing — [binding.md](binding.md), the
finish-grade convention.

---

## 6 — Music, and what reacts to it

If the shot is cut to music, attach it and bind it to timing only:

```
@Audio1 → the music, for timing. NOT any voice, NOT speech, NOT singing.
```

Then state, once, that the movement and the practical lights both react to it. `LIGHTING` is the
place for the lights — *the pendants breathe with the music, swelling until both faces read, sinking
until they are nearly silhouettes* — and `ACTION` for the body. `SCORE: the attached track only.`

---

## 7 — Cuts

Seedance cuts only when it is told to, in the grammar it reads. Describing shot changes in prose
produces one continuous take with mush at the transitions — the earlier clips that *felt like a
single drifting shot* were exactly this.

```
BEAT 1 — <slug>
…
EDIT: hard cut.

BEAT 2 — <slug>
…
```

Labelled `BEAT` blocks, an `EDIT: hard cut.` between them, and the cut points landing where the
blockout cuts. Cut budget per model in [scenes.md](scenes.md). A one-take shot says so in
`FORMAT MODE`: *one continuous take, no cuts*.

---

## 8 — Verified prompt · CINEMATIC · 2.5 · 8 s · one take

This landed first time, linted clean, after the batch that copied the blocks. Two dancers coming to
rest after a duet, in the café, while the room lengthens behind them.

```
SCENE CONTEXT: a coffee shop at the quiet hour. A long reclaimed-timber counter down the right with a curved-glass pastry case, a chrome espresso machine and kraft cup stacks, vintage wooden speaker cabinets above it, a glassware shelf behind. Round tables and bentwood chairs down the left against a banquette, a persian rug on polished concrete, red terracotta tile at the counter base, pale aqua gloss tile floor to ceiling, brass dome pendants on black cords, a steel shopfront at the far end with a low sunrise through it. Across the shot this same room lengthens: the counter runs on, the tables recede, the pendants multiply away into depth. It is this cafe getting longer, not another place.

FORMAT MODE: seedance 2.5, 8s, 16:9, audio on, one continuous take, no cuts.

ACTIVE REFERENCES:
@Video1 the blockout, for the camera move and roughly where the two stand. NOT the dancing, NOT their posture, NOT its grey surfaces, NOT its unlit look.
@Audio1 the music, for timing. NOT any voice, NOT speech, NOT singing.
@Image1 the cafe, for the room and everything in it. NOT its camera angle.
@Image2 Yuna, for her face, hair, ear jewellery and her whole outfit. NOT the pose, NOT the framing, NOT the studio light, NOT the grey background.
@Image3 Kojo, for his face, locs, beard and his whole outfit. NOT the pose, NOT the framing, NOT the studio light, NOT the grey background.

CAST: Yuna, East Asian, late twenties, lean, black shaggy wolf cut with a blunt fringe and a bleached platinum panel at one temple, freckles, bare nose. Kojo, Black, mid-twenties, tall and lean-strong, shoulder-length locs, full beard, clear skin. ONLY these two, NOBODY else.

STAGING: they stand a few feet apart on the open concrete, both full-figure, both faces visible, turned toward each other. The gap stays about the SAME throughout.

WARDROBE: Yuna in an oversized cream hand-knit off one shoulder, fair isle bands in red, gold and blue, rust cargo trousers, black boots, silver hoops and a cuff in one ear. Kojo in an open forest-green track jacket, cream collar, twin cream sleeve stripes, black tee, gold rope chain, black cargos. EXACT throughout.

GAZE AND EYELINES: they hold each other's eyes almost the whole take. She looks away once and comes back. He does NOT look away. NOBODY looks at camera, and neither looks at the room.

EVENT AND SHARED DIRECTION: two people stay in front of each other longer than they have a reason to. Played by both: do not be the one who breaks it.

MICRO-BEHAVIOUR: natural blink, breath moving in both chests, eyes wet from the light rather than from crying.

RULES: the camera does what the blockout camera does and nothing more. They stay on the floor.

BEAT 1
OPEN: already standing, already looking at each other, already breathing hard from something that finished just before we arrived.
CAMERA: the blockout's move, nothing added.
ACTION: they are coming down off dancing and almost still. Small weight shifts foot to foot, a shoulder settling, a hand that lifts and lowers. Twice, one starts a movement toward the other and lets it die. Around them the room lengthens, counter and chairs drawing into depth, pendants multiplying into the distance.
PERFORMANCE: wants, to stay in front of the other one; blocked by, no reason left to stand there and nothing either will say; plays, holding the look past the point it is comfortable, breathing out slowly to steady it, starting to turn away and not going; turns on, neither of them leaves.

PHYSICS: real mass, gravity absolute. Weight arrives before the limb carrying it. Knit sleeves, locs and hair lag each shift then settle.

LIGHTING: the brass pendants are the only source and they breathe with the music, swelling warm until both faces read, sinking until they are nearly silhouettes with the eyes still catching, then swelling again. Continuous, never a strobe. Deep teal in the shadows, sunrise warm at the far end.

SCORE: the attached track only.

STYLE: photoreal large-format capture, 40mm spherical, real grain, halation on the tungsten. Palette 60 deep teal and near-black, 25 warm tungsten, 15 coral and cream.

POSITIVE LOCKS: the room is this tiled cafe with its timber counter, pastry case and bentwood chairs, and it lengthens without becoming anywhere else. They hold each other's eyes almost the whole take. The performance is small, quiet and physical. ONLY two people are present. One continuous take.
```

**Read the proportions.** The video reference gets one line. The room gets its fixtures. The cast
gets their garments. The performance gets `ACTION`, `PERFORMANCE`, `PHYSICS` and `LIGHTING`, which
between them are two-thirds of the prompt. The word *blockout* appears three times in total.

---

## 9 — The checklist, before spending

- [ ] The video role line is one line, under sixty words, and names what it governs before what it excludes
- [ ] The word *blockout* (or *previz*, *animatic*, *reference video*) does not appear in `ACTION` or `PERFORMANCE`
- [ ] Nothing in the prompt is in capitals except block keys and the closed vocabulary
- [ ] `SCENE CONTEXT` names at least five fixtures that identify this room and no other
- [ ] No `NOT … proportions`. Any transform is written as *this room, extending*, and only in the shot where it happens
- [ ] Every cast plate is bound face **and** whole outfit; `WARDROBE` restates the garments once
- [ ] Music attached and bound to timing; lights and body both stated to react to it
- [ ] Cuts are labelled `BEAT`s with `EDIT: hard cut.` — or `FORMAT MODE` says one take
- [ ] `python3 "$SKILL_DIR/scripts/seedance.py" lint` is clean

Then open the render before writing a word about it — [verify.md](verify.md).
