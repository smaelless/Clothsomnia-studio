# RYUK / LUNA swap: group 4 (olive-green)

One chat = one group. Paste this whole file into a new Claude chat with Higgsfield on, then say: "Start group 4."

## Chat flow (follow in this order)

1. **Pilot:** generate the first 2 photos of the group only, show them to me, and wait for my OK.
2. **Batches:** after my OK, run the rest in batches of 8 (`generate_image_batch`, then `jobs_wait`, then show the batch).
3. **Fixes:** I reply with the photo numbers to redo and what is wrong (for example: "3410 glasses tilted"); regenerate only those.
4. **Save:** when I say "save", write every approved result next to its original in the repo with the output name below.
5. **Commit:** only when I say "push", commit and push to the repo's default branch. Then say "group done" and list the final file names.

## How to run (Claude chat with Higgsfield on, not Claude Code)

1. Get the source photos: clone `smaelless/clothsomnia-studio` (default branch). Originals are in `photos/<folder>/worn/IMG_xxxx.jpeg`; the looks are in `references/ryuk/` and `references/luna/`. If you cannot clone, ask me to attach the photos.
2. Upload each original and the look references to Higgsfield (`media_upload`, PUT, `media_confirm`).
3. Per photo, run `generate_image` with `model: gpt_image_2_6`, `aspect_ratio: 3:4`, `resolution: 2k`, `use_unlim: true`, `count: 1`. Pass the original as the main reference and the look's balaclava-front and three-quarter crops (plus the glove crop) as extra references. Use `models_explore` first if you are unsure of the `medias` roles.
4. Use `generate_image_batch` (up to 12 per call) for speed, then `jobs_wait`, then show the batch.
5. Check every result against the original: hoodie, pose and background unchanged; balaclava closed with no face showing; glasses level; gloves on every visible hand; headphones still on. Regenerate anything that fails (up to 2 retries), tell me which ones stay problematic.
6. Save each result next to its original in the repo as the output name shown below. Do not overwrite originals. Commit and push only when I say so.

**Edit rules (apply to every image):**
- This is an EDIT of the original photo, not a new picture. Keep identical: pose, body, trousers/jeans, the hoodie (exact colour, shape, sherpa texture, pocket, seams), background, framing, crop, lighting, shadows, camera angle and the 3:4 format. Do not restyle, retouch or re-pose.
- Change ONLY the head, face, glasses and hands, exactly as in the look below.
- Headphones, when present, STAY exactly where they are, worn over the balaclava.
- The hair is completely covered by the balaclava; the balaclava collar tucks into the hoodie neckline (under the hood when the hood is up; the hood stays up over the balaclava).
- Back view: the balaclava covers the back of the head and neck; no sunglasses unless a temple arm would really be visible at the side of the head.
- Close-up of chin/neck only: the balaclava covers the visible chin, jaw and neck; no sunglasses (eye line is out of frame).
- Face turned down or covered by a hand: keep that exact pose; the sunglasses follow the head angle, level to the head, not to the camera.
- No text, no logos, no extra people or objects, no added jewellery. Photorealistic, same camera look, grain and colour as the original (no glossy AI sheen, no HDR).

---

## Group 4: Olive green hoodie, guys → RYUK

**Folder:** `photos/olive-green/worn/`  |  **Hoodie (do not change):** olive #4F4E44 solid sherpa  |  **Output names:** `IMG_xxxx-ryuk.jpeg`

**Prompt (use for every photo in this group, add the photo's note):**

> Edit this photo. Keep everything exactly the same (pose, body, clothes, hoodie colour and sherpa texture, background, framing, lighting, 3:4) and change only the head, face, glasses and hands. The person in this photo is a man. Give him the RYUK look: a full-head charcoal ribbed-knit balaclava, lighter than black (about #282C33, cool blue-grey cast, deep folds about #161820), fine vertical rib with a seam line up the centre of the crown, NO eye or mouth opening (a closed knit face that follows the real face contour: nose, brow, chin), ribbed collar at the neck. No hair visible. Over it, straight and perfectly level black rectangular wayfarer-style sunglasses (glossy black frame, dark smoked lenses). Visible hands wear matching charcoal ribbed-knit gloves with ribbed cuffs. Glasses: remove ANY eyeglasses the person wears in the original and replace them with the look's sunglasses. Both lenses at the same height, frame horizontal and symmetric in a front view; in a profile or three-quarter view follow the head's perspective but keep the frame level with the horizon, never tilted or sliding down the face. Only add them when the eye line is in the frame. Headphones, if any, stay on. The olive hoodie keeps its exact colour and sherpa texture. No text. Photorealistic, same camera look as the original.

**Photos (16), with notes:**

- `IMG_3507`: CLOSE-UP of chin and neck only (collar of the hoodie in frame): balaclava over the visible chin, jaw and neck; no glasses
- `IMG_3515`: profile, hand at the neck: glove
- `IMG_3516`: back view, hands behind
- `IMG_3518`: back three-quarter, hands behind
- `IMG_3530`: back view, hands behind
- `IMG_3532`: back view, hand raised at the collar: glove
- `IMG_3533`: back three-quarter, hand raised at the collar: glove
- `IMG_3535`: front, looking at camera, hand in the pocket
- `IMG_3536`: front, head down, hands together low: gloves
- `IMG_3538`: front three-quarter, looking away, hands in pockets
- `IMG_3540`: three-quarter, head down, hand in the pocket
- `IMG_3542`: three-quarter, head down, hand low: glove
- `IMG_3543`: three-quarter, eyes closed, hand in the pocket
- `IMG_3575`: sitting on a sofa, looking away, hand resting: glove; the loose eyeglasses lying on the sofa stay as a prop
- `IMG_3586`: lying on a sofa, looking up, arm over the chest: gloves on visible hands
- `IMG_3587`: lying on a sofa, HOOD UP, hand behind the head: balaclava under the hood, gloves on visible hands
