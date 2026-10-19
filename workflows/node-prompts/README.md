# Node Orchestration Prompts

This directory contains structured prompts used to build clean outputs (such as JSON data structures) or pass information between nodes in a multi-step pipeline.

## Files

### Second-node prompt (A/B pair)

Keep both old and new while testing.

| Role | Baseline (old) | Test (new) | What the new one changes |
|---|---|---|---|
| Hybrid one-pass second node | `al1sha1-json-second-node-prompt-v1.0.md` | `al1sha1-json-second-node-prompt-v1.1.md` | Five budgets + injection policy; early capture look; mode-dependent skin floors; morphology NL-only; no jewelry invention; short negatives; escalation without adding sharpness |

- **`al1sha1-scene-brief-first-node-prompt-v1.0.md`**: Prompt for generating high-level scene layouts and briefs (Node 1 in the generation pipeline).
- **`ugc-director-v1.2.md`**: The master workflow orchestration script that coordinates scripts, images, and videos into a unified pipeline structure.

### Suggested A/B test

1. Same first-node scene brief  
2. Run old second node → generate image  
3. Run new second node → generate image  
4. Compare natural phone look vs identity hold vs skin plastic risk  
