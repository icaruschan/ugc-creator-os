# Image Prompt Routing Reference

Use this when drafting character sheets, first-frame stills, solo reference shots, or key-beat image prompts. All routing here focuses on generic creators and photoreal UGC characters.

## Canonical Image Systems

- `Filmaking and Cinematics/Joey's Cinema Skill Files/character-builder` (see `character-builder/SKILL.md`)
  - Default character and character sheet builder. Use for building photoreal characters, face locks (Mode 0), additions (Mode 1), outfit builds (Mode 2), outfit swaps (Mode 3), and multi-angle character sheets (Mode 4).

- `Filmaking and Cinematics/Joey's Cinema Skill Files/banana-pro-director-30` (see `banana-pro-director-30/SKILL.md`)
  - Primary prompt director for UGC stills, key-beats, and scene plates. Provides the lean front-loaded prompt grammar (composition + pose/action + lighting up front), reference delegation (trust references for identity; prompt directs action, camera, and lighting), pre-prompt check discipline, and the photoreal cinema stack (flattering fine-even pores, peach fuzz, subsurface scattering, strand hair physics, atmospheric perspective, optical lens roll-off, 35mm grain, anti-AI closure).

- `workflows/image-generation/realistic_image_prompt_architect_v1.0.md`
  - Companion realism architect for UGC stills. Provides UGC smartphone and handheld camera realities (24-28mm lens physics, auto-exposure, sensor grain), candid environmental proof (fabric weave, wrinkles, micro-glare, real shadows, subtle background clutter), and structured anti-AI guardrails.

- `workflows/image-generation/ugc-character-sheet-prompt-architect-v1.0.md`
  - Secondary / fallback for quick UGC character sheet drafting.

## Routing Rules

- Character sheet / character builder -> Joey's `character-builder` (`Filmaking and Cinematics/Joey's Cinema Skill Files/character-builder`). Default system for face locking, additions, wardrobe builds, and multi-angle reference sheets.
- Generic first-frame / key-beat / scene still -> Synthesize Joey's `banana-pro-director-30` (strongly, for structure, composition front-loading, reference delegation, lighting wrap, atmospheric depth, and cinema stack) with `realistic_image_prompt_architect_v1.0.md` (for UGC smartphone/handheld camera realities, candid physical environment proof, and anti-AI constraints).
- Secondary character sheet fallback -> `workflows/image-generation/ugc-character-sheet-prompt-architect-v1.0.md`.

## Image Prompt Principles (Banana Pro + UGC Realism)

1. **Front-Loaded Composition**: Banana Pro reads the front of the prompt most heavily. Always start with shot type, framing, camera angle, and subject placement, followed immediately by pose, action, and lighting direction.
2. **Reference Delegation (Lean Prompting)**: When character or wardrobe references exist, identify subjects by short, distinguishing visual handles only (e.g., "the woman with dark wavy hair in the green hoodie"). Never re-describe facial bone structure, skin tone, or details already locked in reference images. Trust the references for identity; use the prompt to direct what the character is doing and how the camera frames them.
3. **UGC Camera Reality**: Ground the shot in real phone/camera capture (e.g., smartphone front-camera 24-28mm equivalent, slight handheld framing, natural auto-exposure, mild edge softness, natural sensor grain).
4. **Atmospheric Depth & Light Physics**: Include atmospheric perspective with visible air density/haze between foreground and background (the primary lever against flat AI staging). Light with real physical wrap and anatomical shadow falloff.
5. **Flattering Biological Realism**: Full skin realism is always on (fine natural pore texture, soft peach fuzz at jawline/hairline, warm subsurface scattering, strand-by-strand hair physics), but held to a flattering ceiling (fine and even, never clinical macro-pores, blemishes, or harsh marks).
6. **Environmental Proof**: Ground the scene with physical evidence (fabric weave, small wrinkles, real screen glare, contact shadows, subtle lived-in clutter).
7. **Anti-AI Guardrails**: Close with direct anti-AI constraints (no waxy skin, no beauty-filter smoothing, no plastic shine, no digital over-sharpening, photographed not generated).

## Pre-Prompt Check

Before drafting complex prompts, run a concise bulleted check:
- **References attached**: [List uploaded refs or none]
- **Character**: [Distinguishing handle or locked identity]
- **Outfit / styling**: [Key wardrobe & accessories]
- **Setting / environment**: [Scene location & lighting]
- **Framing / camera**: [Shot type, angle, camera style]

Wait for user alignment, then output the copy-ready prompt.
