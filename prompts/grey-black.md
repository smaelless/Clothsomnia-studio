# Clothsomnia: Grey/Black hoodie prompts

Paste this whole file into a **Claude chat** (claude.ai or the Claude app, not Claude Code) with the Higgsfield
connector turned on, then say: "Generate these 6 images with Higgsfield using my unlimited trial (use_unlim true)."

## Reference images (already uploaded to my Higgsfield workspace)

Pass all four as `image_references` on every generation:

- `539300ee-b420-41a2-93c8-66dd08a29a49`: front, flat lay
- `b9b2ebff-c419-4490-ba08-2497537669d7`: back view (worn: use only for the garment's back, ignore the person)
- `af4970ae-b9c0-40bb-9480-63f4b9ae0cac`: hood and neck label detail
- `83e47eae-914b-48d6-8db1-1b480e2b9a9a`: grey/black seam and texture detail

## Model and settings (best available on the unlimited trial)

- **Images:** `gpt_image_2_6`, `quality: "max"`, `resolution: "4k"`, `use_unlim: true`.
- **If the trial rejects max/4k:** step down one notch at a time (`xhigh`, then `high`; `4k`, then `2k`) and keep the
  highest setting it accepts.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "4k"`, same four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos (colours, panel shapes, sherpa texture) and regenerate any image
  that changes the design.

## Product description (include in every prompt)

Oversized sherpa fleece pullover hoodie, cool slate blue-grey with two wide black sherpa panels running diagonally from the shoulders down to the hem on the front; the black panels continue down the sides of the back. Grey hood, grey ribbed cuffs and hem band, kangaroo pocket, small "Clothsomnia" script label inside the neck. Reproduce the colour layout, proportions and curly sherpa texture exactly as in the references. No people, no mannequin visible, no other brand logos, no hang tags, no text overlays.

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless cool mid-grey backdrop, soft diffused key
   light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view.
3. **Macro detail (4:5)**: Extreme close-up of the sherpa fleece and the neckline/label area, shallow depth of
   field, soft raking light that shows every curl of the fleece.
4. **Lifestyle A (4:5)**: The hoodie laid over a raw concrete bench on a city rooftop at blue hour, soft city lights blurred in the background, calm urban mood. Lifestyle brand photography.
5. **Lifestyle B (4:5)**: The hoodie hanging on a matte-black steel rail in a minimalist concrete loft with large windows, soft overcast daylight. Editorial fashion photography.
6. **Folded flat lay (1:1)**: Neatly folded hoodie, top-down, on smooth light-grey concrete with a black ceramic cup and a pair of wireless headphones (unbranded), soft even daylight, premium feel.

## Videos (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "4k"` (fallback `1080p`), `use_unlim: true`.
Use the best generated studio image (shot 1) as `start_image` and the four reference photos as `image_references`.
No people, no text.

7. **Hero turntable (1:1, 8s, no audio)**: The hoodie on an invisible mannequin slowly rotates 360° on the
   cool mid-grey studio set; the sherpa fleece catches the soft light; smooth, loopable.
8. **Lifestyle motion (3:4, 10s, soft ambient audio)**: A slow cinematic dolly-in on the scene from shot 4,
   with gentle natural movement in the light and air, ending on a close-up of the fleece texture.
