---
title: "Recovery gates as a resource in repetition-code process tomography: exhaustive gate-optimal designs for three, five and seven qubits"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.08310"
summary: "arXiv:2611.08310v1 Announce Type: new Abstract: Process tomography built on stabilizer codes compares the logical channel of a repetition code with a reference channel, and the decoder that produces t"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.08310v1 Announce Type: new Abstract: Process tomography built on stabilizer codes compares the logical channel of a repetition code with a reference channel, and the decoder that produces that channel is almost always fixed to the standard minimum-weight one. We ask how many physical single-qubit Pauli gates the decoder actually needs when the measurement basis is fixed---the constraint under which the count is a resource rather than a bookkeeping artefact. Exhaustive enumeration of every recovery design for n=3, 5 and 7 qubits, with rank decided by exact modular arithmetic at two primes, gives minimal counts of 0, 1 and 5 gates, against 6, 10 and 14 for first-order decoding and 6, 50 and 308 for full minimum-weight decoding. The count depends only on how many sites are corrected and never on which, so the two halves of the design problem separate. Correcting more sites is not monotonically better: at n=7 full decoding loses three dimensions of rank, and under a calibration-residual floor the precision curve at n=3 is U-shaped. The three-gate design is 9.5 times more precise than the standard six-gate decoder at the median of 40 sampled working points, and more precise at every one of them (1.8 to 88 times); the size of that factor belongs to the working point, the ordering does not. Reaching a 10,mrad rms error then costs 1.2imes10^{7} shots in 65,s on a current superconducting device at a well-conditioned point, while nge5 stays out of reach for conditioning reasons rather than gate-count reasons. Finally, the optimal designs are not covariant under chain reversal: they separate the mirror pair of arXiv:2610.19779 by 1.3imes10^{-3} while leaving the Jacobian at full rank.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.08310) | 2026-11-06
