# Seedance model matrix

Verified August 2026. Everything here changes the schema, so resolve the model before composing.

---

## The one-screen version

| | 1.0 lite | 1.0 pro / pro-fast | 1.5 pro | 2.0 | 2.5 |
|---|---|---|---|---|---|
| Duration | 2–12 s | 2–12 s (def 5) | 4–12 s (def 5) | auto or 4–15 s | auto or **4–30 s** |
| Resolution | 480p / 720p / 1080p | 480p / 720p / 1080p | 480p / 720p / 1080p | 480p → **4K** | **480p / 720p only** |
| Aspect | 21:9 16:9 4:3 1:1 3:4 9:16 (+9:21 on t2v) | same | same + auto | auto + same | auto + same |
| fps | 24 | 24 | 24 | 24 | 24 |
| **Native audio** | **none** | **none** | yes | yes | yes |
| Multi-reference | 1–4 images | first+last frame only | first+last frame only | 9 img / 3 vid / 3 aud, 12 max | **30 img / 10 vid / 10 aud, 50 max** |
| Prompt window | ~1,000 w practical | ~1,000 w practical | ~1,000 w practical | ~1,000 w practical | **20,000 chars ≈ 3,000 w** |
| Practical cut budget | 2 | 2 | 2–3 | 3–4 | 5–6 |

**fps is 24 everywhere and is not a parameter.** Never request another rate.

**The prompt window is the under-discussed row.** Seedance 2.5 accepts 20,000 characters — roughly 3,000 words — and that is why the rig's working ceiling now scales with duration (400 + 45 × duration) instead of sitting at one flat number for every job. On 2.0 and below, treat ~1,000 words as the practical adherence ceiling: those models top out at 15 s, and a clip that short cannot absorb three pages without the description diluting itself.

**The two traps.** Seedance 2.5 is the newest and is capped at 720p — it is the wrong choice for anything that needs to hold up at 1080p or above, and "30 s 4K Seedance 2.5" claims are wrong. Seedance 1.0 in all variants produces **silent video**; a dialogue prompt on 1.0 renders mute lips.

**2.5, specifically.** Three headline changes: 30-second duration, 50 references, and the 20,000-character prompt window. The third is the one that changes how you write. Thirty seconds and fifty plates only matter if the whole sequence — CONTEXT, six beats and the PROMPT SEGMENTS tier — fits inside a single prompt, and the character window is what makes it fit. Before 2.5 a sequence meant separate clips that then had to be made to match.

---

## Choosing

| The job | Model | Why |
|---|---|---|
| Long unbroken take, 20–30 s | 2.5 | Only model past 15 s. Accept 720p. |
| Many characters or props to hold consistent | 2.5 | 30 image references is the widest identity net available |
| Delivery master at 1080p or 4K | 2.0 | Only model with 4K |
| 15 s with audio at 1080p | 2.0 | 1.5 tops out at 12 s |
| Cheap dialogue coverage at 1080p | 1.5 pro | Native audio, 1080p, low cost. First+last frame only |
| Silent action plates, cheapest possible | 1.0 pro-fast | ~$0.05/s at 1080p on fal, and genuinely fast |
| Iterating blocking before committing budget | 1.0 lite at 480p | Pennies per look |

Beyond 30 s, Seedance 2.5 supports **two rounds of extension**, carrying subject, scene, style and sound forward. Plan a long sequence as 30 s + extension rather than as separate clips that will not match.

---

## Model IDs

**fal.ai**
```
fal-ai/bytedance/seedance/v1/pro/text-to-video
fal-ai/bytedance/seedance/v1/pro/image-to-video
fal-ai/bytedance/seedance/v1/pro/fast/text-to-video
fal-ai/bytedance/seedance/v1/pro/fast/image-to-video
fal-ai/bytedance/seedance/v1.5/pro/text-to-video
fal-ai/bytedance/seedance/v1.5/pro/image-to-video
bytedance/seedance-2.0/text-to-video      (+ /fast)
bytedance/seedance-2.0/image-to-video
bytedance/seedance-2.0/reference-to-video
bytedance/seedance-2.5/text-to-video
bytedance/seedance-2.5/image-to-video
bytedance/seedance-2.5/reference-to-video
```
The v1 `lite` endpoints are deprecated and redirect to pro/fast.

**Replicate** — `bytedance/seedance-1-pro`, `-1-pro-fast`, `-1.5-pro`, `-2.0`, `-2.0-fast`, `-2.0-mini`, `-2.5`

**Kie.ai** — `bytedance/seedance-1.5-pro`, `bytedance/seedance-2-fast`, `bytedance/seedance-2-5`, plus V1 Pro / Lite / Pro-Fast. All via `POST /api/v1/jobs/createTask`. Kie restricts Seedance 1.0 durations to **5 s or 10 s only**.

**Volcengine / BytePlus ModelArk** — `seedance-1-0-lite-t2v-250428`, `seedance-1-0-lite-i2v-250428`, `seedance-1-0-pro-250528`, `doubao-seedance-1-5-pro-251215`, `doubao-seedance-2-0-260128` (intl: `dreamina-seedance-2-0-260128`), `doubao-seedance-2-5-260628`. Direct first-party API availability for 2.5 was still rolling out at launch; aggregators had it first.

---

## Parameters

| Parameter | Where | Note |
|---|---|---|
| `duration` | all | Integer seconds, or `auto` on 2.0 / 2.5 |
| `resolution` | all | See matrix. 2.0 adds `4k` at a separate token rate |
| `aspect_ratio` | all | Prompt body must NOT contain the ratio — it is a parameter. State it in `FORMAT MODE` for the human |
| `generate_audio` | 1.5 / 2.0 / 2.5 | Default true. Absent on 1.0 |
| `camera_fixed` / `fixed_lens` | all | Locks the camera. Set it *and* write it in `CAMERA` |
| `end_image_url` | 1.0 / 1.5 / 2.0 / 2.5 | Last-frame conditioning |
| `seed` | all | Reuse to iterate one composition |
| `bitrate_mode` | 2.0 | standard / high |
| `enable_safety_checker` | all | |
| `negative_prompt` | **nowhere** | Does not exist on any Seedance endpoint. Use the `POSITIVE LOCKS` tail |

On Kie's 2.5, the three input modes — first-frame image-to-video, first+last frame, and multimodal reference-to-video — are **mutually exclusive**. Pick one per call.

---

## Cost

**fal.ai**, token formula `(height × width × 24 × duration) / 1024`:

| Model | Rate | Worked |
|---|---|---|
| 1.0 pro | $2.50 / M tokens | 1080p 5 s ≈ $0.62 |
| 1.0 pro-fast | $1.00 / M | 1080p 5 s ≈ $0.24 |
| 1.5 pro | $2.40 / M with audio, $1.20 without | 720p 5 s w/ audio ≈ $0.26 |
| 2.0 | $0.014 / 1k (480p–1080p), $0.008 / 1k (4K) | 720p $0.30/s · 1080p $0.68/s |
| 2.5 | $0.0214 / 1k | 720p ≈ $0.47/s · 480p ≈ $0.22/s |

Two things that surprise people:
- **Reference videos are billed as duration.** In 2.0/2.5 reference mode the formula uses `input_duration + output_duration`. A 20 s reference video attached to a 10 s render bills 30 s.
- **Supplying video references applies a ×0.6 multiplier** to the rate, which often more than pays for the added input duration.

Audio is free on 2.0 and 2.5. On 1.5 pro it **doubles** the price.

**Kie.ai, Seedance 1.0, per second** — 480p $0.014 pro / $0.010 lite · 720p $0.030 / $0.0225 · 1080p $0.070 / $0.050. Kie's 1.5 / 2.0 / 2.5 per-second rates are not published; a Kie blog quoted figures roughly 7× under fal's, which is not credible — quote fal's numbers and flag Kie's as unconfirmed.

---

## Known weaknesses

**On-screen text.** The worst area, across every version. Hands-on testing of 2.0 found in-frame text corruption effectively unavoidable. 2.5 claims improvement, not a fix. Generate clean, add type in post. If a word is unavoidable, wrap the exact string in quotes to raise its weight.

**Dialogue timing.** Lip-sync itself is strong — 92–99.8% measured on 2.0. The failure is script length: if the line is longer than the clip, the model speeds up delivery and desyncs. Budget 2–2.5 words per second.

**Fast motion.** Running, combat and extreme rotation produce limb stretching and inter-frame ghosting. Fast camera + fast cuts + busy scene simultaneously is a documented failure combination.

**Three or more simultaneous characters.** The main driver of ID drift and the duplicate-subject "twins" artifact.

**Without references,** expressions read flat and faces drift toward recognisable film and TV likenesses.

**Speed.** 2.0 and 2.5 are slow — 10 s took 5–10 minutes in testing, longer at peak. Seedance 1.0 pro was the fast one (5 s at 1080p in ~41 s).

**Content restrictions.** After the 2026 copyright actions, consumer channels block photoreal real-person face references and reject celebrity names, brands and violence keywords. Describe by build and wardrobe.

---

## Official prompt formula

ByteDance's own shape, for reference — the Prompt Rig is a superset of it:

```
<Subject> in <Scene>, <Main Action>.
Visual style: <style>.
Camera: <shot size, position, movement>.
Sound: <dialogue, ambience, SFX, music>.
```

Their four lines map onto rig blocks:

| ByteDance line | Rig blocks |
|---|---|
| `<Subject> in <Scene>, <Main Action>` | `SCENE CONTEXT` + `CAST` + `ACTION` |
| `Visual style` | `STYLE` |
| `Camera` | `CAMERA` + `LENS` |
| `Sound` | `AUDIO` + `SCORE` + `SFX` + `DIALOGUE` |

Everything the rig adds — the lifespan tiers, the reference exclusions, the per-beat structure — sits on top of that shape rather than against it. Required: subject and action. Everything else optional. Their stated governing principle is worth keeping in mind — nail down everything the model would otherwise have to guess.
