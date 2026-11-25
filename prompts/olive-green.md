# Clothsomnia: Olive Green hoodie prompts

Paste this whole file into a **Claude chat** (claude.ai or the Claude app, not Claude Code) with the Higgsfield
connector turned on, then say: "Generate these 6 images with Higgsfield using my unlimited trial (use_unlim true)."

## Reference images (already uploaded to my Higgsfield workspace)

Pass all four as `image_references` on every generation:

- `bfe8842e-4b2f-49c3-9d6b-65376d7c47ce`: front view (worn: use only for the garment, ignore the person)
- `b49ebb57-09c1-4860-8f04-d29d5c3259b9`: back view (worn: use only for the garment, ignore the person)
- `c1b94720-b961-43a0-8bfb-1795317de4b6`: fleece texture and hood close-up
- `e5119c64-ac91-4dec-bd4f-99f7da3c5642`: relaxed fit, how the fleece drapes

## Model and settings (best available on the unlimited trial)

- **Images:** `gpt_image_2_6`, `quality: "medium"`, `resolution: "2k"`, `use_unlim: true`. This is the highest
  setting the free trial covers (2k max, quality low/medium only); anything above it costs credits.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "2k"`, same four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos (colours, panel shapes, sherpa texture) and regenerate any image
  that changes the design.

## Product description (include in every prompt)

Oversized solid muted olive / sage green sherpa fleece pullover hoodie, dropped shoulders, olive hood, olive ribbed cuffs and hem band, kangaroo pocket. These references are on-model photos: copy only the hoodie, not the person. Reproduce the colour layout, proportions and curly sherpa texture exactly as in the references. No people, no mannequin visible, no other brand logos, no hang tags, no text overlays.

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless warm stone-beige backdrop, soft diffused key
   light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view.
3. **Macro detail (4:5)**: Extreme close-up of the sherpa fleece and the neckline/label area, shallow depth of
   field, soft raking light that shows every curl of the fleece.
4. **Lifestyle A (4:5)**: The hoodie tossed on a light-grey linen sofa with a chunky knit blanket and a book, soft afternoon window light, lazy Sunday mood. Lifestyle brand photography.
5. **Lifestyle B (4:5)**: The hoodie hanging on a wooden peg in a cedar cabin in the Atlas mountains, misty forest through the window, soft natural light. Editorial fashion photography.
6. **Folded flat lay (1:1)**: Neatly folded hoodie, top-down, on raw wood with a sprig of olive branch and a clay mug, soft even daylight, premium feel.

## Videos (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "720p"` (the highest the free trial covers),
`use_unlim: true`. Use the four reference photos as `image_references`. No people, no text.
Video 7 uses the best studio image (shot 1) as `start_image`; video 8 uses the approved shot 4 image.

7. **Hero turntable (1:1, 8s, no audio, start_image = shot 1)**: The hoodie on an invisible mannequin slowly rotates 360° on the
   warm stone-beige studio set; the sherpa fleece catches the soft light; smooth, loopable.
8. **Lifestyle motion (3:4, 10s, soft ambient audio, start_image = shot 4)**: A slow cinematic dolly-in on the scene from shot 4,
   with gentle natural movement in the light and air, ending on a close-up of the fleece texture.
