# Chapter 15 — Process Control, Defects and Yield

## 15.1 Sources of variation

| Level | Examples |
|---|---|
| Within slit | Along-slit bow variation, wiggling |
| Within wafer | Radial CD, tilt, depth |
| Wafer-to-wafer | Chamber wall state, temperature drift |
| Chamber-to-chamber | Hardware differences, consumables |
| Lot-to-lot | Incoming stack film thickness |

## 15.2 Incoming variation

The etch sees the stack's actual thickness. A thicker-than-nominal stack needs more etch time and mask; endpoint and depth control must adapt. **Feed-forward** from deposition thickness metrology to etch time is standard.

## 15.3 Run-to-run control

Measured post-etch CD and depth update recipe offsets for later wafers (feedback). Multi-variable controllers use a model of how recipe knobs (bias, pressure, gas ratio, temperature) influence each profile metric.

## 15.4 Fault detection

Sensors (RF forward/reflected power, matching network positions, optical emission, chamber pressure) are monitored for signature drift. Optical emission is also an endpoint tool (Chapter 11).

## 15.5 Chamber matching

Matching chambers means matching their *outputs* (profile) rather than their settings, because hardware differs. Parameters such as bias coupling, wall state, and edge-ring wear are tuned to bring chambers within spec.

## 15.6 Typical yield detractors

- Under-etch or bottom residue → open contact;
- Over-etch → leakage;
- Wiggling → slit-to-channel spacing violation or fill voids;
- Collapse in wet steps → catastrophic die loss;
- Particle plugging → localised failures.

## 15.7 Learning from failures

A good habit is to maintain a defect library with cross-section images and the parameter history for each failure mode, then link patterns in inline data to known failure signatures.
