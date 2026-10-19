# 5 Claude Skills That Replace Your Meta Ads Agency

<aside>
🤍

Hey, it's Cindy 🤍 Here are 5 Claude skills that do the work agencies charge $5–10K a month for: competitor spying, bulk creative, and account health checks in minutes.

</aside>

---

## Table of Contents

## The Problem

Running Meta ads manually is a full-time job.

Every week you're manually scrolling the Ad Library to see what competitors are running. You're briefing copywriters and waiting days for variations. You're spending money on creative before you know if the hook, copy, or CTA is any good.

Agencies charge $5–10K/month to handle this. Claude does it in minutes.

Here are the 5 skills that replace them.

---

## Skill 1 — /spy

**What it does:** Pulls every active ad from any Facebook page via the Meta Ad Library API. Diffs against last week's pull to surface only new creative. Returns a structured intelligence report with hooks, CTAs, offer types, creative angles, and how long each ad has been running.

**What you find out:**

- Which hooks your competitors are testing right now
- Which ads have been running 30+ days (the winners)
- What new creative they launched this week

**Install:**

```
npx skills add https://github.com/AgriciDaniel/claude-ads
```

> **Prerequisite:** You'll need a Meta Ad Library API access token. Set it as `$META_ACCESS_TOKEN` in your environment.
> 

---

## Skill 2 — /competitive-ads-extractor

**What it does:** Give it 3–5 competitor names or URLs. It pulls their active ads, ranks hooks by how often they appear, identifies offer structures and CTA patterns, then outputs a gap analysis showing emotional angles your competitors aren't using that you could own.

**The output:**

- Top hooks ranked by frequency
- Offer structure patterns across competitors
- CTA analysis
- Gap analysis — angles nobody in your market is running

**Install:**

```
npx skills add https://github.com/ComposioHQ/awesome-claude-skills/tree/master/competitive-ads-extractor
```

---

## Skill 3 — /bulk-creative

**What it does:** Give it your product description and your CLAUDE.md brand context. Generates 20 distinct ad copy variations — short, medium, and long format — in about 10 minutes. What used to take a copywriter 4–8 hours.

**How to get the most out of it:**

Make sure your CLAUDE.md has your brand voice, your target audience, and your core offer before running this. The richer the context, the tighter the output.

**Install:**

```
npx skills add https://github.com/AgriciDaniel/claude-ads
```

---

## Skill 4 — /ads meta

**What it does:** Runs 186 checks across your Meta account. Detects creative fatigue, audience overlap, CPM anomalies, and frequency violations. Returns a unified health score from 0 to 100 with a prioritised action plan.

**What it catches:**

- Creative fatigue before your ROAS drops
- Audience overlap eating your own budget
- Frequency violations and CPM anomalies
- Placement underperformance

**Install:**

```
npx skills add https://github.com/AgriciDaniel/claude-ads
```

> Run `/ads meta` before making any budget changes. Think of it as your account health check.
> 

---

## Skill 5 — /ads-score

**What it does:** Paste in any ad — yours or a competitor's. It scores it across 6 dimensions on a 1–10 scale and tells you exactly where it's weak and why — before you put money behind it.

**The 6 dimensions:**

1. Hook strength
2. Copy effectiveness
3. CTA clarity
4. Emotional resonance
5. Offer structure
6. Visual-copy alignment

**Install:**

```
npx skills add https://github.com/AgriciDaniel/claude-ads
```

> Run this on every ad before launch. If it scores below 7 on hook strength, rewrite the hook before spending a dollar.
> 

---

## How to Chain Them

These 5 skills work best in sequence:

1. Run `/spy` on Monday morning to see what competitors launched last week
2. Run `/competitive-ads-extractor` on your top 3–5 competitors to find the gaps
3. Use `/bulk-creative` to generate 20 variations targeting those gaps
4. Run `/ads-score` on your top 5 variations before launch
5. Run `/ads meta` weekly to catch fatigue and overlap before they hurt your numbers

The whole workflow takes under an hour. Agencies charge a monthly retainer for this.

---

## Setup Checklist

- [ ]  Install Claude Code: `npm install -g @anthropic-ai/claude-code`
- [ ]  Authenticate: run `claude` and sign in
- [ ]  Create your CLAUDE.md with your brand voice and audience: `~/.claude/CLAUDE.md`
- [ ]  Set your Meta API token: `export META_ACCESS_TOKEN=your_token_here`
- [ ]  Install claude-ads skill pack: `npx skills add https://github.com/AgriciDaniel/claude-ads`
- [ ]  Install competitive-ads-extractor: `npx skills add https://github.com/ComposioHQ/awesome-claude-skills/tree/master/competitive-ads-extractor`
- [ ]  Test `/spy` with one competitor handle
- [ ]  Run `/ads meta` on your account

---

## Follow for More