# Clothsomnia – Navy/White hoodie: generation prompts

Paste this whole file into a **Claude chat** (claude.ai or the Claude app, not Claude Code) that has the Higgsfield connector,
then say: "Generate these 6 images with Higgsfield using my unlimited trial (use_unlim true)."

## Reference images (already uploaded to my Higgsfield workspace)

Pass all four as `image_references` on every generation:

- `6477b042-a764-46d2-8299-5c5636207328`: front, flat lay
- `5c696f73-8bf4-4028-b9e2-f0218953fb73`: back, flat lay
- `10b9483e-7dcf-4569-abbe-97bf4187bfd3`: "Clothsomnia" neck label close-up
- `a7f4d315-b866-438e-ae63-669b091471bb`: sherpa texture / hem detail

## Model and settings (best available on the unlimited trial)

- **Images:** `gpt_image_2_6`, `quality: "max"`, `resolution: "4k"`, `use_unlim: true`.
  It is the most accurate trial model at copying a product from reference photos.
- **If the trial rejects max/4k:** step down one notch at a time (`xhigh`, then `high`; `4k`, then `2k`) and keep the
  highest setting it accepts.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "4k"`, all four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos: the panel shapes, the navy colour and the sherpa texture must match.
  Regenerate any image that changes the design.

## Product description (keep in every prompt)

Oversized sherpa fleece pullover hoodie, deep navy with two wide off-white sherpa panels running diagonally
from the shoulders down to the hem on the front; the white panels continue down the sides of the back. Navy hood,
navy ribbed cuffs and hem band, kangaroo pocket, small "Clothsomnia" script label inside the neck.
Reproduce the colour-block layout, proportions and curly sherpa texture exactly. No people, no other brand logos,
no hang tags, no text overlays.

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless warm light-grey backdrop, soft diffused
   key light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view, showing how the white panels wrap to the back.
3. **Macro detail (4:5)**: Extreme close-up where navy and off-white sherpa meet at the seam, with the
   "Clothsomnia" neck label visible, shallow depth of field, soft raking light to show the fleece curls.
4. **Cozy bed (4:5)**: The hoodie casually laid on an unmade bed with crisp white linen, morning sunlight
   through sheer curtains, warm and dreamy, a cup of mint tea on a bedside table, lifestyle brand photography.
5. **Moroccan riad (4:5)**: The hoodie draped over a carved cedar-wood chair in a sunlit Moroccan riad courtyard,
   zellige tiles, terracotta pots, soft golden-hour light, editorial fashion photography.
6. **Folded flat-lay (1:1)**: Neatly folded hoodie, top-down, on a beige linen surface with minimal props
   (dried pampas grass, a small ceramic dish), soft even daylight, premium packaging-shot feel.

## Videos (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "4k"` (fallback `1080p`), `use_unlim: true`.
This is the strongest video model on the trial. Use the best generated studio image (shot 1) as `start_image` and the
four reference photos as `image_references`. No people, no text.

7. **Hero turntable (1:1, 8s, no audio)**: The hoodie on an invisible mannequin slowly rotates 360° on the
   light-grey studio set; the sherpa fleece catches the soft light; smooth, loopable.
8. **Cozy morning (3:4, 10s, soft ambient audio)**: Slow cinematic dolly-in across the bed from shot 4: sunlight
   moves across the hoodie, the curtains drift in a light breeze, dust motes float in the light; ends on a close-up of
   the "Clothsomnia" neck label.
