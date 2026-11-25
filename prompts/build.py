"""Generates one Higgsfield prompt pack per colourway: python3 prompts/build.py"""
from pathlib import Path

COMMON_RULES = (
    "Reproduce the colour layout, proportions and curly sherpa texture exactly as in the references. "
    "No people, no mannequin visible, no other brand logos, no hang tags, no text overlays."
)

COMMON_REALISM = (
    "REALISM = real product photography for an online store, not an illustration or 3D render. "
    "Shot on a full-frame camera, 50-85mm lens, natural or softbox light, true-to-life colour that "
    "matches the references. Fabric must behave like real heavy fleece: soft weight, natural "
    "wrinkles and folds where it bends, slight imperfections, visible individual curls, no plastic "
    "sheen, no airbrushed smoothness, no glow, no HDR, no over-sharpening. Keep the exact same "
    "colours in every image (do not drift under warm light). Simple believable scenes only, ordinary "
    "real-life props, no fantasy lighting. If a render looks AI-made, CGI or glossy, regenerate it."
)

COLOURS = {
    "navy-white": {
        "title": "Navy/White",
        "refs": [
            ("6477b042-a764-46d2-8299-5c5636207328", "front, flat lay"),
            ("5c696f73-8bf4-4028-b9e2-f0218953fb73", "back, flat lay"),
            ("10b9483e-7dcf-4569-abbe-97bf4187bfd3", '"Clothsomnia" neck label close-up'),
            ("a7f4d315-b866-438e-ae63-669b091471bb", "sherpa texture / hem detail"),
        ],
        "desc": "Oversized sherpa fleece pullover hoodie, deep navy centre panel in an inverted V (wide at the "
                "shoulders, narrowing to a point at the hem) with wide off-white sherpa side panels; the white "
                "panels continue down the sides of the back. Navy hood and sleeves, wide soft sherpa cuffs and "
                "hem band in navy, same fine pile as the body, NOT ribbed knit, diagonal slit pockets as a subtle "
                "seam only, nearly invisible, never a drawn line, no kangaroo pocket, no drawstrings, no hood "
                'cords, small "Clothsomnia" script label inside the neck.',
        "bg": "warm light-grey",
        "scene_a": "casually laid on an unmade bed with crisp white linen, morning sunlight through sheer "
                   "curtains, a cup of mint tea on the bedside table, warm and dreamy",
        "scene_b": "draped over a carved cedar-wood chair in a sunlit Moroccan riad courtyard, zellige tiles, "
                   "terracotta pots, soft golden-hour light",
        "flat": "beige linen surface with dried pampas grass and a small ceramic dish",
    },
    "burgundy-offwhite": {
        "title": "Burgundy/Off-white",
        "refs": [
            ("dbaaaaf3-f4a7-45cd-b718-6becc30185b9", "front, flat lay"),
            ("3eabe880-ceea-4da3-880f-6dc8cece5f60", "back view (worn: use only for the garment's back, ignore the person)"),
            ("45f90e6a-28bc-4a5c-97a0-3ccd1a64e696", '"Clothsomnia" neck label close-up'),
            ("7c86c63c-5f2b-49f0-a262-7286508e144f", "sleeve and panel texture detail"),
        ],
        "desc": "Oversized sherpa fleece pullover hoodie, deep burgundy / wine red centre panel in an inverted V "
                "(wide at the shoulders, narrowing to a point at the hem) with wide off-white sherpa side panels; "
                "the off-white panels continue down the sides of the back. Burgundy hood and sleeves, wide soft "
                "sherpa cuffs and hem band in burgundy, same fine pile as the body, NOT ribbed knit, diagonal "
                "slit pockets as a subtle seam only, nearly invisible, never a drawn line, no kangaroo pocket, "
                'no drawstrings, no hood cords, small dark "Clothsomnia" script label inside the neck.',
        "bg": "warm cream",
        "scene_a": "draped over a deep velvet armchair beside a softly glowing fireplace, a knitted throw and a "
                   "steaming cup of tea nearby, cozy winter evening light",
        "scene_b": "hung on a brass hook against a hand-painted Moroccan tiled wall in deep reds and creams, "
                   "warm light from a pierced-metal lantern",
        "flat": "warm oatmeal linen with a few dried rose petals and a brass tray",
    },
    "grey-black": {
        "title": "Grey/Black",
        "refs": [
            ("539300ee-b420-41a2-93c8-66dd08a29a49", "front, flat lay"),
            ("b9b2ebff-c419-4490-ba08-2497537669d7", "back view (worn: use only for the garment's back, ignore the person)"),
            ("af4970ae-b9c0-40bb-9480-63f4b9ae0cac", "hood and neck label detail"),
            ("83e47eae-914b-48d6-8db1-1b480e2b9a9a", "grey/black seam and texture detail"),
        ],
        "desc": "Oversized sherpa fleece pullover hoodie, cool slate grey centre panel in an inverted V (wide at "
                "the shoulders, narrowing to a point at the hem) with wide black sherpa side panels; the black "
                "panels continue down the sides of the back. Grey hood and sleeves, wide soft sherpa cuffs and "
                "hem band in grey, same fine pile as the body, NOT ribbed knit, diagonal slit pockets as a subtle "
                "seam only, nearly invisible, never a drawn line, no kangaroo pocket, no drawstrings, no hood "
                'cords, small "Clothsomnia" script label inside the neck.',
        "bg": "cool mid-grey",
        "scene_a": "laid over a raw concrete bench on a city rooftop at blue hour, soft city lights blurred in the "
                   "background, calm urban mood",
        "scene_b": "hanging on a matte-black steel rail in a minimalist concrete loft with large windows, soft "
                   "overcast daylight",
        "flat": "smooth light-grey concrete with a black ceramic cup and a pair of wireless headphones (unbranded)",
    },
    "black": {
        "title": "Black",
        "refs": [
            ("1bacc6bc-425e-4add-90b7-20420888052a", "front, flat lay (ignore the hang tag)"),
            ("0cc913ab-9a39-476e-8dc9-66b1379a4378", "front, laid out"),
            ("970b01b2-a60d-4256-adc3-a5998c6a3dd1", "sherpa texture close-up"),
            ("8bfc9146-5820-49c8-b351-8dcdcb5bf9de", "side / sleeve detail"),
        ],
        "desc": "Oversized solid jet-black curly sherpa fleece pullover hoodie, dropped shoulders, black hood, "
                "wide soft sherpa cuffs and hem band in black, same fine pile as the body, NOT ribbed knit, kangaroo pocket, small label inside the neck. The curly sherpa "
                "texture must stay visible, not a flat black shape.",
        "bg": "deep charcoal with a subtle gradient",
        "scene_a": "draped over a chair on a Casablanca street at night, Art Deco facade behind, warm street "
                   "lamps and wet pavement reflections, moody streetwear editorial",
        "scene_b": "hanging from a hook on a plain white-washed wall, one hard beam of sunlight cutting across "
                   "the fleece, high-contrast minimal look",
        "flat": "matte black slate with a silver ring and a pair of black sunglasses (unbranded)",
    },
    "white": {
        "title": "White",
        "refs": [
            ("d5ac7a02-9916-43a7-9131-4ac7244a32c8", "front, full flat lay (best reference)"),
            ("69ae6ff2-ca8a-45c3-b5d0-30a89bffe439", "side flat lay"),
            ("30c1bd0e-5190-4abb-8a18-bb86380302bc", "hood and neck label detail (ignore the hang tag)"),
            ("c55d7baf-a4b5-4264-8641-90acbe68c62c", "fleece texture and cuff detail"),
        ],
        "desc": "Oversized pure bright-white sherpa fleece pullover hoodie, dropped shoulders, white hood, "
                "wide soft sherpa cuffs and hem band in white, same fine pile as the body, NOT ribbed knit, kangaroo pocket, small dark woven label inside the neck. Keep the "
                "white clean and neutral, not cream or yellow.",
        "bg": "soft pale grey (so the white stands out)",
        "scene_a": "folded at the foot of a bed with soft grey linen in a bright minimalist bedroom, cool "
                   "morning light, airy and calm",
        "scene_b": "hanging against a blue-washed wall in a Chefchaouen alley, potted plants, soft daylight, "
                   "the white popping against the blue",
        "flat": "light-grey linen with a eucalyptus sprig and a white ceramic cup",
    },
    "off-white": {
        "title": "Off-white",
        "refs": [
            ("bca9dee8-11a0-483c-af00-51363a34bc4b", "front, laid out (ignore the hang tag)"),
            ("fad629f9-537a-4cc4-82c3-ec3078f0ad25", "front with kangaroo pocket"),
            ("635e78d2-24c8-4fb4-afd1-3029303662a8", "hood and neck detail (ignore the hang tag)"),
            ("09c24a31-d00e-42d0-98df-f3397b304591", "sherpa texture / sleeve detail"),
        ],
        "desc": "Oversized cream / ivory off-white curly sherpa fleece pullover hoodie, dropped shoulders, cream "
                "hood, wide soft sherpa cuffs and hem band in cream, same fine pile as the body, NOT ribbed knit, kangaroo pocket, small label inside the neck. Keep the warm "
                "cream tone, not pure white.",
        "bg": "warm sand-beige",
        "scene_a": "draped over a wooden fence post by a calm lake at golden hour, warm sunlight, ochre cliffs "
                   "blurred in the background",
        "scene_b": "laid on a woven Berber rug on a Sahara dune at sunrise, soft warm light and long shadows",
        "flat": "natural linen with dried wheat stems and a small woven basket",
    },
    "olive-green": {
        "title": "Olive Green",
        "refs": [
            ("bfe8842e-4b2f-49c3-9d6b-65376d7c47ce", "front view (worn: use only for the garment, ignore the person)"),
            ("b49ebb57-09c1-4860-8f04-d29d5c3259b9", "back view (worn: use only for the garment, ignore the person)"),
            ("c1b94720-b961-43a0-8bfb-1795317de4b6", "fleece texture and hood close-up"),
            ("e5119c64-ac91-4dec-bd4f-99f7da3c5642", "relaxed fit, how the fleece drapes"),
        ],
        "desc": "Oversized solid muted olive / sage green sherpa fleece pullover hoodie, dropped shoulders, olive "
                "hood, wide soft sherpa cuffs and hem band in olive, same fine pile as the body, NOT ribbed knit, kangaroo pocket. These references are on-model photos: "
                "copy only the hoodie, not the person.",
        "bg": "warm stone-beige",
        "scene_a": "tossed on a light-grey linen sofa with a chunky knit blanket and a book, soft afternoon "
                   "window light, lazy Sunday mood",
        "scene_b": "hanging on a wooden peg in a cedar cabin in the Atlas mountains, misty forest through the "
                   "window, soft natural light",
        "flat": "raw wood with a sprig of olive branch and a clay mug",
    },
    "grey": {
        "title": "Grey",
        "refs": [
            ("205a3007-7340-43aa-b882-c1b4905d3476", "front view (worn: use only for the garment, ignore the person)"),
            ("2fced592-a34b-497f-b347-cc4c35f46018", "back view (worn: use only for the garment, ignore the person)"),
            ("f5e74915-1854-4887-9c76-0d0ae0ece19d", "sherpa texture close-up"),
            ("3c681b3e-d758-47eb-bd0e-65ed1d522f42", "hood up, hood shape"),
        ],
        "desc": "Oversized solid cool slate grey (neutral mid-grey, about #6D6C76 / RGB 109, 108, 118; not charcoal, "
                "not silver, not blue-grey, not beige-grey) sherpa fleece pullover hoodie, dropped shoulders, roomy "
                "soft hood, wide soft sherpa cuffs and hem band in grey, same fine pile as the body, NOT ribbed "
                "knit, one large kangaroo pocket. The fleece is a FINE, TIGHT, SHORT curly pile (small dense "
                "curls like lamb's wool, as in the texture reference), not long fluffy teddy fur. Plain front and "
                "back: no drawstrings, no hood cords, no logos, no prints, no text. These references are on-model "
                "photos: copy only the hoodie, not the person.",
        "realism": "REALISM = real product photography for an online store, not an illustration or 3D render. "
                   "Shot on a full-frame camera, 50-85mm lens, natural or softbox light, true-to-life colour that "
                   "matches the references. Fabric must behave like real heavy fleece: soft weight, natural "
                   "wrinkles and folds where it bends, slight imperfections, visible individual curls, no plastic "
                   "sheen, no airbrushed smoothness, no glow, no HDR, no over-sharpening. Keep the exact same "
                   "slate grey in every image (do not drift to charcoal, blue, or lavender under warm light). Simple "
                   "believable scenes only, ordinary real-life props, no fantasy lighting. If a render looks AI-made, "
                   "CGI or glossy, regenerate it.",
        "bg": "light warm grey (#D9D6D2)",
        "macro": "Close-up of the sherpa fleece at the chest and the hood seam, 85-100mm macro look, shallow depth of "
                 "field, soft side light so every individual curl of the pile is visible. Real fabric, tight "
                 "curls, no fur-like strands.",
        "scene_a": "draped over the back of a plain wooden chair in a real home interior next to a window, soft overcast "
                   "daylight, one ceramic mug on a table nearby, natural creases, shallow depth of field",
        "scene_b": "hanging on a plain wooden hanger on a white plaster wall (slightly textured, as in a real room), soft "
                   "window light from the side, gentle natural shadow, no props",
        "flat": "a plain off-white linen cloth or light wooden floor, no props or only one "
                "simple ceramic mug",
    },
}

DEFAULT_MACRO = ("Extreme close-up of the sherpa fleece and the neckline/label area, shallow depth of\n   field, soft raking light "
                 "that shows every curl of the fleece.")

TEMPLATE = """# Clothsomnia: {title} hoodie prompts

Paste this whole file into a **Claude chat** (claude.ai or the Claude app, not Claude Code) with the Higgsfield
connector turned on, then say: "Generate these 6 images with Higgsfield using my unlimited trial (use_unlim true)."

## Reference images (already uploaded to my Higgsfield workspace)

Pass all four as `image_references` on every generation:

{refs}

## Model and settings (best available on the unlimited trial)

- **Images:** `gpt_image_2_6`, `quality: "medium"`, `resolution: "2k"`, `use_unlim: true`. This is the highest
  setting the free trial covers (2k max, quality low/medium only); anything above it costs credits.
- **Second opinion:** also run shot 1 on `nano_banana_pro` (`resolution: "2k"`, same four references as
  `image_references`, `use_unlim: true`) and keep whichever model matches the real hoodie best for the rest.
- Check every result against the reference photos (colours, panel shapes, sherpa texture) and regenerate any image
  that changes the design.

## Product description (include in every prompt)

{desc} {rules}{realism}

## Shots

1. **Studio front (1:1)**: Ghost-mannequin front view, centred, seamless {bg} backdrop, soft diffused key
   light from top-left, gentle floor shadow, e-commerce catalogue quality.
2. **Studio back (1:1)**: Same setup, back view.
3. **Macro detail (4:5)**: {macro}
4. **Lifestyle A (4:5)**: The hoodie {scene_a}. Lifestyle brand photography.
5. **Lifestyle B (4:5)**: The hoodie {scene_b}. Editorial fashion photography.
6. **Folded flat lay (1:1)**: Neatly folded hoodie, top-down, on {flat}, soft even daylight, premium feel.

## Videos (after the images are approved)

Model: `seedance_2_5`, `mode: "omni_reference"`, `resolution: "720p"` (the highest the free trial covers),
`use_unlim: true`. Use the four reference photos as `image_references`. No people, no text.
Video 7 uses the best studio image (shot 1) as `start_image`; video 8 uses the approved shot 4 image.

7. **Hero turntable (1:1, 8s, no audio, start_image = shot 1)**: The hoodie on an invisible mannequin slowly rotates 360° on the
   {bg} studio set; the sherpa fleece catches the soft light; smooth, loopable.
8. **Lifestyle motion (3:4, 10s, soft ambient audio, start_image = shot 4)**: A slow cinematic dolly-in on the scene from shot 4,
   with gentle natural movement in the light and air, ending on a close-up of the fleece texture.
"""

out = Path(__file__).parent
for slug, c in COLOURS.items():
    refs = "\n".join(f"- `{mid}`: {label}" for mid, label in c["refs"])
    extra = {"realism": COMMON_REALISM, "macro": DEFAULT_MACRO}
    extra.update({k: v for k, v in c.items() if k != "refs"})
    if extra["realism"]:
        extra["realism"] = "\n\n**Realism (include in every prompt):** " + extra["realism"]
    (out / f"{slug}.md").write_text(TEMPLATE.format(refs=refs, rules=COMMON_RULES, **extra))

index = ["# Clothsomnia prompt packs", "",
         "One file per colourway. Paste a file into a Claude chat with Higgsfield on (not Claude Code, where the",
         "unlimited trial is blocked) and ask it to generate the images. Reference photos are already uploaded.", ""]
index += [f"- [{c['title']}]({slug}.md)" for slug, c in COLOURS.items()]
index += ["- [Packaging](packaging.md)"]
(out / "README.md").write_text("\n".join(index) + "\n")
print("wrote", len(COLOURS), "packs")
