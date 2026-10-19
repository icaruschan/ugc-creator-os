# The UGC AI Video Toolkit — Complete Workflow Guide

**Version:** April 2026
**Tools covered:** Script Writer V1.0 · UGC Director V1.2 · UGC Video Architect V3.1 · UGC Video Deconstructor V2 · al1sha1 Video Architect V4.6

---

## OVERVIEW

This toolkit is a multi-stage production system for creating AI-generated UGC content using Seedance 2.0 on Higgsfield. Each tool handles a different stage of production, but the path is not always strictly linear. In practice there are three common entry points:

- **Idea-led:** Director → Architect → Seedance
- **Script-led:** Script Writer → Architect → Seedance
- **Reference-led:** Deconstructor → Architect → Seedance

```
LAYER 1 — PRE-PRODUCTION
UGC Director V1.2
"What should this video be?"
Figures out concept, format, hook, script, story arc

           ↓

LAYER 2 — PRODUCTION
UGC Video Architect V3.1  OR  al1sha1 Video Architect V4.6
"How do we build this video?"
Generates JSON-first production packages plus prompt-ready execution layers

           ↓

LAYER 3 — STYLE INTELLIGENCE
UGC Video Deconstructor V2
"What makes this video work?"
Reverse engineers any reference video into a structured style analysis plus key-beat image prompts

           ↓

SEEDANCE 2.0 ON HIGGSFIELD
Copy-paste the timestamp prompt → run the Seedance operator layer if you need final prompt cleanup → generate → extend → edit
```

The Deconstructor can feed into Layer 2 at any point — it's not strictly sequential. Think of it as a style intelligence layer you can tap whenever you have a reference video you want to learn from. If you also have a separate start-frame image, the Deconstructor can preserve that as the opening-frame truth while still using the video for pacing, structure, and realism cues.

The Script Writer sits alongside the Director when the bottleneck is not concept discovery but **scripting itself** — especially when you're starting from source material, messy research notes, a weak draft, or long-form content that needs to become a stronger short-form script.

---

## THE TOOLS AT A GLANCE

### Script Writer V1.0
**What it does:** Takes a topic, source material, messy notes, transcript, draft, or existing content and turns it into a retention-first short-form script package with multiple angles, a chosen script, a structural breakdown, creator-pack notes, and assumptions.
**Use it when:** You already know roughly what the video is about, but the scripting angle, hook, pacing, or reframing is the bottleneck.
**Output:** 3 Angles + Chosen Script + Breakdown + Creator Pack + Assumptions

### UGC Director V1.2
**What it does:** Takes a vague idea, product, niche, or mood and turns it into a complete content plan plus a ready-to-paste Architect input plus a Seedance timestamp prompt.
**Use it when:** You have a half-formed idea and need help figuring out what the video should be before you build it.
**Output:** Part 1 (Creative Brief) + Part 2 (Architect Input) + Part 3 (Seedance Timestamp Prompt)

### UGC Video Architect V3.1
**What it does:** Takes a detailed brief and builds a JSON-first, Seedance-optimized production package — JSON schema, primary generation prompt, timestamp breakdown, sound design, @ reference syntax, extension chain.
**Use it when:** You already know what you want and need to execute it with maximum detail and precision.
**Output:** Appendix A JSON first + Part 1 (Brief) + Part 2 (Primary Generation Prompt) + Part 3 (Timestamp Prompt) + triggered extras if needed

### al1sha1 Video Architect V4.6
**What it does:** Same as the UGC Architect but locked to the al1sha1 LoRA character. Outputs both SAFE (Anchor A) and RAW (Anchor B) JSON blocks first, then the execution prompts.
**Use it when:** You're generating content for the al1sha1 character specifically.
**Output:** Appendix A SAFE JSON + Appendix B RAW JSON first + Part 1 (Brief) + Part 2 (Primary Generation Prompt) + Part 3 (Timestamp Prompt) + triggered extras if needed

### UGC Video Deconstructor V2
**What it does:** Analyzes any uploaded video and extracts everything that makes it feel authentic — camera, lighting, performance energy, voice profile, hook frame, micro-expressions, environment, props — then turns that analysis into both a video prompt and a key-beat image prompt pack. It can also take a separate start-frame image and preserve that as the opening-frame truth.
**Use it when:** You have a reference video you want to study or replicate, especially if you also want to lock the opening frame with a still image.
**Output:** Step 1 (Full Deconstruction Analysis) + Step 2 (Ready-to-paste UGC prompt) + Step 3 (Key Beat Image Prompt Pack)

---

## THE THREE CORE WORKFLOWS

---

### WORKFLOW 1 — Idea to Video (Starting from Scratch)

**Use this when:** You have an idea but no reference and no fully formed concept.

**The path:** Director → Architect → Seedance

**Step-by-step:**

1. Open the UGC Director
2. Describe your idea as naturally as you would to a person. Include whatever you have — even one sentence is enough to start.
3. The Director outputs three things:
   - Part 1: Full creative brief (concept, hook, arc, script, CTA)
   - Part 2: Pre-filled Architect input — copy this entire block
   - Part 3: Ready-to-paste Seedance timestamp prompt
4. If you're happy with Part 3, paste it directly into Higgsfield and generate.
5. If you want more control or need to adjust details, take Part 2 and paste it into the UGC Architect as your prompt. The Architect will build a more detailed, fully-checked output with the completeness checklist applied.
6. Take the Architect's timestamp prompt into Higgsfield. If needed, run the `seedance-operator` skill as a final cleanup pass to tighten camera logic, lighting, constraints, and beat clarity without changing the concept. Upload your reference assets. Generate.
7. If your video is longer than 15s, use the extension chain — generate Clip 1, download it, upload as @Video1, paste Clip 2 prompt, generate, repeat.

**Example:**

User prompt to Director:
*"I want to make a TikTok about how I use Claude Code to automate my content writing. It's for other creators and I want it to feel like I'm just sharing something that changed my workflow."*

Director detects: **Organic UGC — Educational / Talking Head**

Director outputs:
- Concept: Creator shares genuine workflow hack, positioned as "something I wish someone told me earlier"
- Hook: She looks directly into camera and says "I haven't manually written a caption in three weeks" — audio hook, pattern interrupt
- Arc: Hook (0–3s) → context / problem (3–12s) → the tool and how she uses it (12–35s) → results + soft CTA (35–45s)
- Full script written out
- Part 2: Architect input pre-filled with subject casting, scene, voice profile, camera specs, timestamps
- Part 3: Seedance timestamp prompt ready to paste

---

### WORKFLOW 2 — Reference to Video (Replicating a Style)

**Use this when:** You find a video that's performing well and want to understand why and replicate it with your own subject.

**The path:** Deconstructor → optional still generation → Architect → Seedance

**Step-by-step:**

1. Find a UGC video whose style, energy, or performance you want to replicate. Could be a creator in your niche, a competitor's ad, anything.
2. Upload it to the UGC Deconstructor.
3. The Deconstructor outputs:
   - Step 1: Full analysis — camera, lighting, voice profile, hook frame, performance energy, countenance, micro-expressions, environment, props
   - Step 2: A ready-to-paste UGC prompt based on the analysis
   - Step 3: A key-beat image prompt pack for the hook, setup, payoff, product/demo beat if relevant, and closing/CTA
4. You have two options from here:
   - **Fast path:** Take Step 2 directly into Higgsfield. Add your own subject image as @Image1. Generate.
   - **Full path:** Use Step 3 to generate a still reference image for your subject or for `al1sha1`, then take the Step 1 analysis into the Architect as **Mode F** when you have both a start frame and a reference video. The Architect uses `@Image1` to lock the first 0:00-0:02 and `@Video1` to carry pacing, camera behavior, and edit rhythm after that.
5. Generate in Seedance. Your video inherits the reference's camera style, energy, and performance feel — applied to your subject and your dialogue.

**Example:**

You find a protein coffee UGC ad on TikTok that's getting massive views. The creator's energy is medium-high, the camera is slightly high angle handheld, the hook is a product reveal with no speaking, the voice is warm and casual with upspeak.

You upload it to the Deconstructor. It extracts:
- Hook frame: Creator holds product up to camera, eyebrows raised, no dialogue in first 2 seconds
- Performance energy: MEDIUM-HIGH, warm and inviting countenance
- Voice: Warm mid-range, slight upspeak, breathy texture, audible inhales before sentences
- Camera: iPhone handheld, slightly high angle, micro-sway, auto-focus hunting
- Environment: Clean kitchen counter, natural window light from left, minimal background

You can use Step 3 to generate a matching first-frame still, then take the Step 1 analysis into the Architect as **Mode F** (start frame + video reference). The Architect maps the reference style onto your subject while preserving the opening frame. You now have a Seedance prompt that replicates everything that made the original work.

---

### WORKFLOW 3 — Known Brief to Video (Fastest Path)

**Use this when:** You know exactly what you want — concept, format, script, subject. You don't need the Director to figure it out.

**The path:** Architect directly → Seedance

**Step-by-step:**

1. Open the UGC Architect (or al1sha1 Architect if using that character).
2. Write your brief directly — include subject description or attach image, scene, dialogue, camera preference, model, platform.
3. The Architect outputs the full production package — JSON first, then the brief, primary generation prompt, timestamp prompt, and any triggered extras.
4. Copy the timestamp prompt into Higgsfield with your reference assets. Generate.
5. Extend if needed.

**Example:**

You already know: you want a car rant, mid-20s woman in the driver's seat, talking about why most creators fail at consistency, for Instagram Reels, Seedance 2.0, 12 seconds.

You go straight to the Architect. No Director needed. You write:
*"Mode A. Car rant. Mid-20s mixed race woman, natural hair pulled back loosely, oversized hoodie, sitting in driver's seat of a parked car at night. Dashboard glow + streetlights. Seedance 2.0. 12s. Dialogue: 'Most creators fail not because they run out of ideas — they run out of systems. The ones who stay consistent aren't more creative. They're more organized.' Energy HIGH. Countenance — intense and direct."*

The Architect builds the full JSON, timestamp breakdown, sound design, generation settings. You paste and generate.

---

## HOW THE TOOLS COMPLEMENT EACH OTHER

The key insight is that each tool covers a different type of uncertainty:

| If you have... | Use... |
|----------------|--------|
| A vague idea, no concept yet | Director first |
| A reference video you want to learn from | Deconstructor first |
| A clear brief, just need the prompt | Architect directly |
| A concept AND a reference to match | Director → Deconstructor → Architect |
| al1sha1 content specifically | al1sha1 Architect (skip the UGC Architect) |

**The Director removes creative uncertainty.**
You don't need to know what format to use, what the hook should be, how to structure the arc, or what to say. The Director figures all of that out from whatever you give it.

**The Deconstructor removes stylistic uncertainty.**
You don't need to know what camera angle to use, what energy level to set, how to describe the voice, or which still frame moments are worth recreating as reference images. The Deconstructor pulls all of that from a reference video that already works.

**The Architect removes technical uncertainty.**
You don't need to know what @ syntax Seedance needs, how to structure the timestamp breakdown, what fields to fill, how to keep JSON consistent with the prompt layers, or how to write the sound design. The Architect handles all of that.

**Together they eliminate all three types of uncertainty** — creative, stylistic, and technical — at every stage of production.

---

## THE HANDOFF — Director or Deconstructor to Architect

The Director's Part 2 output is formatted exactly as the UGC Architect expects. The Deconstructor's Step 1 + Step 2 output can also hand off directly into the Architect. The handoff is zero friction:

1. Run the Director with your idea
2. Copy everything in the Part 2 code block (between the triple backticks)
3. Paste it directly into the UGC Architect as your prompt
4. The Architect reads every field and builds the full production output

Reference-led handoff:

1. Run the Deconstructor on the reference video
2. Use Step 1 for the technical/style truth and Step 3 if you want a still image anchor
3. If you have both a start frame image and a reference video, pass them into the Architect as **Mode F**
4. The Architect locks the first 0:00-0:02 to `@Image1` and follows `@Video1` for pacing after that

Nothing needs to be reformatted. The Director pre-fills every field the Architect uses — subject description, hook frame, scene, performance energy, dialogue, voice profile, camera specs, reference assets, triggers.

**What the Architect adds on top of an upstream handoff:**
- JSON block(s) first so the structured version is always available
- Brief + primary generation prompt + timestamp prompt for human-readable execution
- Completeness checklist applied — the commonly skipped fields are forced in
- Sound design and generation settings integrated into the output package
- Extension chain structured per clip if content is long form
- Hybrid image + video handling through **Mode F** when both assets exist

---

## SEEDANCE 2.0 PRODUCTION TIPS

### The @ Reference System
Every asset you upload to Higgsfield gets a tag — @Image1, @Image2, @Video1, @Audio1 etc. Reference them directly in your prompt to tell Seedance exactly what each file does.

Common setups:
- @Image1 = starting frame / character reference
- @Image2 = product image (referenced at exact timestamp it appears)
- @Video1 = motion reference OR previous clip for extension
- @Audio1 = voiceover file OR voice ID reference

**Hybrid setup:**
- `@Image1` = locked opening frame / character continuity
- `@Video1` = pacing, camera behavior, edit rhythm
- Best used through **Mode F** when you want both image-locked opening fidelity and reference-video motion/style

### Voice ID Technique
Instead of describing a voice in text, find a video of a real person with the voice quality you want. Extract the audio. Upload as @Audio1. Use this syntax:
*"Use @Audio1 as voice ID reference for her voice. Do not make her say the words in the audio, just use it as a voice ID."*

Seedance replicates the timbre, texture, and tone for your custom dialogue. Far more realistic than text description alone.

### The Timestamp Method
Break your script into 4–5 second blocks. For each block: exact dialogue + exact visuals. Seedance follows exact instructions — vague prompts produce random outputs, timestamped prompts produce exactly what you specify.

Example structure:
```
0–4s: Hook
Dialogue: "I haven't manually written a caption in three weeks."
Visuals: Subject holds phone toward camera, eyebrows raised, slight smirk. 
Medium close-up, eye-level, handheld.

5–12s: Setup
Dialogue: "Claude Code does it all. I give it my video transcript and 
it writes the caption, the hook, the hashtags — everything."
Visuals: Subject leans slightly forward, gestures with free hand on 
"everything." Brow furrows briefly on "all."
```

### The Extension Chain
Seedance maxes at 15 seconds per generation. For longer content:
1. Generate Clip 1 (up to 15s)
2. Download it
3. Upload back to Higgsfield as @Video1
4. Prompt: *"Extend the previously generated clip from its last frame. Keep the voice the same as the original clip. If @Video1 exists as a reference asset, continue following @Video1 for pacing, camera behavior, and edit rhythm."*
5. Add new assets if needed (@Image2 for a new product etc.)
6. Generate Clip 2
7. Repeat until full video is covered
8. Stitch in CapCut / Premiere / DaVinci

Three clips = 45 seconds. The model maintains character, voice, environment, and lighting across all extensions.

### The Canva Character Limit Workaround
Seedance caps prompts at 2000 characters. Long timestamp prompts often exceed this.

Workaround:
1. Copy your full timestamp prompt
2. Paste it as text into a Canva design (white background, readable font)
3. Export as PNG
4. Upload to Higgsfield as a reference image (it gets tagged @Image2 or next available)
5. Use this short prompt instead: *"Transcribe this image and use the movements and dialogue described here."*

Seedance reads the text in the image and follows all instructions. No character limit.

---

## SCENARIO LIBRARY

### Scenario A — Product Review UGC Ad (Short Form)

**Goal:** 30-second TikTok-style UGC ad for a skincare serum. Creator feels real, not scripted.

**Tools:** Director → Architect → Seedance

1. Director prompt: *"UGC ad for a vitamin C serum called Glow Lab. Target audience: women 22-35 interested in skincare. I want it to feel like a genuine recommendation, not an ad. About 30 seconds, TikTok."*
2. Director detects: UGC Ad — Product Demo / Talking Head hybrid
3. Director writes concept: Creator shares a personal skin concern (dullness), introduces the product as something she stumbled on, shows it, explains one specific benefit she noticed, CTA.
4. Director outputs Part 2 Architect input — subject invented as a 27-year-old woman with warm medium skin, casual outfit, natural bathroom lighting, product in hand.
5. Paste Part 2 into Architect. Architect adds completeness check, sound design, extends to 2-clip extension chain since 30s exceeds 15s max.
6. Generate Clip 1 (hook + product intro). Extend for Clip 2 (benefit + CTA).

---

### Scenario B — Replicating a Viral Style (Reference-Led)

**Goal:** You've found a gym check video that's performing exceptionally. You want to make the same style of content for a fitness supplement brand.

**Tools:** Deconstructor → Architect → Seedance

1. Upload the viral gym check video to the Deconstructor.
2. Deconstructor extracts: high angle handheld mirror selfie, high energy, warm and inviting countenance, upward inflection, fast casual pace, audible inhales, gym locker room environment with natural overhead fluorescent.
3. Use Step 3's key-beat image prompts to identify the strongest still for the opening mirror-check frame.
4. If you're making this with `al1sha1`, paste that beat prompt into the al1sha1 image system to generate a first-frame still that matches the reference video's framing, lighting, pose, and fidelity.
5. Take the Step 1 analysis to the Architect. Use **Mode F** if you have both a start frame image of your subject and the reference video.
6. Architect maps the extracted style onto your subject with your own dialogue and product reference while preserving the opening frame.
7. Generate on Seedance.

---

### Scenario B2 — Reference Reel to al1sha1 First Frame

**Goal:** You found an Instagram Reel with a hook frame you want to reuse, but you need a matching `al1sha1` still before building the video.

**Tools:** Deconstructor → al1sha1 image system → al1sha1 Architect → Seedance

1. Upload the Reel to the Deconstructor.
2. Review Step 3 and pick the beat whose still frame should become your `@Image1` anchor. Usually this is the hook beat or strongest payoff beat.
3. Paste that beat's `Image Prompt` and `al1sha1 Handoff Notes` into the al1sha1 image system to generate the first-frame still while preserving camera angle, pose direction, wardrobe construction, prop placement, lighting direction, and fidelity.
4. Upload the finished still as `@Image1`.
5. Take the Deconstructor's Step 1 analysis into the al1sha1 Architect as the style/motion reference, using the Reel as `@Video1` and the finished still as `@Image1`.
6. Use **Mode F** so `@Image1` locks the first 0:00-0:02 and `@Video1` supplies pacing and camera behavior after that.
7. Generate in Seedance with `@Image1` as the first-frame anchor and `@Video1` as the motion/style reference.

---

### Scenario C — Long Form Educational Content (Creator Authority)

**Goal:** 3-minute TikTok tutorial on how to use AI tools for content creation. Building audience authority.

**Tools:** Director → Architect (with extend trigger) → Seedance extension chain

1. Director prompt: *"3-minute TikTok tutorial on using AI for content creation. My audience are small creators aged 20-30 who are overwhelmed by content demands. I want to position myself as someone who figured this out and is sharing it. Educational UGC, organic, no product to sell."*
2. Director detects: Organic UGC — Educational / Tutorial, long form
3. Director structures: Hook (0–5s) → Context/problem (5–30s) → Tool 1 (30s–1:30) → Re-hook at 1:30 → Tool 2 (1:30–2:30) → Re-hook at 2:30 → Summary + soft CTA (2:30–3:00)
4. Director outputs a full talking points script (not word-for-word, since this is semi-scripted long form)
5. Paste Part 2 into Architect with "extend" trigger. Architect outputs 12-clip extension chain (180s ÷ 15s = 12 clips).
6. Generate each clip in sequence. Each builds on the last via @Video1 extension.
7. Edit together in CapCut. Add captions.

---

### Scenario D — al1sha1 UGC Ad (Character-Specific)

**Goal:** 15-second al1sha1 video promoting a content creation tool. Bedroom studio setting. Seedance 2.0.

**Tools:** al1sha1 Architect directly → Seedance

1. Skip the Director — you know what you want.
2. Prompt to al1sha1 Architect: *"Mode B. Image attached (bedroom studio, RGB lighting, white corset, blue jeans). Seedance 2.0. 15s. Dialogue: 'I used to spend two hours on captions. Now it takes me five minutes. This tool does the thinking for me.' Energy MEDIUM. Countenance warm and inviting. Kling RAW + Seedance SAFE both."*
3. Architect outputs SAFE JSON (Anchor A) + RAW JSON (Anchor B) first, then the brief, primary generation prompt, timestamp prompt, and any triggered extras.
4. Use the SAFE option for Seedance/Veo. Use the RAW option for Kling/Higgsfield.
5. Upload al1sha1 LoRA image as @Image1. Generate.

---

### Scenario E — Voice ID for Maximum Realism

**Goal:** You want al1sha1's voice to sound like a specific real creator whose voice has the same sultry, husky quality.

**Tools:** al1sha1 Architect with Mode E2 → Seedance

1. Find a TikTok or Instagram video of a creator whose voice matches al1sha1's timbre — sultry, low-mid range, slight vocal fry.
2. Extract the audio from that video (use a tool like 4K Video Downloader or SnapSave, then strip audio in CapCut).
3. Save as MP3, max 15 seconds.
4. In al1sha1 Architect prompt, specify: *"Mode E2. I have a voice ID reference audio — [brief description of whose voice it is]. Upload as @Audio1."*
5. Architect populates the voice_id_source field and uses the correct Seedance syntax: *"Use @Audio1 as voice ID reference for her voice. Do not make her say the words in the audio, just use it as a voice ID."*
6. Upload audio to Higgsfield alongside your LoRA image. Generate.

Result: al1sha1 speaks in a voice that's been modeled on a real human reference rather than generated from text description. Significantly more realistic.

---

## QUICK REFERENCE — Which Tool for What

| Situation | Tool | Mode |
|-----------|------|------|
| Have source material, messy notes, or a weak draft and need a stronger script | Script Writer | — |
| Half-baked idea, need concept + script | Director | — |
| Have a reference video to copy style from | Deconstructor | — |
| Need first-frame stills from a reference video | Deconstructor Step 3 | — |
| Clear brief, just need the prompt built | Architect | A or B |
| Have a reference image of subject | Architect | B |
| Have a reference video for motion | Architect | C |
| Want to lock first and last frame | Architect | D |
| Have both a start frame image and a reference video | Architect | F |
| Have a voiceover file | Architect | E1 |
| Want to copy a voice from a real video | Architect | E2 |
| al1sha1 character content | al1sha1 Architect | Any |
| Content over 15 seconds | Any Architect | extend trigger |
| Want 3 camera angle options | Any Architect | variations trigger |
| Single generation multi-angle | Any Architect | multishot trigger |
| Prompt over 2000 characters | — | Canva workaround |

---

## COMMON MISTAKES TO AVOID

**1. Skipping the timestamp method**
Vague prompts produce inconsistent results in Seedance. Always break your script into 4–5 second timestamp blocks with exact dialogue AND exact visuals per block. This is the single biggest lever for output quality.

**2. Describing emotions instead of physics**
"She looks excited" tells Seedance nothing. "Brow lifts on emphasis, eyes widen, slight lean forward" gives the model actual muscle movements to render. Always describe facial performance as physics.

**3. Forgetting the @ product reference**
If a product appears in your video, tag it by @ at the exact timestamp it's mentioned — not generically. "She picks up @Image2 when she says [product name]" is correct. "@Image2 is the product" without a timestamp is not specific enough.

**4. Not using voice ID**
Describing a voice in text ("warm and husky with vocal fry") produces decent but not great results. Referencing a real voice via @Audio1 voice ID produces dramatically more realistic output. Use it whenever voice realism matters.

**5. Hitting the 2000 character limit without a plan**
Long timestamp prompts will exceed Seedance's character limit. Always check length before generating. If over 2000 characters, use the Canva workaround immediately — don't try to shorten the prompt, you'll lose detail.

**6. Not maintaining @Image1 on extensions**
When extending from a generated clip, always re-upload @Image1 as the character reference on every extension clip. Without it, character consistency can drift on longer clips.

**7. Confusing Mode C with Mode F**
Mode C is video-only. If you also have a separate start-frame image and want the opening frame preserved, use **Mode F** instead.

**8. Using the Director when you already know what you want**
The Director adds creative overhead. If you know the concept, script, and visual style — go straight to the Architect. The Director is for when you're starting from nothing.

---

## TOOLKIT VERSION HISTORY

| Tool | Current Version | Key Capability |
|------|----------------|----------------|
| Script Writer | V1.0 | Retention-first scripting from topics, source material, drafts, and repurposed content |
| UGC Director | V1.2 | Part 2 handoff matches Architect V3.1 format exactly |
| UGC Video Architect | V3.1 | JSON-first output, Mode F hybrid input, Timestamp method, Voice ID E2 |
| al1sha1 Video Architect | V4.6 | JSON-first SAFE/RAW output, Mode F hybrid input, dual anchor workflow |
| UGC Video Deconstructor | V2 | Reference-video deconstruction + start-frame-aware handoff + key-beat image prompts |
