---
title: "Stabilizers for Compiling Logical Circuits under Hardware Constraints"
date: "2026-04-29"
updated: "2026-04-29"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.25042"
summary: "arXiv:2604.25042v1 Announce Type: new Abstract: To implement quantum algorithms on a quantum computer, we must overcome the twin problems of fault-tolerance -- how can we realize a relatively noiseles"
last_verified: "2026-04-29"
review_by: "2026-07-28"
stale: false
---

arXiv:2604.25042v1 Announce Type: new Abstract: To implement quantum algorithms on a quantum computer, we must overcome the twin problems of fault-tolerance -- how can we realize a relatively noiseless computation by cleverly combining noisy components? -- and compilation -- how can we realize an arbitrary quantum algorithm given the basic operations available on the quantum device at hand? We show how treating the former problem via error-correcting codes enables greater flexibility in resolving the latter. Specifically, we explicitly leverage the fact that error-correcting codes introduce redundancy which renders physically distinct operators logically indistinguishable. In terms of computation, it suffices to implement any operator logically equivalent to some target, yet from a compilation perspective, certain choices may be preferable to others. Our novel contribution is making this intuition precise in the general setting of the special unitary group. In particular, we describe how to reduce the problem of making a compilation-ideal choice to a least squares problem and provide a closed form solution thereof. Using our framework, it is possible to circumvent inserting costly swaps to adhere to hardware connectivity; instead, we could realize the logical target through a distinct physical Hamiltonian that is natively accessible. We elucidate our approach using the [[4,2,2]] code. We discuss connections to compressed sensing that may pave the way to efficient compilation leveraging physical degrees of freedom.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.25042) | 2026-04-29
