# Asset Planning Reference

Use this to decide what the user should generate/upload before final video prompting.

## Asset Types

- **Character sheet**: identity anchor for the creator. Use for same face, hair, body type, wardrobe logic, and expression range.
- **First-frame still**: literal opening frame for Seedance. Use when the first 0:00-0:02 must match a specific composition.
- **Key-beat stills**: optional stills for important moments such as product hold, reaction, CTA, or transformation.
- **Solo reference shot**: clean single image of the intended creator when the character sheet is too broad or the first frame needs a natural pose.
- **Product reference**: product/prop truth: shape, color, label, packaging, orientation, and handling.
- **Voice ID/audio reference**: voice timbre and texture or exact voiceover.
- **Motion reference video**: the source video or generated previous clip used for pacing, movement, camera behavior, or extension.

## When To Recommend Each Asset

- Character consistency matters -> character sheet.
- The hook frame must match a specific visual -> first-frame still.
- Product is handled, shown near lens, opened, poured, applied, or demonstrated -> product reference.
- Hands/props are complex -> key-beat stills plus physics locks.
- User wants the same voice quality -> voice ID/audio reference.
- User wants to copy movement/editing from the reference -> keep the original video as motion reference.
- User wants an extension -> previous generated clip as `@Video1`.

## Seedance Reference Roles

Use only assets the user has or plans to upload:

- `@Image1`: character sheet, start frame, or subject reference. State the role clearly.
- `@Image2`: product, last frame, secondary prop, or environment reference.
- `@Video1`: motion reference or previous generated clip for extension.
- `@Audio1`: exact voiceover or voice ID.

Character sheet rule: use as identity anchor only. Do not animate or recreate its grid unless explicitly requested.

## Asset Plan Template

```markdown
## Asset Plan
- Character identity: [needed/not needed] - [why]
- First-frame still: [needed/not needed] - [why]
- Key-beat stills: [beats] - [why]
- Product reference: [needed/not needed] - [why]
- Voice/audio: [exact VO / voice ID / none]
- Motion reference: [reference video / previous clip / none]

## Suggested Upload Roles
- @Image1 = [...]
- @Image2 = [...]
- @Video1 = [...]
- @Audio1 = [...]
```
