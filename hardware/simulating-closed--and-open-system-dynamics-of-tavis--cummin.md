---
title: "Simulating closed- and open-system dynamics of Tavis--Cummings lattices on fault-tolerant quantum computers"
date: "2026-11-11"
updated: "2026-11-11"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.14398"
summary: "arXiv:2611.14398v1 Announce Type: new Abstract: Tavis--Cummings lattices couple cavities containing several emitters and host polaritonic many-body dynamics whose real-time correlations are costly to "
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

arXiv:2611.14398v1 Announce Type: new Abstract: Tavis--Cummings lattices couple cavities containing several emitters and host polaritonic many-body dynamics whose real-time correlations are costly to compute classically in two dimensions, especially when unequal emitter relaxation or dephasing rates break permutation symmetry. We analyze logical resources for fault-tolerant closed- and open-system simulation of an atom-resolved lattice with L cavities, N emitters per cavity, and photon cutoff n_{max}, including target observable estimation. Building on ladder-operator block encoding, we construct circuits for photon hopping and local light--matter exchange and combine them to encode the lattice Hamiltonian. By updating source and destination photon occupations in place, the hopping circuit eliminates the auxiliary Llceillog_2(n_{max}+1)rceil-qubit photon register used by two-register implementations. Across three uniform-coefficient examples with 16 to 256 cavities, the controlled walk uses 4.75--8.11% fewer Toffoli gates than the paired two-register implementation under matched shared preparation, precision, control, and workspace conventions. For closed systems, we implement real-time evolution with generalized quantum signal processing and bound the cost of estimating retarded cavity spectral functions. For open systems with photon loss, emitter relaxation, and dephasing, we use a sampled first-order dilation and bound the runs and timesteps needed to estimate transient photon statistics such as g^{(2)}(0). With state-preparation and measurement costs explicit, these estimates provide a reference for assessing fault-tolerant light--matter lattice simulation costs.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.14398) | 2026-11-11
