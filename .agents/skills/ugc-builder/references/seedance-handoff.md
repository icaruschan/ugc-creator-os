# Seedance Handoff Reference

Use this when turning an approved rebuild plan into copy-ready Seedance UGC video prompts or extension chains.

## Primary Video System

- `workflows/video-generation/seedance-ugc-architect-v1.1.md`
  - **The primary UGC video engine.** Generates copy-ready Seedance 2.0 / 2.5 prompts for organic short-form UGC videos (direct, casual, human, lightly imperfect, natural pacing, and easy for Seedance to follow). Character-flexible for any creator or product.

## Secondary / Companion Systems

- `workflows/video-generation/ugc-video-architect-v3.1.md`
  - Use when a broader pre-production video packaging and director breakdown is needed before final Seedance prompt synthesis.
- `Filmaking and Cinematics/Joey's Cinema Skill Files/cinema-director-v3`
  - Reference for advanced camera physics, 16-slot production spine, acting/dialogue precision, or multi-shot sequences when cinematic precision is requested.

Skip older versions: `seedance-ugc-architect-v1.0.md`.

---

## Core UGC Prompt Formula (from V1.1)

```text
Character + UGC Camera/Shot + Scene + Lighting + Dialogue/Action + Natural Performance + Relevant Realism Cues + Soft Constraints
```

Where **Scene** = `environment + wardrobe + props + real-world situation`.

---

## Generation Modes

1. **Natural Mode (Default)**:
   - For casual UGC flow, talking-head reviews, selfie-vlogs, unboxings, and candid moments.
   - Pacing is described organically without rigid timestamps.
   - Focuses on fluid body language, casual eyelines, breathing room, and believable speech cadence.

2. **Precision Mode (Timestamped)**:
   - Use when precise multi-beat choreography, timed product reveals, or exact spoken beats are required within a 5-15s clip.
   - Format beats clearly: `[00:00-00:03] ... [00:03-00:06] ...`
   - Keeps beats focused: 1-2 major action shifts maximum per 5 seconds.

3. **Top-Lock Extension Mode**:
   - Use when chaining clips or extending a previously generated video.
   - Begin with the locked extension clause:
     ```text
     Seamlessly extend the previously generated video from @Video1. Maintain the same character identity, face, hair, wardrobe, body proportions, camera framing, lighting, voice tonality, lip-sync style, product state, and video quality from the final frame.
     ```

4. **Canva / Dense Action Mode**:
   - Use when heavy prompt instructions risk exceeding Seedance's character budget. Keep descriptions compact, punchy, and focused strictly on visible pixels and audible sound.

---

## Upload Tag Conventions & Roles

State each reference role explicitly in the handoff:

- `@Image1` = Character identity anchor (from Joey's `character-builder` or canonical face lock) or first-frame still.
- `@Image2` = Product reference (locks label typography, bottle/box geometry, and color) or outfit reference.
- `@Video1` = Reference video (controls camera motion, pacing, cadence) OR extension source video.
- `@Audio1` = Voice ID sample (controls vocal timbre/tone; exact dialogue must still be written in the prompt).

*Rule: Character sheets are identity anchors, not literal video frames. The prompt directs what happens in this specific video.*

---

## Physics & Continuity Locks

Include only when drift would break realism:
- Phone/camera stays in the same hand throughout the shot.
- Product label remains crisp, legible, and unmirrored.
- Product does not morph, duplicate, change scale, or switch hands.
- Only the active creator speaks; background individuals remain passive.
- Natural eye contact: glances briefly at screen/product, returns to camera lens.

---

## Prompt Package Template

```markdown
## Seedance UGC Prompt ([Natural Mode | Precision Mode | Extension Mode])
```text
[Copy-ready Seedance prompt following V1.1 formula]
```

## Upload Roles
- @Image1 = [e.g., Character Sheet / Face Lock from Mode 0/4]
- @Image2 = [e.g., Product reference image — clean packaging]
- @Video1 = [e.g., Reference video for motion pacing / or Previous clip for extension]
- @Audio1 = [e.g., Voice tone reference or leave blank if native text-to-speech]

## Generation Notes
- Engine: Seedance 2.0 / 2.5
- Aspect Ratio: 9:16 (vertical mobile UGC)
- Duration: [e.g., 5s, 8s, 10s]
- Dialogue / Audio: [Exact spoken lines or ambient sounds]
- Continuity & Realism Checks: [Key physical locks, natural hand movements, lighting consistency]
```
