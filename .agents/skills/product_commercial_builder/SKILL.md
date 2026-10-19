---
name: product-commercial-builder
description: Use when the user wants to build a product commercial, start the commercial builder, or generate consistent storyboard-to-video prompts.
---

# Product Commercial Builder

## Overview
This skill guides the agent in conducting a step-by-step, interactive dialogue with the user to create a high-fidelity 10-15s product commercial video.

The workflow is based directly on the visual-to-motion relationships extracted from the reference videos in the local [videos](assets/reference-videos/) directory (such as chocolate drizzling, package tearing, and bar snapping).

Instead of generating all prompts at once, the agent works cooperatively with the user: generating a prompt, waiting for the user to upload the resulting image, and using that image to lock consistency for the next beat.

All output prompts must be written to a dedicated product directory at the active workspace root: `output/{product_name}/` (e.g., `output/hersheys-kisses/storyboard_prompts.txt` under the workspace root, not inside the hidden `.agents/` skill directory or varying terminal working directories) to keep runs isolated.

---

## The Interactive Production Workflow

### Phase 1: Product Scan & Backdrop (Interactive)

1.  **Initialize Output Folder:** The agent must ensure a dedicated product folder exists under the active workspace root: `output/{product_name}/` (using a lowercase, hyphenated product name, resolved directly from the workspace root directory).
2.  **Request Reference Assets:** Ask the user to upload all raw product images (showing different angles, wrapper text, interior details, or ingredients) and describe the main product concept.
3.  **Perform Visual Identity Scan:** Analyze the files to extract:
    *   *Exterior Packaging:* Brand logo, exact spelling, colors, material texture.
    *   *Product Anatomy:* Raw mold shape, geometric details, surface details.
    *   *Interior Anatomy:* Visible fillings, colors, crunch layers.
4.  **Design the Backdrop (Scene Environment):** Propose a custom studio background layout that complements the product (color blocks, marble/wood surfaces, or raw ingredient dustings).
5.  **Draft the Prep/Polish Prompt:** Output a single prompt for GPT Image 2 / Nanabanana to clean up the product, fix lighting, and place it in the new backdrop.
6.  **Checkpoint (Wait for User):** Stop execution. Ask the user to generate the polished product image and upload it to proceed.

---

### Phase 2: Storyboard Loop (Feedback & Steering)

For each storyboard beat in sequence, the agent will:
1.  **Propose the Next Beat Prompt:** Generate a detailed prompt for GPT Image 2 / Nanabanana.
2.  **Explain the Animation/Motion Rationale:** Detail how this still frame will influence the video model's motion, using the reference commercials under `assets/reference-videos/` as guidance:
    *   *Macro Hook (Beat 1):* Reference the KitKat logo stamp close-up (`kitkat_pistachio_kunafa.mp4`).
    *   *Package Reveal (Beat 2):* Reference the Bueno package center position (`kinder_bueno_chocolate.mp4`).
    *   *Wrapper Tear (Beat 3):* Reference the Bueno tear physics (`kinder_bueno_chocolate.mp4`).
    *   *Slide-Out (Beat 4):* Reference the Bueno/KitKat sliding motion.
    *   *Action / Snapping / Oozing (Beat 5):* Reference the KitKat pistachio oozing (`kitkat_pistachio_kunafa.mp4`) or Oniro split (`oniro_choco_cookies.mp4`).
    *   *Cross-Section (Beat 6):* Reference the KitKat/Bueno filling macro crops.
    *   *Ingredient Splash (Beat 7):* Reference the Almarai yogurt crescent formation (`yogo_yogurt_ramadan.mp4`).
    *   *Branding End (Beat 8):* Reference the final pack spin and logo cards.
3.  **Interactive Checkpoint:** Stop and ask the user to:
    *   *Option A:* Approve/tweak the prompt (the user can pitch modifications to details, camera angles, or colors).
    *   *Option B:* Generate the frame and upload the finished image.
4.  **Write Prompts to File:** Once a storyboard prompt is finalized, append it to `output/{product_name}/storyboard_prompts.txt` under the active workspace root with its corresponding Beat label so you have a clean record.
5.  **Update Visual Continuity:** Once the user uploads the generated image, scan its specific visual details (the exact color of the wrapper, the reflection pattern, the chocolate sheen). **You must inject these specific visual markers into the next prompt** to maintain absolute consistency across the storyboard.

---

### Phase 3: Video Prompt Compilation

Once all 8-10 beat images are generated:
1.  Instruct the user to upload all finished frames in order (which will be tagged as `@Image1` through `@Image8` / `@Image10` in Seedance 2.0 or Kling 3.0).
2.  Compile the final timestamped motion prompt.
3.  Write the compiled prompt to `output/{product_name}/final_video_prompt.txt` under the active workspace root.

#### Video Prompt Structure
*   **Asset Map:** Declare the roles of `@Image1` through `@Image8`.
*   **Scene Setup:** Standardize camera body, lens focal length, studio lighting, and backdrop.
*   **Timestamp Breakdown:** 2-3s blocks detailing exact camera motion, packaging tears, floating rotations, and snapping physics matching the uploaded images.
*   **Sound Design:** Aligned audio chimes, paper tears, snaps, cream squishes, and background beats.
*   **Generation Settings:** Aspect ratio, resolution, model duration (10-15s), and negative constraints.

---

## Technical Realism Constraints

*   **No Buzzwords:** Never write "cinematic", "8K", "masterpiece", "perfect skin", "hyper-realistic".
*   **Physics-Based Action:** Describe motion as physics (e.g. "tearing", "oozing", "dripping", "rotating").
*   **Absolute Continuity:** The background, lighting, logo text, and product shape must remain identical from prompt to prompt.

---

## Reference Video Guide (For the Agent)
When planning storyboard frames and compiling the final video prompt, read and inspect the files in [assets/reference-videos/](assets/reference-videos/) to align the motion design:
*   `kimo_cono_ice_cream.mp4` -> Wafer roll-up and interior coating logic.
*   `yogo_yogurt_ramadan.mp4` -> Splashing yogurt and floating ingredients forming shapes.
*   `oniro_choco_cookies.mp4` -> Liquid chocolate drizzle and cookie split filling detail.
*   `kinder_bueno_chocolate.mp4` -> Wrapper peel/tear, slide-out extraction, and floating spin.
*   `kitkat_pistachio_kunafa.mp4` -> Logo stamp close-up, snapping in half with cream oozing, and final logo slide-in.
