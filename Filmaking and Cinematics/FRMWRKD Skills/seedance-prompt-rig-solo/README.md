# seedance-prompt-rig — Quick Start

A Claude skill that writes ByteDance Seedance video prompts (1.0 · 1.5 pro · 2.0 · 2.5) on the
Prompt Rig: three tiers sorted by how long each fact stays true, 27 named blocks, per-block word
budgets, reference role lines with exclusions, and a linter that runs before you spend a credit.

**Made by FRMWRKD** — the YouTube channel about making film with AI tools. Every rule in here was
paid for on a real render.

> ⚠️ **Beta:** fully usable, still developing. Your purchase includes every future update free via
> Gumroad. Found a failure the skill did not catch? Send it in and it becomes a rule.

## 1. Install

**Claude Code (CLI):**

```bash
mkdir -p ~/.claude/skills
unzip seedance-prompt-rig.skill -d ~/.claude/skills/
```

That leaves `~/.claude/skills/seedance-prompt-rig/SKILL.md` in place. Start a new session; the
skill loads on any request naming Seedance, a video prompt, a blockout, a fight, a two-hander, etc.

**Claude Desktop / Cowork:** Settings → Capabilities → Skills → add skill → select
`seedance-prompt-rig.skill`. Done.

## 2. Requirements

- Claude Code or Claude Desktop (Cowork mode)
- Python 3.10+ for the linter — no dependencies, no API keys
- Optional: `ffmpeg` / `ffprobe` for the post-render checks in `references/verify.md`
- Optional: the companion `shot-builder` skill (cast turnarounds, location plates, generation).
  This skill consumes its tokens if present and runs standalone if not.

## 3. First prompt in five minutes

1. *"Write a Seedance 2.5 prompt: two men in a car at night, one line of dialogue, 8 seconds."*
   Claude picks the model, a preset, writes CONTEXT → BEATS → PROMPT SEGMENTS, lints it and shows
   a pre-flight before handing you one clean fenced block.
2. Paste it into fal.ai, Replicate, BytePlus, Dreamina or Artlist (tag dialect is converted for you).
3. Render came back wrong? *"The face drifted"* → Claude reads `references/fixes.md` and changes
   one thing.
4. Working with a 3D blockout or previz video? Say so. The reference gets one compact role line
   and the prompt spends everything on the performance (`references/blockout.md`).

## 4. Lint anything, any time

```bash
python3 ~/.claude/skills/seedance-prompt-rig/scripts/seedance.py lint prompt.txt --model 2.5 --duration 8
python3 ~/.claude/skills/seedance-prompt-rig/scripts/seedance.py models
python3 ~/.claude/skills/seedance-prompt-rig/scripts/seedance.py budget --duration 30
```

It checks word budgets per tier, the capitals vocabulary, one camera move per beat, reference
bindings without exclusions, unbalanced audio brackets, dialogue that will not fit the clip, cut
budget per model, negative walls, constants misfiled into beats, video role lines that shout,
`identity ONLY` bindings, excluded room proportions, and timestamps past the end of the clip.

## 5. What is in the folder

```
seedance-prompt-rig/
├── SKILL.md                 the rig in one screen, the five laws, the workflow
├── references/
│   ├── blocks.md            all 27 blocks: fill rules, budgets, a worked line each
│   ├── presets.md           CINEMATIC · ACTION · MOTION GRAPHICS · COMMERCIAL · STYLISED
│   ├── models.md            the Seedance capability matrix, IDs per provider, pricing
│   ├── binding.md           reference role lines, fidelity grades, tag syntax per platform
│   ├── camera.md · sound.md · action.md · scenes.md · density.md
│   ├── performance.md       the beat-level acting unit
│   ├── acting-task.md       the scene-level acting unit (two-handers, subtext, dead eyes)
│   ├── finish.md            finish-grade work, emblems, multi-character staging
│   ├── blockout.md          video-to-video from a 3D blockout — NEW
│   ├── verify.md            the post-render discipline — NEW
│   ├── fixes.md             symptom → cause → fix
│   └── examples.md          seven worked prompts
└── scripts/seedance.py      models · blocks · budget · lint
```

## 6. Formerly `shot-builder-cinematic-action`

Same grammar, same block names, same linter. Prompts and saved `PROMPT SEGMENTS` packs written
under the old name work unchanged. If you have the old folder installed, delete it and install this
one — running both loads the same skill twice.

---

FRMWRKD · youtube.com/@FRMWRKD · Updates ship free through Gumroad.
