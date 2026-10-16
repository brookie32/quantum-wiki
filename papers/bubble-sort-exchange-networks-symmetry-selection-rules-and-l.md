---
title: "Bubble-Sort Exchange Networks: Symmetry Selection Rules and Language-Model Distillation on Exchange-Only Spin Chains"
date: "2026-10-16"
updated: "2026-10-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.22093"
summary: "arXiv:2610.22093v1 Announce Type: new Abstract: On a chain of exchange-coupled quantum dots a Heisenberg exchange pulse of area pi is a SWAP, so the parallel bubble-sort SWAP network of superconductin"
last_verified: "2026-10-16"
review_by: "2027-01-14"
stale: false
---

arXiv:2610.22093v1 Announce Type: new Abstract: On a chain of exchange-coupled quantum dots a Heisenberg exchange pulse of area pi is a SWAP, so the parallel bubble-sort SWAP network of superconducting chains is native to exchange-only (EO) spin qubits, and any other pulse area fuses routing with an entangling interaction. We build a variational "bubble-sort exchange network" (odd-even transposition, one parameter per pulse) and study it as a Born machine read out by Pauli spin blockade. Exchange conserves total spin, so the reachable readout distributions are fixed by the total-spin content of the initial product state. For the two-spin singlet-triplet encoding we derive a selection rule -- outcomes with k triplet pairs are bounded by the initial weight in sectors S <= k (S = 0 excluded for k = 1) -- and prove by a transportation argument that it is also sufficient: the reachable distributions form the polytope cut out by the rule, and its total-variation floor is attained. Products of singlets and T0's forbid whole outcome classes; the Neel state forbids none; the three-spin EO code has no floor. We then distil, in noise-free simulation, next-token distributions of GPT-2 over restricted vocabularies into the network, with matrix-product-state (MPS) Born machines as classical control. At six logical qubits the three-spin chain reaches KL = 0.011 nat at depth N and 0.004 at 2N, below the bond-dimension-4 MPS; the two-spin chain from the Neel state reaches 0.014 at 2N and 0.004 at 3N, against 0.28-1.5 from singlet/triplet products for the first teacher. Final states lie largely outside the code space: leakage is a resource, not an error. No arrangement of disjoint pulses meets every pair in fewer than N-1 rounds, and at depth 2N the chain distils as well as a 2D array or non-local couplings. Sector-restricted simulation extends this to 10-14 logical qubits (up to 30 dots).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.22093) | 2026-10-16
