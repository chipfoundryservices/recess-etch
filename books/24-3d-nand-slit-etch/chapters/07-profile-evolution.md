# Chapter 7 — Etch-Front Evolution, ARDE and Failure Modes

## 7.1 Etch rate versus depth

For a slit, etch rate declines with depth. Three phases are typical:

1. **Early, near-mask phase.** Neutral supply is plentiful; rate is high and the profile responds to mask shape.
2. **Middle phase.** Neutral transport and ion deflection both matter; rate falls roughly as a power law in depth.
3. **Deep phase.** Ion-limited; the rate is small but fairly constant, and the profile is most sensitive to charging.

Recipes are therefore **stepped**: parameters change at depth boundaries (more bias, less polymer former, more oxygen) so that the process stays in the intended regime throughout.

## 7.2 A catalogue of defects

| Defect | Description | Primary cause |
|---|---|---|
| **Bowing** | Maximum CD below the mask, narrower above and below | Ion deflection onto sidewall, thin passivation |
| **Taper** | Top wider than bottom | Polymer thickness gradient |
| **Necking / pinch-off** | CD reduction partway down | Excess polymer, etch-stop onset |
| **Scalloping** | Periodic roughness at oxide/nitride interfaces | Rate mismatch between materials |
| **Tilt** | Slit axis not vertical | Asymmetric charging or sheath non-uniformity at wafer edge |
| **Twisting / wiggling** | Lateral oscillation of the slit along its length | Mechanical instability plus local charging (Chapter 8) |
| **Under-etch** | Slit does not reach the target | Etch stop, ARDE |
| **Punch-through** | Slit passes the landing layer | Over-etch, poor selectivity |

## 7.3 Interplay of mechanisms

These defects do not occur independently. Reducing bowing by adding passivation increases the risk of pinch-off. Raising ion energy reduces etch-stop risk but increases mask erosion, which changes the mouth shape, which changes charging. Process development is multi-objective.

## 7.4 Edge-of-wafer effects

Near the wafer edge the plasma sheath bends, so the ion trajectory acquires a lateral component. Over a depth of several micrometres, a ≈ 1° tilt displaces the bottom by ≈ 0.1 µm, which is comparable to the slit width. Edge rings with tuned height and material, and edge-specific bias adjustments, address this.

## 7.5 Model-based insight

The simplest first-order predictor of etch rate at depth is a series combination of ion-limited rate R_ion(AR) and neutral-limited rate R_n(AR), with R_n scaling as the transmission probability computed in Chapter 4. This reproduces the qualitative trend and, importantly, explains why *slit* ARDE is milder than *hole* ARDE at the same aspect ratio.
