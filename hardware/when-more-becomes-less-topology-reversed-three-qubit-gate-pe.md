---
title: "When More Becomes Less: Topology-Reversed Three-Qubit Gate Performance on IBM Quantum Processors"
date: "2026-08-24"
updated: "2026-08-24"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.21004"
summary: "arXiv:2608.21004v1 Announce Type: new Abstract: The exact Toffoli gate admits a six-CX decomposition, denoted by CCX_6, that is optimal under unrestricted two-qubit connectivity. On a linear three-qub"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

arXiv:2608.21004v1 Announce Type: new Abstract: The exact Toffoli gate admits a six-CX decomposition, denoted by CCX_6, that is optimal under unrestricted two-qubit connectivity. On a linear three-qubit topology, however, CCX_6 contains 4 nearest-neighbor CX gates and 2 non-nearest-neighbor CX gates. By contrast, an alternative exact decomposition, denoted by CCX_8, uses only 8 nearest-neighbor CX gates. Because CCX is locally equivalent to CCZ, we perform the experiments using the corresponding czs and czl circuits. We compare these circuits on sampled linear triples of the 156-qubit IBM Quantum Heron processors exttt{ibm_fez} and exttt{ibm_kingston}. Under the compilation protocol, the nominal czs circuit becomes a twelve-CZ implementation, whereas the linear-nearest-neighbor circuit retains eight native CZ gates. Experimentally measured ensemble-feature-selection estimates favor the eight-CZ realization on nearly all retained triples. We test the same ordering by preparing a three-qubit hypergraph state, which probes the coherent conditional phase rather than only computational-basis populations. The measured hypergraph-state infidelity is lower for the czl circuit for most triples on both processors. Phase-altered interleaved randomized benchmarking provides a complementary comparison of Clifford surrogates preserving the two compiled entangling structures. Within the scope of the tested circuits and phase-sensitive input state, the results demonstrate that hardware connectivity can reverse the operational ranking of exact decompositions: a circuit with more abstract two-qubit gates can yield the better physical implementation.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.21004) | 2026-08-24
