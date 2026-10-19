# ACTING TASK — the scene-level performance register

`PERFORMANCE` is the **beat-level** unit: one character, one shot, four lines — wants, blocked by,
plays, turns on. [performance.md](performance.md) owns it and it is correct for most work.

This file is the **scene-level** unit: two or more characters, dialogue with subtext, the scene
where the performance *is* the shot. The two are not alternatives to pick between casually —
**`PERFORMANCE` is for iterating, `ACTING TASK` is for finishing.**

The method is Tigran's, and these definitions are his and are authoritative. **Do not replace them
with textbook Stanislavski summaries.** Pair with [finish.md](finish.md).

`ACTING TASK` and `MICRO-BEHAVIOUR` are not new block keys — there are twenty-seven and no more
([blocks.md](blocks.md)). They are the two named sub-blocks that live inside the
`EVENT AND SHARED DIRECTION` / `PERFORMANCE` area of a finish-grade prompt.
`EVENT AND SHARED DIRECTION` is a real CONTEXT-tier block, block 9, written once for the whole
scene; the per-character tasks hang off it, in the same tier, immediately below.

Use it when: two or more characters share a scene · there is dialogue with subtext · the beat is a
conflict, a negotiation, a reaction · the user says a face reads dead, glassy, flat or over-acted ·
you are paying to finish a performance shot.

---

## 0 — The core principle

An acting task is when the character is **INVESTED in his or her tactic for reaching the goal.**

- It is NOT a description of external behaviour ("eyes flick", "brows lift", "he looks sad"). That
  is playing the result, and it produces dead faces.
- It is NOT necessarily physical. The tactic can live entirely **in the eyes**: a different look for
  someone who humiliates than for someone who begs; a person arguing from conviction checks BOTH of
  the partner's eyes, hunting a sparkle of trust, registering whether the partner is interested or
  drifting — and adjusting to what he finds.
- **The eye movement IS the doing.** Aliveness is the mind visibly working on the task, moment to
  moment.
- Never fix dead eyes with lighting tricks. Fix them by giving the eyes a task.

---

## 1 — The ladder, worked strictly in this order

**0. Read the WHOLE scene dialogue first.** Never build a task from one line. The task lives across
the entire exchange — where it holds, where it breaks. Check every line of every character before
directing any of them.

**1. The GOAL OF THE SCENE — one shared direction.** The scene has ONE goal: a single direction ALL
characters play toward, usually unspoken — a mutual silent agreement about how this time will be
lived. *(A mother packs her son's suitcase, army in an hour: the goal is **make it painless — hide
the feeling, never lose the positiveness.** It belongs to both at once.)* The scene goal is never
the film's dramaturgic function. Characters never know or play the film's purposes; those are
accomplished THROUGH them, as a byproduct.

**1a. The ENDING names the event.** Always look at how the scene ENDS before naming its event. The
last line is the key you read the whole scene backward through. Watch for the double-meaning last
line — spoken about one thing, meant about another.

**1b. ALL in one event.** The event must contain EVERY character in the scene, including silent
ones, as participants or mirrors of the same process. If a character stands outside the named event,
the event is named wrong.

**1c. The PHYSICAL ACTION is the channel.** The surface activity — the terrain — stays as the
physical action, and each character pursues the event THROUGH it, via his own distinct, visible
behaviour. The invisible task must have a physical channel the camera can read. **Give every
character in the scene his own physical channel for the same event: different behaviours, one event,
one terrain.**

**2. Each character's MOTIVE — different fuel, same direction.** Everyone pushes along the same
scene direction, but each for his own reason. Same vector, different fuel; the fuel is what makes
each performance distinct while the scene reads unified. Motives can be alternative hypotheses — the
director picks. Given circumstances constrain them: a man who took the job at a compromised place is
ALREADY compromised and cannot play a moral innocent.

**3. Each character's GOAL — the personal fight.** Born from the motive: what this person is
fighting for inside the scene. Ordinary, personal, playable. Never the same words as the scene goal,
never the theme.

**4. OBSTACLE.** What presses against the direction — the real feeling trying to surface, the thing
too big to stay ordinary. One crack and the shared goal collapses. This pressure is what the
audience actually feels, precisely because nobody plays it; everyone plays keeping it out.

**5. TACTIC — the acting task proper.** The invested, moment-to-moment pursuit, written as what the
character is DOING to the partner, with the eye-work named as purposeful action:

- checking both of the partner's eyes for a sparkle of trust
- registering after each point: did it land, or is he about to smirk
- stealing looks and snapping back before being caught
- measuring the partner, memorising him, comparing what I feel with what he shows

The moment-to-moment steps are keyed to the actual dialogue words, and in the delivered prompt a
step is usually a BEAT of its own. Mark the point where a character's fuel runs out and the line
breaks — **the break IS the delivery of the scene.**

---

## 2 — The blocks, as they go in the prompt

Written once for the whole scene, in the CONTEXT tier, under `GAZE AND EYELINES`:

```
EVENT AND SHARED DIRECTION
THE EVENT, containing everyone and never spoken aloud: [name it from the ending]
The terrain is [physical action], and each pursues the event through a different physical channel:
[A] through [channel], [B] through [channel].
THE SHARED DIRECTION, played by all: [one line]
THE ESSENTIAL AXIS: [the opposition the audience actually reads]
```

Then one per character, immediately below it, still in the CONTEXT tier:

```
ACTING TASK — [NAME] (fully invested in the tactic; the work happens in the eyes)
MOTIVE: [why THIS character pushes the shared direction]
GOAL: [the personal fight]
OBSTACLE: [what presses against the line, and what one crack costs]
TACTIC: [what is done to the partner, with the eye-work as action]
Moment to moment:
— {dialogue words} — [verb at the partner + what the eyes check]
— {dialogue words} — [verb + eye-work]
— [where the line breaks, if it breaks]
```

Then the safety block, once, last of the three (§3):

```
MICRO-BEHAVIOUR
[blink cadence, gaze engagement, catchlight, breath, micro-pause, asymmetry]
```

### The assembled order

```
SCENE CONTEXT → FORMAT MODE → ACTIVE REFERENCES → CAST → STAGING → WARDROBE →
GAZE AND EYELINES → EVENT AND SHARED DIRECTION → ACTING TASK (one per character) →
MICRO-BEHAVIOUR → RULES

BEAT 1 — <slug>      OPEN · CAMERA · LENS · ACTION · DIALOGUE · SFX · EDIT
BEAT 2 — <slug>      …

PHYSICS → LIGHTING → AUDIO → SCORE → STYLE → VOICE → POSITIVE LOCKS
```

The whole apparatus sits in CONTEXT, above the first beat, and is never restated. That is the point
of putting it there: a task is true from the first frame to the last, so it is paid for once and
cannot disagree with itself across a cut. Restated per beat it is re-decided per beat, which is the
performance equivalent of wardrobe drift.

**Where a scene runs per-character `ACTING TASK` blocks, drop the per-beat `PERFORMANCE` block.**
They are the same job at two scales, and carrying both gives the model two directions for one face
and it averages them. The beats then carry only `ACTION`, `DIALOGUE` and the camera — which is what
leaves room for six of them.

Rules:

- Verbs directed at the partner. **No adjectives of emotion as instruction** — "sadly", "nervously",
  "angrily" are forbidden.
- **No facial choreography** — "brows lift", "mouth trembles". Externals only in the safety block.
- Nobody plays the emotion; everyone plays the direction. The audience receives the feeling through
  the pressure.
- **Every character in frame gets a task, including silent listeners.** A listener's task is real:
  "decide if he's serious", "wait for the punchline", "protect the mood".
- Use the name every time. Pronouns across characters are unresolvable and produce the twins
  artefact — that rule holds inside a task exactly as it holds in `CAST`.

---

## 3 — MICRO-BEHAVIOUR, the AI-model safety block

The one place external choreography is permitted, and it is a model necessity rather than direction.
Keep it in its own block so it can never be mistaken for the task.

```
MICRO-BEHAVIOUR
Natural blink cadence on every face throughout, at rest and while speaking, increasing as the
pressure rises. Every gaze stays engaged in the task and focused on something specific. Eyes wet and
alive with a real catchlight from [the named source in LIGHTING]. Visible breath in the chest. A
micro-pause of about a quarter second before any reaction. Expressions asymmetric, one brow and one
side of the mouth.
```

Without this, faces go glassy and unblinking — the deadest failure mode there is. The catchlight
clause has to name a source that actually exists in `LIGHTING`; ask for a catchlight with nothing to
motivate it and the model either ignores it or invents a lamp.

---

## 4 — Contrast pairing: build duos on mirrored +/−

A two-character scene is richer when the pair is built on CONTRAST — each carries a plus and a
minus, mirrored against the other, with one axis being the essential one the audience reads.

- Each character gets one + and one −, inverted relative to the partner.
- **Name the ESSENTIAL AXIS** of the scene. That opposition is what the audience reads; the other
  traits are colour. It goes on the last line of `EVENT AND SHARED DIRECTION`.
- Both still push the same scene direction. The contrast lives UNDER it and leaks out through the
  tactics and the eyes: one character's ordinariness is real, the other's is armour, and it cracks.
- **The seeming trait is often scar tissue over its opposite.** "Careless" = hope lost, not care
  absent. Direct the history, not the surface.

**Keep the +/− notation out of the prompt body.** It is author-side craft — the model cannot use the
notation, only the motives and tactics it produces. Work it out, then write the motives.

---

## 5 — Staging an acting scene

Two things carry a two-hander more than any adjective:

**The eyeline ladder.** Build the escalation out of *who is allowed to look at whom*, beat by beat,
and it will read with the sound off. A ladder that runs "never looks up → finds him only in a
reflection → first direct look → first and only returned look → asks for the look → does not get it"
is a whole scene's dramaturgy expressed as blocking. It goes in the `GAZE AND EYELINES` block, built
beat by beat, naming the beat each rung belongs to — and it says who never looks at camera.

**The camera runs the same ladder.** Locked → creep → creep → handheld → handheld → locked. The
frame loses its composure at the moment the character does, and recovers for the aftermath. That
ladder is written across the per-beat `CAMERA` lines, one rung per beat — one camera move per beat,
as always, so the ladder and the one-move law want the same thing.

**Lock the screen sides in `POSITIVE LOCKS`**, as assertions: who is screen-left, who is
screen-right, which side of the line the camera stays on. That is what makes the coverage survive
the cuts. Standing blocking — who faces where, who turns and how many times — stays in `STAGING`.

---

## 6 — Common failures to catch

- Task built from one line instead of the whole dialogue → re-read the scene first.
- The film's reveal or theme assigned to a character as his task → characters never play the film's
  purposes.
- Scene goal confused with character goal → the scene goal is shared; character goals differ.
- Motive ignores given circumstances (playing innocence while already complicit) → re-derive.
- Prescribed eye or face choreography instead of eye-work as purposeful action → rewrite as verbs at
  the partner.
- Emotion adjectives as direction → replace with the task that produces the emotion.
- The task restated inside every beat → hoist it back into CONTEXT; it is one fact with a scene-long
  lifespan and the beats were re-rolling it.
- An expression baked into the character reference plate bound in `ACTIVE REFERENCES` → it becomes a
  mask worn for every beat, and no task written below it can take it off. **Generate character
  sheets with a completely neutral, unsmiling, mouth-closed head-and-shoulders view** when the shot
  is an acting shot, and exclude the plate's expression on the role line where the plate has one.

---

## 7 — Worked reference

`02-Projects/AI Film/Seedance 2.5 vs 2.0/01-Storyboard/prompts-v2/advanced/A6-hairline.md` — a full
15-second two-hander written on this grammar: six beats, five hard cuts, twenty-eight words of
dialogue, two `ACTING TASK` blocks, an eyeline ladder and a matching camera ladder. Its companion
`A6b-extension.md` is the same scene continued with four words of dialogue.

Method credit: the ladder, the event rules and the contrast build are Tigran's (`tig-acting-task`).
