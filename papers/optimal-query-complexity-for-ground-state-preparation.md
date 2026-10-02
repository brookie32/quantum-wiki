---
title: "Optimal Query Complexity for Ground-State Preparation"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.35668"
summary: "arXiv:2609.35668v2 Announce Type: replace Abstract: We determine the optimal query complexity of ground-state preparation to trace-distance error arepsilon when an energy threshold in the spectral gap"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2609.35668v2 Announce Type: replace Abstract: We determine the optimal query complexity of ground-state preparation to trace-distance error arepsilon when an energy threshold in the spectral gap is known. Let U_H be an alpha-block-encoding of a Hamiltonian with unique ground state |psi_0rangle, and suppose |langlepsi_0|U_I|0rangle|gegamma for a state-preparation oracle U_I. The threshold lies at least Delta/2 above the ground-state energy and at least Delta/2 below every excited-state energy. We give two algorithms that prepare a state within trace distance arepsilon of the ground state. One uses O((alpha/Delta)(gamma^{-1}+log(1/arepsilon))) calls to U_H in expectation; the other uses O((alpha/(gammaDelta))log(1/arepsilon)) calls to U_H in the worst case. We prove a lower bound matching the expected query count; the corresponding worst-case lower bound follows from Somma and de Wolf [SdW26]. The respective bounds on calls to U_I are O(1/gamma) in expectation and O(gamma^{-1}log(1/arepsilon)) in the worst case. On (N+1)-dimensional systems, these U_I bounds are also optimal when the expected or worst-case count of U_H calls, respectively, is o((alpha/Delta)sqrt N). Both algorithms use a constant-accuracy spectral filter to construct a purifier, which we then sequentially compose during amplitude amplification to prepare a state with constant overlap with the ground state. The expected-query algorithm repeats the preparation followed by one high-accuracy spectral filter until success. The worst-case algorithm uses filters of increasing accuracy and limits the total number of queries.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.35668) | 2026-10-02
