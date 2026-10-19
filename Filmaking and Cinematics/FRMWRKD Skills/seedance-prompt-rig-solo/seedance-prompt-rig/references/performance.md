# PERFORMANCE — the beat-level acting unit

The difference between a shot with movement in it and a shot with acting in it. This file owns
exactly one block: `PERFORMANCE`, in the BEATS tier, one per beat.

> **This is the compressed register: one character, one beat.** For two or more characters, dialogue
> with subtext, or any shot where the performance *is* the point, use
> [acting-task.md](acting-task.md) instead — `EVENT AND SHARED DIRECTION` plus per-character
> `ACTING TASK` blocks, which direct the character's investment in a tactic rather than the
> behaviour it produces. The two are not alternatives to pick between casually:
> **`PERFORMANCE` is for iterating, `ACTING TASK` is for finishing.**

---

## The core problem

**The model cannot render biography.** "He is a sarcastic know-it-all who is secretly a dreamer"
describes a person; it does not describe a frame. There is nothing in it for a lens to record, so
the model draws nothing, and the face goes slack.

Everything in `PERFORMANCE` must convert to something a camera could photograph: eyes, breath, jaw,
hands, the tempo of a movement. If a line of the block could not be shot, it is not doing any work.

---

## The unit

Four lines, in this order, indented under the key.

```
PERFORMANCE: wants — <a playable objective, physical, achievable in this beat>
             blocked by — <what stands in the way, present in the frame>
             plays — <the visible behaviour: eyes, breath, hands, jaw, tempo>
             turns on — <the ONE moment the performance changes gear>
```

Worked:

```
PERFORMANCE: wants — to get the next sentence out without his voice going
             blocked by — the question was small enough to land
             plays — eyes fixed on the road, jaw working once, breath held a half-beat too long
             turns on — the second the name is said again; he stops answering and starts holding
```

### wants

Playable and physical. A want is something the character could succeed at inside this beat.

| Not playable | Playable |
|---|---|
| to feel afraid | to find the latch before the cabin swings again |
| to be sad | to get the sentence out without her voice going |
| to show he is confident | to make the other three drop their answers and take his |

Fear, sadness and confidence are *results*. Direct the pursuit and the result appears on its own.
Direct the result and you get the stock face for it.

### blocked by

Must be in the frame or in the body. Not in the backstory — the model cannot see backstory.

| Weak | Strong |
|---|---|
| his troubled past | his own weight holding the buckle shut |
| she is conflicted | the other three already have answers they like |
| the tension of the moment | a jammed lever that will not move |

### plays

The tactic, as behaviour. This is the field that actually renders, so give it the most words of the
four.

The reliable vocabulary:

- **Eyes** — where they go and when. **Eye-line is the single strongest acting instruction
  available.** `his eyes go screen-left and down first, to where the other man is lying low` is
  directable; `he looks thoughtful` is not. Scene-level eyeline ladders live in
  `GAZE AND EYELINES`; this is the beat's own version of the same instrument.
- **Breath** — held, caught, released, working. Visible in the chest and the nostrils, and it reads
  at any shot size, including a wide.
- **Hands** — checking, testing, gripping, abandoning. Hands leak intention before faces do, and the
  model renders hand behaviour more reliably than it renders subtle expression.
- **Jaw and brow** — set, working, loosening. Brow movement matched to the beat is what stops the
  frozen-mask face.
- **Tempo** — the speed of a movement carries more emotion than its shape. A slow reach and a fast
  reach are different characters doing the same action.

### turns on

One moment per beat where the performance changes gear. Not a plot event — a shift in *how they are
playing it*.

```
turns on — the lever failing; she stops solving and starts listening
turns on — the last word landing; he holds their eyes instead of moving on
turns on — the second he sees his own hands and forgets the fight entirely
```

Without a turn, a performance is one note for the whole clip. With one, there is a before and an
after — and that shape is what makes six seconds feel like a scene rather than a loop.

---

## Micro-behaviour that always earns its words

Cheap to write, disproportionately effective. These are externals, and externals are legitimate here
only because the model renders certain absences as artefacts:

- **Blinking.** Say it. Absent instruction, faces go glassy and unblinking. `natural blink cadence
  throughout` is four words that fix the deadest failure mode there is.
- **Breath.** Chest rise, or a sharp intake at the turn.
- **A micro-pause before a reaction.** Real people take a beat. Instant reactions read as puppetry.
- **Eyes wet and alive, with a catchlight.** A catchlight needs a source to come from — tie it to
  one of the sources named in `LIGHTING`. Asked for with no motivating source, it either does not
  appear or it appears as a floating highlight with nothing behind it.
- **Asymmetry.** One brow, one side of the mouth. Symmetrical expressions read as rendered.

---

## Multiple characters

**Three or more performing simultaneously is the drift cliff.** Identities cross-contaminate and the
twins artefact appears, on every Seedance version.

Handling:

- **One performer per beat.** Everyone else is present but not acting — sitting, watching, blurred
  by depth. A second `PERFORMANCE` block in the same beat is two performances competing for one
  render.
- **Cut for the second performance.** Shot-reverse is well supported; a genuine two-hander in a
  single frame is not. That is a second beat and an `EDIT: hard cut.`
- **Never use pronouns across characters.** "He looks at him" is unresolvable and produces the twins
  artefact. Use the name or the alias every time: "the tall one looks at the one on the couch".
- **Extras are texture.** Push them into motion blur, into the background, or out of the shot. A
  crowd is a condition, not a cast.

If the scene genuinely needs two people acting at once, you have left this register. Go to
[acting-task.md](acting-task.md).

---

## Speech and performance together

When the character speaks, the acting has to survive the line. `PERFORMANCE` and `DIALOGUE` are two
separate blocks in the same beat, and each carries only its own half: the behaviour here, the words
and the per-beat delivery intention there. Keep the shot to one job.

```
PERFORMANCE: wants — to make the other three drop their answers and take his
             blocked by — they already like their own
             plays — eyes moving between them, landing each beat AT them, checking whether it lands
             before pressing on
             turns on — the last two words, where he stops selling and just holds their eyes
DIALOGUE: bright and fast with a nasal edge, pitching an idea he already knows will win:
{No brainer. Deep future — space future.}
```

The language and the fixed voice identity are not in either block — they are in `VOICE`, written
once in `PROMPT SEGMENTS` and pasted verbatim. `DIALOGUE` carries only what changes beat to beat.
Word ceilings, delivery direction and the bracket grammar: [sound.md](sound.md).

Note what is absent from both blocks: no character history, no adjectives about his personality, no
explanation of what the moment means. Every word is something the lens or the microphone can record.
That is the standard.
