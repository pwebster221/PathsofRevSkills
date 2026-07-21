# VenusFace distill — stage 1: VISION

The unique soul-render. Fuse the card's persona pole with its dragon prompt.
Consumes `enrichment-context?track=vision` (persona, pole, dragon_prompt).
Op: generate (gpt-image-2, 9:16). Proven: Emperor/Hierophant/Lovers/Chariot
shadow renders, 2026-07-08.

## Method

1. **Dragon prompt first, verbatim.** The card's `dragon_prompt` is the body
   and the colors — it opens the prompt unchanged. Never rewrite it; the
   decan palette it carries is canon.
2. **Extract the pole from the persona.** The tier chose the pole (zodiac→
   shadow §Defense, planetary→gift §Gift, mother→interaction §Defense+Gift
   held together). Read only that pole's section(s) of the persona plus §2
   (the faces) for staging material.
3. **Distill to 2–3 positioning-and-attitude directives** — a second
   paragraph opening "Positioning and attitude — the {persona epithet}, at
   its {pole}:". Each directive must be *stageable*: a placement, a bearing,
   a gaze, a relation between figure and ground. Interior states must be
   translated to composition ("founds-to-be-seen" → banners hung to be
   witnessed; "the unreachable ideal" → a luminous city past the wall the
   gaze reaches toward). Never paste persona prose; never psychology the
   renderer can't paint.
4. **Close with the ache.** One sentence naming the emotional register the
   composition should carry ("the ache of authority-as-image…").

## Guardrails

- The persona is a scoring instrument ~190 lines long — never include it
  wholesale; the model drowns in unpaintable psychology.
- Natal glyphs/degrees from the dragon prompt stay exact (23°13′ etc.).
- persona=null → render the dragon prompt alone, un-enriched. No invention.

## Worked example (Emperor, shadow)

Dragon prompt verbatim, then: presiding over a realm it has itself founded,
staged as its own mirror and proof · bearing self-witnessing, ruling for the
eyes upon it · gaze past the founded realm toward a luminous ideal kingdom
on the horizon it can never possess · ache: dominion raised as the shape of
a self.
