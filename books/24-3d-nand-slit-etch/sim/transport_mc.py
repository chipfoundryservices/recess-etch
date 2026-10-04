#!/usr/bin/env python3
"""Free-molecular Monte Carlo of neutral transport in a slot vs a hole.

Geometry (all lengths in units of the opening width/diameter):
  slot : infinite along y, width 1, depth AR   (2-D walls x=0 and x=1)
  hole : circular, diameter 1, depth AR        (cylinder wall)
Particles enter the top with a cosine (diffuse) angular distribution,
move ballistically and re-emit diffusely (cosine law) at the walls.
At each wall hit a particle is lost with probability s (the reactive
sticking coefficient). We tally the fraction that reaches the bottom.

With s = 0 the hole result is the classical Clausing transmission
probability; this is the validation check.
"""
import csv, sys
import numpy as np

rng = np.random.default_rng(24)


def cosine_dir(n):
    """Cosine-law direction about the +normal: returns (normal, t1, t2)."""
    u = rng.random(n)
    phi = 2 * np.pi * rng.random(n)
    cth = np.sqrt(u)
    sth = np.sqrt(1 - u)
    return cth, sth * np.cos(phi), sth * np.sin(phi)


def slot(ar, s, n):
    # state: x in [0,1], z in [0,ar] (z=0 top), direction (dx,dz)
    x = rng.random(n)
    dz, dx, _ = cosine_dir(n)            # enters downward (+z)
    dx = dx * np.where(rng.random(n) < .5, 1, -1)
    z = np.zeros(n)
    thru = 0
    while x.size:
        with np.errstate(divide="ignore", invalid="ignore"):
            tw = np.where(dx > 0, (1 - x) / dx, np.where(dx < 0, -x / dx, np.inf))
            tz = np.where(dz > 0, (ar - z) / dz, np.where(dz < 0, -z / dz, np.inf))
        hit_end = tz < tw
        t = np.minimum(tw, tz)
        x = x + dx * t
        z = z + dz * t
        bottom = hit_end & (dz > 0)
        thru += int(bottom.sum())
        keep = ~hit_end                    # wall hits only
        keep &= rng.random(x.size) >= s    # absorption
        x, z, dx, dz = x[keep], z[keep], dx[keep], dz[keep]
        m = x.size
        nrm, t1, _ = cosine_dir(m)
        # reflected into the slot: wall at x~0 -> +x ; wall at x~1 -> -x
        x = np.clip(np.where(x < .5, 0.0, 1.0), 0, 1)
        dx = np.where(x == 0.0, nrm, -nrm)
        dz = t1
    return thru / n


def hole(ar, s, n):
    r = np.sqrt(rng.random(n)) * 0.5
    a = 2 * np.pi * rng.random(n)
    px, py = r * np.cos(a), r * np.sin(a)
    dzv, t1, t2 = cosine_dir(n)
    az = 2 * np.pi * rng.random(n)
    dxv = np.sqrt(1 - dzv**2) * np.cos(az)
    dyv = np.sqrt(1 - dzv**2) * np.sin(az)
    z = np.zeros(n)
    thru = 0
    while px.size:
        # solve |p + d t|_xy = 0.5
        A = dxv**2 + dyv**2
        B = px * dxv + py * dyv
        C = px**2 + py**2 - .25
        with np.errstate(divide="ignore", invalid="ignore"):
            tw = np.where(A > 1e-14, (-B + np.sqrt(np.maximum(B * B - A * C, 0))) / A, np.inf)
            tz = np.where(dzv > 0, (ar - z) / dzv, np.where(dzv < 0, -z / dzv, np.inf))
        hit_end = tz < tw
        t = np.minimum(tw, tz)
        px, py, z = px + dxv * t, py + dyv * t, z + dzv * t
        thru += int((hit_end & (dzv > 0)).sum())
        keep = ~hit_end & (rng.random(px.size) >= s)
        px, py, z = px[keep], py[keep], z[keep]
        m = px.size
        rho = np.hypot(px, py)
        nx, ny = -px / rho, -py / rho                  # inward normal
        tx, ty = -ny, nx                               # tangent in xy
        nrm, t1, t2 = cosine_dir(m)
        dxv = nrm * nx + t1 * tx
        dyv = nrm * ny + t1 * ty
        dzv = t2
        # put on the wall exactly
        px, py = -nx * .5, -ny * .5
    return thru / n


def main():
    ars = [1, 2, 5, 10, 20, 40, 60, 80, 100, 150]
    ss = [0, 0.001, 0.01, 0.05, 0.1, 0.3]
    rows = []
    for ar in ars:
        for s in ss:
            n = 400_000 if ar <= 60 else 200_000
            ps, ph = slot(ar, s, n), hole(ar, s, n)
            rows.append(dict(AR=ar, s=s, slot=ps, hole=ph, N=n,
                             se_slot=(ps * (1 - ps) / n) ** .5,
                             se_hole=(ph * (1 - ph) / n) ** .5))
            print(rows[-1], file=sys.stderr, flush=True)
    with open("transport_results.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
