# Appendix F — Worked Problems

**F.1 Mean free path.** At 20 mTorr and 300 K with d = 0.4 nm, what is λ, and how does it compare with a 5 µm deep feature?

*Solution.* n = P/(k_BT) = 2.667 Pa / 4.14 × 10⁻²¹ J = 6.4 × 10²⁰ m⁻³. λ = 1/(√2 π d² n) = 1/(4.443 × 1.6 × 10⁻¹⁹ × 6.4 × 10²⁰) ≈ 2.2 × 10⁻³ m = 0.22 cm. This is 440 times the 5 µm depth, so collisions inside the feature are negligible.

**F.2 Stack depth.** A stack has 176 tiers, each 28 nm oxide + 32 nm nitride. How deep is it, and what is the slit aspect ratio for a 110 nm average width?

*Solution.* Depth = 176 × 60 nm = 10.56 µm. AR = 10 560 / 110 ≈ 96.

**F.3 Neutral flux at the bottom.** Using Appendix B, estimate the relative flux of a non-reactive neutral at the bottom of that slit and of a hole of the same depth and diameter.

*Solution.* At AR ≈ 100 and s = 0, W_slot = 0.047 and W_hole = 0.013. The slit delivers about 3.6 times the flux.

**F.4 A reactive radical.** The same, for a radical with s = 0.1.

*Solution.* W_slot ≈ 5 × 10⁻³ and W_hole ≈ 4 × 10⁻⁵ (Appendix B). The ratio is about 100. In the hole the radical is effectively absent at the bottom.

**F.5 Ion angle.** An ion with 3 keV energy and 0.3 eV transverse energy: half-angle? What fraction of a slit of AR 96 does it subtend?

*Solution.* θ ≈ arctan √(0.3/3000) = arctan(0.01) = 0.57°. The slit subtends arctan(1/96) = 0.60°. The ion angle is comparable to the slit angle, so a substantial fraction strikes the sidewall: tight angular control matters.

**F.6 Tilt.** An edge-wafer tilt of 0.5° over 10 µm depth: bottom displacement?

*Solution.* 10 µm × tan(0.5°) = 0.087 µm = 87 nm, comparable to the slit width itself.

**F.7 Mask budget.** Stack depth 10.5 µm, selectivity 8, margin 30 %. Mask thickness?

*Solution.* Consumed = 10.5/8 = 1.31 µm; with margin 1.31 × 1.3 = 1.7 µm.

**F.8 Series model.** R_ion = 300 nm/min, R₀ = 800 nm/min, AR = 100 slot (W = 0.047). Net rate?

*Solution.* R_n = 800 × 0.047 = 37.6 nm/min. R = 1/(1/300 + 1/37.6) = 33.4 nm/min. (This is a toy illustration; real neutral-limited behaviour depends on how much of the etch is neutral-limited.)
