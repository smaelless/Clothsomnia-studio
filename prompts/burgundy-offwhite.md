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

- **Images:** `gpt_image_2_6`, `quality: "medium"`, `resolution: "2k"`, `use_unlim: true`. This is the highest
  setting the free trial covers (2k max, quality low/medium only); anything above it costs credits.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "2k"`, same four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos (colours, panel shapes, sherpa texture) and regenerate any image
  that changes the design.

## Product description (include in every prompt)

Oversized sherpa fleece pullover hoodie, deep burgundy / wine red (#4C181F) centre panel in an inverted V (wide at the shoulders, narrowing to a point at the hem) with wide cream off-white (#E8DFCE, warmer and slightly darker than snow-white) sherpa side panels; the off-white panels continue down the sides of the back. Burgundy hood and sleeves, wide soft sherpa cuffs and hem band in burgundy, same fine pile as the body, NOT ribbed knit, diagonal slit pockets as a subtle seam only, nearly invisible, never a drawn line, no kangaroo pocket, no drawstrings, no hood cords, small dark "Clothsomnia" script label inside the neck. Reproduce the colour layout, proportions and curly sherpa texture exactly as in the references. The fleece is a FINE, TIGHT, SHORT curly pile (small dense curls like lamb's wool), not long fluffy teddy fur. No drawstrings, no hood cords, no prints or text on the outside of the garment. No people, no visible mannequin (studio shots use an invisible ghost-mannequin effect), no other brand logos, no hang tags, no text overlays.

**Realism (include in every prompt):** REALISM = real product photography for an online store, not an illustration or 3D render. Shot on a full-frame camera, 50-85mm lens, natural or softbox light, true-to-life colour that matches the references. Fabric must behave like real heavy fleece: soft weight, natural wrinkles and folds where it bends, slight imperfections, visible individual curls, no plastic sheen, no airbrushed smoothness, no glow, no HDR, no over-sharpening. Keep the exact same colours in every image (see the colour lock), neutral daylight only, never warm or coloured light on the garment. Simple believable scenes only, ordinary real-life props, no fantasy lighting. If a render looks AI-made, CGI or glossy, regenerate it.

**Colour lock (include in every prompt):** Burgundy #4C181F (deep wine red) for centre, hood, sleeves, cuffs and hem; cream off-white #E8DFCE for the side panels (cream is warmer and slightly darker than snow-white; never render the two whites the same). Measured from the real product photos. If a render is lighter, bluer, warmer, greener or more saturated than these values, regenerate it.

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless light warm grey (#D9D6D2) backdrop, soft diffused key
   light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view.
3. **Macro detail (4:5)**: Extreme close-up of the sherpa fleece and the neckline/label area, shallow depth of
   field, soft raking light that shows every curl of the fleece.
4. **Lifestyle A (4:5)**: The hoodie draped over a plain armchair beside a window in a living room, soft overcast daylight, a knitted throw and a cup of tea nearby. Lifestyle brand photography.
5. **Lifestyle B (4:5)**: The hoodie hung on a brass hook against a plain cream plaster wall, soft window light from the side, no props. Editorial fashion photography.
6. **Folded flat lay (1:1)**: Neatly folded hoodie, top-down, on warm oatmeal linen with a few dried rose petals and a brass tray, soft even daylight, premium feel.

## Videos (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "720p"` (the highest the free trial covers),
`use_unlim: true`. Use the four reference photos as `image_references`. No people, no text.
Video 7 uses the best studio image (shot 1) as `start_image`; video 8 uses the approved shot 4 image; video 9 uses shot 1 again.

7. **Hero turntable (1:1, 8s, no audio, start_image = shot 1)**: The hoodie on an invisible mannequin slowly rotates 360° on the
   light warm grey (#D9D6D2) studio set; the sherpa fleece catches the soft light; smooth, loopable.
8. **Lifestyle motion (3:4, 10s, soft ambient audio, start_image = shot 4)**: A slow cinematic dolly-in on the scene from shot 4,
   with gentle natural movement in the light and air, ending on a close-up of the fleece texture.
9. **Reels cut (9:16, 8s, soft ambient audio, start_image = shot 1)**: Vertical clip for Meta Reels and Stories. A slow vertical push-in
   on the hoodie on the light warm grey (#D9D6D2) studio set, a gentle fabric ripple as if a breeze passes, ending on a close-up of the fleece curls.
