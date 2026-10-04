# Chapter 13 — Metrology and Inspection

## 13.1 The measurement challenge

The quantities that matter, bottom CD, bow depth, tilt and landing depth, are buried several micrometres below the surface. Top-down imaging sees only the mouth.

## 13.2 Techniques

| Technique | What it gives | Limitation |
|---|---|---|
| **Top-down CD-SEM** | Top CD, line-edge roughness | Blind to depth |
| **High-voltage SEM (HV-SEM) / BSE imaging** | Bottom features through the stack by high-energy electrons | Resolution falls with depth |
| **Optical CD (scatterometry, OCD)** | Averaged profile model: CD, depth, sidewall angle | Needs a model; limited to periodic targets |
| **X-ray scatterometry (CD-SAXS)** | Shape and tilt of buried HAR structures, nondestructive | Throughput, tool availability |
| **Cross-section SEM / FIB** | Direct profile image | Destructive, slow, one location |
| **TEM** | Interface detail, sidewall film thickness | Very slow, sample prep |
| **Electrical test** | Leakage and continuity at slit bottom | Late feedback |

## 13.3 Inline versus offline

Inline tools provide fast feedback but with model dependence. Offline tools give ground truth but are slow. A good control scheme uses cross-section data to calibrate inline models periodically.

## 13.4 Defect inspection

Systematic defects (a failed region of the wafer) and random defects (particles, residue plugs) are distinguished by pattern across the wafer. Optical inspection finds mask-level defects; bottom residues need HV-SEM or electrical test.

## 13.5 Metrology for wiggling

Wiggle amplitude and period are extracted by top-down imaging at the mouth, since the mask opening follows the bottom to some extent, plus rare cross-sections through a plane that cuts along the slit. Statistical metrics (RMS lateral displacement, spectral content along the slit) give a quantitative handle.
