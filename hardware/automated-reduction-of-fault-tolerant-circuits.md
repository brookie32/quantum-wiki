---
title: "Automated reduction of fault-tolerant circuits"
date: "2026-10-08"
updated: "2026-10-08"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.09749"
summary: "arXiv:2610.09749v1 Announce Type: new Abstract: We present an automated method for reducing fault-tolerant circuits through fault-equivalent rewrites. Starting from a known fault-tolerant circuit, the"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

arXiv:2610.09749v1 Announce Type: new Abstract: We present an automated method for reducing fault-tolerant circuits through fault-equivalent rewrites. Starting from a known fault-tolerant circuit, the search applies non-reducing enabling rules to expose Bell-pair reductions, each of which removes an ancilla preparation and a CNOT gate. Because every search transition preserves fault equivalence, the resulting circuits inherit the fault-tolerance properties of the input circuit. Candidate circuits are evaluated using circuit-level Monte Carlo simulation. For Shor-style syndrome extraction with the [[7,1,3]] code, our method reduces one syndrome-measurement round from 30 to 18 ancilla preparations and from 54 to 42 CNOT gates. At a physical two-qubit error rate of p = 10^{-3}, the optimized circuit lowers the logical error rate by approximately 21% for both logical basis states. The reduction ranges from 13% to 23% over a range of p spanning two orders of magnitude. We also apply the method to Steane-based dynamic syndrome extraction constructed from Goto's verified logical-lvert 0 rangle preparation, in which the verification qubit serves as a flag. The search selects a circuit using four ancillas and 14 CNOT gates, matching the resource counts of the previous design but with an improved CNOT depth. Under depolarizing idle noise at 3p/10 the selected circuit lowers the logical error rate by approximately 15% for both logical basis states, and by approximately 10% at p/10. These results demonstrate that automated fault-equivalent rewriting can identify circuits with lower resource costs or improved logical performance without separately verifying the fault tolerance of every candidate.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.09749) | 2026-10-08
