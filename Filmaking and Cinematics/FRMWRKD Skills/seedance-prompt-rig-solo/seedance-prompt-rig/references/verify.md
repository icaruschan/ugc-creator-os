# Verify before you assert

A prompt is cheap. A render is not. Almost every expensive mistake in a video session is the same
mistake: **claiming something instead of checking it.** The building was fine; the verifying of the
builder's own claims was where it failed. This file is the discipline that stops it.

It applies to the agent running this skill as much as to the person. When you write *fixed*, *done*,
*verified* or *nothing was generated*, one of the checks below must have actually run.

---

## 1 — Editing the source is not verifying the output

*Fixed* was written for a shot without opening the rendered file. The build script had been edited,
the edit was assumed to have landed, and the notes documented it as solved. The shot still opened on
a second of black.

**Rule:** the claim *fixed* is only allowed after the rendered file has been opened and the property
that was broken has been looked at. Not the script, not the log — the file.

---

## 2 — Judge exposure on one full-size frame

Two rounds of *too dark / too bright* corrections were made from a contact sheet, and both were
wrong. They ended the second one full-size frame was opened.

**Rule:** exposure, focus, skin, grain and eye-catchlights are judged on one frame at delivery
resolution. Contact sheets are for coverage and continuity, never for exposure.

---

## 3 — Test the property, not a proxy for it

A minimum-file-size check rejected a perfectly good near-black shot at 120 KB because *small file*
was standing in for *broken render*. Compression made the proxy lie.

**Rule:** test the thing you care about. *Do the frames differ from each other* (a frozen or
black clip) is a frame comparison. *Is the shot the right length* is a duration probe. Bytes are not
a test of anything.

```bash
# frame count and duration, not file size
ffprobe -v error -select_streams v:0 -count_frames \
  -show_entries stream=nb_read_frames,duration -of csv=p=0 shot.mp4

# mean luminance of frames 0, 12 and 24 — a black-opening clip shows it here
ffmpeg -v error -i shot.mp4 -vf "select='eq(n\,0)+eq(n\,12)+eq(n\,24)',signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | grep YAVG
```

---

## 4 — Provenance is not integrity

Two render queues ran at the same time. Every file either one produced passed every check, because
each file finished. Verification cannot tell you which code built a file — only that a file exists
and is well-formed.

**Rule:** one render job at a time, and the rule is a check (a lock file, a `pgrep` before launch),
not a sentence in a brief. The brief that said *do not run two render jobs* was broken by the person
who wrote it.

---

## 5 — An empty log is not a dead process

The duplicate queue was alive the whole time. Its log was empty because its output was pipe-buffered.

**Rule:** a process is dead when `pgrep` says so, not when its log stops growing. Run long jobs with
unbuffered output (`python3 -u`, `PYTHONUNBUFFERED=1`) so the log means something.

---

## 6 — Events must fall inside the shot

Beat events were authored without checking they landed inside the clip. Over half never fired — one
shot's event list ran to 28 s inside a 15 s shot — and nothing failed loudly. The peak was half as
dense as written.

**Rule:** every timestamp in a prompt is checked against the clip duration. The linter now errors on
any event past the end of the clip (`timing.range`). Sum the beats before writing the last one.

---

## 7 — Prose is advice; an assertion is a guarantee

Every rule in the brief that became a check caught errors repeatedly. Every rule that stayed a
sentence got violated, including the brief's own *don't run two render jobs*.

**Rule:** if a rule matters enough to write down, it matters enough to make mechanical. That is what
`seedance.py lint` is. Run it every time, before every spend, even on prompts you are sure about —
especially those.

---

## 8 — A document has to earn its authority

A *single source of truth* was written claiming nothing had been generated, without opening the
assets folder. Three approved plates were sitting in it.

**Rule:** before writing any status, ledger, or *what exists* document, list the folder. A document
claiming authority it has not earned is worse than no document — the next session trusts it.

---

## 9 — A stated constraint binds every later step

The location plate existed and had been mentioned. Two wrong generations were picked from history
instead of asking for the file, and a 2,000-credit run went out bound to the wrong room.

**Rule:** when the user has said a thing exists, ask once for it rather than guess twice. Every
constraint stated earlier in the session — the plate, the model, the ceiling, the cast — binds every
prompt written after it, without being restated.

---

## 10 — Read the scope of a rule, not its surface

*Don't upload* was about foreign material — plates from another tool, blockout frames. Re-uploading
the platform's own output was never the thing being forbidden, and it was the answer the whole time.
Over-applying the rule stalled the job.

**Rule:** when a rule blocks the only route forward, re-read what it was protecting against before
declaring the route closed.

---

## 11 — Retry before declaring impossible

An upload failed once on a full disk and was declared impossible. It succeeded on the next attempt.

**Rule:** a transient failure gets a second attempt after the obvious cause is cleared. *Impossible*
is a claim about the second try, not the first.

---

## 12 — The post-render check

After every render, before saying anything about it:

- [ ] Opened the file, not the log
- [ ] One full-size frame at the open, one in the middle, one at the close
- [ ] The frames differ (nothing frozen, nothing black)
- [ ] Duration matches `FORMAT MODE`
- [ ] The cuts are where the `EDIT` blocks put them
- [ ] The room is the room — fixtures visible, not just materials
- [ ] Wardrobe matches the plate garment for garment
- [ ] Nobody is copying the reference video's motion
- [ ] Only then: write what you saw, not what you expected

Change one thing and re-render. Not three — [fixes.md](fixes.md).
