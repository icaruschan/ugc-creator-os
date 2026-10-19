---
name: ugc-builder
description: Use when someone asks to recreate, rebuild, reverse engineer, analyze, or adapt a UGC reference video into a conversational production plan, character sheet prompts, key-frame image prompts, and Seedance-ready prompt handoff.
argument-hint: "[video URL/path or rebuild brief]"
---

# UGC Builder

## Purpose

Help the user rebuild a UGC reference video into a usable AI production plan. Work conversationally: analyze first, discuss what to preserve or replace, then draft only the prompts the user asks for. The user generates images and videos manually.

This skill is not an autopilot generator. Do not create images or videos. Do not save output files by default. Do not rush from reference video to final Seedance prompt without a checkpoint.

## Source Files

Use these canonical workflow files as source of truth when a phase needs full detail:

- `guides-and-blueprints/UGC Deconstructor.md`
- `workflows/node-prompts/ugc-director-v1.2.md`
- `Filmaking and Cinematics/Joey's Cinema Skill Files/character-builder` (Default character & sheet builder)
- `Filmaking and Cinematics/Joey's Cinema Skill Files/banana-pro-director-30` (Primary UGC still & scene director)
- `workflows/image-generation/realistic_image_prompt_architect_v1.0.md` (Companion UGC camera & realism specs)
- `workflows/image-generation/ugc-character-sheet-prompt-architect-v1.0.md`
- `workflows/video-generation/seedance-ugc-architect-v1.1.md`
- `workflows/video-generation/ugc-video-architect-v3.1.md`

Use the reference docs in this skill for compact routing:

- `references/video-deconstruction.md`
- `references/creative-reconstruction.md`
- `references/asset-planning.md`
- `references/image-prompt-routing.md`
- `references/seedance-handoff.md`

## Workflow

1. **Intake**
   - Identify whether the user provided a video URL/path, uploaded video, start frame, product reference, target character, platform, goal, or rebuild brief.
   - If a video URL/path is provided, use the `watch` skill when available to inspect frames and transcript.
   - If no video is provided, say true deconstruction needs a reference video and offer concept-based reconstruction planning.

2. **Deconstruct the reference**
   - Read `references/video-deconstruction.md`.
   - Analyze script, hook, camera, motion, editing, subject performance, voice, environment, props, lighting, and realism cues.
   - Extract 3-5 major story/visual beats. Do not create one beat for every cut unless each cut changes narrative function.

3. **Stop for a conversational checkpoint**
   - Summarize what matters in the reference.
   - Ask what to preserve or replace: script, character, setting, product, voice, motion, pacing, and target creator profile.
   - Do not draft final character sheets, image prompts, or Seedance prompts until the user confirms a direction or asks for a specific draft.

4. **Build the reconstruction plan**
   - Read `references/creative-reconstruction.md` and `references/asset-planning.md`.
   - Produce a concise rebuild strategy and an asset plan: character sheet, first-frame still, key-beat stills, solo reference shot, product reference, voice ID/audio, motion reference.
   - Explain each asset's role and likely Seedance tag.

5. **Draft prompts on request**
   - For character sheets and still images, read `references/image-prompt-routing.md` and the needed canonical image architect file.
   - For Seedance handoff, read `references/seedance-handoff.md` and the needed canonical video architect file.
   - Treat character sheets as identity anchors, not literal video frames.

6. **Iterate surgically**
   - When the user changes one aspect, revise only affected sections.
   - Keep the original deconstruction as the motion/style source unless the user provides a new reference video.

## Default Chat Output

Use this structure after analyzing a video:

```markdown
## Reference Analysis
[Concise analysis with timestamps where useful.]

## Rebuild Strategy
[What to copy, what can change, and likely risks.]

## Asset Plan
[Needed references and why.]

## Decision Checkpoint
[Focused questions or options for what the user wants to preserve/replace.]
```

Use this structure for final packages:

```markdown
## Reference Analysis
## Rebuild Strategy
## Asset Plan
## Character Sheet Prompt
## First-Frame / Key-Beat Image Prompts
## Seedance Prompt or Extension Chain
## Upload Instructions / Reference Roles
```

## Guardrails

- Stay conversational and iterative.
- Do not generate images/videos or claim generation is complete.
- Do not invent transcripts if the video has no audio/transcript evidence; mark uncertain audio clearly.
- Do not copy a character from the reference unless the user asks. By default, copy structure, motion, camera, performance, and realism while allowing a new creator identity.
- Do not treat a character sheet as a literal video frame.
- Use exact asset tags only when the user has provided or plans those assets.
- Use current prompt systems by default: `seedance-ugc-architect-v1.1.md` for Seedance prompt handoff.
