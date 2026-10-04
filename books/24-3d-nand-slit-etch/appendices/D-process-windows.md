# Appendix D — Representative Process Windows

> **Illustrative values only.** These ranges describe the *type* of conditions used in HAR dielectric etch and are not any manufacturer's recipe. They are provided to give a sense of scale and to support the worked problems in Appendix F.

| Parameter | Typical range | Primary effect |
|---|---|---|
| Pressure | 5–50 mTorr | Plasma density, ion angular spread (collisions in sheath) |
| Source power | 1–5 kW | Ion and radical flux |
| Bias power (low frequency) | 3–20 kW | Ion energy, mask loss, wafer heating |
| Bias frequency | 0.4–2 MHz | Width of ion energy distribution |
| Pulsing duty cycle | 20–80 % | Charge relief, radical/ion balance |
| Wafer temperature | –60 °C to +60 °C | Polymer sticking, etch rate |
| Polymer-forming gas (C₄F₆ / C₄F₈) | 10–60 sccm | Sidewall passivation |
| Hydrofluorocarbon (CH₂F₂ / CHF₃) | 10–80 sccm | Nitride etch, polymer composition |
| Oxygen | 10–100 sccm | Polymer removal, mask attack |
| Argon | 50–500 sccm | Dilution, sputtering |
| Mask selectivity (stack : a-C) | 5–15 | Mask thickness budget |
| Etch time (full slit) | 5–30 min | Throughput |

## D.1 Stepped recipe skeleton

| Step | Depth range | Intent |
|---|---|---|
| 1. Breakthrough | Cap oxide | Open through cap with mask-preserving chemistry |
| 2. Main etch | 0 – ⅔ of depth | Fast etch, moderate polymer |
| 3. Deep etch | ⅔ – full depth | Higher bias, less polymer, more O₂ |
| 4. Soft landing | Last 0.2–0.5 µm | Reduced bias, selectivity to source layer |
| 5. Over-etch | Fixed small time | Clear slow regions |
