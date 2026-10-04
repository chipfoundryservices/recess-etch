# Chapter 16 — The Road Ahead

## 16.1 More layers

Each doubling of layer count roughly doubles the depth and keeps the width fixed, so the aspect ratio doubles. The transport results of Chapter 4 give a feel for the consequence: at AR 150 the hole delivers ~0.8 % of non-reactive neutral flux, and effectively none of a reactive radical, while a slit still passes about 3.5 % and has a direct-flight floor even with reactive loss.

## 16.2 Multi-deck (string-stacked) architectures

Rather than etch the whole stack in one go, build two or more decks, each etched separately and joined. The slit etch can then be done per deck (with the joint needing alignment) or once through the full stack. Per-deck etch relaxes aspect ratio at the price of an alignment and a joint with its own failure modes.

## 16.3 Wafer bonding (array and periphery on separate wafers)

Fabricating the CMOS periphery and the array on separate wafers and bonding them removes thermal and plasma-damage constraints on the periphery, and lets each be optimised. For the slit etch this relaxes the need to protect the underlying circuits, and changes the landing structure.

## 16.4 Cryogenic and advanced dielectric etch

Cryogenic wafer temperature, tailored pulsing, and new gas chemistries (including hydrogen-fluoride-containing mixtures) have been reported to raise the achievable depth and etch rate. They shift the balance of transport and chemistry described in Chapters 4 and 6.

## 16.5 Atomic-layer-style etching

Self-limited steps decouple the neutral supply from the ion step: an adsorption phase gives sufficient time for neutrals to diffuse to the bottom (long exposure, transport-limited but not rate-limiting), followed by a short ion-driven removal step. The time needed scales with 1/W, so it is the Chapter 4 transmission that sets the cycle time.

## 16.6 What stays hard

- Mechanical stability of ever-taller walls;
- Charging in deeper insulating stacks;
- Metrology that sees the bottom;
- Cost and throughput of low-rate, deep etches.

## 16.7 Closing thoughts

The throughline of this book is that the slit is a transport problem first and a chemistry problem second. Compute the transport, assign each job in the process to a species that can actually get there, and most of the design choices follow.
