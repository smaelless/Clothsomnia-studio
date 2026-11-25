# Clothsomnia: Black hoodie prompts

Paste this whole file into a **Claude chat** (claude.ai or the Claude app, not Claude Code) with the Higgsfield
connector turned on, then say: "Generate these 6 images with Higgsfield using my unlimited trial (use_unlim true)."

## Reference images (already uploaded to my Higgsfield workspace)

Pass all four as `image_references` on every generation:

- `1bacc6bc-425e-4add-90b7-20420888052a`: front, flat lay (ignore the hang tag)
- `0cc913ab-9a39-476e-8dc9-66b1379a4378`: front, laid out
- `970b01b2-a60d-4256-adc3-a5998c6a3dd1`: sherpa texture close-up
- `8bfc9146-5820-49c8-b351-8dcdcb5bf9de`: side / sleeve detail

## Model and settings (best available on the unlimited trial)

- **Images:** `gpt_image_2_6`, `quality: "max"`, `resolution: "4k"`, `use_unlim: true`.
- **If the trial rejects max/4k:** step down one notch at a time (`xhigh`, then `high`; `4k`, then `2k`) and keep the
  highest setting it accepts.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "4k"`, same four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos (colours, panel shapes, sherpa texture) and regenerate any image
  that changes the design.

## Product description (include in every prompt)

Oversized solid jet-black curly sherpa fleece pullover hoodie, dropped shoulders, black hood, black ribbed cuffs and hem band, kangaroo pocket, small label inside the neck. The curly sherpa texture must stay visible, not a flat black shape. Reproduce the colour layout, proportions and curly sherpa texture exactly as in the references. No people, no mannequin visible, no other brand logos, no hang tags, no text overlays.

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless deep charcoal with a subtle gradient backdrop, soft diffused key
   light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view.
3. **Macro detail (4:5)**: Extreme close-up of the sherpa fleece and the neckline/label area, shallow depth of
   field, soft raking light that shows every curl of the fleece.
4. **Lifestyle A (4:5)**: The hoodie draped over a chair on a Casablanca street at night, Art Deco facade behind, warm street lamps and wet pavement reflections, moody streetwear editorial. Lifestyle brand photography.
5. **Lifestyle B (4:5)**: The hoodie hanging from a hook on a plain white-washed wall, one hard beam of sunlight cutting across the fleece, high-contrast minimal look. Editorial fashion photography.
6. **Folded flat lay (1:1)**: Neatly folded hoodie, top-down, on matte black slate with a silver ring and a pair of black sunglasses (unbranded), soft even daylight, premium feel.

## Videos (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "4k"` (fallback `1080p`), `use_unlim: true`.
Use the best generated studio image (shot 1) as `start_image` and the four reference photos as `image_references`.
No people, no text.

7. **Hero turntable (1:1, 8s, no audio)**: The hoodie on an invisible mannequin slowly rotates 360° on the
   deep charcoal with a subtle gradient studio set; the sherpa fleece catches the soft light; smooth, loopable.
8. **Lifestyle motion (3:4, 10s, soft ambient audio)**: A slow cinematic dolly-in on the scene from shot 4,
   with gentle natural movement in the light and air, ending on a close-up of the fleece texture.
