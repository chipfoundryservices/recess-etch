# Chapter 10 — Bias, Pulsing, Temperature and Reactor Design

## 10.1 Why bias is the main lever

By Chapter 5, ion flux, energy and angular spread at the bottom of the slit largely determine etch rate and profile. The reactor lets you set these through bias power, bias frequency and plasma density.

## 10.2 Low-frequency, high-power bias

HAR dielectric tools deliver kilowatts of bias power, often at around 400 kHz–2 MHz and sometimes at two frequencies together. Consequences:

- ions cross the sheath in a fraction of an RF cycle, so energy is spread over a wide range;
- the high-energy part of the distribution has a narrow angle and reaches the bottom;
- heat load on the wafer is very large, so electrostatic chuck cooling is a design limit.

## 10.3 Pulsing

Pulsed plasmas (source, bias, or both) switch levels with duty cycles of tens of per cent at kilohertz rates. Their value:

- **Charge relief** in the off-time lets electrons reach the feature bottom;
- **Radical-ion balance** changes because radicals persist in the afterglow while ions decay;
- **Lower average heat load** for the same peak ion energy.

The cost is complexity: duty cycle, frequency and phase between source and bias become recipe parameters, with strong interactions.

## 10.4 Temperature

Wafer temperature is controlled through the electrostatic chuck. Near room temperature or modestly below, polymer deposition and oxide etch have a convenient balance. At cryogenic temperature (for example below –50 °C) the physisorbed layer of etch species thickens, the etch rate can increase markedly, and the sidewall passivation changes character. The benefits reported for deep stacks are higher etch rate at depth and better profile control; the challenges are hardware, condensation of by-products, and chamber wall conditioning.

## 10.5 Edge and uniformity hardware

- **Focus ring / edge ring** material and height tune the sheath near the edge and thus tilt.
- **Multi-zone chuck temperature** and gas injection correct radial profiles.
- **Electrode design** for uniform field across a 300 mm wafer.

## 10.6 Chamber conditioning

Fluorocarbon processes deposit on chamber walls. A chamber that has just been cleaned behaves differently from one with a seasoned, polymer-coated wall, because the wall's sticking coefficient to radicals changes. This is the same transport effect as in Chapter 4, at the reactor scale, and it explains the first-wafer effect.
