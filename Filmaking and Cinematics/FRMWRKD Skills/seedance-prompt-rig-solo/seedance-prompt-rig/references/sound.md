# Sound — AUDIO, SCORE, SFX, DIALOGUE and VOICE

**Seedance 1.0 produces silent video.** No audio flag, no lip-sync, nothing. If the user is on 1.0
and the beat has a line in it, say so before composing, not after the render. Everything below
applies to 1.5 pro, 2.0 and 2.5.

On those versions audio and picture are generated **jointly, in a shared latent**. It is not a dub
pass bolted on after the frames exist — the sound is being decided at the same moment as the image,
by the same words. That is why the bracket grammar works at all, and why prose descriptions of sound
get averaged into mush.

Sound is not one block. It is **five blocks across two tiers**, split by how long each part stays
true:

| Block | Tier | Carries | Rewritten |
|---|---|---|---|
| `AUDIO` | 03 · PROMPT SEGMENTS | the standing ambience, and what is banned from it | never |
| `SCORE` | 03 · PROMPT SEGMENTS | music — or plainly that there is none | never |
| `VOICE` | 03 · PROMPT SEGMENTS | each speaker's fixed identity | never — pasted verbatim |
| `SFX` | 02 · BEATS | this beat's own sound only | every beat |
| `DIALOGUE` | 02 · BEATS | the words spoken in this shot, and their delivery intention | every beat |

The split is the point. The bed, the score and the voices are constants; retype them per shot and
the model re-decides them per shot, and a voice that gets re-decided is a voice that changes between
cuts. Only the two beat-level blocks are written again.

Pair this file with [models.md](models.md) — whether audio exists at all is a model question, and it
is settled before you write a word of this.

---

## The bracket grammar

Seedance 1.5 and up read a delimiter grammar. Use it.

| Content | Wrap in | Lives in | Example |
|---|---|---|---|
| Music / score | `( )` | `SCORE` | `(low sustained strings, no percussion)` |
| Sound effects | `< >` | `AUDIO` / `SFX` | `<a metal latch clicks>` |
| Dialogue | `{ }` | `DIALOGUE` | `{I thought you weren't coming.}` |
| On-screen text | `【 】` | `TYPOGRAPHY` | Avoid entirely — see below |

**Brackets must balance.** An unclosed brace leaks the rest of the prompt into the dialogue track,
and the model will cheerfully speak your `EDIT` line aloud. The linter checks this before anything
else because it is the failure that wastes a whole render.

---

## AUDIO — the standing ambience

The room, running from the first frame to the last. Written once, in `PROMPT SEGMENTS`, and never
restated in a beat.

```
AUDIO: <a sealed cabin, road noise arriving muffled through glass> <steady tyre hum on cold
asphalt> <the engine held at a low constant note>. Room sound ONLY.
```

Rules:

- **Bracket grammar here too**, one event per `< >` pair. The bed is three or four continuous
  textures, not a list of incidents — incidents are `SFX`.
- **State silence explicitly.** "no music, room sound ONLY" is four words that stop the model
  inventing a soundbed under your scene.
- Name what the space does to sound, not just what is in it: *arriving muffled through glass* tells
  the model there is a boundary, and it renders the boundary.
- **Omit this block entirely on Seedance 1.0.** The render is silent and the words are wasted.

**Prevents:** the generic cinematic soundbed the model adds whenever audio is left unspecified.

---

## SCORE — music, or plainly that there is none

Separate from `AUDIO` for one reason: **most cinematic work wants no music at all**, and "none"
needs saying. Score belongs in post, where it can be cut to picture and removed when it is wrong. A
score baked into a render cannot be taken out.

```
SCORE: none. NO music of any kind at any point. Everything in this clip is engine, tyre hum and
room tone.
```

When the render genuinely needs music in it:

```
SCORE: (a single low pulse under everything, no melody, no percussion, no swell)
```

Rules:

- **Describe function, not genre.** `(a single low pulse under everything)` outperforms `(epic
  cinematic soundtrack)` every time — genre names pull in an entire arrangement, tempo and mix that
  nobody asked for.
- Say what the music does not do. In this one place a short negation earns its keep, because the
  model's default for music is *build*: `no melody, no percussion, no swell`.
- Leaving `SCORE` unstated is how you get library music you then have to fight in the edit.

**Prevents:** unrequested music, and a score that cannot be removed from the render.

---

## SFX — this beat's own sound

Only what this shot adds on top of the bed. Written per beat, and it is usually the shortest block
in the beat.

```
SFX: <the engine note climbing and staying there> <a palm settling flat against a headliner> <one
sharp breath through the nose>
```

**One event per pair of angle brackets.** Object and action, never adjective:

```
<a metal latch clicks>                    good
<heels ploughing into a hard floor>       good
<webbing creaking as she tests the strap> good
<intense dramatic impact sounds>          useless
```

Rules:

- **Order them the way they happen.** The model uses SFX order as a secondary timing signal, which
  is useful precisely because the rig avoids timecodes. Two or three events, in sequence, is a
  legible shape; six is a pile.
- **Never restate `AUDIO`.** The bed is already running. Repeating it doubles the ambience and
  steals attention from the events that are actually this beat's.
- **Breath is a sound effect and it is the cheapest realism in the whole rig.** `<one sharp breath
  through the nose>` costs six words and does more for a close-up than any adjective in `STYLE`.

**Prevents:** generic audio mush, and the beat whose sound has nothing to do with its picture.

---

## DIALOGUE — the words spoken in this shot

One block, one beat, one speaker. The shape is **who · delivery intention · the line**, with the
line last and inside braces:

```
DIALOGUE: RAY, plain and level, stating a fact rather than opening a subject, and NOT being kind:
{Ma asked about you.}
```

The language and the voice identity are not here — they are in `VOICE`, written once. What lives
here is the intention *for this beat only*.

### The word ceiling is real

**2 to 2.5 words per second.** Over that, the model compresses delivery to fit the clip and lip-sync
desyncs — the most common dialogue failure by a wide margin.

| Duration | Comfortable | Ceiling |
|---|---|---|
| 5 s | 8 w | 12 w |
| 8 s | 14 w | 20 w |
| 10 s | 18 w | 25 w |
| 12 s | 22 w | 30 w |
| 15 s | 28 w | 37 w |
| 30 s | 56 w | 75 w |

Count the words before you write the braces. `python3 scripts/seedance.py budget --duration 12` does
it for you.

The line is also not the only thing happening. A shot that needs a look, a turn and a reaction as
well has less room than the table suggests. **Cut the line, not the performance** — the performance
is what you cannot fix in post, and the line is what you can.

### One speaker per beat

Two people talking in one shot is where dialogue falls apart: the model splits its lip-sync
attention, and both faces get half of it. Give each line its own beat and cut between them. This is
exactly what Seedance's shot-reverse handling is built for. If a second voice must be audible, put
the speaker off-screen so there are no lips to sync.

### Never put emotion inside the braces

`{sadly} Don't.` speaks the word "sadly". Everything inside the braces is spoken aloud, without
exception. Direction goes before the colon; only the words the character says go inside.

---

## VOICE — accent, register, delivery

The fixed identity of every speaker, in `PROMPT SEGMENTS`. This is the block that stops a character
sounding like a different actor in every shot.

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
  voice. This is the entire reason the block sits in `PROMPT SEGMENTS` and not in a beat.
- **Four to six attributes per speaker:** pitch height, weight, texture, pace, accent, one habit.
  More than that and the model averages them away into a neutral read.
- **Always anchor the language.** Dialogue language drifts if unstated, and it drifts mid-clip.
  State it once here, at the head of each speaker's line.
- Officially supported lip-sync languages: **Mandarin, English, Japanese, Korean, Spanish,
  Indonesian, plus Cantonese and Sichuanese.** Portuguese is claimed on some endpoints. Anything
  outside that list will be spoken, but the mouth will not agree with it.
- **Better still, when the model supports it: bind an audio reference.**
  `@Audio2 → voice identity for MARCUS: timbre and pace. NOT the words.` An exclusion clause is
  mandatory here as everywhere — see [binding.md](binding.md).
- Two speakers who are meant to sound related get the **same placement and vowels, different weight
  and pace**. Identical strings produce one voice; unrelated strings produce two strangers.

**Prevents:** a character whose voice changes between shots.

---

## When the pauses are the content

The 2 to 2.5 words per second ceiling assumes **continuous speech**. Most scenes worth shooting are
not that. In a sparse script — where the silence is doing the work and the lines are what survives
the silence — budget **1.2 to 1.5 words per second** instead, and treat that as the real number.

| Duration | Continuous speech | Sparse, pauses carrying the scene |
|---|---|---|
| 5 s | 12 w | 6–7 w |
| 8 s | 20 w | 10–12 w |
| 12 s | 30 w | 14–18 w |
| 30 s | 75 w | 36–45 w |

The reason is not politeness about pacing. **Nothing performs during a silence in a generated
render.** A three-second pause asked for inside a take is three seconds of video you are paying
video rates for, in which the model has no instruction, and it will fill them — with a drift, a
blink loop, a small unmotivated head movement, or a face going slack. And you cannot tune it: the
pause is welded to the frames either side of it.

So **write the gaps into the edit, not into the take.** Generate the line tight, hold the last frame
under `EDIT`, and let the cut carry the silence. A pause built in the timeline is free, adjustable
and repeatable. A pause built in the model is none of those.

The practical rule: if a beat's script is mostly white space, the beat is short and the words are
few. Length in the render is not how you buy weight — restraint in the line is.

---

## Directing delivery without adjectives

The delivery intention in `DIALOGUE` is the highest-leverage line of text in an audio prompt, and
almost everyone wastes it on an adjective. The rules below are the whole method.

**Direct the intention, never the emotion.** "Sad" returns a sad-voice cliché — the model has a
stock read for every emotion word and it will hand you that read. An intention returns the line:

| Adjective | Intention |
|---|---|
| sadly | an inventory, the way you check a fuel gauge |
| angrily | closing a subject he has closed twice already |
| nervously | trying to get the sentence out before the thought catches up |
| warmly | offering something he expects to be refused |

**Name what the speaker is NOT doing.** Negative direction is unusually strong for voice — far
stronger than it is for picture, where naming an artefact summons it. A voice instruction that
fences off the three obvious reads leaves only the one you want:

```
DIALOGUE: RAY, level, not pushing it, not softening it, and NOT being kind:
{Ma asked about you.}
```

**Use effort and volume rather than adjectives.** These are physical, and the model renders physical
instructions:

- half-voiced, barely on the cords
- barely above the noise floor of the room
- he doesn't finish pushing the air out
- said on the way out of a breath, not the start of one
- full chest, but no louder than conversation

**Refuse the arc.** A line given a beginning, a middle and an end reads as *performed* — the model's
default is to shape every sentence into a small dramatic curve. If the character is holding
something down, say so explicitly: `flat, one level from first word to last, no lift at the end`.
Flatness has to be directed; it is never the default.

**Put the pause inside the line, not only between lines.** Where a person hesitates says more than
the words do, and a mid-line break is inside the model's control in a way that a silent gap is not:

```
DIALOGUE: MARCUS, answering a question he already answered, the break landing before the name and
not after it:
{I told her. I told her — Ray.}
```

**Never put emotion inside the braces.** Repeated here because it is the single most common mistake
in this block: everything between `{` and `}` is spoken. Direction before the colon, words inside.

---

## On-screen text

**Do not.** Corrupted lettering is the model's worst failure area across every version, and close to
unavoidable in 2.0. The 2.5 release claims reduced uncontrolled subtitles — an improvement claim,
not a fix.

If a word genuinely must be in-frame, wrap the exact string in quotes to raise its weight and accept
the odds: `the sign reads "OPEN"`. Anything longer than a word or two: generate clean and add type
in post, which is what every real spot does anyway.

The same applies to subtitles — **no captions, ever.** Speech invites the model to burn in
subtitles, so any prompt with a `DIALOGUE` block should carry a positive clause covering it:
`the frame contains the two men, the windscreen and the road only.` That is a `POSITIVE LOCKS`
line, not a ban. See [blocks.md](blocks.md) §27 and [finish.md](finish.md).

---

## When the voice has to be finish-grade

A video model emits audio as a **by-product of rendering picture**. Asking it for a voice track
spends video credits per attempt and hands back a whole clip you have to accept or bin — you cannot
re-roll the read without re-rolling the frames. When a project needs the voice to be genuinely
finished — a spot, a piece to camera, anything where the line carries the film — the stronger route
is a dedicated text-to-speech pass, cut to picture, with the render generated silent or with the
generated audio discarded. Iterating a read there costs seconds and pennies. This is a routing
decision, not a criticism of the model: in-render audio is excellent for texture, presence and a
short line inside a scene, and it is the wrong tool for a performance you intend to ship.

---

## The five blocks assembled

One beat out of a sequence, with everything sound-related in its correct tier:

```
BEAT 4 — the name
OPEN: RAY already turned in his seat, half-lit, MARCUS forward and unmoved.
CAMERA: locked off. The frame does NOT travel — ONLY the operator's breathing shows.
LENS: medium two-shot from the dash, 35mm, MARCUS sharp, RAY soft.
ACTION: RAY's head comes round → he waits one full second → he says it → MARCUS's hands
stay exactly where they are.
PERFORMANCE: wants — to make MARCUS answer without asking him to
             blocked by — MARCUS has not looked at him since the door came down
             plays — eyes on the side of MARCUS's face, breath let out before the line, hand flat on
             his own knee
             turns on — the silence after it, where he stops waiting and starts sitting
DIALOGUE: RAY, level, not pushing it, not softening it, and NOT being kind:
{Ma asked about you.}
SFX: <the engine note steady under it> <one breath let out through the nose before the line>
EDIT: hard cut.

AUDIO: <a sealed cabin, road noise arriving muffled through glass> <steady tyre hum on cold
asphalt>. Room sound ONLY.
SCORE: none. NO music of any kind at any point.
VOICE:
RAY — Southern California, Black American speech, mid thirties. Heavy, slow, fully voiced.
Ordinary conversational volume inside a very quiet car. No tension anywhere in it.
```

Four words spoken across a beat that runs six seconds. That is 0.7 words per second, well under even
the sparse budget, and the beat is not underwritten — the pause after the line is doing the work,
and it is being paid for by the cut, not by the model.
