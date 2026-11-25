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

- **Images:** `gpt_image_2_6`, `quality: "max"`, `resolution: "4k"`, `use_unlim: true`.
- **If the trial rejects max/4k:** step down one notch at a time (`xhigh`, then `high`; `4k`, then `2k`) and keep the
  highest setting it accepts.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "4k"`, same four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos (colours, panel shapes, sherpa texture) and regenerate any image
  that changes the design.

## Product description (include in every prompt)

Oversized pure bright-white sherpa fleece pullover hoodie, dropped shoulders, white hood, white ribbed cuffs and hem band, kangaroo pocket, small dark woven label inside the neck. Keep the white clean and neutral, not cream or yellow. Reproduce the colour layout, proportions and curly sherpa texture exactly as in the references. No people, no mannequin visible, no other brand logos, no hang tags, no text overlays.

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless soft pale grey (so the white stands out) backdrop, soft diffused key
   light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view.
3. **Macro detail (4:5)**: Extreme close-up of the sherpa fleece and the neckline/label area, shallow depth of
   field, soft raking light that shows every curl of the fleece.
4. **Lifestyle A (4:5)**: The hoodie folded at the foot of a bed with soft grey linen in a bright minimalist bedroom, cool morning light, airy and calm. Lifestyle brand photography.
5. **Lifestyle B (4:5)**: The hoodie hanging against a blue-washed wall in a Chefchaouen alley, potted plants, soft daylight, the white popping against the blue. Editorial fashion photography.
6. **Folded flat lay (1:1)**: Neatly folded hoodie, top-down, on light-grey linen with a eucalyptus sprig and a white ceramic cup, soft even daylight, premium feel.

## Videos (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "4k"` (fallback `1080p`), `use_unlim: true`.
Use the best generated studio image (shot 1) as `start_image` and the four reference photos as `image_references`.
No people, no text.

7. **Hero turntable (1:1, 8s, no audio)**: The hoodie on an invisible mannequin slowly rotates 360° on the
   soft pale grey (so the white stands out) studio set; the sherpa fleece catches the soft light; smooth, loopable.
8. **Lifestyle motion (3:4, 10s, soft ambient audio)**: A slow cinematic dolly-in on the scene from shot 4,
   with gentle natural movement in the light and air, ending on a close-up of the fleece texture.
