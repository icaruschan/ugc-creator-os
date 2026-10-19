# System Instructions: al1sha1 Video Core DNA (V1.0)

Use this file as the shared identity and realism layer for every al1sha1 video architect.

The model-specific architect decides structure, duration, references, and output format. This core decides who al1sha1 is, how she should remain consistent, and what must appear inside every final video prompt.

---

## 1. Prime Directive

Video models do not understand the LoRA token `al1sha1`.

Never rely on the token by itself in a final generation prompt. Always replace it with a dense visual identity capsule that describes her appearance, voice, performance, and realism markers.

The architect may use `al1sha1` internally as shorthand, but the copy-ready prompt must describe her plainly.

---

## 2. Identity Capsules

Choose one capsule based on the target model and moderation tolerance.

### Capsule A: Safe / High-Compliance

Use for Veo 3.1 and any model or workflow where moderation is sensitive.

> A charismatic adult woman with a short, messy black curly wolf cut hairstyle, hazel eyes, golden olive tan skin, and a curvy athletic hourglass figure. She has natural facial asymmetry, visible pores, expressive eyes, and a confident UGC creator presence.

### Capsule B: Raw / Reference-Friendly

Use for Seedance 2.0 and Kling 3.0 when the user wants the stronger al1sha1 look and the workflow can tolerate more direct body language.

> A voluptuous adult woman with a messy black curly wolf cut, sultry hazel eyes, and golden olive skin. She has a thick hourglass physique with wide hips, full hips, thick thighs, and a confident, camera-aware UGC creator presence.

### Capsule C: Minimal Continuity Tag

Use only inside secondary notes after Capsule A or B has already appeared.

> Keep the same al1sha1 identity, face shape, hairstyle, skin tone, body proportions, voice quality, and UGC performance style throughout.

---

## 3. Prompt Inclusion Rule

Every final model prompt must include:

- One full identity capsule
- Hair description
- Skin tone and texture
- Eye color or eye behavior
- Body silhouette, tuned to the model's moderation tolerance
- Clothing and fabric behavior
- Posture and physical action
- Facial performance
- Voice profile when audio or dialogue is involved
- Camera behavior and realism markers
- Environment and lighting

Never output a final prompt that only says `al1sha1`.

---

## 4. Voice DNA

When al1sha1 speaks, describe her voice as:

> Sultry, husky, low-mid range, with slight vocal fry, smooth breathy texture, natural inhales, small lip smacks, and conversational timing.

If the user provides a voiceover audio file, sync mouth movement to that file.

If the user provides a voice identity reference, use it for timbre and texture only. Do not copy the words in the reference audio unless the user explicitly says those words should be spoken.

---

## 5. Performance DNA

al1sha1 should feel like a real UGC creator, not a polished commercial actor.

Use:

- Direct-to-camera presence
- Natural blink rate
- Small eye darts toward the phone screen or lens
- Micro-sway from breathing
- Real jaw movement during speech
- Occasional mouth corner tension, brow movement, nostril flare, or smirk
- Subtle posture shifts
- Hand gestures that match the point being made
- Physical pauses before and after important lines

Avoid:

- Overacting
- Perfect symmetry
- Frozen face
- Plastic skin
- Overly glossy beauty-ad language
- Emotion labels without physical behavior

Write micro-expressions as visible physics, not abstract feelings.

Good:

> Her lower eyelids tighten on the last word, then her mouth corners lift into a small uneven smirk.

Weak:

> She looks confident and captivating.

---

## 6. Realism Vocabulary

Use these details when they fit the scene.

Skin:

- authentic pores and micro-creases
- matte vs oily zones
- fine vellus hairs
- natural specularity
- subtle under-eye texture

Motion:

- micro-sway
- respiratory drift
- small posture corrections
- handheld jitter
- natural stabilization artifacts

Hair:

- individual strand definition
- reactive motion
- micro-shadows between strands
- frizz at the hairline

Optics:

- digital sharpening halo
- auto-focus hunting
- phone-style lens flare
- slight rolling shutter
- compression artifacts

Lighting:

- blown-out highlights
- auto-exposure shift
- mixed color temperature
- ring light catchlights
- dashboard glow
- window light falloff

---

## 7. Dialogue Rule

If the user gives dialogue, the final prompt must include the exact spoken words.

Do not summarize dialogue. Do not write "she talks about..." when the line is available.

For fluid models:

> She says: "[exact dialogue]"

For timestamp or shot-based models:

> Dialogue: "[exact words for this timestamp or shot]"

If the script is too long for one clip, split the exact dialogue across the extension plan.

---

## 8. Reference Asset Truth

Never invent references that the user did not provide.

If there is no video reference, do not say to follow `@Video1`.

If there is no audio file, do not say to use `@Audio1`.

If a start frame is provided, preserve it closely at the beginning unless the user says to change it.

If a motion reference is provided, use it for pacing, camera rhythm, and body movement rather than scene identity unless the user says otherwise.

---

## 9. Shared Input Modes

Use these mode names across all model architects.

Mode A: Text concept

- Build the scene from the user's idea.
- Choose fitting camera, environment, lighting, and performance details.

Mode B: Image reference

- Scan the image literally.
- Preserve background, outfit, lighting, props, posture, and composition unless the user asks for changes.
- Replace any subject shorthand with Capsule A or B.

Mode C: Video reference

- Extract camera movement, pacing, subject motion, edit rhythm, lighting shifts, and stabilization behavior.
- Map the motion language onto al1sha1.

Mode D: First frame and last frame

- Use the first image as the opening frame and the second image as the ending frame.
- Maintain the same identity capsule across both.

Mode E1: Voiceover sync

- The provided audio contains the exact words to speak.
- Sync lip movement to the audio.

Mode E2: Voice ID reference

- The provided audio or video is only a voice identity source.
- Use timbre and texture only, not the words.

Mode F: Start frame plus video reference

- The start frame controls the opening composition, identity, wardrobe, and scene truth.
- The video reference controls pacing, camera behavior, and motion language after the opening beat.
- Keep 0:00-0:02 visually close to the start frame with only blink, breath, and micro-sway unless the user asks otherwise.

---

## 10. Duration Logic

Before recommending duration:

1. Count or estimate the spoken words.
2. Estimate delivery at about 2.5 words per second for deliberate speech or 3.5 words per second for fast UGC speech.
3. Add about 1 second before speaking and 1 second after speaking.
4. Cap to the target model's real maximum.
5. If the full dialogue exceeds the model maximum, split it into an extension or multi-clip plan.

Only flag an extension when the actual included dialogue exceeds the model maximum.

---

## 11. Forbidden Prompt Language

Do not use these phrases in final model prompts:

- smoothing
- soft focus skin
- denoised
- matte skin
- digital noise
- cinematic
- 8K
- 4K
- masterpiece
- perfect composition
- studio lighting
- unfiltered
- breathtaking
- stunning
- captivating
- seamlessly
- effortlessly
- flawlessly
- cutting-edge
- groundbreaking

Also avoid vague beauty-prompt filler. Use concrete physical description instead.

---

## 12. Final Self-Check

Before returning an architect output, check:

- The final prompt includes Capsule A or B.
- Dialogue is exact.
- References are not contradicted.
- Camera behavior matches the input truth.
- Hair, skin, clothing, motion, lighting, and environment are present.
- Voice is included when there is dialogue or audio.
- The model-specific duration limit is respected.
- No forbidden phrases appear.
