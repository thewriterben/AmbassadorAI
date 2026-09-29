# When Pigs Fly — boar pose prompts

Prompts for Nano Banana Pro that add to the owner's boar drawings without
replacing them. The drawings are the style every backdrop is matched to, and
an animation needs frames that match each other exactly, which generated
images are weakest at. So each prompt works from the owner's frames: it
attaches them and asks for the same boar in one new pose.

**Every time:**
- Start a new chat for each pose.
- Attach the drawings named with the prompt, from `tool/art/source/`.
- If the pose comes out wrong, run the prompt again in a new chat rather
  than correcting it over several replies.

The background is white, like the drawings, and the splitter clears it.
Size doesn't matter: the splitter finds the scale and lines each pose up on
the boar's own frames.

## The slots

| Slot | What it is | Until drawn |
|---|---|---|
| `landwin` | The touchdown after flying the whole passage | repeats `land` |
| `stand2` | A second standing pose, alternating with `stand` every 0.55 s | repeats `stand` |

The game picks `landwin` when every era was flown and `land` when the
reserve ran out short. The piglet's `land` is a teary flop, which used to
play after a win too.

## The shared part

Every prompt below starts with this paragraph:

```
Create a pixel art game sprite of the boar in the attached drawings: exactly the same character, with the same design, proportions, colours, markings, wings, palette and pixel size. One boar only, full body, nothing cropped, seen from the side, facing the same way as the attached drawings. Plain pure white #FFFFFF background: no ground, no shadow, no scenery, no text, no labels, no border.
```

## Happy landings

**Piglet** (`boar_piglet_landwin`). Attach `boar_piglet_land_drawn.jpg` and
`boar_piglet_stand_drawn.jpg`.
```
Create a pixel art game sprite of the boar in the attached drawings: exactly the same character, with the same design, proportions, colours, markings, wings, palette and pixel size. One boar only, full body, nothing cropped, seen from the side, facing the same way as the attached drawings. Plain pure white #FFFFFF background: no ground, no shadow, no scenery, no text, no labels, no border.
Pose: a proud, happy landing at the end of a long flight. Its hooves are just touching down, legs reaching for the ground, little white wings raised and spread for balance, head up, a big joyful smile with eyes squeezed shut in delight. No tears, no sweat drops.
```

**Juvenile** (`boar_juvenile_landwin`). Attach `boar_juvenile_land_drawn.jpg`
and `boar_juvenile_stand_drawn.jpg`.
```
Create a pixel art game sprite of the boar in the attached drawings: exactly the same character, with the same design, proportions, colours, markings, wings, palette and pixel size. One boar only, full body, nothing cropped, seen from the side, facing the same way as the attached drawings. Plain pure white #FFFFFF background: no ground, no shadow, no scenery, no text, no labels, no border.
Pose: a triumphant landing at the end of a long flight. Its hooves are just touching down, legs reaching for the ground, golden wings raised high, head up, a confident grin with bright eyes. No sweat drops, nothing tired.
```

**Razorback** (`boar_razorback_landwin`). Attach
`boar_razorback_land_drawn.jpg` and `boar_razorback_stand_drawn.jpg`.
```
Create a pixel art game sprite of the boar in the attached drawings: exactly the same character, with the same design, proportions, colours, markings, wings, palette and pixel size. One boar only, full body, nothing cropped, seen from the side, facing the same way as the attached drawings. Plain pure white #FFFFFF background: no ground, no shadow, no scenery, no text, no labels, no border.
Pose: a victorious landing at the end of a long flight. Its hooves are just touching down, legs reaching for the ground, great wings spread wide, head raised, a fierce proud grin, tusks bared, eyes bright.
```

## The razorback's second buck

**Razorback** (`boar_razorback_stand2`). Attach
`boar_razorback_stand_drawn.jpg`.

The current stand kicks the hind legs up. This is the other half of the
buck, and the game shows the two in turn.
```
Create a pixel art game sprite of the boar in the attached drawings: exactly the same character, with the same design, proportions, colours, markings, wings, palette and pixel size. One boar only, full body, nothing cropped, seen from the side, facing the same way as the attached drawings. Plain pure white #FFFFFF background: no ground, no shadow, no scenery, no text, no labels, no border.
Pose: the other half of the buck in the attached standing drawing. All four hooves planted on the ground, crouched low and gathered, head down, ready to kick again; wings folded as in the attached drawing; the same fierce face. Keep the body the same size as in the attached drawing: the two poses will alternate as an idle animation.
```

## In-between wing frames (optional)

Only if a wingbeat looks choppy on the phone. Attach the two frames the new
one goes between (for example `boar_piglet_cycle_1.png` and `_2.png`), and
say which two they are when sending the result: the frames are renumbered
to fit it in.
```
Create a pixel art game sprite of the boar in the attached drawings: exactly the same character, with the same design, proportions, colours, markings, wings, palette and pixel size. One boar only, full body, nothing cropped, seen from the side, facing the same way as the attached drawings. Plain pure white #FFFFFF background: no ground, no shadow, no scenery, no text, no labels, no border.
Pose: the in-between frame of a wingbeat, exactly halfway between the two attached frames. The body, head and legs stay exactly where they are in both frames; only the wings move, to halfway between their position in the first attached frame and in the second.
```

## How they go in

`split_frames.py`, as for the other poses:

    python tool/art/split_frames.py <image> tool/art/source/boar_<stage> --frames 1 \
        --ref tool/art/source/boar_<stage>_cycle_1.png --names landwin --floor <the stage's stand frame>

- **`--holes`:** add it for the juvenile and razorback.
- **`--scale`:** add it if the head match misjudges a pose, using the size
  found for the stage's other poses.
- **Then:** `import_boars.py`.
