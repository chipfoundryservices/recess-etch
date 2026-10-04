# Chapter 9 — Hard Mask Engineering

## 9.1 The selectivity budget

The mask must survive the entire etch. Define the selectivity S as the ratio of stack etch rate to mask etch rate. Required mask thickness is

t_mask = (stack depth / S) + margin.

For a 10 µm stack and S = 10, the consumed mask is 1 µm, and a practical mask is substantially thicker than that to allow for faceting and non-uniformity. Thick masks cause their own problems: they raise the aspect ratio of the *overall* opening and increase pattern-transfer difficulties.

## 9.2 Material choices

| Mask | Strengths | Weaknesses |
|---|---|---|
| **Amorphous carbon (a-C)** | High selectivity to oxide/nitride, strippable by O₂ ashing | Stress, thickness uniformity, line wiggling in the mask itself |
| **Doped a-C (B, W, other)** | Higher etch resistance, lower thickness | Strip complexity, residues |
| **Poly-Si** | Good selectivity in some chemistries | Needs different strip, contamination sensitivity |
| **Metal-containing masks** | Very high selectivity | Contamination control, stripping |

## 9.3 Mask erosion and faceting

Ions striking the mask at oblique angles remove material faster at 45° than at normal incidence, which rounds the mask corner. A faceted mask enlarges the opening at the top, producing a **funnel** that later shows up as a wider upper CD, and changes how ions are focused into the feature. Faceting is reduced by lower ion energy during the early phase, higher mask selectivity, and carbon-rich polymer deposition on the mask.

## 9.4 Mask patterning

The slit is a line pattern, which is easier to print than a dense hole array, but the line is long, so **line-edge roughness** and **line wiggling in the mask** transfer into the stack. The mask opening etch is therefore a critical precursor step with its own CD and roughness specifications.

## 9.5 Mask strip

After slit etch, the carbon mask is stripped in an oxygen plasma. Because the slit is open to the stack and to the memory pillars, the strip must not oxidise exposed metal or consume the exposed poly. Passivation from the etch (fluorocarbon residue) is also removed here, with a following clean.
