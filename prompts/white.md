# Clothsomnia: White hoodie prompts

Paste this whole file into a **Claude chat** (claude.ai or the Claude app, not Claude Code) with the Higgsfield
connector turned on, then say: "Generate these 6 images with Higgsfield using my unlimited trial (use_unlim true)."

## Reference images (already uploaded to my Higgsfield workspace)

Pass all four as `image_references` on every generation:

- `d5ac7a02-9916-43a7-9131-4ac7244a32c8`: front, full flat lay (best reference)
- `69ae6ff2-ca8a-45c3-b5d0-30a89bffe439`: side flat lay
- `30c1bd0e-5190-4abb-8a18-bb86380302bc`: hood and neck label detail (ignore the hang tag)
- `c55d7baf-a4b5-4264-8641-90acbe68c62c`: fleece texture and cuff detail

## Model and settings (best available on the unlimited trial)

- **Images:** `gpt_image_2_6`, `quality: "medium"`, `resolution: "2k"`, `use_unlim: true`. This is the highest
  setting the free trial covers (2k max, quality low/medium only); anything above it costs credits.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "2k"`, same four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos (colours, panel shapes, sherpa texture) and regenerate any image
  that changes the design.

## Product description (include in every prompt)

Oversized clean snow-white (#E5E2DE, slightly cool) sherpa fleece pullover hoodie, dropped shoulders, white hood, wide soft sherpa cuffs and hem band in white, same fine pile as the body, NOT ribbed knit, kangaroo pocket, small dark woven label inside the neck. Keep the white clean and neutral, not cream or yellow. Reproduce the colour layout, proportions and curly sherpa texture exactly as in the references. The fleece is a FINE, TIGHT, SHORT curly pile (small dense curls like lamb's wool), not long fluffy teddy fur. No drawstrings, no hood cords, no prints or text on the outside of the garment. No people, no visible mannequin (studio shots use an invisible ghost-mannequin effect), no other brand logos, no hang tags, no text overlays.

**Realism (include in every prompt):** REALISM = real product photography for an online store, not an illustration or 3D render. Shot on a full-frame camera, 50-85mm lens, natural or softbox light, true-to-life colour that matches the references. Fabric must behave like real heavy fleece: soft weight, natural wrinkles and folds where it bends, slight imperfections, visible individual curls, no plastic sheen, no airbrushed smoothness, no glow, no HDR, no over-sharpening. Keep the exact same colours in every image (see the colour lock), neutral daylight only, never warm or coloured light on the garment. Simple believable scenes only, ordinary real-life props, no fantasy lighting. If a render looks AI-made, CGI or glossy, regenerate it.

**Colour lock (include in every prompt):** Snow-white #E5E2DE everywhere (slightly cool white, cooler and slightly lighter than the cream Off-White #E8DFCE; not cream, not pure #FFFFFF). Measured from the real product photos. If a render is lighter, bluer, warmer, greener or more saturated than these values, regenerate it.

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless soft pale grey (so the white stands out) backdrop, soft diffused key
   light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view. NOTE: this colourway has no back-view reference. Upload a real back photo and add its ID to image_references first, otherwise skip this shot (the model would invent the back).
3. **Macro detail (4:5)**: Extreme close-up of the sherpa fleece and the neckline/label area, shallow depth of
   field, soft raking light that shows every curl of the fleece.
4. **Lifestyle A (4:5)**: The hoodie folded at the foot of a bed with soft grey linen in a bright minimalist bedroom, cool morning light, airy and calm. Lifestyle brand photography.
5. **Lifestyle B (4:5)**: The hoodie hanging on a plain wooden hanger against a pale sand plaster wall, soft daylight, the white clearly distinct from the wall. Editorial fashion photography.
6. **Folded flat lay (1:1)**: Neatly folded hoodie, top-down, on light-grey linen with a eucalyptus sprig and a white ceramic cup, soft even daylight, premium feel.

## Videos (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "720p"` (the highest the free trial covers),
`use_unlim: true`. Use the four reference photos as `image_references`. No people, no text.
Video 7 uses the best studio image (shot 1) as `start_image`; video 8 uses the approved shot 4 image; video 9 uses shot 1 again.

7. **Hero turntable (1:1, 8s, no audio, start_image = shot 1)**: The hoodie on an invisible mannequin slowly rotates 360° on the
   soft pale grey (so the white stands out) studio set; the sherpa fleece catches the soft light; smooth, loopable.
8. **Lifestyle motion (3:4, 10s, soft ambient audio, start_image = shot 4)**: A slow cinematic dolly-in on the scene from shot 4,
   with gentle natural movement in the light and air, ending on a close-up of the fleece texture.
9. **Reels cut (9:16, 8s, soft ambient audio, start_image = shot 1)**: Vertical clip for Meta Reels and Stories. A slow vertical push-in
   on the hoodie on the soft pale grey (so the white stands out) studio set, a gentle fabric ripple as if a breeze passes, ending on a close-up of the fleece curls.
