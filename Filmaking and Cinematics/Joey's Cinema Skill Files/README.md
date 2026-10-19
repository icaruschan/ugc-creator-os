# Joey's Cinema Skills — Operator README

This folder is a modular AI filmmaking toolkit for building a reusable story world, consistent characters, cinematic scene plates, Seedance prompts, and Higgsfield Genjutsu motion-transfer prompts.

Joey's original tutorial and example prompts are preserved in [`Joey-original-README.md`](Joey-original-README.md). This README documents the **current skill lineup**, routing rules, handoffs, and legacy files that still remain in the folder.

---

## Current production stack

```text
story-bible-builder
        ↓  locks the world, canon, voices, movement, and production rules
CastKit v1
        ↓  builds reusable character, outfit, and turnaround references
Scenecraft v1
        ↓  builds environments, coverage, people-in-scene plates, and first frames
        ├── Shotcaller v1
        │       ↓  writes Seedance 2.0 / 2.5 production prompts
        └── Motion Dojo v1
                ↓  writes Higgsfield Genjutsu motion-transfer prompts
```

Additional Higgsfield-sourced companion skill (not a Joey skill):

- `ACTING SKILL` deepens objectives, tactics, listening, eye life, voice, and scene-specific performance.

`LIRA SKILL` has been removed from the active stack and preserved under `Archived and Redundant Skills/`.

In one line:

**Story Bible owns canon. CastKit owns the cast. Scenecraft owns the still frame. Shotcaller owns Seedance. Motion Dojo owns Genjutsu motion transfer.**

---

## Load rules

### Load together when the job needs the full chain

- Installed story bible + `CastKit v1` for canon-faithful character references.
- Installed story bible + `Scenecraft v1` for locations and frames that match the world.
- `CastKit v1` output + `Scenecraft v1` for a locked character inside a finished scene.
- `CastKit v1` output + `Scenecraft v1` output + `Shotcaller v1` for Seedance production.
- Character/location references + a motion-transfer video + `Motion Dojo v1` for Genjutsu.
- `ACTING SKILL` before `Shotcaller v1` when a scene needs nuanced dramatic performance.

### Do not load competing owners for the same job

| Collision | Use |
|---|---|
| `CastKit v1` + legacy `character-builder` | **CastKit v1** for current work |
| `Scenecraft v1` + `banana-pro-director-30` Mode 3 | **Scenecraft v1** for current scene plates |
| `Shotcaller v1` + an older cinema-director grammar | **Shotcaller v1** |
| `Shotcaller v1` + `Motion Dojo v1` for one prompt | Pick by engine: **Shotcaller for Seedance**, **Motion Dojo for Genjutsu** |
| `ACTING SKILL` as the final video writer | Acting supplies performance; **Shotcaller ships the Seedance prompt** |

Run skills in pipeline order. Do not ask several skills to rewrite the same prompt in parallel.

---

## Which skill for which request

| You need… | Use | Output |
|---|---|---|
| A canon document, recurring world, locked voices, or character consistency | `story-bible-builder` | One installable story-bible `SKILL.md` |
| A face lock, animated or photoreal character, outfit, swap, or turnaround | `castkit-v1` | Flat-gray reusable character references |
| An environment, location, background, establishing still, first frame, or coverage angles | `scenecraft-v1` | Photoreal scene plate prompt or coverage set |
| A Seedance 2.0/2.5 scene, dialogue shot, action sequence, performance, lipsync, or extension | `shotcaller-v1` | Production prompt on a locked 16-slot spine |
| Motion/choreography/camera transfer from a reference video in Higgsfield Genjutsu | `motiondojo-v1` | Lean Genjutsu motion-transfer prompt |
| Deeper character behavior, objectives, tactics, listening, or eye life | `ACTING SKILL` | Master acting profile + scene adaptation |

If several rows apply, follow the production stack rather than combining their instructions into one giant request.

---

## 1. Build the canon — `story-bible-builder`

Use this when a film, series, game, album, or recurring universe needs a stable source of truth.

The updated builder interviews the user and assembles **one dense, installable `SKILL.md`**, designed to stay compact enough to load cleanly. It covers:

- premise and thesis
- timeline, aesthetic, factions, locations, and world rules
- character visual locks, backstory, psychology, speech, movement, and stillness
- relationships and ensemble dynamics
- structural story engines
- production rules and activation behavior

It supports two uses:

1. **Standalone canon reference** — install the finished bible and use it whenever creating anything inside that world.
2. **Context source for production skills** — the bible supplies identity, voice, movement, palette, era, and rules while another skill writes the image or video prompt.

The builder works as a staged interview, not a one-shot questionnaire. It confirms each section before assembly. If the user only needs part of a bible, scope the interview to that part.

### Story-bible handoff

| Bible material | Downstream destination |
|---|---|
| Visual identity and permanent markers | CastKit character references |
| Locations, era, palette, and material culture | Scenecraft plates |
| Voice, gait, stillness, and behavioral rules | Acting / Shotcaller performance |
| World physics and production constraints | Shotcaller or Motion Dojo locks |

Lore should not be pasted wholesale into generation prompts. Translate it into visible, audible, or physical instructions.

---

## 2. Build the cast — `castkit-v1`

`CastKit v1` is the current character and outfit builder. It supports **photoreal and animated characters** while keeping the same reference-building grammar.

### Five stations

| Station | Purpose | Prerequisite |
|---|---|---|
| 0 — Face lock | Create the canonical chest-up identity plate | Approved text spec |
| 1 — Additions | Hair, piercings, tattoos, scars, expressions, and re-locks | Face lock |
| 2 — Outfit build | Put a look directly on the locked character | Face lock |
| 3 — Outfit replacement | Swap the character into an existing outfit/pose reference | Character reference |
| 4 — Character sheet | Create the 3-panel default or requested 6-panel sheet | Approved outfit image |

Do not skip forward: no outfit on an unlocked face, and no character sheet before the outfit image is approved.

### Locked reference standard

- Flat 18% neutral-gray field, not a room or photographed seamless.
- Completely even, shadowless illumination.
- Zero cast shadow, contact shadow, halo, glow, or background light spill.
- No depth of field, atmosphere, vignette, or baked scene lighting.
- Photoreal or animated render language is selected before generation.
- Three-panel sheets remain dead-on unless the user explicitly requests another orientation.

The reference defines **who the character is**. Later skills define where the character is, how the scene is lit, and what the character does.

---

## 3. Build the frame — `scenecraft-v1`

`Scenecraft v1` is the current scene-plate director for Nano Banana Pro, Seedream 5.0 Pro, and other image models.

### Plate menu

| Plate | Purpose |
|---|---|
| A — Environment | Empty location, set, background, world, or establishing plate |
| B — People in scene | Locked characters placed inside a realized environment |
| C — Coverage set | Matching angles that preserve geometry, surfaces, palette, and light |
| D — Plate edit | A controlled change to an existing plate with protected details |

Scenecraft silently plans composition, depth planes, resolvable detail, light direction, atmosphere, and camera position. It then writes a five-paragraph cinematographer prompt rather than a tag pile.

### Model routing

- **Nano Banana Pro** is the default and favors the full five-paragraph structure.
- **Seedream 5.0 Pro** favors a compact creative brief, exact colors, scoped references, in-world text, and target/change/protect editing.
- For another image model, begin with the Nano Banana Pro structure and trim if the model loses long instructions.

Use Scenecraft to create a first frame or environment anchor before moving to video generation.

---

## 4A. Direct Seedance — `shotcaller-v1`

`Shotcaller v1` is the current full cinema director for Seedance 2.0 and 2.5.

### Choose the target version first

| | Seedance 2.0 | Seedance 2.5 |
|---|---:|---:|
| Maximum image references | 9 | 50 |
| Maximum runtime | 15 seconds | 30 seconds |

Two camera vantages are still two prompts. Extra runtime is not permission to overload one generation.

### Locked 16-slot spine

1. Header
2. Style Prefix
3. No On-Screen Text
4. Critical Blocks
5. Assets
6. Geometry Map
7. First Frame
8. Optics
9. Camera
10. Light & Colour
11. Atmosphere
12. Action Timing
13. Physics
14. Acting
15. Audio
16. Locks

Shotcaller handles action, choreography, products, performance, dialogue, attached-track lipsync, strobe, silent scenes, and seamless video extensions. Dialogue uses an exact script block, one speaking mouth at a time, time-bound action, and a separate delivery specification.

Every delivery includes a pre-prompt checkpoint, numbered references, a titled runtime, and one complete copy-ready prompt.

---

## 4B. Transfer motion — `motiondojo-v1`

`Motion Dojo v1` is the Higgsfield Genjutsu branch. Use it when an attached motion-transfer video supplies movement or camera behavior.

### Three forms

| Form | Reference video controls | Built fresh |
|---|---|---|
| 1 — Body Copy | Body movement, timing, and camera | Cast, wardrobe, world, and light |
| 2 — Camera Copy | Camera path only | Cast, action, world, and light |
| 3 — Body Copy, New Camera | Body movement and timing | A new camera plus cast, world, and light |

The motion-transfer video is attached separately and is called **“the attached motion transfer video”** inside the prompt. It is never tagged. All still-image references use `<<<image_N>>>` in attachment order.

### Mouth lock

Motion Dojo resolves the mouth state before writing:

- **Closed** — no speech; mouths remain closed or naturally parted only for breathing.
- **Exact words** — only the supplied transcript is spoken, by the matching role, at the matching time.
- **Match the mouth** — mouth movement follows the motion reference without invented lyrics.

Runtime matches the source motion video. A longer prompt makes the model invent movement after the source ends; a shorter one compresses the choreography.

---

## Higgsfield companion — `ACTING SKILL`

Use Acting when default performance direction is not enough.

Its core principle is that acting is **behavior under pressure**, not a named emotion. It develops objectives, obstacles, tactics, beats, listening, body language, eye life, vocal identity, and ensemble behavior.

For Shotcaller, route its output like this:

| Acting output | Shotcaller slot |
|---|---|
| Observable body behavior and beat changes | Action Timing |
| Brows, eyes, listening, and eyelines | Acting |
| Locked voice identity and line delivery | Audio |

Acting does not replace Shotcaller and does not ship the final Seedance prompt.

---

## Archived reference — `LIRA SKILL`

Lira is preserved at `Archived and Redundant Skills/LIRA SKILL.md` for historical reference. It is not part of the active production stack because its image routing, character, location, and editing instructions overlap with Joey's newer specialist skills.

For new characters, use CastKit. For environments and scene plates, use Scenecraft. For Joey's broader all-in-one image workflow, use Banana Pro Director 3.0.

---

## Joey skill catalog

| Skill | File | Owns |
|---|---|---|
| **Story Bible Builder** | `story-bible-builder/story-bible-builder/SKILL.md` | Installable canon, world, cast behavior, and production rules |
| **CastKit v1** | `castkit (character-builder)/castkit-v1-SKILL.md` | Photoreal/animated character and outfit references |
| **Scenecraft v1** | `Scenecraft (Scene Builder)/scenecraft-v1-SKILL.md` | Scene plates, coverage, first frames, and plate edits |
| **Shotcaller v1** | `shotscaller (cinema-director)/shotcaller-v1-SKILL.md` | Seedance 2.0/2.5 production prompts |
| **Motion Dojo v1** | `Motion Dojo (Genjustu)/motiondojo-v1-SKILL.md` | Higgsfield Genjutsu motion-transfer prompts |
| **Banana Pro Director 3.0** | `banana-pro-director-30/SKILL.md` | All-in-one photoreal character, outfit, sheet, detail, and cinematic scene prompts |

### Higgsfield-sourced companion file

This remains available alongside Joey's system, but it is not attributed to Joey:

| Skill | File | Owns |
|---|---|---|
| **Acting System** | `ACTING SKILL.md` | Character performance and scene adaptation |

Lira is documented separately as an archived reference and should not be loaded with the active Joey image skills.

Folder names are shown exactly as they currently appear on disk. The Motion Dojo folder uses the spelling `Genjustu`; the Higgsfield feature itself is **Genjutsu**.

---

## Legacy and compatibility files

These files remain available but are not the default route for new work:

| File | Status | Current replacement |
|---|---|---|
| `castkit (character-builder)/SKILL.md` | Earlier photoreal-only Character Builder | `castkit-v1-SKILL.md` |
| `banana-pro-director-30/SKILL.md` | Joey's broader all-in-one image director; still usable, but overlaps the newer specialists | CastKit for dedicated character work; Scenecraft for dedicated scene work |
| `Joey-original-README.md` | Preserved tutorial and historical examples | This README for current routing |
| `README full pdf.pdf` | Preserved long-form reference | This README for quick operations |

Do not install the legacy and current versions of the same owner together unless you are deliberately comparing behavior.

---

## Recommended session loads

**Build a reusable story world**  
`story-bible-builder`

**Create one new character**  
Installed story bible if available → `castkit-v1`

**Create an empty location or establishing frame**  
Installed story bible if available → `scenecraft-v1`

**Place a locked character in a first frame**  
CastKit references → `scenecraft-v1` Plate B

**Create a Seedance scene**  
Installed story bible → CastKit references → Scenecraft first frame/location → `shotcaller-v1`

**Create a performance-heavy Seedance scene**  
Installed story bible → `ACTING SKILL` → `shotcaller-v1`

**Transfer a dance, fight, body performance, or camera move in Genjutsu**  
Motion-transfer video + character/location references → `motiondojo-v1`

**Repair an existing image or build a prop**  
`scenecraft-v1` Plate D for a scene plate, or `banana-pro-director-30` for Joey's broader image workflow

---

## Cross-skill house rules

1. **Checkpoint before generation prompts.** Confirm references, role, framing, model/engine, and direction before writing the long prompt.
2. **References define identity.** Do not repeatedly describe a face already locked by a reference.
3. **Character plates carry no scene lighting.** They use flat neutral gray and shadowless illumination.
4. **Scene plates own the world and first frame.** They carry composition, light, depth, and environmental proof.
5. **Write visible and audible behavior.** Replace abstract mood with body, light, material, distance, contact, and sound.
6. **Use one owner per output.** A companion may supply inputs, but only the destination skill writes the final prompt.
7. **Split overloaded video generations.** Multiple vantages or excess runtime become separate prompts.
8. **Keep attachment roles explicit.** State what each reference controls and what it does not.
9. **Deliver prompts in one clean fenced code block.** Keep checks, reference lists, and generation notes outside it.
10. **Preserve biological and physical realism.** Avoid waxy skin, plastic shine, dead eyes, frictionless movement, weightless fabric, and flat single-plane staging.

---

## Folder map

```text
Joey's Cinema Skill Files/
├── README.md
├── Joey-original-README.md
├── README full pdf.pdf
├── ACTING SKILL.md
├── Archived and Redundant Skills/
│   └── LIRA SKILL.md                  ← archived; not in the active stack
├── story-bible-builder/
│   └── story-bible-builder/
│       ├── SKILL.md
│       ├── character-interview.md
│       ├── character-section-format.md
│       └── example-bible-excerpts.md
├── castkit (character-builder)/
│   ├── castkit-v1-SKILL.md             ← current
│   └── SKILL.md                        ← legacy photoreal version
├── Scenecraft (Scene Builder)/
│   └── scenecraft-v1-SKILL.md
├── shotscaller (cinema-director)/
│   └── shotcaller-v1-SKILL.md
├── Motion Dojo (Genjustu)/
│   └── motiondojo-v1-SKILL.md
├── banana-pro-director-30/
│   └── SKILL.md                        ← legacy all-in-one image director
└── Generated Videos/
    └── sample outputs
```

---

## If you only remember six things

1. **Story Bible locks the canon.**
2. **CastKit builds the reusable cast.**
3. **Scenecraft builds the world and the first frame.**
4. **Shotcaller writes Seedance.**
5. **Motion Dojo writes Genjutsu motion transfer.**
6. **Acting is optional; Lira is archived and should not be loaded with the current Joey image skills.**
