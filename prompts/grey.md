# Clothsomnia: Grey hoodie prompts

Paste this whole file into a **Claude chat** (claude.ai or the Claude app, not Claude Code) with the Higgsfield
connector turned on, then say: "Generate these 6 images with Higgsfield using my unlimited trial (use_unlim true)."

## Reference images (already uploaded to my Higgsfield workspace)

Pass all four as `image_references` on every generation:

- `205a3007-7340-43aa-b882-c1b4905d3476`: front view (worn: use only for the garment, ignore the person)
- `2fced592-a34b-497f-b347-cc4c35f46018`: back view (worn: use only for the garment, ignore the person)
- `f5e74915-1854-4887-9c76-0d0ae0ece19d`: sherpa texture close-up
- `3c681b3e-d758-47eb-bd0e-65ed1d522f42`: hood up, hood shape

## Model and settings (best available on the unlimited trial)

- **Images:** `gpt_image_2_6`, `quality: "medium"`, `resolution: "2k"`, `use_unlim: true`. This is the highest
  setting the free trial covers (2k max, quality low/medium only); anything above it costs credits.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "2k"`, same four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos (colours, panel shapes, sherpa texture) and regenerate any image
  that changes the design.

## Product description (include in every prompt)

Oversized solid cool slate grey (neutral mid-grey, about #6D6C76 / RGB 109, 108, 118; not charcoal, not silver, not blue-grey, not beige-grey) sherpa fleece pullover hoodie, dropped shoulders, roomy soft hood, wide soft sherpa cuffs and hem band in grey, same fine pile as the body, NOT ribbed knit, one large kangaroo pocket. The fleece is a FINE, TIGHT, SHORT curly pile (small dense curls like lamb's wool, as in the texture reference), not long fluffy teddy fur. Plain front and back: no drawstrings, no hood cords, no logos, no prints, no text. These references are on-model photos: copy only the hoodie, not the person. Reproduce the colour layout, proportions and curly sherpa texture exactly as in the references. The fleece is a FINE, TIGHT, SHORT curly pile (small dense curls like lamb's wool), not long fluffy teddy fur. No drawstrings, no hood cords, no prints or text on the outside of the garment. No people, no visible mannequin (studio shots use an invisible ghost-mannequin effect), no other brand logos, no hang tags, no text overlays.

**Realism (include in every prompt):** REALISM = real product photography for an online store, not an illustration or 3D render. Shot on a full-frame camera, 50-85mm lens, natural or softbox light, true-to-life colour that matches the references. Fabric must behave like real heavy fleece: soft weight, natural wrinkles and folds where it bends, slight imperfections, visible individual curls, no plastic sheen, no airbrushed smoothness, no glow, no HDR, no over-sharpening. Keep the exact same slate grey in every image (do not drift to charcoal, blue, or lavender under warm light). Simple believable scenes only, ordinary real-life props, no fantasy lighting. If a render looks AI-made, CGI or glossy, regenerate it.

**Colour lock (include in every prompt):** Slate grey #6D6C76 (RGB 109,108,118) everywhere. Measured from the real product photos. If a render is lighter, bluer, warmer, greener or more saturated than these values, regenerate it.

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless light warm grey (#D9D6D2) backdrop, soft diffused key
   light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view.
3. **Macro detail (4:5)**: Close-up of the sherpa fleece at the chest and the hood seam, 85-100mm macro look, shallow depth of field, soft side light so every individual curl of the pile is visible. Real fabric, tight curls, no fur-like strands.
4. **Lifestyle A (4:5)**: The hoodie draped over the back of a plain wooden chair in a real home interior next to a window, soft overcast daylight, one ceramic mug on a table nearby, natural creases, shallow depth of field. Lifestyle brand photography.
5. **Lifestyle B (4:5)**: The hoodie hanging on a plain wooden hanger on a white plaster wall (slightly textured, as in a real room), soft window light from the side, gentle natural shadow, no props. Editorial fashion photography.
6. **Folded flat lay (1:1)**: Neatly folded hoodie, top-down, on a plain off-white linen cloth, no props, soft even daylight, premium feel.

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
