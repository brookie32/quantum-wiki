---
title: "Gradient Blindness in Adaptive Architecture Search for IQP Born Machines"
date: "2026-11-19"
updated: "2026-11-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.24174"
summary: "arXiv:2611.24174v1 Announce Type: new Abstract: Instantaneous quantum polynomial (IQP) Born machines learn a probability distribution from data with a circuit of commuting gates that a classical compu"
last_verified: "2026-11-19"
review_by: "2027-02-17"
stale: false
---

arXiv:2611.24174v1 Announce Type: new Abstract: Instantaneous quantum polynomial (IQP) Born machines learn a probability distribution from data with a circuit of commuting gates that a classical computer trains at hundreds of qubits. Adaptive algorithms grow a sparse circuit from a small seed by adding in every round the candidate gates with the largest loss gradient. Such algorithms never add a candidate whose gradient vanishes, so the choice of seed decides which circuits they can reach. Here we show that a candidate gate has a nonzero gradient for some angles of the circuit exactly when its generator is the sum of an odd number of linearly independent generators already in the circuit. The common seed of one-qubit gates therefore never adds a gate on an even number of qubits, which exact gradients on 12 qubits confirm. A seed of one-qubit gates plus the edges of the Chow-Liu tree sees every candidate, and its circuits match the full circuits on 12 and 16 qubits with 10 to 13 percent of their parameters. At 484 qubits, a heredity pool keeps the search over higher-order gates feasible, and the circuits grown from this seed reach a lower test loss than the dense two-body circuit with 6 percent of its parameters, although the higher-order gates add no gain.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.24174) | 2026-11-19
