# Chapter 3 — Plasma Etch Fundamentals for High-Aspect-Ratio Features

## 3.1 The four-component model

Reactive-ion etching of dielectrics is usually described with the **ion-neutral synergy** model of Coburn and Winters (J. Appl. Phys. 50, 3189, 1979): neither energetic ions nor reactive neutrals alone etch efficiently; the combination does. For fluorocarbon etching of oxide and nitride, four species matter:

- **Etchant neutrals** (F, O) that attack the surface chemically;
- **Polymer precursors** (CFₓ, CₓFᵧ radicals) that deposit a thin fluorocarbon film;
- **Energetic ions** (CFₓ⁺, Ar⁺, O₂⁺) that supply energy for etching through that film;
- **Inhibitors**, in the sense of the film itself, which protects surfaces that ions do not strike.

## 3.2 The flux budget in a narrow feature

The surface at the *bottom* of a HAR feature sees a flux of each species reduced relative to the flux at the mouth. For each species:

- **Neutrals** arrive with an isotropic (cosine-like) angular distribution, travel in straight lines, and are reflected or consumed at the walls. Their flux at the bottom falls roughly as 1/AR for non-reactive species and much faster once the walls consume them (Chapter 4).
- **Ions** arrive nearly vertically, because the sheath accelerates them along the normal. Their loss at the walls comes from angular spread and charging-induced deflection (Chapter 5).

The ratio of ion flux to neutral flux at the bottom therefore **rises** with depth. This is the origin of several HAR behaviours: the etch becomes more ion-limited and less chemical, and polymer thickness at the bottom shrinks.

## 3.3 Ion energy and the sheath

The sheath voltage sets the ion energy. Two knobs matter:

- **Source power** (typically RF at a few MHz to tens of MHz, or microwave) controls plasma density, hence ion flux;
- **Bias power** at a low frequency (hundreds of kHz to a few MHz) controls ion energy and its distribution.

Low bias frequency is important because ions respond to the instantaneous sheath voltage, giving a **wide bimodal energy distribution** with a high-energy peak. High-energy ions have narrower angular spread, which is what HAR etches want. The trade-off is mask erosion and substrate damage.

## 3.4 Aspect-ratio-dependent etching (ARDE)

ARDE is the observation that deeper or narrower features etch more slowly. Gottscho and co-workers (J. Vac. Sci. Technol. B 10, 2133, 1992) categorised the mechanisms: Knudsen transport of neutrals, ion shadowing, differential charging, and neutral shadowing. In a slit the dominant contributors are (i) neutral starvation of etchant, (ii) a polymer-clogging effect that is *opposite* in sign, and (iii) charging. The measured etch rate versus depth is the product of all three.

## 3.5 The "etch-stop" regime

If the passivating-polymer flux at the bottom exceeds the ion-driven removal rate, the feature stops etching altogether. This is an aspect-ratio-dependent **etch stop**. It sets an upper bound on the achievable depth for a given chemistry and motivates higher ion energies, pulsing, oxygen addition and low temperature (Chapters 6 and 10).

## 3.6 Selectivity in alternating stacks

The stack contains SiO₂ and Si₃N₄, and the mask is carbon. The oxide-to-nitride etch-rate ratio should be close to 1, to avoid **scalloping** of the walls where the two materials meet. At the same time the etch rate of mask must be several times lower than that of the stack. The chemistry in Chapter 6 is designed around these two opposing constraints.
