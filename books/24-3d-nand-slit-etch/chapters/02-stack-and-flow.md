# Chapter 2 — Stack Architecture and the Gate-Replacement Flow

## 2.1 The film stack

From the bottom up, a representative 3D NAND stack contains:

| Region | Typical content | Etch relevance |
|---|---|---|
| Substrate / periphery | Si with CMOS logic (or bonded to a separate array wafer) | Must not be damaged by plasma |
| Source line | Doped poly-Si, sometimes with a sacrificial layer | Slit landing target |
| Lower select gate | Oxide / nitride or poly | Different etch rate from main stack |
| Memory stack | N pairs of SiO₂ (≈ 25–35 nm) and SiN (≈ 25–35 nm) | The bulk of the etch |
| Upper select gate | Oxide / nitride | Transition layer |
| Cap and hard mask | Oxide cap, carbon-based mask | Sets selectivity budget |

Each oxide–nitride pair is one **tier**. With a pair thickness near 60 nm, 200 pairs is roughly 12 µm; real stacks are often built from two or more decks to keep each etch manageable (Chapter 16).

## 2.2 Flow in outline

1. **Deposit** the alternating stack and the cap.
2. **Staircase** formation at the array edge so that each word line can be contacted (repeated trim-and-etch).
3. **Channel-hole etch**: the first extreme-AR etch.
4. **Memory film and channel deposition**: blocking oxide, charge-trap nitride, tunnel oxide, poly-Si, core fill.
5. **Slit etch**: the subject of this book.
6. **Nitride removal** through the slit by wet etch, leaving air gaps between oxide layers.
7. **Word-line formation**: high-k blocking layer, barrier, tungsten fill through the slit.
8. **Slit fill / isolation** and source-line contact.
9. **Contact and metal** layers.

## 2.3 Why the slit comes after the channel holes

If the slit were etched first, channel-hole patterning would have to cross a topography of tall free-standing walls. Etching the holes first gives mechanical anchoring: the filled channel pillars tie the stack together, which is exactly what keeps the slit walls from collapsing *during the later wet steps*. It also means the slit etch must run on a stack that is already full of dissimilar materials at the pillar locations, a point that matters for sidewall passivation and charging (Chapters 5 and 6).

## 2.4 Slit layout

Slits run through the array at a pitch of a few micrometres, defining **blocks** between them. Inside a block, rows of channel holes run parallel to the slit. The minimum distance from slit sidewall to the nearest channel hole is a design rule that exists *because of* slit profile variation: bowing and tilt eat into it. Typical slit openings are of order 100 nm with taper that makes the bottom narrower than the top.

## 2.5 What the slit etch must achieve

A convenient summary is the "five Ts":

- **Through**: clear the entire stack along the full slit length, all the way across the wafer.
- **Taper**: keep a controlled, small sidewall angle.
- **Targeted landing**: stop on, or a defined distance into, the source structure.
- **Twist-free**: no twisting, wiggling or tilt that varies along the slit.
- **Tidy**: no residue, no mask damage that propagates to later steps.

The rest of the book unpacks how each is achieved and how each fails.
