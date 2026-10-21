---
title: "Collision-aware Bayesian mitigation of photon loss in linear optical quantum circuits"
date: "2026-10-21"
updated: "2026-10-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.27529"
summary: "arXiv:2610.27529v1 Announce Type: new Abstract: Photon loss is the dominant noise source in linear optical quantum circuits. Each lost photon turns an ideal n-photon outcome into a pattern with fewer "
last_verified: "2026-10-21"
review_by: "2027-01-19"
stale: false
---

arXiv:2610.27529v1 Announce Type: new Abstract: Photon loss is the dominant noise source in linear optical quantum circuits. Each lost photon turns an ideal n-photon outcome into a pattern with fewer photons, so the detector counts no longer follow the ideal output distribution, and the lossless events that do follow it become exponentially rare as the photon number grows. Discarding the lossy events (postselection) therefore wastes most of the data at realistic loss rates, and the ideal distribution has to be inferred from the lossy counts themselves. Recycling-based mitigation (Mills & Mezher, Quantum 2026; Quandela's photon_recycling) reweights lossy samples to recover lossless probabilities, but its estimators are biased and restricted to the no-collision sector, where each output mode holds at most one photon. We instead treat the raw counts as Multinomial observations under per-photon binomial loss and infer the ideal output distribution and the loss rate jointly from a Bayesian posterior, which extends naturally to outputs with collisions. On data from the independent Perceval simulator at the scale of prior work (n=4 photons in m=20 and m=10 modes), the posterior has lower KL divergence than both recycling and postselection at every tested loss rate in the no-collision benchmark. In the collision regime it recovers the loss rate and the collision-pattern probabilities, which recycling cannot estimate, and stays below recycling at every loss rate and below postselection except at low loss, where the two are comparable. Its advantage over recycling grows with the sample count, and it supplies credible intervals that the baselines lack.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.27529) | 2026-10-21
