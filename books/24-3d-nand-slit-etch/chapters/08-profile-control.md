# Chapter 8 — Profile Control: Taper, CD, Wiggling and Collapse

## 8.1 Setting the target profile

The slit's cross-section is specified by top CD, bottom CD, and a maximum allowed bow. A common requirement is a bottom/top CD ratio above a threshold such as 0.6–0.8, and a bow that stays within a tolerance of a few nanometres. The number of tiers means the sidewall angle is typically only ~0.5°–1° from vertical.

## 8.2 Controlling taper and bowing

Taper is set by how the polymer thickness varies with depth. Practical levers:

- **Step-wise polymer-former reduction** with depth, to keep the profile from pinching;
- **Bias ramp**: increase ion energy as depth increases;
- **Temperature profile** across the wafer and over time;
- **Mask shape**: a straight, vertical mask opening gives less initial bowing.

## 8.3 The wiggling problem

Slit **wiggling** (also called *line wiggling* or *striation*) is a lateral, nearly periodic displacement of the slit along its length. Two explanations coexist and probably act together:

1. **Mechanical.** A tall, thin wall under film stress behaves like a slender column. Compressive stress in the stack can drive buckling. Where the wall is partially anchored by channel pillars, the unanchored segments buckle.
2. **Plasma-driven.** Small local asymmetries in sidewall polymer deposit or charge amplify through a feedback loop: a slight lean directs ions toward one sidewall, thinning its passivation, causing it to etch further and leaning more.

Mitigations include stress management in the stack, lower-stress deposited films, mask designs that break symmetry, **dummy channel structures** near the slit to provide anchorage, and process settings that reduce charging.

## 8.4 Pattern collapse and the wet steps

After the slit is etched, the next steps expose the free-standing walls to wet chemistry and capillary forces. Collapse risk grows as the wall's slenderness rises. This is a strong reason to keep stack stress low and to dry carefully (low surface-tension drying) after the nitride removal.

## 8.5 A control strategy

An effective slit etch strategy has three layers:

1. **Design for etchability**: dummy channels, symmetric layout, dimensioned slits.
2. **Recipe architecture**: multi-step recipe with depth-dependent parameters.
3. **Feedback**: inline metrology (Chapter 13) drives chamber-to-chamber and lot-to-lot offsets.
