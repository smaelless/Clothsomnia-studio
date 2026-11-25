# Clothsomnia: Navy/White hoodie prompts

Paste this whole file into a **Claude chat** (claude.ai or the Claude app, not Claude Code) with the Higgsfield
connector turned on, then say: "Generate these 6 images with Higgsfield using my unlimited trial (use_unlim true)."

## Reference images (already uploaded to my Higgsfield workspace)

Pass all four as `image_references` on every generation:

- `6477b042-a764-46d2-8299-5c5636207328`: front, flat lay
- `5c696f73-8bf4-4028-b9e2-f0218953fb73`: back, flat lay
- `10b9483e-7dcf-4569-abbe-97bf4187bfd3`: "Clothsomnia" neck label close-up
- `a7f4d315-b866-438e-ae63-669b091471bb`: sherpa texture / hem detail

## Model and settings (best available on the unlimited trial)

- **Images:** `gpt_image_2_6`, `quality: "max"`, `resolution: "4k"`, `use_unlim: true`.
- **If the trial rejects max/4k:** step down one notch at a time (`xhigh`, then `high`; `4k`, then `2k`) and keep the
  highest setting it accepts.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "4k"`, same four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos (colours, panel shapes, sherpa texture) and regenerate any image
  that changes the design.

## Product description (include in every prompt)

Oversized sherpa fleece pullover hoodie, deep navy with two wide off-white sherpa panels running diagonally from the shoulders down to the hem on the front; the white panels continue down the sides of the back. Navy hood, navy ribbed cuffs and hem band, kangaroo pocket, small "Clothsomnia" script label inside the neck. Reproduce the colour layout, proportions and curly sherpa texture exactly as in the references. No people, no mannequin visible, no other brand logos, no hang tags, no text overlays.

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless warm light-grey backdrop, soft diffused key
   light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view.
3. **Macro detail (4:5)**: Extreme close-up of the sherpa fleece and the neckline/label area, shallow depth of
   field, soft raking light that shows every curl of the fleece.
4. **Lifestyle A (4:5)**: The hoodie casually laid on an unmade bed with crisp white linen, morning sunlight through sheer curtains, a cup of mint tea on the bedside table, warm and dreamy. Lifestyle brand photography.
5. **Lifestyle B (4:5)**: The hoodie draped over a carved cedar-wood chair in a sunlit Moroccan riad courtyard, zellige tiles, terracotta pots, soft golden-hour light. Editorial fashion photography.
6. **Folded flat lay (1:1)**: Neatly folded hoodie, top-down, on beige linen surface with dried pampas grass and a small ceramic dish, soft even daylight, premium feel.

## Videos (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "4k"` (fallback `1080p`), `use_unlim: true`.
Use the best generated studio image (shot 1) as `start_image` and the four reference photos as `image_references`.
No people, no text.

7. **Hero turntable (1:1, 8s, no audio)**: The hoodie on an invisible mannequin slowly rotates 360° on the
   warm light-grey studio set; the sherpa fleece catches the soft light; smooth, loopable.
8. **Lifestyle motion (3:4, 10s, soft ambient audio)**: A slow cinematic dolly-in on the scene from shot 4,
   with gentle natural movement in the light and air, ending on a close-up of the fleece texture.
