# Image Generation Workflows

This directory contains instructions and frameworks to generate consistent static images, character assets, and realistic scenes.

## Files

### al1sha1 architects (A/B versions)

Keep both old and new while testing. Do not overwrite the baseline until the new version wins on your side-by-side gens.

| Role | Baseline | Previous test | Current test | What the current test changes |
|---|---|---|---|---|
| JSON architect | `al1sha1_JSON_Architect_V10.4.md` | `al1sha1_JSON_Architect_V10.6.md` | `al1sha1_JSON_Architect_V10.7.md` | Literal preserve/replace/exclude contract; generator-safe direct JSON; viewer-relative pose mapping; source-vs-output quality separation; reference-coverage audit |
| GPT Image 2 architect | `al1sha1-gpt-image-2-architect-v1.0.md` | `al1sha1-gpt-image-2-architect-v1.1.md` | — | Same five-budget + injection doctrine for single-JSON + implicit/explicit/edit prompts |

> The GPT Image 2 row still uses a two-version pair, so its Current test column is intentionally not applicable. Its active A/B test remains v1.0 versus v1.1.

**Design note for V10.6 / GPT Image v1.1:**  
Identity lock, morphology, realism libraries, and heavy negatives are **kept**. They are no longer all dumped into the final prompt every time.

```text
Internal control library = detailed and complete
Final generation prompt  = selectively budgeted
Recovery pass            = stronger controls when needed
```

Final prompts get:
1. early natural-phone / soft-video look sentence  
2. **mode-matched** anti-plastic skin floor (pores not forced on soft video stills)  
3. five budgets: Capture / Skin / Identity / Morphology / Constraints  
4. per-field injection policy (`usage` / `inject_when` / `prompt_budget`)  
5. morphology scalars internal-only (NL translation when body_visible)  
6. jewelry non-invention hard invariant  
7. escalation paths if skin goes plastic or identity drifts  

**Design note for V10.7:**  
V10.7 analyzes references privately, then outputs standalone text-to-image JSON geared toward vertical short-form social-media UGC. It treats every output field as generator-visible, keeps scene fidelity full-strength in both Implicit and Explicit variants, and changes only the reference person's identity to al1sha1. Paste-ready JSON begins with `prompt_type` and `creative_context`; it excludes architect/version metadata, routing labels, reference-process language, analysis contracts, audit fields, morphology scalars, and declarative `internal_control_only` fields.

### Other files

- **`al1sha1-character-sheet-prompt-sets.md`**: Preset prompt recipes to generate visual character sheets, facial turnarounds, and expressions for al1sha1.
- **`ugc-character-sheet-prompt-architect-v1.0.md`**: Standalone system prompt that turns a character idea or image reference into a copy-ready UGC-style character reference sheet prompt.
- **`al1sha1-seedream-to-nano-banana-correction-v1.0.md`**: Correction instructions used to resolve physical anomalies and morphology mismatches between the Seedream and Nanabanana image generators.
- **`realistic_image_prompt_architect_v1.0.md`**: A universal prompt-generating framework designed to help LLMs write image prompts that look like real photography (by specifying focal length, sensor grain, and exposure behavior rather than quality buzzwords).

### Suggested A/B test

1. Same reference image / same text brief  
2. Generate with the known-good direct reconstruction prompt or baseline architect  
3. Generate with V10.7 using the same engine and reference  
4. Score pose/hand geometry, crop/perspective, wardrobe construction, prop interaction, room layout, lighting, UGC realism, and al1sha1 identity  
5. Reject a result that preserves identity but loses the reference scene  
6. Iterate only the failed category while keeping the preserve/replace contract fixed
