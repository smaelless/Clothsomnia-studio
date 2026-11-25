# Clothsomnia: Burgundy/Off-white hoodie prompts

Paste this whole file into a **Claude chat** (claude.ai or the Claude app, not Claude Code) with the Higgsfield
connector turned on, then say: "Generate these 6 images with Higgsfield using my unlimited trial (use_unlim true)."

## Reference images (already uploaded to my Higgsfield workspace)

Pass all four as `image_references` on every generation:

- `dbaaaaf3-f4a7-45cd-b718-6becc30185b9`: front, flat lay
- `3eabe880-ceea-4da3-880f-6dc8cece5f60`: back view (worn: use only for the garment's back, ignore the person)
- `45f90e6a-28bc-4a5c-97a0-3ccd1a64e696`: "Clothsomnia" neck label close-up
- `7c86c63c-5f2b-49f0-a262-7286508e144f`: sleeve and panel texture detail

## Model and settings (best available on the unlimited trial)

- **Images:** `gpt_image_2_6`, `quality: "max"`, `resolution: "4k"`, `use_unlim: true`.
- **If the trial rejects max/4k:** step down one notch at a time (`xhigh`, then `high`; `4k`, then `2k`) and keep the
  highest setting it accepts.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "4k"`, same four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos (colours, panel shapes, sherpa texture) and regenerate any image
  that changes the design.

## Product description (include in every prompt)

Oversized sherpa fleece pullover hoodie, deep burgundy / wine red with two wide off-white sherpa panels running diagonally from the shoulders down to the hem on the front; the off-white panels continue down the sides of the back. Burgundy hood, burgundy ribbed cuffs and hem band, kangaroo pocket, small dark "Clothsomnia" script label inside the neck. Reproduce the colour layout, proportions and curly sherpa texture exactly as in the references. No people, no mannequin visible, no other brand logos, no hang tags, no text overlays.

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless warm cream backdrop, soft diffused key
   light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view.
3. **Macro detail (4:5)**: Extreme close-up of the sherpa fleece and the neckline/label area, shallow depth of
   field, soft raking light that shows every curl of the fleece.
4. **Lifestyle A (4:5)**: The hoodie draped over a deep velvet armchair beside a softly glowing fireplace, a knitted throw and a steaming cup of tea nearby, cozy winter evening light. Lifestyle brand photography.
5. **Lifestyle B (4:5)**: The hoodie hung on a brass hook against a hand-painted Moroccan tiled wall in deep reds and creams, warm light from a pierced-metal lantern. Editorial fashion photography.
6. **Folded flat lay (1:1)**: Neatly folded hoodie, top-down, on warm oatmeal linen with a few dried rose petals and a brass tray, soft even daylight, premium feel.

## Videos (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "4k"` (fallback `1080p`), `use_unlim: true`.
Use the best generated studio image (shot 1) as `start_image` and the four reference photos as `image_references`.
No people, no text.

7. **Hero turntable (1:1, 8s, no audio)**: The hoodie on an invisible mannequin slowly rotates 360° on the
   warm cream studio set; the sherpa fleece catches the soft light; smooth, loopable.
8. **Lifestyle motion (3:4, 10s, soft ambient audio)**: A slow cinematic dolly-in on the scene from shot 4,
   with gentle natural movement in the light and air, ending on a close-up of the fleece texture.
