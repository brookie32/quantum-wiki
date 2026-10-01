---
title: "Learning Random Quantum Circuits and the Emergence of Pseudorandomness"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39821"
summary: "arXiv:2609.39821v1 Announce Type: new Abstract: We give an efficient algorithm for learning k-dimensional brickwork random quantum circuits using only copies of the output state obtained by applying U"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39821v1 Announce Type: new Abstract: We give an efficient algorithm for learning k-dimensional brickwork random quantum circuits using only copies of the output state obtained by applying U to the all-zero input. For a depth-d circuit on n sites with random 2ell-qubit gates, the algorithm learns the original circuit U with high probability in ext{poly}(n,2^{ell d}) time for every constant dimensional lattice. In particular, the algorithm is polynomial time as long as ell d = O(log n). In one dimension, this reaches the natural boundary suggested by pseudorandomness: pseudorandom states require ell d=omega(log n), and structured cryptographic constructions suggest that this scale may be achievable from above. In higher dimensions, it remains plausible that the same ell d=omega(log n) scale remains the threshold for ancilla-free pseudorandomness, and our results help clarify the conditions under which pseudorandomness can arise in this setting. The main idea behind our algorithm is a local correlation criterion that identifies gates in the final layer without learning their entire backward light cones, avoiding a bottleneck in the previous approaches. A key technical ingredient is a Carbery-Wright type anticoncentration inequality for low-degree polynomials of Haar random unitaries whose small-ball exponent is independent of the matrix dimension. The dimension-independent exponent is crucial for handling gates of growing locality. This anticoncentration result may also be of independent interest.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39821) | 2026-10-01
