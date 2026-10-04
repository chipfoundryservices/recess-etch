# Chapter 6 — Chemistry for the Oxide–Nitride Stack

## 6.1 Design requirements

The slit chemistry must satisfy four requirements simultaneously:

1. Etch **SiO₂ and Si₃N₄ at similar rates**, so interfaces do not scallop.
2. **Passivate the sidewall** so that the lateral etch rate is a tiny fraction of the vertical one.
3. Maintain an **open feature** at depth (no etch stop).
4. **Preserve the mask**, with selectivity high enough to survive the whole depth.

## 6.2 The fluorocarbon family

Fluorocarbon gases are classified by their F:C ratio, which controls the balance between etching and polymer deposition:

| Gas | F:C | Behaviour |
|---|---|---|
| CF₄ | 4 | Strongly etching, F-rich, little polymer |
| C₄F₈ | 2 | Strong polymer former, good oxide selectivity to Si |
| C₄F₆ | 1.5 | Heavier polymer, produces high selectivity to mask and Si |
| CH₂F₂ / CHF₃ | 1–1.5 plus H | Hydrogen assists nitride etching and changes the polymer |
| NF₃ | — | F source, no carbon |

Hydrofluorocarbons (with H) matter for the nitride: hydrogen helps remove nitrogen as HCN or NH-containing products, so the nitride does not lag the oxide. A typical slit recipe blends a heavy polymer-former, a hydrofluorocarbon, oxygen, and argon.

## 6.3 The role of oxygen

Oxygen has two opposite effects:

- **Removes polymer** (CO, CO₂ formation), preventing etch stop at depth and opening the bottom;
- **Attacks the carbon mask** and increases lateral etch if overused.

Because O atoms are consumed on the walls at near-unity sticking (Chapter 4's s > 0 regime), they hardly reach the bottom. The effective O flux at depth comes from ions (O₂⁺, O⁺) and from the small line-of-sight fraction. This is why oxygen content must be adjusted as depth increases.

## 6.4 Sidewall passivation

The sidewall film is a fluorocarbon polymer on a thin modified (fluorinated) oxide/nitride layer. Its job is to absorb the grazing ion flux that would otherwise etch the sidewall. Characteristics of a good film:

- thin and **conformal** near the mask, thicker where the ion flux is higher;
- **carbon-rich** (conductive enough to limit charging);
- removable in a later clean step.

Where the passivation is thin the wall bows; where it is too thick the feature narrows and can pinch off.

## 6.5 The time-multiplexed (cyclic) approach

Cyclic processes alternate etching and deposition steps. Compared with a continuous mix, this gives independent control of each phase but introduces **scalloping** at the cycle period and reduces throughput. For the very deepest slits, short cycles, or ALE-like surface-limited steps, are a route to further profile control (Chapter 16).

## 6.6 Temperature

Surface temperature changes polymer sticking and the desorption of etch products. Lower temperature increases the thickness of the physisorbed reactant layer, raising the etch rate at a given ion flux and leaving a different sidewall film. Cryogenic dielectric etch is now a serious option for deep stacks (Chapter 10, Chapter 16).

## 6.7 Chemistry–transport coupling

A rule of thumb that follows from Chapter 4: the more reactive a species, the less of it reaches the bottom; therefore **a species whose job is at the bottom should have a low sticking coefficient or be delivered as an ion**, while one whose job is on the upper sidewall can be a high-sticking radical. Chemistry selection is largely an exercise in assigning each job to the species with the right sticking coefficient.
