# Clothsomnia: packaging prompts

Paste this whole file into a **Claude chat** (claude.ai or the Claude app, not Claude Code) with the Higgsfield
connector turned on, then say: "Generate these 4 images with Higgsfield using my unlimited trial (use_unlim true)."

## Reference images (already uploaded to my Higgsfield workspace)

Pass all four as `image_references` on every generation:

- `90e9b3a6-ea1e-4f9a-b6e2-c876013ec899`: frosted zip bag, straight-on (clearest text)
- `170eed82-9628-4026-aa79-c7cc0f5eb4ac`: white gift box, front
- `dbc7d21c-215b-4c00-be4d-1d73369b353e`: zip bag on the navy/white hoodie
- `ffd47111-3e5d-4c2d-893e-094cb88173f5`: gift box with bags and hoodies

For a shot that features a specific hoodie, you can also add that colour's front reference ID from its prompt file
(e.g. `navy-white.md` or `burgundy-offwhite.md`).

## Model and settings (best available on the unlimited trial)

- **Images:** `gpt_image_2_6`, `quality: "medium"`, `resolution: "2k"`, `use_unlim: true` (the highest the free trial
  covers). GPT Image is the strongest trial model for printed text, which matters here.
- **Text check:** compare every letter on the packaging with the references and regenerate any image with a typo.

## Packaging description (include in every prompt)

**Frosted zip bag:** a matte, semi-transparent frosted white zip-lock bag. Printed in black:
- "Clothsomnia" at the top: "Cloth" in an upright serif, "somnia" in an italic serif.
- "MADE WITH CARE AND LOVE IN MOROCCO BY DREAMERS" in bold geometric sans-serif capitals, 4 lines.
- "BE THE DIFFERENCE" in small capitals.
- Instagram, TikTok and Facebook icons followed by "Clothsomnia" at the bottom.

The folded sherpa hoodie shows softly through the frosted plastic.

**Gift box:** a white rigid mailer box. "Cloth" (upright serif) above "somnia" (italic serif) in large black letters,
fine black wavy contour-line artwork in two corners, a vertical rule with "More Than Clothes" in the top-right
corner, a handwritten signature at bottom-left, and the social icons with "Clothsomnia" along the bottom edge.

Keep all printed text exactly as written above. No people, no other brand logos, no extra text. No hang tags. Real product photography, not a render, with neutral daylight. Hoodie colours must match the hex values in `colours.md`.

## Shots

1. **Gift box hero (1:1)**: The closed white gift box standing at a slight angle on a seamless warm-cream studio set,
   with a frosted bag holding the navy/white hoodie leaning beside it. Soft diffused light and gentle shadows,
   premium e-commerce quality.
2. **Unboxing flat lay (4:5)**: Top-down view of the open gift box. Inside, the frosted bag with a folded burgundy
   sherpa hoodie visible through it; the lid rests beside the box. Beige linen surface, a dried pampas sprig,
   soft morning daylight.
3. **Collection stack (4:5)**: Several frosted bags stacked neatly, each showing a different hoodie colour through the
   plastic (navy, burgundy, steel grey/black, black, white, cream, olive, grey), with the gift box on top. Warm minimalist shelf, editorial look.
4. **Bag close-up (4:5)**: Macro shot of the frosted bag over a folded cream sherpa hoodie. The fleece curls are
   visible through the plastic, and the "MADE WITH CARE AND LOVE IN MOROCCO BY DREAMERS" print is sharp. Shallow
   depth of field, soft side light.

## Video (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "720p"` (the highest the free trial covers), `use_unlim: true`.
Use the best gift-box image (shot 1 or 2) as `start_image` and the four packaging references as `image_references`.

5. **Unboxing (9:16, 10s, soft ambient audio)**: The lid of the white Clothsomnia gift box lifts off on its own
   (no hands), revealing the frosted bag. The bag gently opens and the folded sherpa hoodie rises slightly as if
   breathing. The camera slowly pushes in; warm, dreamy light. Ends on the "Clothsomnia" logo on the box lid.
   Keep all printed text legible and unchanged.
