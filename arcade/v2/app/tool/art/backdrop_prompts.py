"""Writes the Nano Banana prompts for every era's backdrop pieces, each era
written out in full, ready to paste.

    python tool/art/backdrop_prompts.py              # writes BACKDROP-PROMPTS.md
    python tool/art/backdrop_prompts.py --json out.json

The prompts carry what making 1816 taught (see BACKDROP-BRIEF.md): one
layer per skyline, night colours, magenta in every gap, the moon where the
city will not hide it, the shaft matching its capital. Edit the eras or the
wording here and regenerate, so the Markdown and anything built from the
JSON stay the same text.
"""
import argparse
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# The prompts never lean on the chat's history: Nano Banana grows unreliable
# over a long chat, so each era starts a new one, and a piece can be
# redone in yet another. What must match (the era's palette, the capital
# under a shaft) is attached, not remembered.
STYLE = ("Style: match the attached boar sprite exactly: crisp hard-edged pixels, no anti-aliasing, no blur, "
         "limited palette, clean dark outlines, light from the left. If a finished image of this same era is "
         "attached, use exactly its palette and pixel size.")

# Each era as the prompts describe it. "setting" opens every prompt; the rest
# fill the pieces. Cities are evocative, never portraits: where a famous
# building is what a model would copy (the resort hotel in 1944, the
# capital in 1971), the place is left unnamed.
ERAS = [
    dict(year=1816, era="The pound, by weight", setting="Regency London, 1816",
         sky="a cool blue-black night with a faint coal-smoke haze",
         sky_detail="a few faint small stars, thin grey-blue haze bands, a dim soft glow low down",
         moon=True,
         colours="muted dark slate blue and blue-grey",
         far="Georgian terraces, church spires and a dome or two",
         mid="Georgian brick terraces with rows of chimney pots, dormer and sash windows, a church spire and a clock tower",
         near="rooftops crowded with chimney pots, and bare winter trees",
         column="a fluted Portland stone column with a Corinthian capital",
         column_colour="cool pale grey-white stone",
         ground="wet cobblestones", ground_colour="dark blue-grey stone"),
    dict(year=1873, era="Silver steps back", setting="a growing American city, 1873",
         sky="a deep blue night",
         sky_detail="faint small stars, a thin low haze, a dim warm gaslight glow low down",
         moon=True,
         colours="muted dark blue and blue-grey with a hint of brick red",
         far="church steeples, mansard roofs and brick blocks",
         mid="red-brick commercial blocks with heavy cornices, mansard roofs, cast-iron shopfronts and a church steeple",
         near="rooflines with cornices and chimneys, and telegraph poles with sagging wires",
         column="a cast-iron column with raised bands and a flared, decorated head",
         column_colour="bottle green, clearly lighter than the city behind it, highlighted on the left",
         ground="brick paving with an iron rail track", ground_colour="dark brown-red brick and grey iron"),
    dict(year=1913, era="A central banking system", setting="New York, 1913",
         sky="a violet-grey dusk turning to night",
         sky_detail="a few faint stars, thin violet haze bands, a dim glow low down",
         moon=True,
         colours="muted dark violet-grey and slate",
         far="early skyscrapers and tall brick buildings",
         mid="brick buildings with wooden water tanks on their roofs and fire escapes, and early steel-framed skyscrapers with ornate tops",
         near="flat rooftops with wooden water tanks, chimneys and roof railings",
         column="a riveted steel I-beam with diagonal lattice bracing",
         column_colour="light blue-grey steel",
         ground="large granite paving slabs", ground_colour="dark grey granite"),
    dict(year=1923, era="The papiermark", setting="Berlin, 1923",
         sky="a smoggy mauve night",
         sky_detail="no stars, heavy low smog bands, a dull reddish glow low down",
         moon=False,
         colours="muted dark mauve, grey and soot brown",
         far="sawtooth factory roofs, tall smokestacks and domes in the smog",
         mid="tall tenement blocks with only a few lit windows, sawtooth-roof factories and tall smokestacks trailing smoke",
         near="factory roofs, chimneys and short stacks",
         column="a tall red-brick factory chimney bound with iron bands, blackened with soot at the top",
         column_colour="dull brick red, clearly lighter than the city behind it",
         ground="the worn stone setts of a factory yard", ground_colour="dark grey-brown stone"),
    dict(year=1933, era="Gold called in", setting="a Depression-era American city, 1933",
         sky="a brown-red hazy night",
         sky_detail="no stars, thick low haze, a dull red-brown glow low down",
         moon=False,
         colours="muted dark brown-red and charcoal",
         far="Art Deco setback towers",
         mid="Art Deco setback skyscrapers and office blocks with many dark, unlit windows",
         near="flat rooftops with water towers and stair housings",
         column="an Art Deco pillar with vertical flutes and a stepped chevron top",
         column_colour="pale stone with muted brass flutes, not bright gold",
         ground="cracked asphalt", ground_colour="dark charcoal grey"),
    dict(year=1944, era="Bretton Woods", setting="a mountain resort, 1944",
         sky="a warm dusk turning to night",
         sky_detail="a few faint stars, thin cloud, a band of warm dusk glow low down",
         moon=True,
         colours="muted dark blue-green and warm brown",
         far="dark mountain peaks",
         mid="a pine forest with one grand wooden resort hotel with long verandas, not any real hotel",
         near="dark pine treetops",
         column="a timber post bound with iron straps",
         column_colour="weathered warm brown wood with dark iron, clearly lighter than the forest behind it",
         ground="a gravel path at the edge of a lawn", ground_colour="dark grey gravel and dark green grass"),
    dict(year=1971, era="The window closes", setting="a low, classical capital city, 1971",
         sky="an amber-brown evening turning to night",
         sky_detail="a few faint stars, a warm amber haze low down",
         moon=True,
         colours="muted dark brown and warm grey",
         far="low domes and colonnades",
         mid="neoclassical government buildings with pediments, colonnades and domes, all of a similar low height",
         near="treetops and low rooflines",
         column="a white marble column with a simple Doric capital",
         column_colour="cool white marble with pale grey veining",
         ground="pale stone plaza paving", ground_colour="muted, darkened grey stone"),
    dict(year=1979, era="Rates raised", setting="a late-1970s American downtown, 1979",
         sky="a brown hazy night",
         sky_detail="no stars, a thick low brown haze, a dim orange-brown city glow low down",
         moon=False,
         colours="muted dark brown-grey and concrete grey",
         far="brutalist concrete blocks, glass box towers and construction cranes",
         mid="brutalist concrete office blocks, dark glass box towers, construction cranes and small red aviation lights",
         near="parking-garage roofs and rooftop machinery",
         column="a board-marked concrete pillar",
         column_colour="warm light grey concrete",
         ground="concrete pavement with expansion joints", ground_colour="dark grey concrete"),
    dict(year=2009, era="Issuance in code", setting="a glass city at night, 2009",
         sky="an amber-brown night",
         # No grid in the image: asked for "a very faint grid", Nano Banana drew
         # graph paper over the whole sky. The game draws its own faint,
         # scrolling grid over the 2009 sky.
         sky_detail="no stars, no lines, no grid and no pattern, only a thin warm haze and a soft amber city glow low down",
         moon=False,
         colours="muted dark brown and dark amber, never bright gold",
         far="tall glass towers",
         mid="dense glass towers with many rows of small lit windows and small red aviation lights",
         near="rooftops with antennas and satellite dishes",
         column="a dark glass pillar with light along its edges and faint circuit lines",
         column_colour="dark teal glass with bright cyan edges",
         ground="a dark glass floor with thin glowing circuit lines", ground_colour="near-black glass with dim cyan lines"),
]

MAGENTA = ("Background: everything that is not {what}, including every gap, is one flat solid pure magenta #FF00FF, "
           "with no shading, gradient, glow, shadow or haze on it. No magenta or pink anywhere in the {art}.")
SEAM_ACROSS = ("Seamless: the strip repeats side by side forever, so the right edge must continue exactly into the left "
               "edge: whatever is cut off at the right edge continues at the left edge at the same height, with no gap "
               "or jump.")
NEVER = "Never include: text, letters, numbers, signs, logos, people, animals, or any recognizable real building or famous landmark."


def pieces(e):
    s = e["setting"]
    moon = ("If there is a moon, make it a thin, pale, cool-white crescent near one side, between 20% and 35% of the "
            "way down from the top: lower down, the city will hide it. " if e["moon"] else "No moon. ")
    return [
        dict(part="sky", name="Sky", aspect="9:16", prompt="\n".join([
            f"Create a pixel art night sky for a side-scrolling mobile game. Setting: {s}, {e['sky']}.",
            STYLE,
            "Content: only sky, with no buildings, no ground and no horizon line. Fill the whole portrait image edge to "
            "edge. Dark and low-contrast, so gold coins and a golden flying boar stand out clearly in front of it. "
            "The sky is one smooth, continuous gradient from darkest at the very top to lightest at the bottom, with "
            "no bands, stripes, steps or lines anywhere in it. "
            f"Subtle atmosphere only: {e['sky_detail']}. {moon}"
            "Nothing bright, gold or yellow-orange above the bottom third.",
            NEVER,
        ])),
        dict(part="far", name="Far skyline", aspect="16:9", prompt="\n".join([
            f"Create a pixel art skyline strip for a side-scrolling mobile game: the most distant layer. Setting: {s}.",
            f"Draw only this one layer: a single row of distant {e['far']}, with nothing in front of it and nothing "
            "behind it.",
            f"Colours: {e['colours']}; hazy and low-contrast, only slightly lighter than the night sky; very few tiny lit "
            "windows. No beige, cream, white or pale daytime fog.",
            STYLE,
            "Layout: everything stands on the bottom edge and fills only the lower 65% of the image; the top 35% is "
            "empty background.",
            MAGENTA.format(what="part of this layer", art="art"),
            SEAM_ACROSS,
            NEVER,
        ])),
        dict(part="mid", name="Mid skyline", aspect="16:9", prompt="\n".join([
            f"Create a pixel art skyline strip for a side-scrolling mobile game: the main layer of the scene. Setting: {s}.",
            f"Draw only this one layer: a single row of {e['mid']}, with nothing in front of it and nothing behind it.",
            f"Colours: {e['colours']}; darker than a distant hazy skyline would be, with architectural detail and small "
            "warm lit windows scattered sparingly. Keep it darker and duller than a pale stone column, so columns "
            "stand out in front of it. No beige, cream, white or pale daytime fog.",
            STYLE,
            "Layout: everything stands on the bottom edge and fills only the lower 65% of the image; the top 35% is "
            "empty background.",
            MAGENTA.format(what="part of this layer", art="art"),
            SEAM_ACROSS,
            NEVER,
        ])),
        dict(part="near", name="Near skyline", aspect="16:9", prompt="\n".join([
            f"Create a pixel art strip for a side-scrolling mobile game: the nearest, darkest layer. Setting: {s}.",
            f"Draw only this one layer: a single low row of {e['near']}, with nothing in front of it and nothing behind it.",
            "Colours: nearly black silhouettes, tinted only faintly toward the night sky; almost no lit windows. No "
            "beige, cream, white or pale daytime fog.",
            STYLE,
            "Layout: everything stands on the bottom edge and fills only the lower 30% of the image; the top 70% is "
            "empty background.",
            MAGENTA.format(what="part of this layer", art="art"),
            SEAM_ACROSS,
            NEVER,
        ])),
        dict(part="capital", name="Column capital", aspect="1:1", prompt="\n".join([
            f"Create a pixel art game asset: the top of one standing column, seen straight on from the front. "
            f"Setting: {s}. Material: {e['column']}. Colour: {e['column_colour']}.",
            STYLE,
            "Make it light and crisp: after the coins, it must be the most readable thing in front of a dark night city.",
            "Layout: one perfectly vertical column, centered. Its capital (the decorative top) spans nearly the full "
            "width of the image; the shaft continues straight down out of the bottom edge. Nothing above the capital. "
            "No orange, amber or gold trim along its top edge.",
            MAGENTA.format(what="the column", art="column"),
            "Never include: text, letters, numbers, logos, people.",
        ])),
        dict(part="shaft", name="Column shaft", aspect="9:16", prompt="\n".join([
            "Create a pixel art game asset: a straight vertical section of the shaft of the same column as the "
            "attached column capital, seen straight on from the front. It must match that column exactly: the same "
            "material, the same colour, the same palette and pixel size, and the same fluting or banding as the shaft "
            "visible under that capital, kept plain and simple so it repeats well: at most one thin band. "
            f"Material: {e['column']}. Colour: {e['column_colour']}.",
            STYLE,
            "Layout: one shaft, perfectly vertical and centered, running off the top and bottom edges, with no capital, "
            "no base and no ends.",
            "Seamless: the section repeats end to end forever, so the top edge must continue exactly into the bottom "
            "edge: the same outline, grooves and bands in line, with no step or jump.",
            MAGENTA.format(what="the shaft", art="column"),
            "Never include: text, letters, numbers, logos, people.",
        ])),
        dict(part="ground", name="Ground", aspect="16:9", prompt="\n".join([
            "Create a pixel art ground strip for a side-scrolling mobile game, seen from the side as a cross-section. "
            f"Setting: {s}. Surface: {e['ground']}. Colour: {e['ground_colour']}.",
            STYLE,
            "Layout: the top edge is a perfectly flat, level line straight across the very top of the image, where a "
            "character's hooves stand. All the texture and detail sits in the top 30%; below that it is plain, dark, "
            "near black. Dark and low-contrast overall. Fill the whole image, with no background colour.",
            "Seamless: the strip repeats side by side forever, so the right edge must continue exactly into the left "
            "edge, with no visible seam, step or change in brightness.",
            "Never include: text, letters, numbers, logos, people, animals, puddles or anything bright.",
        ])),
    ]


FIXES = [
    ("The edges don't join",
     "The edges don't join. Redo it so the right edge continues exactly into the left edge: the same things at the "
     "same heights, with no gap or jump."),
    ("Several layers in one skyline, haze in the gaps, or pale daytime colours",
     "Redraw this as only one single row, with nothing in front of it or behind it. Night colours: dark and muted, "
     "only slightly lighter than a deep night sky; no beige, cream or pale fog. Every gap and everything above the "
     "row must be flat solid pure magenta #FF00FF, with no haze in the gaps."),
    ("The magenta is shaded or glowing",
     "Make the background one flat solid #FF00FF, with no shading, glow or gradient."),
    ("The style or colours drifted from the earlier images",
     "Match the palette, colours and pixel size of the attached image of this era exactly."),
    ("The shaft doesn't match the capital",
     "Redo the shaft in exactly the colour, material and fluting of the shaft under the attached capital."),
    ("A hard line or band across the sky",
     "Remove the band across the top of the sky. The whole sky is one smooth gradient, darkest at the top, with no "
     "edge, stripe or change of colour anywhere."),
    ("Lines, a grid or a pattern over the sky",
     "Remove every line, grid and pattern. The sky is only a smooth gradient with a soft glow low down, nothing else."),
    ("A famous landmark appeared",
     "Remove the famous landmark. Use only ordinary period buildings of the same style, none of them a real building."),
]


def data():
    return dict(eras=[dict(year=e["year"], era=e["era"], setting=e["setting"], pieces=pieces(e)) for e in ERAS],
                fixes=[dict(problem=p, reply=r) for p, r in FIXES])


def markdown(d):
    out = ["# When Pigs Fly — backdrop prompts", "",
           "Every era's seven pieces for Nano Banana, written out in full: paste as they are. Generated by",
           "`tool/art/backdrop_prompts.py`; the rules behind them are in `BACKDROP-BRIEF.md`.", "",
           "**Start a new Nano Banana chat for each era.** Long chats stop working properly, so no",
           "prompt relies on what a chat has already seen: what must match is attached instead.", "",
           "**Attach to every prompt:** one of the boar drawings (for style) and that era's",
           "code-drawn background render (for mood). From the second piece on, also attach the era's",
           "finished sky, so the palette carries over. For the shaft, attach the finished capital.", "",
           "If a chat misbehaves partway through an era, start another and carry on with the same",
           "attachments; nothing is lost. Save each image as `{year}_{piece}` (`.webp`, `.png` or `.jpg`)",
           "in `tool/art/source/backdrop/`, then run `python tool/art/import_backdrops.py --preview",
           "<folder>`. No cropping: the importer trims every piece to shape.", ""]
    for e in d["eras"]:
        out += [f"## {e['year']}: {e['era']}", "", f"*{e['setting'][0].upper()}{e['setting'][1:]}.*", ""]
        for p in e["pieces"]:
            out += [f"### {p['name']} ({p['aspect']}) → `{e['year']}_{p['part']}`", "", "```", p["prompt"], "```", ""]
    out += ["## When a result comes back wrong", "",
            "Reply in the same chat. If that chat is already long or misbehaving, paste the piece's prompt into a",
            "new chat with its attachments instead, and add the reply's text to the end of it.", ""]
    for f in d["fixes"]:
        out += [f"**{f['problem']}**", "", "```", f["reply"], "```", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="also write the prompts as JSON here")
    args = ap.parse_args()
    d = data()
    path = os.path.join(HERE, "BACKDROP-PROMPTS.md")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(markdown(d))
    print(f"{path}: {len(d['eras'])} eras, {sum(len(e['pieces']) for e in d['eras'])} prompts")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False)
        print(f"json: {args.json}")


if __name__ == "__main__":
    main()
