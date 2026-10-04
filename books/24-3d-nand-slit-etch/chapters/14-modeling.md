# Chapter 14 — Modelling and Simulation

## 14.1 Model hierarchy

| Scale | Question | Method |
|---|---|---|
| **Reactor** | Plasma density, species fluxes at the wafer | Fluid or hybrid plasma models |
| **Sheath** | Ion energy and angle distribution | Particle-in-cell, Monte Carlo |
| **Feature** | How the profile evolves | Level-set / string / cell-based Monte Carlo |
| **Atomistic** | Sputter yields, surface reactions | Molecular dynamics, DFT |

Each level feeds parameters to the next. The model in Chapter 4 is a deliberately minimal feature-scale transport model.

## 14.2 The transport code in this book

`sim/transport_mc.py` has fewer than 150 lines and no dependencies beyond NumPy. It tracks particles in a vectorised loop: for each active particle, find the nearest wall or end, advance to it, test for absorption, and re-emit with a cosine-law direction. Appendix A describes the algorithm and Appendix E derives the analytic limits it should reproduce.

## 14.3 Validation

The first rule of simulation is to test against a known answer. Here the hole result at s = 0 reproduces Clausing's table within the statistical error (Chapter 4). A second check: the limiting behaviour W·AR → 4/3 for holes. For the slot the code reproduces the logarithmic growth of W·AR expected from the 2-D geometry.

## 14.4 Adding physics

A realistic feature simulator adds:

- **Surface reaction models**: Langmuir-type coverage of etchant and polymer, with ion-assisted removal;
- **Angular and energy distributions** for ions from sheath models;
- **Charging**: a self-consistent electric field solved on the evolving geometry;
- **Surface diffusion** of adsorbed species, which can transport etchant down the wall;
- **Profile evolution** via level sets or Monte Carlo surface movement.

## 14.5 Calibration

Free parameters (sticking coefficients, yields) are calibrated against cross-section images at several depths and several recipes. Models are used to rank options and understand trends, rarely to predict absolute numbers.

## 14.6 Limits of model-based development

Models cannot capture every mechanism. Wiggling in particular depends on stress and plasma feedback, which is hard to model end-to-end. Treat models as a way to **discard bad ideas quickly** and to explain results, not as a replacement for experiments.
