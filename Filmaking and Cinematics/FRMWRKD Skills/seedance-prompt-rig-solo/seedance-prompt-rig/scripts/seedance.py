#!/usr/bin/env python3
"""seedance.py — capability lookup, block reference, budgets, and a prompt linter
for the Prompt Rig schema (01 CONTEXT / 02 BEATS / 03 PROMPT SEGMENTS).
Part of the seedance-prompt-rig skill, made by FRMWRKD.

    python3 seedance.py models
    python3 seedance.py models --model 2.5
    python3 seedance.py blocks
    python3 seedance.py blocks --tier beats
    python3 seedance.py budget --duration 30
    python3 seedance.py lint prompt.txt --model 2.5 --duration 30
    python3 seedance.py lint prompt.txt --model 2.0 --duration 10 --strict

No dependencies. Exit code 1 if the linter finds an ERROR, 0 otherwise
(WARNs never fail the run, so it is safe in a pipeline).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------------
# capability table, verified 2026-08
# --------------------------------------------------------------------------

MODELS = {
    "1.0-lite": {
        "label": "Seedance 1.0 lite",
        "durations": (2, 12),
        "resolutions": ["480p", "720p", "1080p"],
        "audio": False,
        "refs": {"image": 4, "video": 0, "audio": 0, "total": 4},
        "cut_budget": 2,
        "chars": 4000,
        "note": "SILENT. Deprecated on fal (redirects to pro/fast). Cheapest blocking passes.",
    },
    "1.0-pro": {
        "label": "Seedance 1.0 pro / pro-fast",
        "durations": (2, 12),
        "resolutions": ["480p", "720p", "1080p"],
        "audio": False,
        "refs": {"image": 2, "video": 0, "audio": 0, "total": 2},
        "cut_budget": 2,
        "chars": 4000,
        "note": "SILENT. First+last frame only. pro-fast is ~$0.05/s at 1080p and genuinely fast.",
    },
    "1.5": {
        "label": "Seedance 1.5 pro",
        "durations": (4, 12),
        "resolutions": ["480p", "720p", "1080p"],
        "audio": True,
        "refs": {"image": 2, "video": 0, "audio": 0, "total": 2},
        "cut_budget": 3,
        "chars": 5000,
        "note": "Native audio. First+last frame only. Audio DOUBLES the price on this model.",
    },
    "2.0": {
        "label": "Seedance 2.0 / fast / mini",
        "durations": (4, 15),
        "resolutions": ["480p", "720p", "1080p", "4k"],
        "audio": True,
        "refs": {"image": 9, "video": 3, "audio": 3, "total": 12},
        "cut_budget": 4,
        "chars": 6000,
        "note": "Only version with 4K. Audio is free. Reference videos bill for their own duration.",
    },
    "2.5": {
        "label": "Seedance 2.5",
        "durations": (4, 30),
        "resolutions": ["480p", "720p"],
        "audio": True,
        "refs": {"image": 30, "video": 10, "audio": 10, "total": 50},
        "cut_budget": 6,
        "chars": 20000,
        "note": "Longest take, widest reference net, 20,000-character prompt window. CAPPED AT 720p.",
    },
}

ALIASES = {
    "1": "1.0-pro", "1.0": "1.0-pro", "v1": "1.0-pro", "pro": "1.0-pro",
    "lite": "1.0-lite", "1.0lite": "1.0-lite", "1-0-lite": "1.0-lite",
    "1.5pro": "1.5", "1-5": "1.5", "v1.5": "1.5",
    "2": "2.0", "v2": "2.0", "2-0": "2.0",
    "2-5": "2.5", "v2.5": "2.5",
}

# --------------------------------------------------------------------------
# the twenty-seven blocks
# --------------------------------------------------------------------------

CONTEXT_BLOCKS = {
    "SCENE CONTEXT": "the scene itself, in a paragraph",
    "FORMAT MODE": "duration, aspect, fps, cut budget",
    "ACTIVE REFERENCES": "the bound plates, and the exclusions on each",
    "LOCATION MAP": "the space and its distances",
    "CAST": "who is in it, and what stays identical about each",
    "STAGING": "blocking relative to camera",
    "WARDROBE": "what is worn, and what must not change",
    "GAZE AND EYELINES": "attention and its direction",
    "EVENT AND SHARED DIRECTION": "the scene's single intent",
    "RULES": "the do-not-break list",
}
BEAT_BLOCKS = {
    "OPEN": "the first frame, already moving",
    "ACTION": "what happens, in order",
    "CAMERA": "the shot's single move",
    "LENS": "framing for this beat only",
    "PERFORMANCE": "the performance beat",
    "DIALOGUE": "the words spoken in this shot",
    "SFX": "this beat's own sound",
    "EDIT": "the out-point — cut, morph, dissolve or hold",
}
SEGMENT_BLOCKS = {
    "PHYSICS": "how bodies and matter behave",
    "LIGHTING": "every source, named and placed",
    "AUDIO": "ambience, and what is banned from it",
    "SCORE": "music — or plainly that there is none",
    "STYLE": "capture format, optics, palette",
    "STYLE LOCK": "the anti-drift clause for stylised work",
    "TYPOGRAPHY": "type, weight, and how it enters and leaves",
    "VOICE": "accent, register, delivery",
    "POSITIVE LOCKS": "constraints written as assertions",
}
# named sub-blocks of the finish register; they sit in the CONTEXT tier
SUB_BLOCKS = {
    "ACTING TASK": "one per character, the investment in a tactic",
    "MICRO-BEHAVIOUR": "the anti-glassy-stare safety block",
    "MICRO-BEHAVIOR": "the anti-glassy-stare safety block",
}

TIER_OF: dict[str, str] = {}
for _k in CONTEXT_BLOCKS: TIER_OF[_k] = "context"
for _k in SUB_BLOCKS: TIER_OF[_k] = "context"
for _k in BEAT_BLOCKS: TIER_OF[_k] = "beats"
for _k in SEGMENT_BLOCKS: TIER_OF[_k] = "segments"
ALL_BLOCKS = set(TIER_OF)

BEAT_HEAD_RE = re.compile(r"^\s*(?:#{1,4}\s*)?(BEAT|SHOT|SEGMENT)\s*[-–—]?\s*(\d+)\b", re.I)
KEY_RE = re.compile(r"^\s*([A-Z][A-Z0-9 '\-]*[A-Z])\s*:")

# --------------------------------------------------------------------------
# budgets
# --------------------------------------------------------------------------

WORDS_PER_SECOND_COMFORT = 2.0
WORDS_PER_SECOND_CEILING = 2.5
WORDS_PER_SECOND_SPARSE = 1.5          # when the pauses are the content

# The rig prices what you actually loaded. A block you did not load costs
# nothing and buys nothing; a block you did load gets a real allowance.
CONTEXT_PER_BLOCK, CONTEXT_CAP = 35, 480     # + 25 per reference beyond two, + 5 per beat
BEAT_PER_BLOCK, BEAT_PER_SECOND = 18, 8      # only ACTION and PERFORMANCE really scale with time
SEGMENTS_PER_BLOCK, SEGMENTS_CAP = 38, 360
BEAT_FLOOR, BEAT_CAP = 80, 260
HARD_WORDS = 3000

CAPS_BUDGET = 6
CAPS_VOCAB = {"ONE", "ONLY", "NEVER", "NOT", "NO", "NOBODY", "SAME", "EXACT", "EXACTLY", "EVERY"}
CAPS_RE = r"\b(ONE|ONLY|NEVER|NOT|NOBODY|NO|SAME|EXACTLY|EXACT|EVERY)\b"
VIDEO_ROLE_WORDS = 60   # a blockout / previz gets one compact line, then the prompt moves on
SHOUT_RUN = 4           # this many consecutive capitalised words is a wall, not a lock


def context_budget(n_blocks: int, n_refs: int, n_beats: int = 1) -> int:
    """35 words a block, plus 25 for every reference beyond the second (a scoped
    role line runs 15-25 words and every reference needs one), plus 5 a beat
    because a GAZE ladder and a STAGING exception list grow with the beat count."""
    return min(CONTEXT_CAP,
               CONTEXT_PER_BLOCK * n_blocks + 25 * max(0, n_refs - 2) + 5 * max(0, n_beats))


def beat_budget(n_blocks: int, seconds: float | None) -> int:
    """18 words a block of near-constant overhead, plus 8 per second of screen
    time — which is what ACTION and PERFORMANCE actually spend. `seconds` is THIS
    beat's screen time, not the whole clip's."""
    return max(BEAT_FLOOR, min(BEAT_CAP,
               int(BEAT_PER_BLOCK * max(1, n_blocks) + BEAT_PER_SECOND * (seconds or 6))))


def segments_budget(n_blocks: int) -> int:
    """38 words a block. This tier is written once and pasted forever, so it is
    the cheapest words you will ever buy — but an unfilled block is still noise."""
    return min(SEGMENTS_CAP, SEGMENTS_PER_BLOCK * max(1, n_blocks))


def working_ceiling(duration: float | None) -> int:
    """Adherence, not the parser, is the limit — and it scales with duration."""
    if not duration:
        return 900
    return int(400 + 45 * duration)


# camera moves that must not co-occur inside a single CAMERA field
MOVE_TERMS = [
    "push in", "push-in", "creep in", "pull out", "pull-out", "pull back", "dolly in", "dolly out",
    "pan", "whip pan", "tilt", "track", "tracking", "follow", "orbit", "arc around",
    "crane", "boom", "zoom", "rack focus", "dolly zoom", "drone", "aerial", "roll",
]
MOVE_QUALIFIERS = {"handheld", "hand-held", "hand-felt", "gimbal", "steadicam", "locked", "static", "fixed"}

STOPWORDS = {
    "the", "a", "an", "and", "or", "of", "in", "on", "at", "to", "it", "is", "are", "was",
    "were", "as", "with", "for", "from", "by", "that", "this", "his", "her", "their", "its",
    "he", "she", "they", "him", "them", "not", "no", "so", "but", "then", "than", "into",
    "over", "under", "out", "up", "down", "one", "two", "all", "every", "any", "each",
}


def resolve_model(name: str) -> str:
    key = (name or "").strip().lower().replace("seedance", "").strip(" -_")
    if key in MODELS:
        return key
    if key in ALIASES:
        return ALIASES[key]
    raise SystemExit(
        f"unknown model {name!r}. known: {', '.join(sorted(MODELS))} "
        f"(aliases: {', '.join(sorted(ALIASES))})"
    )


def words(s: str) -> int:
    return len(re.findall(r"[A-Za-z0-9'’-]+", s))


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------

def cmd_models(args) -> int:
    keys = [resolve_model(args.model)] if args.model else list(MODELS)
    for k in keys:
        m = MODELS[k]
        lo, hi = m["durations"]
        r = m["refs"]
        print(f"\n{m['label']}   [{k}]")
        print(f"  duration      {lo}-{hi}s (integer)" + ("  or auto" if k in ("2.0", "2.5") else ""))
        print(f"  resolution    {' / '.join(m['resolutions'])}")
        print(f"  fps           24 (fixed, not a parameter)")
        print(f"  audio         {'native' if m['audio'] else 'NONE — silent video'}")
        print(f"  references    {r['image']} img / {r['video']} vid / {r['audio']} aud, {r['total']} total")
        print(f"  cut budget    {m['cut_budget']} beats per clip")
        print(f"  prompt window ~{m['chars']:,} characters")
        print(f"  note          {m['note']}")
    if not args.model:
        print("\nfps is 24 on every version. negative_prompt exists on no Seedance endpoint.")
    print()
    return 0


def cmd_blocks(args) -> int:
    tiers = [
        ("01 CONTEXT — one scene, written once", CONTEXT_BLOCKS, "context"),
        ("02 BEATS — one shot each", BEAT_BLOCKS, "beats"),
        ("03 PROMPT SEGMENTS — many projects", SEGMENT_BLOCKS, "segments"),
    ]
    want = (args.tier or "").lower()
    for title, blocks, key in tiers:
        if want and want not in key:
            continue
        print(f"\n{title}")
        for name, job in blocks.items():
            print(f"  {name:<28} {job}")
    if not want or want == "context":
        print("\n   finish-register sub-blocks (CONTEXT tier)")
        for name, job in SUB_BLOCKS.items():
            if name == "MICRO-BEHAVIOR":
                continue
            print(f"  {name:<28} {job}")
    print("\n27 keys. SCENE CONTEXT is always present; the other 26 are added when the job needs them.")
    print("Order in the delivered prompt is CONTEXT -> BEATS -> PROMPT SEGMENTS.\n")
    return 0


def cmd_budget(args) -> int:
    d = args.duration
    print(f"\nclip {d}s")
    print(f"  dialogue comfortable      {int(d * WORDS_PER_SECOND_COMFORT)} words")
    print(f"  dialogue ceiling          {int(d * WORDS_PER_SECOND_CEILING)} words")
    print(f"  dialogue when the pauses")
    print(f"    are the content         {int(d * WORDS_PER_SECOND_SPARSE)} words")
    print("  past the ceiling the model compresses delivery and lip-sync desyncs")
    print(f"\nprompt budgets for a {d}s clip — the rig prices the blocks you load")
    print(f"  CONTEXT tier              {CONTEXT_PER_BLOCK} w/block, +25 per reference beyond two,")
    print(f"                            +5 per beat (cap {CONTEXT_CAP})")
    for n in (5, 7, 10):
        print(f"    {n:>2} blocks, 3 refs       {context_budget(n, 3, 4)} words")
    print(f"  one BEAT                  {BEAT_PER_BLOCK} w/block + {BEAT_PER_SECOND} x that beat's seconds "
          f"(floor {BEAT_FLOOR}, cap {BEAT_CAP})")
    print(f"  PROMPT SEGMENTS tier      {SEGMENTS_PER_BLOCK} w/block (cap {SEGMENTS_CAP})")
    print()
    for k in (1, 2, 3, 6):
        per = d / k
        bb = beat_budget(7, per)
        total = context_budget(7, 3, k) + segments_budget(7) + bb * k
        print(f"    {k} beat(s), {per:>5.1f}s each   {bb:>3} w/beat   total ~{total:>5} w "
              f"(7 blocks a tier, 3 refs)")
    print(f"\n  working ceiling           {working_ceiling(d)} words  (400 + 45 x duration)")
    print(f"  hard ceiling              {HARD_WORDS:,} words / 20,000 characters (Seedance 2.5 API cap)")
    print(f"  capitals                  {CAPS_BUDGET} per BEAT, from "
          f"{' '.join(sorted(CAPS_VOCAB - {'EXACTLY'}))}")
    print()
    return 0


# --------------------------------------------------------------------------
# parsing
# --------------------------------------------------------------------------

class Block:
    __slots__ = ("key", "value", "region", "line")

    def __init__(self, key: str, value: str, region: str, line: int) -> None:
        self.key, self.value, self.region, self.line = key, value, region, line

    def __repr__(self) -> str:  # pragma: no cover
        return f"<{self.key} @{self.region}>"


def parse(text: str) -> tuple[list[Block], int, list[str]]:
    """Walk the prompt and assign every recognised block to a region.

    Regions are 'context', 'beat:<n>' and 'segments'. A BEAT/SHOT/SEGMENT
    heading opens a beat region. The first PROMPT SEGMENTS key seen after a
    beat has opened closes the beats and opens the segments region — which is
    exactly the delivered order, so this needs no lookahead.

    Returns (blocks, n_beats, unknown_keys).
    """
    lines = text.splitlines()
    blocks: list[Block] = []
    unknown: list[str] = []
    region = "context"
    n_beats = 0
    cur: Block | None = None

    for i, ln in enumerate(lines, 1):
        head = BEAT_HEAD_RE.match(ln)
        if head:
            n_beats += 1
            region = f"beat:{n_beats}"
            cur = None
            continue
        m = KEY_RE.match(ln)
        if m:
            key = re.sub(r"\s+", " ", m.group(1)).strip()
            val = ln.split(":", 1)[1]
            if key in ALL_BLOCKS:
                tier = TIER_OF[key]
                if tier == "segments" and region.startswith("beat:"):
                    region = "segments"
                elif tier == "beats" and region == "context" and n_beats == 0:
                    # a single-beat prompt written without a BEAT heading
                    n_beats = 1
                    region = "beat:1"
                cur = Block(key, val, region, i)
                blocks.append(cur)
                continue
            # an ALL-CAPS key that is not one of the 27
            if len(key) > 2 and key not in {"NOTE", "TODO", "MODEL", "POOL", "PRESET"}:
                unknown.append(f"{key} (line {i})")
            cur = None
            continue
        if cur is not None:
            cur.value += "\n" + ln

    return blocks, max(n_beats, 1 if blocks else 0), unknown


def region_text(blocks: list[Block], pred) -> str:
    return "\n".join(f"{b.key}: {b.value}" for b in blocks if pred(b))


def learn_names(cast_text: str) -> set[str]:
    """Character names are written in caps on purpose — the rig forbids pronouns
    across characters, so the name appears every time. Learn them from CAST so the
    capitals check does not flag the one thing it is supposed to encourage."""
    skip = set(CAPS_VOCAB)
    for k in ALL_BLOCKS:
        skip.update(k.split())
    return {t for t in re.findall(r"\b[A-Z]{2,}\b", cast_text) if t not in skip}


def stray_caps(s: str, names: set[str] = frozenset()) -> list[str]:
    toks = re.findall(r"\b[A-Z]{2,}\b", s)
    skip = set(CAPS_VOCAB) | set(names)
    for k in ALL_BLOCKS:
        skip.update(re.split(r"[\s-]+", k))          # MICRO-BEHAVIOUR → MICRO, BEHAVIOUR
    skip.update({"BEAT", "SHOT", "SEGMENT", "HARD", "CUT", "AT", "US", "OK", "AND", "TASK"})
    return [t for t in toks if t not in skip and not re.fullmatch(r"[0-9K]+", t)]


def shouted_runs(s: str, n: int = SHOUT_RUN) -> list[str]:
    """Runs of n+ consecutive ALL-CAPS words (3+ letters) that are not block keys.
    `THERE IS NO DANCING IN THIS VIDEO` is a run; `NOT the pose, NOT the framing` is not."""
    out = []
    for line in s.splitlines():
        body = re.sub(r"^[A-Z][A-Z -]+:", "", line)         # strip a leading block key
        toks = re.findall(r"[A-Za-z][A-Za-z'’-]*", body)
        run: list[str] = []
        for t in toks + ["end"]:
            if len(t) >= 2 and t.isupper():
                run.append(t)
            else:
                if len(run) >= n:
                    out.append(" ".join(run))
                run = []
    return out


def shingles(s: str, n: int = 5) -> set[str]:
    toks = [t for t in re.findall(r"[a-z]+", s.lower()) if t not in STOPWORDS and len(t) > 2]
    return {" ".join(toks[i:i + n]) for i in range(max(0, len(toks) - n + 1))}


# --------------------------------------------------------------------------
# linter
# --------------------------------------------------------------------------

class Report:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []

    def add(self, level, rule, msg): self.rows.append((level, rule, msg))
    def error(self, rule, msg): self.add("ERROR", rule, msg)
    def warn(self, rule, msg): self.add("WARN", rule, msg)
    def ok(self, rule, msg): self.add("ok", rule, msg)

    def emit(self, strict: bool) -> int:
        order = {"ERROR": 0, "WARN": 1, "ok": 2}
        for level, rule, msg in sorted(self.rows, key=lambda r: order[r[0]]):
            tag = {"ERROR": "ERROR", "WARN": " WARN", "ok": "   ok"}[level]
            print(f"{tag}  {rule:<20} {msg}")
        errs = sum(1 for r in self.rows if r[0] == "ERROR")
        warns = sum(1 for r in self.rows if r[0] == "WARN")
        print(f"\n{errs} error(s), {warns} warning(s)")
        return 1 if errs or (strict and warns) else 0


def lint(text: str, model_key: str, duration: int | None, strict: bool) -> int:
    m = MODELS[model_key]
    rep = Report()
    blocks, n_beats, unknown = parse(text)

    if not blocks:
        rep.error("structure", "no recognised blocks. Keys are ALL CAPS at the head of a line, "
                               "e.g. 'SCENE CONTEXT:'. Run `seedance.py blocks` for the list.")
        return rep.emit(strict)

    by_key: dict[str, list[Block]] = {}
    for b in blocks:
        by_key.setdefault(b.key, []).append(b)

    ctx = [b for b in blocks if b.region == "context"]
    segs = [b for b in blocks if b.region == "segments"]
    beats: dict[int, list[Block]] = {}
    for b in blocks:
        if b.region.startswith("beat:"):
            beats.setdefault(int(b.region.split(":")[1]), []).append(b)
    n_beats = max(len(beats), 1)

    # ---- unknown / misplaced blocks --------------------------------------
    for u in unknown:
        rep.error("blocks.unknown", f"{u} is not one of the 27 blocks. Do not invent block names.")
    if not unknown:
        rep.ok("blocks.unknown", f"{len(blocks)} block(s), all canonical")

    for b in blocks:
        tier = TIER_OF[b.key]
        if tier == "context" and b.region != "context":
            rep.error("blocks.tier", f"{b.key} (line {b.line}) is a CONTEXT block sitting in "
                                     f"{b.region}. It is true for the whole scene — hoist it.")
        if tier == "beats" and not b.region.startswith("beat:"):
            rep.error("blocks.tier", f"{b.key} (line {b.line}) is a BEAT block sitting in "
                                     f"{b.region}. Every beat block belongs under a BEAT heading.")
        if tier == "segments" and b.region != "segments":
            rep.error("blocks.tier", f"{b.key} (line {b.line}) is a PROMPT SEGMENTS block sitting in "
                                     f"{b.region}. It outlives this beat — move it to the bottom.")

    if "SCENE CONTEXT" not in by_key:
        rep.warn("blocks.required", "no SCENE CONTEXT. It is the one block that is always present.")
    for k in ("FORMAT MODE", "STYLE"):
        if k not in by_key:
            rep.warn("blocks.required", f"no {k}. Recommended in every preset.")

    # duplicate blocks in the same region
    for k, bs in by_key.items():
        seen: dict[str, int] = {}
        for b in bs:
            seen[b.region] = seen.get(b.region, 0) + 1
        for region, n in seen.items():
            if n > 1:
                rep.error("blocks.duplicate", f"{k} appears {n} times in {region}. One block, one home.")

    # register clash
    if "STYLE LOCK" in by_key and "POSITIVE LOCKS" in by_key:
        rep.warn("blocks.register", "STYLE LOCK and POSITIVE LOCKS both loaded. Photoreal takes "
                                    "POSITIVE LOCKS and no negations; stylised takes STYLE LOCK.")

    # ---- word budgets ----------------------------------------------------
    n_refs = len({t.lower() for t in re.findall(r"[@\[<]{1,3}\s?(?:Image|Video|Audio)\s?\d+", text, re.I)})
    ctx_w = words(region_text(blocks, lambda b: b.region == "context"))
    seg_w = words(region_text(blocks, lambda b: b.region == "segments"))
    beat_w = {n: words(region_text(blocks, lambda b, n=n: b.region == f"beat:{n}")) for n in beats}
    total_w, total_c = words(text), len(text)

    cbud = context_budget(len({b.key for b in ctx}), n_refs, n_beats)
    if ctx_w > cbud:
        rep.warn("budget.context", f"CONTEXT tier is {ctx_w}w, budget {cbud}w "
                                   f"({len({b.key for b in ctx})} blocks, {n_refs} refs). See density.md.")
    elif ctx_w:
        rep.ok("budget.context", f"CONTEXT {ctx_w}w / {cbud}w")

    sbud = segments_budget(len({b.key for b in segs}))
    if seg_w > sbud:
        rep.warn("budget.segments", f"PROMPT SEGMENTS is {seg_w}w, budget {sbud}w "
                                    f"({len({b.key for b in segs})} blocks).")
    elif seg_w:
        rep.ok("budget.segments", f"SEGMENTS {seg_w}w / {sbud}w")

    per_beat = duration / n_beats if duration else None
    bbuds = {n: beat_budget(len({b.key for b in bs}), per_beat) for n, bs in beats.items()}
    over = [f"beat {n} {w}w/{bbuds[n]}w" for n, w in sorted(beat_w.items()) if w > bbuds.get(n, 999)]
    if over:
        rep.warn("budget.beat", f"{', '.join(over)}"
                                + (f" at {per_beat:.1f}s each" if per_beat else "")
                                + ". Only ACTION and PERFORMANCE should scale with time.")
    elif beat_w:
        worst = max(beat_w, key=lambda n: beat_w[n] - bbuds.get(n, 0))
        rep.ok("budget.beat", f"{n_beats} beat(s), worst {beat_w[worst]}w / {bbuds[worst]}w")

    ceil = working_ceiling(duration)
    if total_c > m["chars"]:
        rep.error("budget.total", f"{total_c:,} characters exceeds {m['label']}'s ~{m['chars']:,}-char window.")
    elif total_w > HARD_WORDS:
        rep.error("budget.total", f"{total_w}w exceeds the {HARD_WORDS:,}w hard ceiling.")
    elif total_w > ceil:
        rep.warn("budget.total", f"{total_w}w over the {ceil}w working ceiling for {duration or '?'}s. "
                                 f"Adherence falls before the parser does — see density.md.")
    else:
        rep.ok("budget.total", f"{total_w}w / {ceil}w working ceiling, {total_c:,} chars")

    # ---- the lifespan check ---------------------------------------------
    # a fact repeated across beats is a constant that belongs in CONTEXT or
    # PROMPT SEGMENTS. It costs words per beat AND gives the model one fresh
    # chance per beat to render it differently.
    # Compared per block key, and only for the blocks where repetition is never
    # legitimate. A CAMERA line repeated verbatim across beats is a locked camera
    # held on purpose; an ACTION or OPEN line repeated is a constant in the wrong tier.
    LIFESPAN_KEYS = {"OPEN", "ACTION", "PERFORMANCE", "LENS", "DIALOGUE"}
    if len(beats) > 1:
        sh: dict[int, set[str]] = {}
        for n, bs in beats.items():
            acc: set[str] = set()
            for b in bs:
                if b.key in LIFESPAN_KEYS:
                    acc |= shingles(b.value)
            sh[n] = acc
        counts: dict[str, int] = {}
        for s in sh.values():
            for g in s:
                counts[g] = counts.get(g, 0) + 1
        shared = sorted((g for g, c in counts.items() if c > 1), key=len, reverse=True)
        # merge overlapping shingles into the longest distinct runs
        merged: list[str] = []
        for g in shared:
            if not any(g in mm for mm in merged):
                merged.append(g)
        if merged:
            cost = sum(len(g.split()) * (counts[g] - 1) for g in merged[:6])
            rep.warn("lifespan", f"{len(merged)} fact(s) restated across beats, ~{cost}w wasted and "
                                 f"{len(merged)} extra decision(s) for the model. Hoist to CONTEXT "
                                 f"or PROMPT SEGMENTS: " + " · ".join(f"“{g}”" for g in merged[:3]))
        else:
            rep.ok("lifespan", "no facts restated across beats")

    # ---- capitals discipline --------------------------------------------
    names = learn_names(" ".join(b.value for b in by_key.get("CAST", [])))
    if names:
        rep.ok("caps.names", f"cast names exempt from the capitals check: {', '.join(sorted(names))}")
    for n, bs in sorted(beats.items()):
        t = region_text(blocks, lambda b, n=n: b.region == f"beat:{n}")
        caps = re.findall(CAPS_RE, t)
        if len(caps) > CAPS_BUDGET:
            rep.warn("caps.budget", f"beat {n} uses {len(caps)} capitalised locks, budget {CAPS_BUDGET}.")
        stray = stray_caps(t, names)
        if stray:
            rep.warn("caps.vocab", f"beat {n} shouts outside the vocabulary: "
                                   f"{', '.join(sorted(set(stray))[:8])}")
    for label, region in (("CONTEXT", "context"), ("SEGMENTS", "segments")):
        stray = stray_caps(region_text(blocks, lambda b, r=region: b.region == r), names)
        if stray:
            rep.warn("caps.vocab", f"{label} shouts outside the vocabulary: "
                                   f"{', '.join(sorted(set(stray))[:8])}")

    # ---- one move per beat ----------------------------------------------
    for n, bs in sorted(beats.items()):
        cam = " ".join(b.value for b in bs if b.key == "CAMERA").lower()
        if not cam:
            rep.error("camera.one-move", f"beat {n} has no CAMERA. State the move, or state the lock.")
            continue
        if any(q in cam for q in MOVE_QUALIFIERS) and re.search(r"\b(lock|static|fixed)\w*", cam):
            rep.ok("camera.one-move", f"beat {n} camera locked")
            continue
        found = {t for t in MOVE_TERMS if re.search(r"\b" + re.escape(t) + r"\b", cam)}
        norm = {t.replace("-", " ").split()[0] for t in found}
        if len(norm) > 1:
            rep.error("camera.one-move", f"beat {n} stacks {len(norm)} moves ({', '.join(sorted(norm))}). "
                                         f"Keep one — a second move is a second beat and a cut.")
        elif norm:
            rep.ok("camera.one-move", f"beat {n} move: {sorted(norm)[0]}")

    for n in beats:
        if not any(b.key == "ACTION" for b in beats[n]):
            rep.warn("structure", f"beat {n} has no ACTION.")

    # ---- reference bindings ---------------------------------------------
    refs = " ".join(b.value for b in by_key.get("ACTIVE REFERENCES", []))
    if refs:
        bad = []
        for ln in [l for l in refs.splitlines() if l.strip()]:
            if not re.search(r"[@\[<]", ln):
                continue
            if "NOT" not in ln and "ONLY" not in ln:
                bad.append(ln.strip()[:52])
            if len(re.findall(r"[@\[<]{1,3}\s?(?:Image|Video|Audio)\s?\d+", ln, re.I)) > 1:
                rep.error("bind.one-role", f"two references on one line: {ln.strip()[:52]}…")
        for b_ in bad:
            rep.error("bind.exclusion", f"role line has no NOT clause: {b_}…")
        if not bad:
            rep.ok("bind.exclusion", "every role line carries an exclusion")
        # video references from a blockout / previz: one compact line, no shouting
        vid_lines = [l for l in refs.splitlines()
                     if re.search(r"[@\[<{]{1,3}\s?video\s?\d*", l, re.I)]
        for ln in vid_lines:
            if words(ln) > VIDEO_ROLE_WORDS:
                rep.warn("bind.video-role", f"video role line runs {words(ln)}w (keep under "
                                            f"{VIDEO_ROLE_WORDS}). One compact line for the video, then spend "
                                            f"the words on the performance — blockout.md.")
            if re.search(r"\b(IGNORE|DISREGARD)\b", ln) or shouted_runs(ln):
                rep.error("bind.video-role", f"video role line shouts: {ln.strip()[:52]}… Heavy negation makes "
                                             f"the actors copy the reference motion. State what it governs, "
                                             f"then NOT clauses, then stop — blockout.md.")
        if vid_lines and not any(rw[1] == "bind.video-role" for rw in rep.rows):
            rep.ok("bind.video-role", f"{len(vid_lines)} video role line(s), compact and quiet")
        # a turnaround bound 'identity ONLY' drops the wardrobe
        for ln in refs.splitlines():
            if re.search(r"[@\[<{]{1,3}\s?image", ln, re.I) and \
               re.search(r"\b(identity|face|likeness)\s+ONLY\b", ln):
                rep.warn("bind.identity-only", f"'{re.search(r'(identity|face|likeness) ONLY', ln).group(0)}' "
                                               f"reads as take the face, ignore the clothes. Bind face and whole "
                                               f"outfit, restate garments once in WARDROBE — blockout.md §5.")
    elif n_refs:
        rep.error("bind.exclusion", f"{n_refs} reference tag(s) in the prompt but no ACTIVE REFERENCES "
                                    f"block. An unbound reference still influences the render, uncontrolled.")

    counts: dict[str, int] = {}
    for kind in ("image", "video", "audio"):
        n = len({t.lower() for t in re.findall(r"[@\[<]{1,3}\s?" + kind + r"\s?(\d+)", text, re.I)})
        counts[kind] = n
        if n > m["refs"][kind]:
            rep.error("bind.budget", f"{n} {kind} refs, {m['label']} allows {m['refs'][kind]}.")
    if sum(counts.values()) > m["refs"]["total"]:
        rep.error("bind.budget", f"{sum(counts.values())} refs total, model allows {m['refs']['total']}.")
    if counts["image"] > 8:
        rep.warn("bind.stability", f"{counts['image']} image refs; quality is stable to about 8 subjects.")

    # ---- audio ------------------------------------------------------------
    speech = re.findall(r"\{([^}]*)\}", text)
    body = re.sub(r"<{2,}[^>]*>{2,}", "", text)
    if body.count("<") != body.count(">"):
        rep.error("audio.brackets", "unbalanced < > — SFX will leak into the track.")
    for o, c in (("{", "}"), ("(", ")")):
        if text.count(o) != text.count(c):
            rep.error("audio.brackets", f"unbalanced {o} {c}.")
    if speech:
        if not m["audio"]:
            rep.error("audio.model", f"dialogue present but {m['label']} produces SILENT video.")
        spoken = sum(words(s) for s in speech)
        if duration:
            hard = int(duration * WORDS_PER_SECOND_CEILING)
            comf = int(duration * WORDS_PER_SECOND_COMFORT)
            sparse = int(duration * WORDS_PER_SECOND_SPARSE)
            if spoken > hard:
                rep.error("audio.wpm", f"{spoken} spoken words over {duration}s; ceiling is {hard}. "
                                       f"Delivery will rush and lip-sync will slip.")
            elif spoken > comf:
                rep.warn("audio.wpm", f"{spoken} spoken words over {duration}s; comfortable is {comf}.")
            elif spoken > sparse:
                rep.ok("audio.wpm", f"{spoken} spoken words fits {duration}s ({spoken/duration:.1f} w/s)")
            else:
                rep.ok("audio.wpm", f"{spoken} spoken words over {duration}s ({spoken/duration:.1f} w/s) — "
                                    f"sparse register, the pauses carry it")
        langs = (r"english|mandarin|chinese|japanese|korean|spanish|indonesian|cantonese|"
                 r"sichuanese|portuguese|german|french|american speech|american english")
        anchor = " ".join(b.value for b in by_key.get("VOICE", [])) + " " + \
                 " ".join(b.value for b in by_key.get("DIALOGUE", []))
        if not re.search(langs, anchor, re.I):
            rep.warn("audio.language", "dialogue present with no language anchor in VOICE or DIALOGUE; "
                                       "the language will drift.")
        spk_names = learn_names(" ".join(b.value for b in by_key.get("CAST", [])))
        for n, bs in sorted(beats.items()):
            dl = " ".join(b.value for b in bs if b.key == "DIALOGUE")
            lines = re.findall(r"\{[^}]*\}", dl)
            # who speaks each line: the last cast name before the opening brace
            speakers, cursor = [], 0
            for mm in re.finditer(r"\{[^}]*\}", dl):
                seg = dl[cursor:mm.start()]
                found = [x for x in re.findall(r"\b[A-Z]{2,}\b", seg) if x in spk_names]
                if found:
                    speakers.append(found[-1])
                cursor = mm.end()
            distinct = len(set(speakers))
            if distinct > 1:
                rep.warn("audio.speakers", f"beat {n} has {distinct} speakers across {len(lines)} lines "
                                           f"({', '.join(sorted(set(speakers)))}). One speaker per beat is the "
                                           f"reliable shape — cut between them, or accept this as the test.")
            elif len(lines) > 1:
                rep.ok("audio.speakers", f"beat {n}: {len(lines)} lines, one speaker")
    if "AUDIO" in by_key and "SCORE" not in by_key and m["audio"]:
        rep.warn("audio.score", "no SCORE block. State 'SCORE: none.' or the model may invent music.")

    # ---- cuts -------------------------------------------------------------
    edits = [b for b in blocks if b.key == "EDIT"]
    cuts = sum(1 for b in edits if re.search(r"\bcut\b", b.value, re.I))
    shots = max(n_beats, cuts + 1)
    if shots > m["cut_budget"]:
        rep.error("cuts.budget", f"{shots} shots; {m['label']} holds about {m['cut_budget']} "
                                 f"before identity drifts. Split into two clips.")
    elif cuts:
        rep.ok("cuts.budget", f"{shots} shots, {cuts} cut(s), within budget")
    if n_beats > 1 and not edits:
        rep.warn("cuts.label", "multiple beats but no EDIT block; this renders as one continuous take.")
    if n_beats > 1 and len(edits) < n_beats - 1:
        rep.warn("cuts.label", f"{n_beats} beats but only {len(edits)} EDIT block(s). "
                               f"Every beat but the last needs an out-point.")

    # ---- events past the end of the clip ----------------------------------
    if duration:
        late = []
        for mm in re.finditer(r"(?<![\w.])(\d{1,2}(?:\.\d)?)\s*s\b", text):
            try:
                v = float(mm.group(1))
            except ValueError:
                continue
            if v > duration + 0.05:
                late.append(mm.group(0).strip())
        fmt_txt = " ".join(b.value for b in by_key.get("FORMAT MODE", []))
        late = [x for x in late if x not in fmt_txt]
        if late:
            rep.error("timing.range", f"{len(late)} timestamp(s) past the {duration}s clip end "
                                      f"({', '.join(late[:4])}). Events past the end never fire and nothing "
                                      f"fails loudly — verify.md §6.")

    # ---- shouting outside the closed vocabulary ---------------------------
    runs = shouted_runs(region_text(blocks, lambda b: True))
    if runs:
        rep.warn("caps.shout", f"{len(runs)} shouted run(s) of {SHOUT_RUN}+ capitalised words "
                               f"({runs[0][:40]}…). A wall of capitals flattens the weighting of the words "
                               f"that matter — sentence case, closed vocabulary only.")

    # ---- excluded room proportions ----------------------------------------
    if re.search(r"\bNOT\s+(?:its|the|their)\s+(?:\w+\s+){0,2}proportions\b", text):
        rep.warn("location.proportions", "'NOT … proportions' tells the model to discard the room. Describe the "
                                         "room by its contents and write any bend as this room extending — "
                                         "blockout.md §4.")

    # ---- timecodes --------------------------------------------------------
    tc = re.findall(r"\b\d{1,2}(?:\.\d)?\s*[-–]\s*\d{1,2}(?:\.\d)?\s*s\b", text, re.I)
    if tc and model_key not in ("2.5",):
        rep.warn("timing", f"{len(tc)} hard timecode(s). Prefer '→' ordering; strict markers destabilise "
                           f"timing on {m['label']}.")
    elif tc:
        rep.ok("timing", f"{len(tc)} timecode(s) — legal at the finish end on 2.5")

    # ---- locks ------------------------------------------------------------
    locks = " ".join(b.value for b in by_key.get("POSITIVE LOCKS", []))
    if locks:
        clauses = [c for c in re.split(r"[.;]", locks) if c.strip()]
        neg_in_locks = re.findall(r"\b(?:no|not|never|without)\s+\w+", locks, re.I)
        if len(clauses) > 6:
            rep.warn("locks.width", f"POSITIVE LOCKS has {len(clauses)} clauses; keep to 4-6. "
                                    f"Each one weakens the description.")
        else:
            rep.ok("locks.width", f"POSITIVE LOCKS {len(clauses)} clause(s), {words(locks)}w")
        if len(neg_in_locks) > 2 and "STYLE LOCK" not in by_key:
            rep.warn("locks.positive", f"{len(neg_in_locks)} negation(s) inside POSITIVE LOCKS. In photoreal "
                                       f"work the model parses the noun, not the negation — state the "
                                       f"positive: 'no extra people' → 'exactly two men are present'.")
    neg = len(re.findall(r"\b(no|not|never|without|avoid|zero)\b", text, re.I))
    if neg > 30:
        rep.warn("locks.global", f"{neg} negations across the prompt. Seedance has no negative_prompt; "
                                 f"these compete with the description for attention.")

    # ---- FORMAT MODE legality --------------------------------------------
    fmt = " ".join(b.value for b in by_key.get("FORMAT MODE", []))
    lo, hi = m["durations"]
    if duration is not None and not (lo <= duration <= hi):
        rep.error("format.duration", f"{duration}s illegal for {m['label']} ({lo}-{hi}s).")
    for res in re.findall(r"\b(480p|720p|1080p|2k|4k)\b", fmt, re.I):
        if res.lower() not in [r.lower() for r in m["resolutions"]]:
            rep.error("format.resolution", f"{res} unavailable on {m['label']} "
                                           f"({' / '.join(m['resolutions'])}).")
    outside = re.sub(re.escape(fmt), "", text) if fmt else text
    if re.search(r"\b\d{1,2}\s*:\s*\d{1,2}\b", outside):
        rep.warn("format.aspect", "aspect ratio outside FORMAT MODE. It is an API parameter — keep it "
                                  "in FORMAT MODE only.")
    if re.search(r"\b(\d{2,3})\s*fps\b", text, re.I) and not re.search(r"\b24\s*fps\b", text, re.I):
        rep.error("format.fps", "fps is fixed at 24 on every Seedance version.")

    # ---- misc -------------------------------------------------------------
    if re.search(r"negative[ _]prompt", text, re.I):
        rep.error("api", "no Seedance endpoint has a negative_prompt parameter. Use POSITIVE LOCKS.")
    typo = " ".join(b.value for b in by_key.get("TYPOGRAPHY", []))
    if re.search(r"【|〖", text) or (typo and not re.search(r"\bnone\b", typo, re.I)):
        rep.warn("text", "on-screen text requested. Corruption is near-unavoidable on every version — "
                         "generate clean and composite type in post.")
    if speech and "TYPOGRAPHY" not in by_key and "POSITIVE LOCKS" not in by_key:
        rep.warn("text", "speech present with neither TYPOGRAPHY nor POSITIVE LOCKS; subtitles often "
                         "burn in. Add 'TYPOGRAPHY: none.'")

    return rep.emit(strict)


def cmd_lint(args) -> int:
    p = Path(args.file)
    if not p.exists():
        raise SystemExit(f"no such file: {p}")
    key = resolve_model(args.model)
    print(f"\nlinting {p.name} against {MODELS[key]['label']}"
          + (f", {args.duration}s" if args.duration else "") + "\n")
    return lint(p.read_text(encoding="utf-8"), key, args.duration, args.strict)


def main() -> int:
    ap = argparse.ArgumentParser(prog="seedance", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("models", help="capability matrix")
    p.add_argument("--model")
    p.set_defaults(fn=cmd_models)

    p = sub.add_parser("blocks", help="the 27 blocks and their tiers")
    p.add_argument("--tier", help="context | beats | segments")
    p.set_defaults(fn=cmd_blocks)

    p = sub.add_parser("budget", help="word and dialogue budgets for a duration")
    p.add_argument("--duration", type=int, required=True)
    p.set_defaults(fn=cmd_budget)

    p = sub.add_parser("lint", help="check a prompt against the rig and the model")
    p.add_argument("file")
    p.add_argument("--model", required=True)
    p.add_argument("--duration", type=int)
    p.add_argument("--strict", action="store_true", help="fail on warnings too")
    p.set_defaults(fn=cmd_lint)

    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
