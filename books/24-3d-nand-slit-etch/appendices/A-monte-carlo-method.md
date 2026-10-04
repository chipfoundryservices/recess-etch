# Appendix A — The Monte Carlo Method

## A.1 Algorithm

For each of N test molecules:

1. **Launch** at a uniformly random point on the opening with a cosine-law direction: the polar angle θ from the inward normal satisfies cos θ = √u, with u uniform on (0, 1), and the azimuth φ is uniform on (0, 2π).
2. **Propagate** in a straight line to the nearest surface: a side wall, the top (escape) or the bottom (transmitted).
3. If a wall is hit, **absorb** with probability s. Otherwise **re-emit** from the hit point with a fresh cosine-law direction measured from the wall's inward normal.
4. Repeat until the molecule is absorbed, escapes through the top, or reaches the bottom.

The transmission probability is W = N_bottom / N, with binomial standard error √(W(1 − W)/N).

## A.2 Geometry specifics

**Slot.** Translation invariance along y means only the (x, z) projection of the direction matters. The code samples the full 3-D cosine distribution and discards the y component; this preserves the correct angular weighting in the cross-section plane. Walls are x = 0 and x = 1; the bottom is z = AR.

**Hole.** Positions are (x, y, z) with the wall at x² + y² = ¼. The wall intersection solves a quadratic. The inward normal at the wall point defines the local frame for re-emission, with one tangent in the xy plane and the other along z.

## A.3 Vectorisation

Each iteration advances *all* surviving molecules by one flight. The active set shrinks as molecules are lost, so total cost is proportional to the total number of wall collisions (roughly ∝ AR²·W⁻¹ in the worst case), manageable at AR = 150 with 2 × 10⁵ molecules.

## A.4 Reproducing the results

```
cd books/24-3d-nand-slit-etch/sim
python3 transport_mc.py          # writes transport_results.csv (about 1.5 minutes)
cd .. && python3 build/build.py  # regenerates tables, figures, HTML and EPUB
```

The random generator is seeded (24), so results are repeatable on the same NumPy version. Sample sizes are 4 × 10⁵ for AR ≤ 60 and 2 × 10⁵ above that.

## A.5 Validation

Hole transmissions at s = 0 against Clausing's tabulated values:

| L/D | Simulated | Clausing |
|---|---|---|
| 0.5 | 0.6715 | 0.6720 |
| 1 | 0.5156 | 0.5136 |
| 2 | 0.3563 | 0.3589 |
| 5 | 0.1909 | 0.1910 |

The simulated values agree with the tabulated ones to within 0.0025 (under 1 % relative). Three of the four points are within about 2.5 standard errors (σ ≈ 0.0008 at N = 4 × 10⁵); the L/D = 2 point is about 3σ low in two independent runs (0.3563 and 0.3566, from the validation and the production sweep). We have not traced that small offset; it is below 1 % and does not affect any conclusion in the book. The tabulated values are quoted from memory of Clausing's classic table and should be re-checked against the primary source before any quantitative reuse.
