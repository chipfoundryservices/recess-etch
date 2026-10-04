# Chapter 5 — Ion Transport, Angular Distributions and Charging

## 5.1 Ions as the delivery vehicle

Chapter 4 showed that neutrals reach the bottom of a deep feature in small and shrinking numbers. Ions are different: the sheath makes them nearly collimated. For an ion of energy E and transverse (thermal) energy kT_i, the angular half-width is roughly

θ ≈ arctan √(kT_i / E).

With kT_i of a few tenths of an eV and E of a few kV, θ is well below 1°. A slit of aspect ratio 60 subtends a half-angle of roughly arctan(1/60) ≈ 1°, so even this tiny spread matters: a fraction of the ions strike the sidewall instead of the bottom. Higher energy narrows the distribution and raises transmission, at the cost of mask loss.

## 5.2 Differential charging

An insulating stack charges. Electrons have an isotropic, thermal angular distribution and cannot follow the narrow channel to the bottom as ions do; they are collected at the top of the sidewalls. Positive ions arriving at the bottom therefore leave it with net positive charge, while the upper sidewall and mask are negative. The resulting electric field inside the feature has two effects:

- it **decelerates and deflects ions**, increasing sidewall strikes (leading to bowing and a reduced bottom flux);
- it can **tilt** the ion trajectories asymmetrically if the feature is asymmetric, because charge accumulates on one side more than the other.

The effect is rooted in the same physics as **notching** (Hwang and Giapis, J. Vac. Sci. Technol. B 15, 70, 1997).

## 5.3 Why the slit charges differently from a hole

In a hole the sidewall surrounds the beam; field lines are roughly axisymmetric and the deflection is radially symmetric, so the charging effect mostly slows the etch. In a slit the two walls face each other across a *finite* width but extend indefinitely along y. Two things follow:

1. Because there is no confinement along y, **no field gradient exists along the slit axis**; charging non-uniformity is a cross-section effect only.
2. Any small left-right asymmetry in the surfaces (for example, one wall facing the array and the other facing a dummy region with a different density of filled channel pillars) produces a net lateral field, driving **tilt**.

## 5.4 Mitigation

Common levers, all of which have costs:

| Lever | Mechanism | Cost |
|---|---|---|
| **Pulsed bias** | Off-time allows electrons to neutralise the bottom | Lower average ion flux, slower etch |
| **Dual-frequency bias** | Broader and higher-energy ion distribution | Mask loss |
| **Higher ion energy** | Overcomes the retarding field | Mask erosion, damage |
| **Conductive coatings (carbon-rich polymer)** | Bleeds off charge on sidewalls | Polymer must be controlled |
| **Lower temperature** | Increases film conductivity and sticking of etch inhibitors in some chemistries | Hardware complexity |

## 5.5 Practical diagnostics

Evidence of charging-limited etching:

- bottom CD and etch rate decrease more rapidly than neutral-transport alone predicts;
- sidewall profile shows bowing just below the mask;
- tilt correlates with local pattern density, not with the tool;
- changing bias pulsing duty cycle changes profile without a change in chemistry.
