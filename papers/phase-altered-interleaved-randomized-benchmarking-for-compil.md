---
title: "Phase-Altered Interleaved Randomized Benchmarking for Compiled Non-Clifford Gates"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2606.30327"
summary: "arXiv:2606.30327v2 Announce Type: replace Abstract: Interleaved randomized benchmarking (IRB) provides a scalable estimate of a gate's error rate, but its standard guarantees require the interleaved g"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2606.30327v2 Announce Type: replace Abstract: Interleaved randomized benchmarking (IRB) provides a scalable estimate of a gate's error rate, but its standard guarantees require the interleaved gate to be Clifford~ite{Magesan2012Interleaved,magesan2012characterizing}. In superconducting processors, many non-Clifford phase gates in compiled circuits are implemented virtually as software-defined frame updates rather than as additional control pulses~ite{mckay2017efficient}. This raises the question of whether inserting or removing such virtual phases measurably changes IRB error estimates. We introduce phase-altered interleaved randomized benchmarking (PA-IRB), a paired-IRB diagnostic protocol comparing phase-stripped and phase-dressed Clifford interleaving gates derived from the same compiled implementation. PA-IRB reports Delta r=r_d-r_s with combined uncertainty to test whether virtual phase gates affect the extracted IRB decay beyond statistical error. As a case study, we apply PA-IRB to a compiled Toffoli gate executed on IBM superconducting processors, where the constituent T/T^agger gates are implemented as virtual Z rotations. Across tested calibration runs, Delta r is consistent with zero within uncertainty, indicating that virtual phase addition or removal does not measurably alter the IRB-derived error estimate under the employed compilation and execution stack. More generally, PA-IRB provides a lightweight, abstraction-aware diagnostic for benchmarking workflows involving software-defined phase operations. The same paired comparison can also be used to place operational bounds on the contribution of non-Clifford components to the compiled gate error, even when those components are physically executed rather than implemented virtually.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2606.30327) | 2026-10-05
