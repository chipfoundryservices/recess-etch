# Chapter 1 — Why 3D NAND Needs a Slit

## 1.1 From planar to vertical

Planar NAND flash scaled by shrinking the floating-gate cell until electrons-per-cell and cell-to-cell coupling made further shrinking unprofitable. The industry's answer, first published as BiCS (Tanaka et al., VLSI Symposium, 2007) and followed by TCAT/V-NAND variants, was to stop shrinking in the plane and build *up*: a stack of alternating films is deposited, and strings of cells are formed by etching a vertical **channel hole** through the whole stack and lining it with charge-trap film and polysilicon.

Stacking changes what the etch tool is asked to do. Bit density now scales with the number of layers, so each generation deepens the stack. The channel hole and the slit are both **high-aspect-ratio (HAR)** features, and they get harder in step with every added layer pair.

## 1.2 What the slit is for

Most production flows use a **gate-replacement** (replacement-metal-gate-like) scheme. The stack is deposited as alternating oxide and sacrificial nitride. After the channel holes are made and filled, the nitride must be *removed* and replaced by tungsten word lines. To reach the nitride, a wet etchant (typically hot phosphoric acid) has to enter the stack from the side. The **slit** is a long, narrow trench etched through the entire stack to give the etchant, and later the tungsten precursors, that access.

The slit has second jobs as well:

- it divides the array into **blocks**, the erase unit of the device;
- after word-line formation it is filled with dielectric (often with a conductive source-line contact inside) to isolate neighbouring blocks;
- it provides the path for the stress relief and by-product removal during gate replacement.

## 1.3 Why a slit is not just a long hole

A slit has the same depth as a channel hole but is *long* in one direction. Geometrically it is the limit of an ellipse stretched without bound. Three consequences run through this entire book:

1. **Neutral transport is better in a slit** than in a hole of the same width and depth. Chapter 4 quantifies this with a Monte Carlo simulation: at an aspect ratio of 100 the slit passes about 3.6 times the free-molecular flux of a circular hole.
2. **Mechanical behaviour is worse.** A long, thin, tall wall of stack material has no lateral support from the neighbouring channel pillars and can bend, twist, or *wiggle* (Chapter 8).
3. **Landing is a line, not a point.** The bottom of the slit must stop on, or just into, a source-line structure along its whole length, so non-uniformity along the slit becomes a yield issue (Chapter 11).

## 1.4 Reading guide

The book has four parts. **Part I** sets up the device and the physics of transport. **Part II** is the etch itself: ions, chemistry, and how profiles go wrong. **Part III** integrates the etch with its neighbouring steps. **Part IV** covers measurement, modelling, control and the road ahead.

> **A note on numbers.** Process values quoted in this book (gas flows, powers, temperatures, critical dimensions, layer counts) are *representative and illustrative*. They are chosen to show relationships and orders of magnitude and do not describe any manufacturer's process. The transport numbers in Chapter 4 and Appendix B are different: they are computed by the simulation shipped in this repository (`sim/transport_mc.py`) and can be reproduced exactly.
