# Density

Load this when a prompt is over budget, when converting somebody else's prompt onto the rig, or when
you are unsure how long a prompt is supposed to be in the first place.

The premise: most AI-film prompts in circulation are three to five times longer than they need to
be, and the excess actively hurts. The model averages across everything it is given, so a fact
stated five times in five blocks does not get five times the weight — it dilutes the four facts that
were only stated once.

Target: **a 1,400-word single-shot prompt compiles to about 460 words with nothing lost** — and the
second shot in that scene then costs one BEAT, not another 1,400 words. That compounding is where
the rig really pays.

---

## The density dial

There is one grammar and one set of twenty-seven blocks. There is not a short register and a long
register; there is a **dial**, and two things set it:

- **The working ceiling — `400 + 45 × duration`.** 5 s ≈ 625 w · 12 s ≈ 940 w · 30 s ≈ 1,750 w. Words
  are bought with screen time. A five-second shot cannot spend a thousand words on itself because
  there is not a thousand words of thing happening.
- **Which of the twenty-seven blocks you loaded.** Every block you load is a fact the model has to
  decide, and one you have to write. Blocks are the coarse dial; word count is what falls out of it.

The hard ceiling — 3,000 words, 20,000 characters — is the Seedance 2.5 API cap and it is nowhere
near where adherence fails. Adherence is what limits you, and adherence scales with duration.

### The draft end

Exploring, iterating, finding the shot. You do not yet know which shot this is, so precision spent
on it is precision spent on a shot you are about to throw away.

- Fewest blocks — a preset, stripped, nothing added back speculatively.
- One or two characters.
- Budget matters more than the last 10%.
- **A 5–8 second single-beat prompt at 500–650 words.**

Iterate here. Change one block per render and you learn what that block does; change five and you
learn nothing.

### The finish end

The shot is locked and you are paying to complete it. Now the last 10% is the entire job, and the
cost of a re-render is higher than the cost of two hundred more words.

- More blocks — `STAGING`, `WARDROBE`, `GAZE AND EYELINES`, `EVENT AND SHARED DIRECTION`,
  `ACTING TASK`, `MICRO-BEHAVIOUR`.
- Three or more characters, or a whole formation.
- Identity has to hold across a film, not across a shot.
- **A 30-second six-beat prompt at 1,400–1,750 words.**

Method for this end of the dial: [finish.md](finish.md).

| | Draft end | Finish end |
|---|---|---|
| The job | find the shot | complete the shot |
| Blocks | a stripped preset | the preset plus the staging and acting apparatus |
| Cast | one or two | three or more, or a formation |
| Beats | one | five or six |
| Duration | 5–8 s | 30 s |
| Words | 500–650 | 1,400–1,750 |

### What the dial does not change

The dial changes **how many blocks** and **how many beats**. It never changes the grammar — same
twenty-seven names, same ALL-CAPS keys, same lower-case prose, same closed capitals vocabulary, same
tier order. And it never licenses restatement. **One fact, one block, at both ends of the dial.** A
finish-grade prompt is longer because it is carrying more facts, not because it is carrying the same
facts more times.

### The one thing that inverts: every prompt is an island

Seedance sees only the text in front of it. Nothing carries between separate API calls — positions,
poses, wardrobe, props, optics, light are spelled out from scratch, every time. *"Same as the
previous shot"* is an instruction to a model that has no "before".

So:

- **Within one prompt, state a fact once.** Restating it is noise the model averages, and it dilutes
  everything you stated once. This is the first law.
- **Between two prompts, restate everything.** Paste the whole `CONTEXT` tier and the whole
  `PROMPT SEGMENTS` tier into the second call, verbatim. Nothing survives the gap.

These are not in tension. They are different scopes, and confusing them is the most common reason a
sequence stops matching: someone applies the no-restatement law across prompts and the second clip
arrives with half a world in it.

---

## The seven cuts

Apply in order. The first three usually get you to budget on their own.

### 1. Kill the restatement

The single biggest win. A typical circulating prompt states the same fact in the scene summary, the
location map, the first-frame block, the camera block and the locks block — five copies.

**Rule: every fact has one home block, and appears only there.**

```
before  (the same fact, five times, in five blocks)
  summary:    … the lens stays within the capsule at all points …
  geography:  … lens positioned within the capsule, tucked tight …
  frame one:  … lens level with her, within the unlit capsule …
  camera:     … held within the cramped capsule, exterior excluded …
  locks:      … lens confined within, exterior excluded throughout …

after   (once, in the block that owns it)
  RULES: the camera NEVER leaves the cabin.
```

131 words → 6.

### 2. Kill the triple negative

`NO glass, NO windows, NO canopy` is three negations doing the job of one positive statement — and
it seeds "glass", "windows" and "canopy" into the frame while trying to exclude them.

```
before  SHUT steel roof, NO glazing, NO viewport, NO canopy, hull closed over
after   LOCATION MAP: a sealed metal ceiling
```

State what is there. Negate only when the artefact is strongly associated with a term you had to use
anyway, or when the work is stylised — in `STYLE LOCK` the negations are load-bearing, because a
stylised brief has to fight the model's gravity back toward photography.

### 3. Kill adjective stacking

Four adjectives for one property is one adjective and three wasted words. Better: replace the
adjective with its **consequence**.

```
before  VERY small, narrow, VERY tight dark metal cockpit
after   SCENE CONTEXT: a cockpit she cannot straighten in

before  massive, huge, enormously powerful arms
after   CAST: arms that can stop the thing, and it costs him to do it
```

Consequence renders. Adjectives get averaged.

### 4. Kill the meta-commentary

Anything describing the *effect* on the viewer rather than the content of the frame. The model cannot
render an effect.

```
cut  the performance carries in the eyes
cut  this is what lands the moment
cut  the takeaway: bodies placed at mixed distances
cut  intent: a loud ensemble music beat
cut  HYPER-CINEMATIC, realism dialled to maximum
```

Zero of these produce a pixel. `HYPER-CINEMATIC` in particular is a word with no referent — it is the
writer's enthusiasm, not an instruction. If a line describes the audience's experience rather than
the frame's contents, it goes.

### 5. Kill the unrenderable

Backstory, personality labels, motive-as-history. Convert to visible behaviour or delete.

```
before  keeps the personality already set up elsewhere — the quick, spiky,
        needling cynic of the group who is privately the biggest romantic
        of them all, consistent with how he plays in every other setup
after   PERFORMANCE: plays — eyes moving between them, landing each beat AT them,
        checking whether it lands before pressing on
```

The rewrite is shorter *and* it is the only version that renders.

### 6. Kill the second camera move

Law 2, applied as compression. A `CAMERA` line with a push and a pull and a roll and an orbit in it
is four moves fighting; keeping one is both better prompting and a large word saving. If the second
move is genuinely needed, it is a second BEAT and a cut — which is cheaper than it looks, because a
BEAT is the only thing you pay for.

### 7. Kill the anti-CG rant

```
before  STRICTLY not computer graphics, not a 3D package, not offline
        rendering, not real-time engine output, not synthetic, not sterile
        digital. ABSOLUTELY no synthetic gloss — fully photographic.
        Beat the artificial look down wherever it appears.
after   STYLE: shot on film — real grain, halation, imperfect focus
```

53 words → 8, and the short version performs better, because naming a real capture medium is a
positive instruction while the long version is a list of things to think about. Note also what the
long version does to itself: it seeds "3D", "render" and "engine" into the frame in the act of
excluding them.

---

## Compression table

Reach for these directly.

| Pattern | Replace with |
|---|---|
| `NO x, NO y, NO z` | the positive statement of what is there, in `POSITIVE LOCKS` |
| four adjectives on one noun | one consequence clause |
| "very / extremely / absolutely" | delete |
| any sentence about how it reads or feels | delete |
| character backstory or personality label | a `plays` line in `PERFORMANCE` |
| a full re-description of the reference image | an `ACTIVE REFERENCES` role line with a `NOT` clause |
| a list of seven optical properties | the two that define the look, in `STYLE` |
| "cinematic, filmic, movie-like, film look" | one capture medium |
| repeated per-beat restatement of the style | hoist it into `PROMPT SEGMENTS` |
| repeated per-beat restatement of wardrobe or geography | hoist it into `CONTEXT` |
| a lock that repeats an unambiguous statement | delete |
| stacked camera moves | one `CAMERA` move, or a second BEAT |
| dialogue longer than duration × 2.5 | cut the line |

---

## Pricing a misfiled constant

A fact that belongs in `CONTEXT` but sits in `BEATS` costs twice. You pay for it **once per beat**,
and you give the model **one fresh chance per beat to render it differently**. The second cost is
the expensive one.

The arithmetic, on a 22-word grade description in a six-beat clip:

```
in BEATS      22 w × 6 = 132 words, and six independent decisions about the grade
in SEGMENTS   22 words, and one decision
saved         110 words, and five chances to drift
```

The words are the small half. Five re-decisions about a grade is how a sequence arrives with beat one
warm, beat four neutral and beat six slightly green, with nothing in the prompt that asked for any of
it.

The lifespan test catches these before you write them — *"would I have to write this again in beat
four?"* — and `seedance.py lint` catches the ones that got through: it reports every fact it finds in
more than one beat and what hoisting it would save.

```bash
python3 "$SKILL_DIR/scripts/seedance.py" lint prompt.txt --model 2.5 --duration 30
```

---

## Converting an existing prompt

Method, in order:

1. **Read it once and list the actual facts.** Usually 15 to 25 of them, hiding inside 1,200 words.
2. **Sort each fact into a tier by lifespan.** Would you write it again in beat four? Yes, and it is
   true of this project only → `CONTEXT`. Yes, and it will still be true next project →
   `PROMPT SEGMENTS`. No → `BEATS`.
3. **Drop every duplicate.** This is where most of the reduction happens.
4. **Drop everything that is not a fact.** Meta, mood, enthusiasm, effect-on-viewer.
5. **Rewrite each surviving fact once, in its block, in the house voice** — sentence case, consequence
   over adjective, one clause per idea, ALL-CAPS key at the head of the line.
6. **Count against the working ceiling for the duration**, not against a flat number. Over? Go back
   to step 3; there is always another duplicate.
7. **Lint.** `python3 scripts/seedance.py lint <file> --model <m> --duration <d>`

Expect roughly 3:1 on the first shot of a scene, and 8:1 or better on every shot after it, because
those cost only a BEAT. If the first shot is coming in under 2:1, you have kept duplicates.

---

## What not to compress

Density is not brevity for its own sake. Protect these, even when over budget:

- **`ACTIVE REFERENCES` role lines and their `NOT` clauses.** The highest-value words in the prompt.
- **The motivated light source in `LIGHTING`.** One clause, non-negotiable.
- **The `plays` line in `PERFORMANCE`.** It is the only thing making the face move.
- **Where the energy goes** in an `ACTION` beat. Consequence is what makes it look real.
- **Blink and breath cues.** Four words, enormous return.
- **The palette split in `STYLE`.** Three numbers, more reliable than any colour adjective.

If you are over budget after cutting all seven categories and these six are all that remain, the shot
is too big for one beat. Split it into two BEATS — or, if the light state or the location changes
across it, into two prompts. [scenes.md](scenes.md).
