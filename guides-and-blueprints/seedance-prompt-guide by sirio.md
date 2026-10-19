The Complete Guide

# Seedance 2.0  Prompt Engineering

Everything you need to write prompts that produce professional results. Built from official documentation, tested techniques, and hundreds of real examples.

[Try Seedance 2.0 on Enhancor — 65% Off](https://app.enhancor.ai/video-generator)

### Contents

- [1\. The Core Formula](https://seedance-prompt-guide.sirioberati.com/#formula)
- [2\. The Rules That Matter](https://seedance-prompt-guide.sirioberati.com/#rules)
- [3\. Camera Movements](https://seedance-prompt-guide.sirioberati.com/#camera)
- [4\. Shot Types & Pairing](https://seedance-prompt-guide.sirioberati.com/#shots)
- [5\. Timeline Prompting](https://seedance-prompt-guide.sirioberati.com/#timeline)
- [6\. Lighting (Biggest Impact)](https://seedance-prompt-guide.sirioberati.com/#lighting)
- [7\. Style & Mood Keywords](https://seedance-prompt-guide.sirioberati.com/#style)
- [8\. Pacing & Motion](https://seedance-prompt-guide.sirioberati.com/#pacing)
- [9\. Audio Design](https://seedance-prompt-guide.sirioberati.com/#audio)
- [10\. Quality Suffix](https://seedance-prompt-guide.sirioberati.com/#quality)
- [11\. Constraints](https://seedance-prompt-guide.sirioberati.com/#constraints)
- [12\. Reference System (@Tags)](https://seedance-prompt-guide.sirioberati.com/#refs)
- [13\. Subject Descriptions](https://seedance-prompt-guide.sirioberati.com/#subjects)
- [14\. The Separation Rule](https://seedance-prompt-guide.sirioberati.com/#separation)
- [15\. Dangerous Keywords](https://seedance-prompt-guide.sirioberati.com/#dangerous)
- [16\. Full Prompt Examples](https://seedance-prompt-guide.sirioberati.com/#examples)
- [17\. Troubleshooting](https://seedance-prompt-guide.sirioberati.com/#troubleshooting)
- [18\. Iteration Strategy](https://seedance-prompt-guide.sirioberati.com/#iteration)
- [19\. Platform-Specific Tips](https://seedance-prompt-guide.sirioberati.com/#platforms)
- [20\. Input Specifications](https://seedance-prompt-guide.sirioberati.com/#specs)

## 1\. The Core Formula

Every Seedance 2.0 prompt should follow this structure. The model reads left to right and gives the strongest weight to whatever comes first. Put your most important instruction at the beginning.

Subject \+ Action \+ Scene \+ Camera \+ Style \+ Constraints

1

#### Subject

Who or what is in the frame. Be specific about age, hair, clothing, expression, skin tone. Use the SAME noun throughout the entire prompt. If you say "a man" at the start, don't switch to "the detective" or "he" later.

2

#### Action

One clear verb in present tense per shot. "She walks slowly toward the window" — not "she walks, turns around, picks up the cup, looks at it, and drinks." Multiple verbs in one shot = blended mess.

3

#### Scene / Environment

Where it takes place, with specific details. "A modern kitchen with marble countertops, morning light through floor-to-ceiling windows, a glass of water on the counter" — not just "a kitchen."

4

#### Camera (ONE instruction only)

This is the most common mistake. Use exactly ONE camera movement per shot. "Slow dolly push-in" or "fixed camera" — never "dolly in while panning left and tilting up." Multiple camera moves = jitter and incoherent output.

5

#### Style

A single strong visual anchor works better than ten adjectives. "35mm film, Kodak color palette" or "Apple keynote style" or "Wes Anderson symmetry." These give the model a clear target. "Beautiful, amazing, cinematic, epic" gives it nothing.

6

#### Constraints

What to avoid. Seedance does NOT support traditional negative prompts — use positive constraint statements instead. "Avoid jitter. Avoid bent limbs. Face stable, no deformation." Add these to EVERY prompt.

**Word count:** 60-100 words is the sweet spot. Under 30 lacks information. Over 200 and the model starts ignoring details. The first 2-3 instructions are followed best — after about 8 requirements, only 4-5 will land.

## 2\. The Rules That Matter

These are the rules that separate prompts that work from prompts that produce garbage. Internalize these before you write a single word.

#### Do This

- One shot, one verb, one camera move
- Use specific film terms ("slow dolly in, 1-2 feet")
- Keep the subject noun identical throughout
- Put the most important instructions first
- Keep prompts to 60-100 words
- Include constraint words in every single prompt
- Append the quality suffix to everything
- Start with 5-second test clips before going longer
- Generate 2-4 variants and compare
- Change only ONE variable when iterating
- Use gentle motion words: slow, smooth, natural, gentle
- Limit scenes to 1-2 characters maximum
- Describe lighting specifically (it has the biggest impact)
- Reference directors/brands for instant style ("Fincher framing")
- Separate subject motion from camera motion

#### Never Do This

- Multiple camera movements in one shot
- Vague adjectives ("beautiful", "epic", "amazing", "cool")
- Technical photography specs (f/2.8, ISO 800, 85mm)
- Fast + complex + intricate all at once
- Switch subject nouns mid-prompt
- Use traditional negative prompts (not supported)
- Skip constraint statements
- Reference long videos (trim to key segments first)
- Change multiple parameters when debugging
- More than 2 characters (consistency breaks down)
- Overload timestamps with multiple actions
- Say "multiple angles" (causes chaos)
- Mix subject movement and camera movement in one instruction
- Use "lots of movement" (instant jitter)
- Write prompts over 200 words

**Priority rule:** The model follows the first 2-3 instructions reliably. After about 8 specific requirements, it hits roughly 4-5. Put your most critical direction first. If you need the lighting to be warm, say it before anything else.

## 3\. Camera Movements

Use exactly ONE per shot. Always pair with a speed modifier (`slow`, `medium`, `fast`) and ideally a distance (`1-2 feet`). The modifier pattern is: speed + movement + distance.

| Movement | Keywords | What It Does | Best For |
| --- | --- | --- | --- |
| **Push in** | `slow dolly-in`, `push in`, `slow push forward 1-2 feet` | Camera moves toward subject | Building tension, intimacy, emphasis on details |
| **Pull back** | `dolly-out`, `pull back`, `slow pull out` | Camera retreats to reveal wider scene | Environmental reveals, showing scale, endings |
| **Pan** | `gentle pan left`, `pan right`, `slow pan` | Camera rotates horizontally on its axis | Scanning a scene, following horizontal action |
| **Tilt** | `tilt up`, `tilt down`, `slow tilt up from ground` | Camera rotates vertically on its axis | Revealing tall subjects, establishing shots |
| **Tracking** | `tracking shot`, `track left/right`, `lateral tracking` | Camera moves sideways alongside subject | Following a walking/running subject, action scenes |
| **Orbit** | `orbit`, `arc shot`, `360 orbit`, `circle halfway` | Camera circles around the subject | Product showcase, portrait emphasis, hero moments |
| **Crane** | `crane up`, `crane down`, `jib up` | Camera rises or descends on vertical axis | Grand reveals, establishing shots, transitions |
| **Aerial** | `aerial sweep`, `drone shot`, `bird's eye view` | High-altitude perspective looking down | Landscapes, cityscapes, showing geographic scale |
| **Handheld** | `handheld`, `handheld slight shake`, `organic handheld` | Subtle natural camera shake | Documentary realism, urgency, intimate moments |
| **Fixed** | `fixed camera`, `static shot`, `locked off`, `tripod stable` | Camera does not move at all | Letting action carry the scene, contemplation, products |
| **Steadicam** | `steadicam`, `gimbal`, `smooth stabilized` | Polished, gliding motion following subject | Walk-and-talk scenes, interior tours, polished ads |
| **Rack focus** | `rack focus`, `shift focus foreground to background` | Focus shifts between planes | Drawing attention, reveals, transitions between subjects |
| **Dolly zoom** | `dolly zoom`, `vertigo effect` | Camera moves while zooming opposite direction | Disorientation, dramatic realization moments |
| **Whip pan** | `whip pan`, `swift horizontal pan` | Extremely fast horizontal camera movement | Scene transitions, urgency, comedic timing |

**The #1 mistake:** Using multiple camera movements in one shot. "Dolly in while panning left and tilting up" will produce jittery garbage. Pick ONE. If you need a different angle, make it a new timestamp beat.

## 4\. Shot Types & Camera Pairing

Each shot type has camera movements that work well with it and ones that feel unnatural. Match them correctly.

| Shot Type | Description | Best Camera Pairing | Avoid |
| --- | --- | --- | --- |
| **Extreme close-up (ECU)** | Fills frame with one detail — eyes, lips, product label, texture | Fixed camera, micro push-in | Panning (feels disorienting at this distance) |
| **Close-up (CU)** | Face fills most of frame, shows emotion | Fixed, micro push-in, rack focus | Fast tracking, orbit |
| **Medium shot (MS)** | Waist up, shows body language and environment | Handheld (intimate), gimbal (polished) | Aerial, extreme movements |
| **Medium wide (MW)** | Knees up, shows more environment context | Tracking, slow pan, steadicam | Extreme close movements |
| **Wide shot (WS)** | Full body + environment, establishing context | Slow push-in, static, crane | Handheld (too shaky for wide framing) |
| **Extreme wide (EWS)** | Landscape-dominant, subject is small in frame | Aerial sweep, static, slow pan | Dolly (too subtle to read at this scale) |
| **Over-the-shoulder (OTS)** | Looking over one person's shoulder at another | Fixed, subtle push-in | Orbit, tracking |
| **Low angle** | Camera below subject looking up, creates power | Fixed, slow tilt up | Handheld (unstable at low angles) |
| **High angle** | Camera above subject looking down, creates vulnerability | Fixed, slow crane down | Tracking (perspective gets confusing) |
| **Dutch angle** | Camera tilted on its axis, creates unease | Fixed, slow push-in | Multiple movements (amplifies disorientation too much) |

## 5\. Timeline Prompting

Timeline prompting is the technique that separates random clips from actual video sequences. You mark what should happen at each point in time using bracket timestamps. Each timestamp represents one clear beat — establish, develop, or land.

### Timestamp Format

Use bracket notation with second markers. Keep each beat to **2-3 sentences, 50-75 words maximum**.

```
[0s] First beat — establishment. Set the scene, introduce the subject.
[3s] Second beat — development. Action begins, camera moves.
[6s] Third beat — shift. Something changes, new angle or emotion.
[8s] Fourth beat — resolution. Final hold, reveal, or exit.
```

### Beat Distribution by Duration

| Video Length | Number of Beats | Timestamp Placement |
| --- | --- | --- |
| 4-5 seconds | 2-3 beats | `[0s]`, `[2s]`, `[4s]` |
| 7 seconds | 3-4 beats | `[0s]`, `[3s]`, `[5s]` |
| 10 seconds | 4 beats | `[0s]`, `[3s]`, `[6s]`, `[8s]` |
| 15 seconds | 5-6 beats | `[0s]`, `[3s]`, `[5s]`, `[8s]`, `[11s]`, `[13s]` |

### What Each Beat Must Contain

1. **Shot type** — Wide, Medium, Close-up, etc.
2. **Subject action** — One verb describing what happens
3. **Camera movement** — One instruction (or "fixed camera")
4. **One atmospheric detail** — Lighting, sound, texture

### Transition Phrases Between Beats

These help the model understand shot changes:

- `Cut to:` — hard cut to a new angle
- `Slow push in begins` — camera starts moving
- `Camera begins tracking right` — lateral motion starts
- `Rack focus from background to subject` — focus shift
- `Hold.` — camera stops, moment lingers

**Overloaded beats:** Stuffing too much into one timestamp is the #1 timeline mistake. "He walks in, looks around, picks up the phone, dials, sits down, crosses his legs" at one timestamp = blended mess. One action per beat.

### Global Style Line

After your timeline beats, add one closing line that sets the overall aesthetic. This acts as a style anchor for the entire video:

```
Cinematic 4K, 35mm film grain, shallow depth of field, warm color grade. Avoid jitter, bent limbs, identity drift.
```

## 6\. Lighting (Biggest Impact)

Lighting has the single biggest impact on output quality. One specific lighting line outperforms ten generic adjectives. Always describe it.

| Lighting Type | Keywords | Mood / Feel | Best For |
| --- | --- | --- | --- |
| **Golden hour** | `warm golden hour sunlight` | Warm, romantic, dreamy | Lifestyle, romance, product beauty shots |
| **Blue hour** | `blue twilight, cool tones` | Melancholy, calm, mysterious | Thriller, emotional scenes, night establishing |
| **Natural window** | `soft natural window light from the right` | Realistic, casual, authentic | UGC, interior scenes, morning routines |
| **Studio soft box** | `clean studio lighting, soft box from left` | Polished, controlled, professional | Product ads, portraits, talking heads |
| **Candlelight** | `warm candlelight, flickering, low key` | Intimate, romantic, warm | Dinner scenes, romance, luxury |
| **Rim light** | `hard rim light` | Dramatic, separating subject from background | Hero shots, dramatic reveals, silhouettes |
| **Backlit** | `backlit subject, silhouette` | Mystery, drama, high contrast | Character introductions, noir, fashion |
| **Rembrandt** | `Rembrandt lighting` | Classic portrait, triangle shadow on cheek | Portraits, interview setups, dramatic close-ups |
| **Neon** | `neon reflections on wet pavement` | Urban, cyberpunk, energetic | Night city, sci-fi, club scenes |
| **Volumetric** | `volumetric light, god rays through fog` | Epic, atmospheric, cinematic | Forest scenes, churches, abandoned spaces |
| **Overcast** | `overcast diffused light, no harsh shadows` | Even, neutral, documentary | Outdoor scenes needing consistent lighting |
| **Chiaroscuro** | `hard chiaroscuro, deep shadows, high contrast` | Dramatic, noir, intense | Thriller, horror, dramatic portraits |
| **Practical** | `practical tungsten lighting, desk lamp only` | Realistic, grounded, intimate | Home interiors, late night scenes, realism |

**Temperature modifier:** Adding `color temperature: warm` or `color temperature: cool` gives the model strong overall color direction with just three words.

## 7\. Style & Mood Keywords

A single strong visual reference ("Wes Anderson symmetry") works better than a stack of vague adjectives ("beautiful cinematic epic amazing"). Anchor your style to something the model can actually target.

### By Genre

| Genre | Keywords That Work |
| --- | --- |
| Cinematic / Film | `cinematic texture, film grain, 35mm, anamorphic lens flare, Kodak color palette` |
| Premium / Commercial | `minimalist clean, premium texture, studio photography, commercial polish` |
| Film Noir | `film noir, chiaroscuro, high contrast, deep shadows, black and white` |
| Sci-Fi / Cyberpunk | `cyberpunk, neon, dark premium, holographic, retro-futuristic` |
| Lifestyle / Vlog | `healing fresh, natural, authentic, soft focus, warm tones` |
| Dreamy / Ethereal | `dreamy soft light, ethereal, pastel, soft focus, lens flare` |
| Vintage | `retro film stock, analog, VHS grain, faded colors, 1970s aesthetic` |
| Documentary | `documentary style, naturalistic, observational, handheld, no staging` |
| Fashion / Editorial | `Vogue editorial, high fashion, dramatic pose, striking lighting` |
| Horror | `unsettling, slow dread, desaturated, cold blue undertones` |

### Color Grade Keywords

| Grade | Keywords | Feel |
| --- | --- | --- |
| Teal and orange | `teal and orange color grade` | Hollywood blockbuster standard |
| Bleach bypass | `bleach bypass, desaturated, gritty` | Raw, intense, war film |
| Warm shadows / cool highlights | `warm shadows with cool highlights` | Balanced cinematic look |
| Desaturated cold | `desaturated with cold blue tones` | Thriller, dystopian |
| High saturation warm | `high saturation, warm tones, vibrant` | Lifestyle, summer, energy |
| Monochrome | `monochrome, black and white, silver tones` | Art film, timeless, dramatic |

### Director / Brand Style Anchors

These are extremely effective. The model understands these references and will match the aesthetic:

- `Wes Anderson symmetry` — centered framing, pastel colors, whimsical
- `Fincher-level precision` — dark, controlled, every frame intentional
- `Apple keynote style` — clean, minimal, premium product focus
- `Euphoria color grade` — neon, saturated, youthful, dramatic
- `Terrence Malick` — golden hour, nature, poetic, magic hour
- `Roger Deakins lighting` — masterful natural light, precise shadows

## 8\. Pacing & Motion

The speed words you use dramatically affect output quality. Fast = chaos. Slow = control.

| Speed Tier | Keywords | Risk Level | When to Use |
| --- | --- | --- | --- |
| Ultra slow | `imperceptible`, `barely moving` | Safest | Macro shots, product close-ups, atmospheric |
| Slow | `slow`, `gentle`, `gradual`, `smooth` | Safe | Most scenes, recommended default |
| Medium | `controlled`, `steady`, `natural pace` | Moderate | Walking scenes, conversation, casual movement |
| Fast | `dynamic`, `swift`, `rapid` | High risk | Use sparingly. Only ONE element should be fast. Never fast camera + fast action together. |

### Motion Quality Words

These describe HOW something moves, not how fast:

- `silky smooth` — premium, polished feel
- `organic` — natural, human-like movement
- `deliberate` — intentional, purposeful motion
- `floating` — weightless, ethereal movement
- `mechanical` — precise, robotic, inhuman

### Atmospheric Motion

These add depth and life to static scenes:

- `steam rising slowly`, `dust particles in light`, `fog drifting`
- `rain hitting window`, `leaves falling`, `hair blown by breeze`
- `candle flame flickering`, `water rippling`, `heat haze`

## 9\. Audio Design

Seedance 2.0 generates synchronized audio. You can describe the sound environment and reference uploaded audio files.

| Audio Type | Keywords | Effect |
| --- | --- | --- |
| Room tone | `reverb`, `echoing` | Large-space resonance (cathedral, parking garage) |
| Muffled | `muffled`, `behind glass` | Enclosed, underwater, distorted |
| Impact | `metallic clink`, `glass shatter` | Collision, breakage, contact sounds |
| Texture | `crunchy`, `gravel`, `fabric rustle` | Footsteps, clothing, surface interaction |
| Ambient | `crackling fire`, `rain on window`, `distant traffic` | Environmental atmosphere |
| Tone | `high-pitched`, `deep rumble`, `sharp` | Specific sound character |
| Digital | `digital screech`, `glitch artifacts`, `static buzz` | Tech malfunction, sci-fi, horror |
| Silence | `complete silence`, `all sound cuts` | Dramatic pause, tension, reveal moment |

### Audio References

Upload audio files and reference them:

- `@audio1 as background music` — uses the audio as soundtrack
- `Use @audio1 as voice style reference` — matches tone/energy, doesn't play the audio
- `Lip-sync to @audio1` — character mouths match the audio track

## 10\. Quality Suffix

Append this to the end of **every single prompt**. It consistently improves output quality across all types of content.

```
4K, Ultra HD, rich details, sharp clarity, cinematic texture, natural colors, soft lighting, no blur, no ghosting, no flickering, stable picture.
```

**Copy-paste this.** It works. Don't modify it. Don't leave it out. It's the cheapest quality improvement you can make.

## 11\. Constraints

Seedance 2.0 does NOT support traditional negative prompts. You must use positive constraint statements instead. Include at least the standard set in every prompt.

### Standard Constraints (use always)

```
Avoid jitter. Avoid bent limbs. Face stable, no deformation. Natural smooth movements. Stable picture.
```

### Situation-Specific Constraints

| Scenario | Add This Constraint |
| --- | --- |
| Any video | `Avoid jitter. Stable picture.` |
| Videos with people | `Avoid bent limbs. Face stable without deformation. Normal human structure.` |
| Videos over 10 seconds | `Avoid temporal flicker. Maintain consistency throughout.` |
| Multi-shot / timeline | `Avoid identity drift. Consistent appearance across all beats.` |
| No text overlays | `Generate video without subtitles or text overlays.` |
| Product shots | `Logo sharp, no warping, no distortion on product surface.` |
| Walking / running | `Natural gait, feet touching ground, no floating.` |

## 12\. Reference System (@Tags)

Upload up to 9 images + 3 videos (15s total) + 3 audio clips. Reference them in your prompt with @ tags. This is one of Seedance's most powerful features — it dramatically improves consistency and control.

| Use Case | Syntax | What It Does |
| --- | --- | --- |
| Character reference | `The woman in @image1 as the lead character` | Locks in appearance, face, clothing |
| First frame | `@image1 as the first frame` | Video starts from this exact composition |
| Product + Subject | `Product in @image1, subject in @image2` | Assigns roles to different images |
| Mood / style | `Match the mood and color palette of @image3` | Visual style reference |
| Camera replication | `Replicate the camera movement from @video1` | Copies movement patterns |
| Action mimicry | `Mimic the actions from @video1` | Copies physical movements |
| Background music | `@audio1 as background music` | Uses audio as soundtrack |
| Voice reference | `Use @audio1 as voice style reference` | Matches vocal tone/energy |
| Lip sync | `Lip-sync to @audio1` | Character mouths match audio |
| Video extension | `Extend @video1 by 5 seconds` | Continues existing footage |

**Character consistency tip:** Upload a reference image and use `@image1 as the character reference` in your prompt. Then describe the character identically in every beat. Don't switch between "a man", "the detective", "him" — use the exact same noun.

## 13\. Subject Descriptions

Vague subject descriptions produce vague results. Specific details give the model something concrete to render. Here's the difference:

Weak

"A businesswoman"

Strong

"A woman in her early 30s, dark navy blazer, dark hair in a loose bun, serious expression, carrying a briefcase"

Weak

"A perfume bottle"

Strong

"A glass perfume bottle with a gold cap, amber-colored liquid, clean white background, professional product photography lighting"

Weak

"An alley at night"

Strong

"A narrow cobblestone alleyway in an old European city, stone walls with climbing ivy, warm evening light from a small window above, wet pavement reflecting light"

## 14\. The Separation Rule

This is critical and widely misunderstood. Subject movement and camera movement must be described as separate, independent instructions. Mixing them causes the model to blend both into one confused motion.

Wrong

"Spinning camera around a dancing person"

Right

"The dancer spins slowly in the center of the room. Camera holds fixed framing."

Wrong

"Camera follows him running through the forest while zooming in"

Right

"A man runs through a dense forest, branches brushing past him. Tracking shot following from the side."

## 15\. Dangerous Keywords

These words seem harmless but consistently produce poor results. Avoid them entirely or replace with specific alternatives.

| Dangerous Word | Why It Fails | Replace With |
| --- | --- | --- |
| `fast` (alone) | Creates total chaos — model speeds up everything simultaneously | Make only ONE element fast. "Fast subject movement, slow camera." |
| `cinematic` (alone) | Too vague, means nothing specific to the model | `cinematic film tone, 35mm, warm shadows` |
| `epic` | Model doesn't understand this concept | Describe the specific visual you want — wide shot, sweeping crane, dramatic lighting |
| `beautiful` | Provides zero actionable guidance | Describe the specific beauty — lighting, composition, colors |
| `amazing` | No practical meaning | What specifically is amazing about it? The lighting? The movement? Describe that. |
| `lots of movement` | Instant jitter, everything moves at once | Describe one specific motion with a speed modifier |
| `multiple angles` | Creates chaotic, unusable output | `single tracking shot` — use timeline beats for different angles |
| `realistic` (alone) | Too broad | `photorealistic, natural skin texture, practical lighting` |

## 16\. Full Prompt Examples

Real prompts you can use as starting points. Each follows the formula, stays under 100 words for simple prompts, and uses specific terminology.

### Simple: Product Beauty Shot

```
Matte black luxury watch on a velvet stand. Smooth gimbal orbit right to left, waist height. Soft studio lighting, cool-toned, crisp reflections on brushed metal surface. High-end product photography, clean background. Logo sharp, no warping, tripod-stable. 4K, Ultra HD, rich details, cinematic texture, no blur, stable picture.
```

41 words. One camera move (orbit). One subject. One lighting direction. Constraints included.

### Simple: Lifestyle Scene

```
A woman in a white linen dress walking slowly through a sunlit lavender field. Golden hour lighting from behind. Slow tracking shot following from the right. Shallow depth of field, warm color grade, 35mm film grain. Avoid jitter, face stable. 4K, rich details, sharp clarity, stable picture.
```

48 words. Subject + Action + Scene + Camera + Style + Constraints. Clean and specific.

### Simple: UGC Product Review

```
A woman in casual clothes standing in a bright modern kitchen, holding a green supplement pouch toward camera. She smiles and speaks naturally. Medium shot, slow dolly push-in. Natural window light from the left, iPhone selfie style, authentic energy. Face stable, no deformation. 4K, sharp clarity, stable picture.
```

50 words. UGC feel achieved through "iPhone style" and "authentic energy" — not by being vague.

### Simple: Film Noir

```
A woman in a red dress walking confidently down a rainy city street at night. Neon signs reflect in wet pavement puddles. Tracking shot following from behind. Film noir, harsh chiaroscuro, deep shadows. Maintain face consistency. 4K, cinematic texture, no jitter, stable picture.
```

44 words. The style is carried by "film noir, chiaroscuro" — two words that do more than twenty adjectives.

### Timeline: Thriller Character Reveal (10s)

```
A figure in a long dark coat on an empty rain-slicked city street at night. High contrast, neon reflections in puddles. 35mm film grain, desaturated cold blue tones, anamorphic lens flare from streetlights. Avoid jitter, identity drift.

[0s] Wide shot. Figure stands at the end of the street. Static camera, framed from behind. Neon signs reflect in puddles.

[3s] Slow dolly forward begins. Closing in on the figure from behind. Rain in foreground, shallow depth of field, bokeh streetlights.

[6s] Medium shot. Figure turns head slightly — profile barely visible. Street light catches jaw. Tension holds.

[8s] Rack focus. Background city blur sharpens briefly, then returns to subject. Hold.
```

112 words total. Style block up front. One camera move per beat. Each beat is 2 sentences.

### Timeline: Product Commercial (10s)

```
Glass bottle on marble surface. Backlit, product in sharp focus, background completely blurred. Clean, minimal. Commercial photography aesthetic, 4K, no film grain, clinical but warm. Color grade: slightly warm whites, deep clean shadows. Avoid jitter.

[0s] Extreme close-up. Product centered, backlit. Cool clean lighting. Fixed camera.

[2s] Slow pull back. Framing widens to reveal full bottle and a single green branch beside it. Precise, no handheld shake.

[5s] Arc shot begins right to left. Camera slowly orbits product at waist height. Light catches glass at different angles.

[8s] Camera settles into medium shot. Static. Product centered. Hold.
```

98 words. Perfect product ad structure: detail → context → orbit showcase → hold.

### Timeline: Cinematic Restaurant Scene (15s)

```
Man in dark suit and woman in black dress at candlelit restaurant. Warm amber lighting, white linen, crystal glassware, deep bokeh. 35mm film, shallow depth of field. Avoid jitter, bent limbs, identity drift.

[0s] Extreme close-up on the man's eyes. Candlelight reflected. Fixed camera. He speaks quietly: "You're different from anyone I've ever met."

[3s] Slow crane pull-back reveals the full table. Two people, candles, wine glasses. She smiles. Warm golden light.

[5s] Medium two-shot. He leans across the table toward her ear. Slow dolly push-in to tight profile.

[8s] Close-up on her face. Her expression freezes. Head jerks sharply. Digital artifacts across her skin. Eyes flash white.

[11s] Medium wide shot. He sits back. Looks at camera. Small smirk. Picks up wine glass. Sips.

[13s] She freezes completely. Eyes open glowing blue. Head rotates slowly toward camera. Blue light fills frame.
```

148 words. 6 beats across 15 seconds. Each beat has: shot type, action, camera, one detail.

## 17\. Troubleshooting

Common problems and exactly how to fix them. When debugging, change only ONE variable at a time so you know what actually made the difference.

| Problem | Root Cause | Fix |
| --- | --- | --- |
| Video is completely static | No motion described | Add one specific movement: "steam rising slowly from a cup, subtle camera drift right" |
| Jittering, shaky output | Multiple camera moves or "fast" keyword | Use ONE camera instruction. Add "avoid jitter". Replace "fast" with "controlled". |
| Character looks different across beats | Inconsistent subject description or no reference image | Use @image reference + identical description in every beat. Same noun throughout. |
| Flat, muddy lighting | No lighting direction in prompt | Add one specific light source: "soft side lighting from the left, warm tone" |
| Wrong composition, correct action | Shot size not specified | Add shot type: "Close-up", "Wide shot", "Medium shot". Keep action the same. |
| Style/color drift | Too many competing style words | Replace with one strong visual anchor: "35mm Kodak film" instead of five adjectives. |
| Bent or extra limbs | Complex character poses without constraints | Add "avoid bent limbs, normal human structure". Simplify the pose. |
| Chaotic multi-angle output | "Multiple angles" in prompt | Replace with "single tracking shot". Use timeline beats for angle changes. |
| Subject doesn't match description | Too abstract or conflicting language | Use concrete details: "white cylindrical object with blue LED ring" not "futuristic gadget" |
| Model ignoring half the instructions | Prompt too long (over 200 words) | Cut to under 100 words. Front-load the 3 most important instructions. |
| Text/subtitles appearing | Model generating text overlays | Add "generate video without subtitles or text overlays" |
| Temporal flicker (long videos) | Consistency breaks over time | Add "avoid temporal flicker". Consider generating shorter clips and stitching. |

## 18\. Iteration Strategy

Prompt engineering is iterative. Don't expect perfection on the first try. Follow this process to converge on great results efficiently.

### The Process

1. **Start short** — 5-second test clip with your core concept. Validate direction before spending credits on 15-second renders.
2. **Generate 2-4 variants** — same prompt, let the model explore different interpretations. Pick the best one.
3. **Change ONE variable** — if the lighting is wrong, fix ONLY the lighting. If the camera is wrong, fix ONLY the camera. Changing multiple things makes it impossible to know what helped.
4. **Front-load what matters** — if the model keeps getting the lighting wrong, move the lighting instruction to the very first line.
5. **Extend when confident** — once a 5s clip looks right, extend to 10s or 15s with the same prompt structure.

### Credit Efficiency Tips

- Tight close-ups produce more consistent output than complex wide shots
- Reuse successful lighting/style phrases across generations
- 4-5 second clips often outperform stretched 10-second versions
- Shorter videos with structured prompts beat longer vague ones every time

## 19\. Platform-Specific Tips

| Platform | Aspect Ratio | Add to Prompt | Tips |
| --- | --- | --- | --- |
| TikTok | 9:16 | `vertical format, 9:16` | Hook in first 2 seconds. Close-ups and medium shots work best. High energy. |
| Instagram Reels | 9:16 | `vertical format, 9:16` | Slightly more polished than TikTok. Can be slower paced. Strong visuals. |
| YouTube Shorts | 9:16 | `vertical format, 9:16` | Longer hooks OK (3-4 seconds). Can be more informational. |
| YouTube | 16:9 | `cinematic widescreen, 16:9` | Default landscape. Wide shots and cinematic framing shine here. |
| Instagram Feed | 1:1 or 4:5 | `square format, 1:1` | Centered compositions. Product in frame center. Clean backgrounds. |
| Facebook | 16:9 or 1:1 | Varies | Mixed formats. Slightly older audience. Subtitles recommended (add separately). |

## 20\. Input Specifications

| Input Type | Formats | Limits |
| --- | --- | --- |
| Images | JPEG, PNG, WebP, BMP, TIFF, GIF | Max 9 images, under 30MB each |
| Videos | MP4, MOV | Max 3 clips, 2-15 seconds each |
| Audio | MP3, WAV | Max 3 clips, under 15 seconds, under 15MB |
| Total files | — | Max 12 files across all types |
| Output duration | — | 4-15 seconds |
| Output resolution | — | Up to 2K |
| Prompt length | — | 30-200 words (60-100 optimal) |

65% Off

## Try These Prompts on Enhancor

Generate Seedance 2.0 videos directly in your browser. No setup, no downloads. Paste your prompt and go.

720p

$0.18/second

was $0.30/s

480p

$0.14/second

was $0.30/s

[Start Generating Videos](https://app.enhancor.ai/video-generator)

No subscription required. Pay-as-you-go credits. Failed generations refunded.

Seedance 2.0 on Enhancor — 65% off — **$0.18/s** at 720p

[Try Now](https://app.enhancor.ai/video-generator)