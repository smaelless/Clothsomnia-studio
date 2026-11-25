# Clothsomnia: RYUK / LUNA swap prompts (10 groups)

Edit the worn-hoodie photos so the model wears the Clothsomnia look: **guys → RYUK**, **girls → LUNA**, **guy + girl together → both**.
Headphones stay. Original eyeglasses are removed and swapped for the look's sunglasses.
Looks: `references/ryuk/README.md` (lighter charcoal mask) and `references/luna/README.md`.

| Group | Photos | Look |
|---|---|---|
| 1 Grey/Black | 16 | RYUK |
| 2 Navy/White | 16 | RYUK |
| 3 Burgundy/Off-white | 16 | RYUK |
| 4 Olive green | 16 | RYUK |
| 5 Grey | 16 | RYUK |
| 6 Off-white (guys) | 2 | RYUK |
| 7 Black (girls) | 14 | LUNA |
| 8 White (girls) | 8 | LUNA |
| 9 Off-white (girls) | 8 | LUNA |
| 10 Off-white (guy + girl) | 4 | RYUK + LUNA |

Total 116 photos. Paste this whole file into a new Claude chat with Higgsfield on, then say: "Do group N" (one group per message).

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

## Group 1: Grey/Black hoodie, guys → RYUK

**Folder:** `photos/grey-black/worn/`  |  **Hoodie (do not change):** slate grey #6D6C76 centre and sleeves with black #171718 side panels  |  **Output names:** `IMG_xxxx-ryuk.jpeg`

**Prompt (use for every photo in this group, add the photo's note):**

> Edit this photo. Keep everything exactly the same (pose, body, clothes, hoodie colour and sherpa texture, background, framing, lighting, 3:4) and change only the head, face, glasses and hands. The person in this photo is a man. Give him the RYUK look: a full-head charcoal ribbed-knit balaclava, lighter than black (about #282C33, cool blue-grey cast, deep folds about #161820), fine vertical rib with a seam line up the centre of the crown, NO eye or mouth opening (a closed knit face that follows the real face contour: nose, brow, chin), ribbed collar at the neck. No hair visible. Over it, straight and perfectly level black rectangular wayfarer-style sunglasses (glossy black frame, dark smoked lenses). Visible hands wear matching charcoal ribbed-knit gloves with ribbed cuffs. Glasses: remove ANY eyeglasses the person wears in the original and replace them with the look's sunglasses. Both lenses at the same height, frame horizontal and symmetric in a front view; in a profile or three-quarter view follow the head's perspective but keep the frame level with the horizon, never tilted or sliding down the face. Only add them when the eye line is in the frame. Headphones, if any, stay on. The grey/black hoodie keeps its exact inverted-V grey centre and black side panels. No text. Photorealistic, same camera look as the original.

**Photos (16), with notes:**

- `IMG_3227`: back view, hood up: hood stays, balaclava under it; nothing else visible to change
- `IMG_3249`: front, HEADPHONES stay on; remove his eyeglasses, swap to RYUK sunglasses; hand in pocket
- `IMG_3252`: back, HEADPHONES stay on; gloves on both hands raised to the headphones
- `IMG_3253`: back three-quarter, HEADPHONES stay on; remove his eyeglasses; balaclava on the back of the head
- `IMG_3282`: back view, hood up, hands at the hood: gloves on both hands
- `IMG_3300`: front, hand at the collar: glove
- `IMG_3302`: front, hand covering the face: glove on that hand, balaclava visible around it
- `IMG_3306`: back three-quarter, hood half up: balaclava on the visible head and neck
- `IMG_3310`: front, looking at camera, hands together low: gloves
- `IMG_3311`: three-quarter, looking away, hand in pocket
- `IMG_3314`: back view, head slightly turned: balaclava, no glasses
- `IMG_3315`: profile, smiling: closed balaclava, level sunglasses in profile
- `IMG_3316`: profile, head down, hands at the cuff: gloves
- `IMG_3318`: three-quarter, head down, hand in pocket
- `IMG_3325`: front, arms crossed: gloves on both hands
- `IMG_3326`: front, head down, hands at the sleeve: gloves

---

## Group 2: Navy/White hoodie, guys → RYUK

**Folder:** `photos/navy-white/worn/`  |  **Hoodie (do not change):** navy #1E1D28 centre and sleeves with white #E5E2DE side panels  |  **Output names:** `IMG_xxxx-ryuk.jpeg`

**Prompt (use for every photo in this group, add the photo's note):**

> Edit this photo. Keep everything exactly the same (pose, body, clothes, hoodie colour and sherpa texture, background, framing, lighting, 3:4) and change only the head, face, glasses and hands. The person in this photo is a man. Give him the RYUK look: a full-head charcoal ribbed-knit balaclava, lighter than black (about #282C33, cool blue-grey cast, deep folds about #161820), fine vertical rib with a seam line up the centre of the crown, NO eye or mouth opening (a closed knit face that follows the real face contour: nose, brow, chin), ribbed collar at the neck. No hair visible. Over it, straight and perfectly level black rectangular wayfarer-style sunglasses (glossy black frame, dark smoked lenses). Visible hands wear matching charcoal ribbed-knit gloves with ribbed cuffs. Glasses: remove ANY eyeglasses the person wears in the original and replace them with the look's sunglasses. Both lenses at the same height, frame horizontal and symmetric in a front view; in a profile or three-quarter view follow the head's perspective but keep the frame level with the horizon, never tilted or sliding down the face. Only add them when the eye line is in the frame. Headphones, if any, stay on. The navy/white hoodie keeps its exact navy centre and white side panels. No text. Photorealistic, same camera look as the original.

**Photos (16), with notes:**

- `IMG_3336`: back view, hood up, both hands on the hood: gloves
- `IMG_3340`: front, HOOD UP, both hands on the hood: balaclava under the hood, gloves
- `IMG_3355`: back three-quarter profile, hand on hip: glove
- `IMG_3364`: front three-quarter, looking away, hands behind
- `IMG_3367`: profile, head down
- `IMG_3369`: profile, hands together low: gloves
- `IMG_3370`: profile, hands together low: gloves
- `IMG_3371`: profile, holding a grey hoodie: gloves on both hands holding it
- `IMG_3383`: back view, hand at the collar: glove
- `IMG_3384`: back view, hand at the collar: glove
- `IMG_3394`: front, HOOD UP, hands in the pocket: balaclava under the hood
- `IMG_3395`: front, HOOD UP, hand in the pocket
- `IMG_3396`: front, HOOD UP, head down, hands low: gloves
- `IMG_3397`: profile, hand on hip: glove
- `IMG_3398`: three-quarter, looking away, hand low: glove
- `IMG_3401`: front, hand in the pocket

---

## Group 3: Burgundy/Off-white hoodie, guys → RYUK

**Folder:** `photos/burgundy-offwhite/worn/`  |  **Hoodie (do not change):** burgundy #4C181F centre and sleeves with off-white/cream #E8DFCE side panels  |  **Output names:** `IMG_xxxx-ryuk.jpeg`

**Prompt (use for every photo in this group, add the photo's note):**

> Edit this photo. Keep everything exactly the same (pose, body, clothes, hoodie colour and sherpa texture, background, framing, lighting, 3:4) and change only the head, face, glasses and hands. The person in this photo is a man. Give him the RYUK look: a full-head charcoal ribbed-knit balaclava, lighter than black (about #282C33, cool blue-grey cast, deep folds about #161820), fine vertical rib with a seam line up the centre of the crown, NO eye or mouth opening (a closed knit face that follows the real face contour: nose, brow, chin), ribbed collar at the neck. No hair visible. Over it, straight and perfectly level black rectangular wayfarer-style sunglasses (glossy black frame, dark smoked lenses). Visible hands wear matching charcoal ribbed-knit gloves with ribbed cuffs. Glasses: remove ANY eyeglasses the person wears in the original and replace them with the look's sunglasses. Both lenses at the same height, frame horizontal and symmetric in a front view; in a profile or three-quarter view follow the head's perspective but keep the frame level with the horizon, never tilted or sliding down the face. Only add them when the eye line is in the frame. Headphones, if any, stay on. The burgundy/off-white hoodie keeps its exact burgundy centre and cream side panels. No text. Photorealistic, same camera look as the original.

**Photos (16), with notes:**

- `IMG_3407`: CLOSE-UP of chin and neck only: balaclava over the visible chin, jaw and neck; no glasses
- `IMG_3408`: profile, hand in the pocket
- `IMG_3409`: profile, hand at the neck: glove
- `IMG_3410`: front three-quarter, hands in pockets
- `IMG_3413`: back three-quarter profile, hand on hip: glove
- `IMG_3414`: front, looking away
- `IMG_3417`: front, head down
- `IMG_3420`: back view, balaclava on the back of the head
- `IMG_3422`: back view, balaclava on the back of the head
- `IMG_3424`: front, hand in the pocket
- `IMG_3425`: front, head down, hands in pockets
- `IMG_3427`: profile, hand in the pocket
- `IMG_3428`: three-quarter, head down, hand low: glove
- `IMG_3430`: three-quarter, head down, hand at the pocket: glove
- `IMG_3440`: full body, HOOD UP, hand in the pocket: balaclava under the hood; keep the shelves and rail behind
- `IMG_3441`: full body, HOOD UP, both hands on the hood: gloves

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

---

## Group 5: Grey hoodie, guys → RYUK

**Folder:** `photos/grey/worn/`  |  **Hoodie (do not change):** slate grey #6D6C76 solid sherpa  |  **Output names:** `IMG_xxxx-ryuk.jpeg`

**Prompt (use for every photo in this group, add the photo's note):**

> Edit this photo. Keep everything exactly the same (pose, body, clothes, hoodie colour and sherpa texture, background, framing, lighting, 3:4) and change only the head, face, glasses and hands. The person in this photo is a man. Give him the RYUK look: a full-head charcoal ribbed-knit balaclava, lighter than black (about #282C33, cool blue-grey cast, deep folds about #161820), fine vertical rib with a seam line up the centre of the crown, NO eye or mouth opening (a closed knit face that follows the real face contour: nose, brow, chin), ribbed collar at the neck. No hair visible. Over it, straight and perfectly level black rectangular wayfarer-style sunglasses (glossy black frame, dark smoked lenses). Visible hands wear matching charcoal ribbed-knit gloves with ribbed cuffs. Glasses: remove ANY eyeglasses the person wears in the original and replace them with the look's sunglasses. Both lenses at the same height, frame horizontal and symmetric in a front view; in a profile or three-quarter view follow the head's perspective but keep the frame level with the horizon, never tilted or sliding down the face. Only add them when the eye line is in the frame. Headphones, if any, stay on. The grey hoodie keeps its exact colour and sherpa texture. No text. Photorealistic, same camera look as the original.

**Photos (16), with notes:**

- `IMG_3467`: back three-quarter, hands behind
- `IMG_3468`: back three-quarter, hands behind
- `IMG_3470`: three-quarter, head down, both hands at the sleeve: gloves
- `IMG_3471`: three-quarter, head down, hands at the cuff: gloves
- `IMG_3482`: front, HOOD UP, hand at the chin: balaclava under the hood, glove
- `IMG_3483`: profile, hand in the pocket
- `IMG_3484`: front, hands low, hood down
- `IMG_3485`: profile, one arm stretched out to a rail: gloves on visible hands
- `IMG_3486`: profile, hand low: glove
- `IMG_3487`: front three-quarter, hand at the collar: glove
- `IMG_3488`: front, hand at the collar: glove
- `IMG_3489`: front, hand in the pocket
- `IMG_3491`: three-quarter, head down, hands holding another hoodie: gloves
- `IMG_3494`: three-quarter, looking away, hand in the pocket
- `IMG_3497`: CLOSE-UP of the lower face in profile (nose, jaw, ear, hood collar): balaclava over all of it; add sunglasses only if the eye line is in frame
- `IMG_3498`: CLOSE-UP of chin and neck only: balaclava over the visible chin and neck; no glasses

---

## Group 6: Off-white hoodie, guys only → RYUK

**Folder:** `photos/off-white/worn/`  |  **Hoodie (do not change):** cream #E8DFCE solid sherpa  |  **Output names:** `IMG_xxxx-ryuk.jpeg`

**Prompt (use for every photo in this group, add the photo's note):**

> Edit this photo. Keep everything exactly the same (pose, body, clothes, hoodie colour and sherpa texture, background, framing, lighting, 3:4) and change only the head, face, glasses and hands. The person in this photo is a man. Give him the RYUK look: a full-head charcoal ribbed-knit balaclava, lighter than black (about #282C33, cool blue-grey cast, deep folds about #161820), fine vertical rib with a seam line up the centre of the crown, NO eye or mouth opening (a closed knit face that follows the real face contour: nose, brow, chin), ribbed collar at the neck. No hair visible. Over it, straight and perfectly level black rectangular wayfarer-style sunglasses (glossy black frame, dark smoked lenses). Visible hands wear matching charcoal ribbed-knit gloves with ribbed cuffs. Glasses: remove ANY eyeglasses the person wears in the original and replace them with the look's sunglasses. Both lenses at the same height, frame horizontal and symmetric in a front view; in a profile or three-quarter view follow the head's perspective but keep the frame level with the horizon, never tilted or sliding down the face. Only add them when the eye line is in the frame. Headphones, if any, stay on. The off-white hoodie keeps its exact cream colour and sherpa texture. No text. Photorealistic, same camera look as the original.

**Photos (2), with notes:**

- `IMG_4235`: three-quarter back, hand at the neck: glove; remove his eyeglasses, swap to RYUK sunglasses; park, fence and lake stay
- `IMG_4238`: front, leaning on the fence post, hand in the pocket; remove his eyeglasses, swap to RYUK sunglasses

---

## Group 7: Black hoodie, girls → LUNA

**Folder:** `photos/black/worn/`  |  **Hoodie (do not change):** black #171718 solid sherpa  |  **Output names:** `IMG_xxxx-luna.jpeg`

**Prompt (use for every photo in this group, add the photo's note):**

> Edit this photo. Keep everything exactly the same (pose, body, clothes, hoodie colour and sherpa texture, background, framing, lighting, 3:4) and change only the head, face, glasses and hands. The person in this photo is a woman. Give her the LUNA look: a full-head pink ribbed-knit balaclava (heathered bubblegum pink, about #D5688C, shadow folds about #A63F5E), fine vertical rib with a seam line up the centre of the crown, NO eye or mouth opening (a closed knit face that follows the real face contour: nose, brow, chin), ribbed collar at the neck. No hair visible. Over it, level cat-eye sunglasses with a translucent pink glitter frame, clear and pale-pink rhinestones on both upper outer corners, rose-brown gradient lenses (dark at the top, lighter and pinker at the bottom) and translucent rose-gold glitter temple arms. Visible hands wear matching pink ribbed-knit gloves with ribbed cuffs. Glasses: remove ANY eyeglasses the person wears in the original and replace them with the look's sunglasses. Both lenses at the same height, frame horizontal and symmetric in a front view; in a profile or three-quarter view follow the head's perspective but keep the frame level with the horizon, never tilted or sliding down the face. Only add them when the eye line is in the frame. Headphones, if any, stay on. The black hoodie keeps its exact colour and sherpa texture. Her nail polish is replaced by the gloves. No text. Photorealistic, same camera look as the original.

**Photos (14), with notes:**

- `IMG_1690`: front, hand on her head: glove; her long hair is fully covered by the balaclava; sea-front background stays
- `IMG_1816`: front, hand in the pocket, hood down
- `IMG_1817`: front, both hands raised at the hood: gloves
- `IMG_1818`: front, both hands raised at the hood: gloves
- `IMG_1820`: front three-quarter, hand in the pocket, looking down
- `IMG_1821`: three-quarter, hand raised at the face: glove
- `IMG_1826`: front, both hands at the collar: gloves
- `IMG_1842`: front, hand at the neck: glove
- `IMG_1843`: front, hand at the chin: glove over the balaclava, other hand low
- `IMG_1844`: front, hand at the chin: glove, other hand on hip
- `IMG_1845`: front, hand at the chin: glove, other hand on hip
- `IMG_1846`: front, hands low, looking away
- `IMG_1851`: front, hand over the face: glove covers that area; other hand low
- `IMG_1853`: three-quarter, head down, hand in the pocket

---

## Group 8: White hoodie, girls → LUNA

**Folder:** `photos/white/worn/`  |  **Hoodie (do not change):** snow white #E5E2DE solid sherpa  |  **Output names:** `IMG_xxxx-luna.jpeg`

**Prompt (use for every photo in this group, add the photo's note):**

> Edit this photo. Keep everything exactly the same (pose, body, clothes, hoodie colour and sherpa texture, background, framing, lighting, 3:4) and change only the head, face, glasses and hands. The person in this photo is a woman. Give her the LUNA look: a full-head pink ribbed-knit balaclava (heathered bubblegum pink, about #D5688C, shadow folds about #A63F5E), fine vertical rib with a seam line up the centre of the crown, NO eye or mouth opening (a closed knit face that follows the real face contour: nose, brow, chin), ribbed collar at the neck. No hair visible. Over it, level cat-eye sunglasses with a translucent pink glitter frame, clear and pale-pink rhinestones on both upper outer corners, rose-brown gradient lenses (dark at the top, lighter and pinker at the bottom) and translucent rose-gold glitter temple arms. Visible hands wear matching pink ribbed-knit gloves with ribbed cuffs. Glasses: remove ANY eyeglasses the person wears in the original and replace them with the look's sunglasses. Both lenses at the same height, frame horizontal and symmetric in a front view; in a profile or three-quarter view follow the head's perspective but keep the frame level with the horizon, never tilted or sliding down the face. Only add them when the eye line is in the frame. Headphones, if any, stay on. The white hoodie keeps its exact colour and sherpa texture. Keep the cafe night lighting and neon sign. No text. Photorealistic, same camera look as the original.

**Photos (8), with notes:**

- `IMG_1648`: sitting at a cafe table, hand under the chin: glove; night scene and neon stay
- `IMG_1649`: sitting, looking at camera, hands low
- `IMG_1650`: sitting, looking away, hands low
- `IMG_1652`: sitting, looking up and away, hands low
- `IMG_1653`: sitting, eyes closed, head tilted, hand on the knee: glove
- `IMG_1654`: sitting, hand at the chin: glove
- `IMG_1659`: sitting, looking away, hand low
- `IMG_1660`: sitting, looking away, hands low

---

## Group 9: Off-white hoodie, girls only → LUNA

**Folder:** `photos/off-white/worn/`  |  **Hoodie (do not change):** cream #E8DFCE solid sherpa  |  **Output names:** `IMG_xxxx-luna.jpeg`

**Prompt (use for every photo in this group, add the photo's note):**

> Edit this photo. Keep everything exactly the same (pose, body, clothes, hoodie colour and sherpa texture, background, framing, lighting, 3:4) and change only the head, face, glasses and hands. The person in this photo is a woman. Give her the LUNA look: a full-head pink ribbed-knit balaclava (heathered bubblegum pink, about #D5688C, shadow folds about #A63F5E), fine vertical rib with a seam line up the centre of the crown, NO eye or mouth opening (a closed knit face that follows the real face contour: nose, brow, chin), ribbed collar at the neck. No hair visible. Over it, level cat-eye sunglasses with a translucent pink glitter frame, clear and pale-pink rhinestones on both upper outer corners, rose-brown gradient lenses (dark at the top, lighter and pinker at the bottom) and translucent rose-gold glitter temple arms. Visible hands wear matching pink ribbed-knit gloves with ribbed cuffs. Glasses: remove ANY eyeglasses the person wears in the original and replace them with the look's sunglasses. Both lenses at the same height, frame horizontal and symmetric in a front view; in a profile or three-quarter view follow the head's perspective but keep the frame level with the horizon, never tilted or sliding down the face. Only add them when the eye line is in the frame. Headphones, if any, stay on. The off-white hoodie keeps its exact cream colour and sherpa texture. The park, fence and lake stay. No text. Photorealistic, same camera look as the original.

**Photos (8), with notes:**

- `IMG_4243`: front, hand in the pocket; remove her clear eyeglasses, swap to LUNA sunglasses
- `IMG_4244`: front three-quarter, one hand low; remove her glasses, swap to LUNA sunglasses
- `IMG_4245`: front, hand at the face: glove; remove her glasses
- `IMG_4248`: close three-quarter, head down, hand on the fence: glove; remove any glasses
- `IMG_4249`: close three-quarter, head down, hand low: glove; remove her glasses
- `IMG_4252`: front, hand on her head, face partly hidden: glove, balaclava follows the covered face
- `IMG_5287`: back view walking, hand in the pocket
- `IMG_5291`: back view walking, hand low: glove

---

## Group 10: Off-white hoodie, guy + girl together → RYUK on him, LUNA on her

**Folder:** `photos/off-white/worn/`  |  **Hoodie (do not change):** cream #E8DFCE solid sherpa on both people  |  **Output names:** `IMG_xxxx-ryuk-luna.jpeg`

**Prompt (use for every photo in this group, add the photo's note):**

> Edit this photo. Keep everything exactly the same (pose, body, clothes, hoodie colour and sherpa texture, background, framing, lighting, 3:4) and change only the head, face, glasses and hands. There are two people: a man and a woman. Give the MAN the RYUK look: a full-head charcoal ribbed-knit balaclava, lighter than black (about #282C33, cool blue-grey cast, deep folds about #161820), fine vertical rib with a seam line up the centre of the crown, NO eye or mouth opening (a closed knit face that follows the real face contour: nose, brow, chin), ribbed collar at the neck. No hair visible. Over it, straight and perfectly level black rectangular wayfarer-style sunglasses (glossy black frame, dark smoked lenses). Visible hands wear matching charcoal ribbed-knit gloves with ribbed cuffs. Give the WOMAN the LUNA look: a full-head pink ribbed-knit balaclava (heathered bubblegum pink, about #D5688C, shadow folds about #A63F5E), fine vertical rib with a seam line up the centre of the crown, NO eye or mouth opening (a closed knit face that follows the real face contour: nose, brow, chin), ribbed collar at the neck. No hair visible. Over it, level cat-eye sunglasses with a translucent pink glitter frame, clear and pale-pink rhinestones on both upper outer corners, rose-brown gradient lenses (dark at the top, lighter and pinker at the bottom) and translucent rose-gold glitter temple arms. Visible hands wear matching pink ribbed-knit gloves with ribbed cuffs. Each person keeps their own look; never mix them. Glasses: remove ANY eyeglasses the person wears in the original and replace them with the look's sunglasses. Both lenses at the same height, frame horizontal and symmetric in a front view; in a profile or three-quarter view follow the head's perspective but keep the frame level with the horizon, never tilted or sliding down the face. Only add them when the eye line is in the frame. Headphones, if any, stay on. Both people keep their exact poses and positions; never swap the looks between them. No text. Photorealistic, same camera look as the original.

**Photos (4), with notes:**

- `IMG_4251`: he is seen from BEHIND (RYUK balaclava on the back of his head, no glasses); she faces camera, hand on her head: LUNA with glove
- `IMG_4253`: he stands left, front three-quarter, hand in the pocket; remove his eyeglasses, RYUK sunglasses. She stands right, head down, hand low: LUNA with glove
- `IMG_4254`: same as 4253: remove his eyeglasses; her head down, hand low
- `IMG_4257`: he is in three-quarter looking right: remove his eyeglasses, RYUK sunglasses. She looks away, hand low: LUNA with glove
