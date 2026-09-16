---
title: "A log-depth in-place quantum Fourier transform that rarely needs ancillas"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2505.00701"
summary: "arXiv:2505.00701v3 Announce Type: replace Abstract: When designing quantum circuits for a given unitary, it can be much cheaper to achieve a good approximation on most inputs than on all inputs. In th"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2505.00701v3 Announce Type: replace Abstract: When designing quantum circuits for a given unitary, it can be much cheaper to achieve a good approximation on most inputs than on all inputs. In this work we formalize this idea, and propose that such "optimistic quantum circuits" are often sufficient in the context of larger quantum algorithms. For the rare algorithm in which a subroutine needs to be a good approximation on all inputs, we provide a reduction which transforms optimistic circuits into general ones. Applying these ideas, we build an optimistic circuit for the in-place quantum Fourier transform (QFT). Our circuit has depth O(log (n / epsilon)) for tunable error parameter epsilon, uses n total qubits, i.e. no ancillas, is local for input qubits arranged in 1D, and is measurement-free. The circuit's error is bounded by epsilon on all input states except an O(epsilon)-sized fraction of the Hilbert space. The circuit is also rather simple and thus may be practically useful. Combined with recent QFT-based fast arithmetic constructions [arXiv:2403.18006], the optimistic QFT yields factoring circuits of nearly linear depth using only 2n + O(n/log n) total qubits. Additionally, we apply our reduction technique to yield an approximate QFT with well-controlled error on all inputs; it is the first to achieve the asymptotically optimal depth of O(log (n/epsilon)) with a sublinear number of ancilla qubits. The reduction uses long-range gates but no measurements.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2505.00701) | 2026-09-16
