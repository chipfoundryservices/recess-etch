# Appendix E — Short Derivations

## E.1 Cosine-law emission

Diffuse emission from a surface element has intensity proportional to cos θ per unit solid angle, so the probability of a polar angle between θ and θ + dθ is ∝ cos θ sin θ dθ. Integrating: P(≤ θ) = sin²θ. Setting P = 1 − u gives cos θ = √u, as used in Appendix A.

## E.2 Flux onto a surface

For an isotropic gas of density n and mean speed v̄, the flux through a surface is Γ = ¼ n v̄. In a feature in free-molecular flow, the same relation holds locally at the opening, with n set by the gas above.

## E.3 Direct-flight transmission through a slot

Consider a molecule entering a slot of width w and depth L. In the cross-section plane, only the in-plane angle ψ from the vertical matters. A molecule goes straight through without touching a wall if tan ψ < w/L (approximately, for the most favourable entry points; averaged over entry position the allowed range is smaller by about a factor of two). Under cosine weighting the in-plane angular density near ψ = 0 is flat, so the fraction is of order (w/L)·(a constant of order ½ to 1). This is the **direct-flight floor**. In the s = 0.1 data it appears as W·AR ≈ 0.5.

The same argument for a hole requires both in-plane components to be small, so the fraction scales as (D/L)², giving W ∼ 1/(4·AR²) = 2.5 × 10⁻⁵ at AR = 100, the same order as the 4 × 10⁻⁵ seen in the simulated hole data at s = 0.1.

## E.4 Long-tube limits

For a long circular tube, the Clausing transmission tends to 4D/(3L), i.e. W·AR → 4/3. For an infinite slit the corresponding result carries a logarithm, W ≈ (ln AR + c)/AR. The fit c ≈ 0.1 over 20 ≤ AR ≤ 150 in Chapter 4 is empirical, not derived.

## E.5 Series model for etch rate

If an ion-driven rate R_ion and a neutral-limited rate R_n act in series (each necessary), the net rate is R = (R_ion⁻¹ + R_n⁻¹)⁻¹. With R_n = R₀·W(AR) this gives the simplest ARDE curve: R → R_n at large AR where W is small, and → R_ion at small AR.
