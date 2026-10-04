# Chapter 4 — Neutral Transport in Slots Versus Holes

This chapter replaces rules of thumb with computed numbers. The Monte Carlo code lives in `sim/transport_mc.py`; method details are in Appendix A and the full results table in Appendix B.

## 4.1 Free-molecular flow

At etch pressures of a few to tens of mTorr the mean free path of a neutral (centimetres to tens of centimetres) is enormously larger than the feature size (≈ 0.1 µm). Gas-phase collisions inside the feature are negligible and transport is **ballistic with surface reflections**: the Knudsen regime. The first-order question is the **transmission probability** W, the fraction of molecules entering the mouth that reach the bottom.

For a circular tube of length L and diameter D, W is the classical **Clausing factor** (Clausing, 1932). For long tubes W → 4D/(3L). For an infinite slit of width w and depth L, W is larger, with a logarithmic correction, because molecules can travel along the free direction without hitting a wall.

## 4.2 The simulation

We model:

- **Slot**: infinite along y, width 1 (all lengths in units of the opening), depth AR;
- **Hole**: circular, diameter 1, depth AR;
- cosine-law entry at the top; **diffuse (cosine-law) re-emission** at every wall hit;
- a **sticking coefficient s**: probability that a molecule is lost at a wall hit (s = 0 is a pure transport problem; s > 0 models radical consumption).

The hole result at s = 0 was checked against Clausing's tabulated values before any slot numbers were used: the simulated transmissions at L/D = 0.5, 1, 2 and 5 are 0.6715, 0.5156, 0.3563 and 0.1909 against the published 0.6720, 0.5136, 0.3589 and 0.1910.

## 4.3 Results, non-reactive species (s = 0)

{{TABLE:s0}}

{{FIG:t_vs_ar}}

Three observations:

1. **Hole.** For AR ≥ 20 the product W·AR sits at ≈ 1.27 ± 0.03, within a few per cent of the analytic limit of 4/3. Transmission falls as 1/AR.
2. **Slot.** W·AR *keeps growing*, from 3.1 at AR = 20 to 5.2 at AR = 150, and tracks ln(AR). A usable fit over 20 ≤ AR ≤ 150 is **W ≈ (ln AR + 0.1)/AR**.
3. **Ratio.** The slot-to-hole transmission ratio is 2.6 at AR = 20, 3.0 at AR = 40 and 3.6 at AR = 100, and 4.1 at AR = 150. It increases with depth, slowly.

The practical meaning: a slit etch is **less neutral-starved than a channel-hole etch of the same depth and width**, the gap widening as the stack grows.

## 4.4 Results with wall consumption (s > 0)

Etching neutrals are consumed on the walls, and the polymer precursors stick. Wall loss changes the picture sharply:

{{TABLE:s_sweep}}

{{FIG:t_vs_s}}

- With even s = 0.01, the hole's bottom flux at AR = 60 is ≈ 1.5 × 10⁻⁴ of the entering flux, compared with 1.7 × 10⁻² for the slot, a factor of **over 100**.
- At high s the hole's flux decays roughly exponentially with AR, while the slot's does not: it approaches a **floor** of direct line-of-sight transmission, on the order of 1/(2·AR) in these runs (0.5 % at AR = 100 for s = 0.1).

The floor exists because particles entering almost parallel to the slot's long axis in the cross-section plane can traverse the entire depth without touching a wall. It is a real property of the geometry, but it is carried by a narrow cone of directions, and the molecules that arrive this way hit the bottom with an anisotropic angular distribution.

## 4.5 What this tells the process engineer

- **Reactive radicals** (atomic F, O) essentially cannot reach the bottom of a deep hole; in a slit a small fraction can, mostly by direct flight.
- Etching at the bottom is therefore driven largely by **ions and by surface-diffused or recycled species**, not by gas-phase neutral supply.
- **Polymer precursors** are subject to the same transport law as etchants. If their sticking coefficient is high, the bottom is *starved* of polymer relative to the sidewall top, which is the mechanism by which the feature stays open (and by which the sidewall near the mouth is protected).
- Slit and hole etches **cannot share a recipe** without compensation: the neutral-to-ion balance at depth is materially different.

## 4.6 Caveats

The model is simplified: straight walls (no taper or bowing), constant s, diffuse re-emission without surface diffusion, no ion or charging effects, no gas-phase chemistry. It isolates geometry. Chapter 14 discusses how these effects are added in feature-scale simulators.
