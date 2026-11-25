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

- **Images:** `gpt_image_2_6`, `quality: "medium"`, `resolution: "2k"`, `use_unlim: true`. This is the highest
  setting the free trial covers (2k max, quality low/medium only); anything above it costs credits.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "2k"`, same four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos (colours, panel shapes, sherpa texture) and regenerate any image
  that changes the design.

## Product description (include in every prompt)

Oversized sherpa fleece pullover hoodie, very dark navy (#1E1D28, almost black-blue, never bright or royal navy) centre panel in an inverted V (wide at the shoulders, narrowing to a point at the hem) with wide snow-white (#E5E2DE) sherpa side panels; the white panels continue down the sides of the back. Navy hood and sleeves, wide soft sherpa cuffs and hem band in navy, same fine pile as the body, NOT ribbed knit, diagonal slit pockets as a subtle seam only, nearly invisible, never a drawn line, no kangaroo pocket, no drawstrings, no hood cords, small "Clothsomnia" script label inside the neck. Reproduce the colour layout, proportions and curly sherpa texture exactly as in the references. The fleece is a FINE, TIGHT, SHORT curly pile (small dense curls like lamb's wool), not long fluffy teddy fur. No drawstrings, no hood cords, no prints or text on the outside of the garment. No people, no visible mannequin (studio shots use an invisible ghost-mannequin effect), no other brand logos, no hang tags, no text overlays.

**Realism (include in every prompt):** REALISM = real product photography for an online store, not an illustration or 3D render. Shot on a full-frame camera, 50-85mm lens, natural or softbox light, true-to-life colour that matches the references. Fabric must behave like real heavy fleece: soft weight, natural wrinkles and folds where it bends, slight imperfections, visible individual curls, no plastic sheen, no airbrushed smoothness, no glow, no HDR, no over-sharpening. Keep the exact same colours in every image (see the colour lock), neutral daylight only, never warm or coloured light on the garment. Simple believable scenes only, ordinary real-life props, no fantasy lighting. If a render looks AI-made, CGI or glossy, regenerate it.

**Colour lock (include in every prompt):** Navy #1E1D28 (very dark, almost black-blue) for centre, hood, sleeves, cuffs and hem; snow-white #E5E2DE for the side panels. Measured from the real product photos. If a render is lighter, bluer, warmer, greener or more saturated than these values, regenerate it.

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless warm light-grey backdrop, soft diffused key
   light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view.
3. **Macro detail (4:5)**: Extreme close-up of the sherpa fleece and the neckline/label area, shallow depth of
   field, soft raking light that shows every curl of the fleece.
4. **Lifestyle A (4:5)**: The hoodie laid on an unmade bed with crisp white linen, soft overcast morning daylight through sheer curtains, a glass of water on the bedside table. Lifestyle brand photography.
5. **Lifestyle B (4:5)**: The hoodie draped over a plain wooden chair in a bright room with a whitewashed wall, soft window daylight, one terracotta pot nearby. Editorial fashion photography.
6. **Folded flat lay (1:1)**: Neatly folded hoodie, top-down, on beige linen surface with dried pampas grass and a small ceramic dish, soft even daylight, premium feel.

## Videos (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "720p"` (the highest the free trial covers),
`use_unlim: true`. Use the four reference photos as `image_references`. No people, no text.
Video 7 uses the best studio image (shot 1) as `start_image`; video 8 uses the approved shot 4 image; video 9 uses shot 1 again.

7. **Hero turntable (1:1, 8s, no audio, start_image = shot 1)**: The hoodie on an invisible mannequin slowly rotates 360° on the
   warm light-grey studio set; the sherpa fleece catches the soft light; smooth, loopable.
8. **Lifestyle motion (3:4, 10s, soft ambient audio, start_image = shot 4)**: A slow cinematic dolly-in on the scene from shot 4,
   with gentle natural movement in the light and air, ending on a close-up of the fleece texture.
9. **Reels cut (9:16, 8s, soft ambient audio, start_image = shot 1)**: Vertical clip for Meta Reels and Stories. A slow vertical push-in
   on the hoodie on the warm light-grey studio set, a gentle fabric ripple as if a breeze passes, ending on a close-up of the fleece curls.
