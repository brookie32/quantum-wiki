---
title: "Where Quantum Fourier Sampling Stops Short: A Three-Gate Audit Protocol for Delay-PUF Security Models"
date: "2026-10-05"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.02636"
summary: "arXiv:2610.02636v1 Announce Type: new Abstract: Quantum Fourier sampling may help audit the spectral learnability of delay-based physical unclonable functions (PUFs). We ask whether that promise survi"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

arXiv:2610.02636v1 Announce Type: new Abstract: Quantum Fourier sampling may help audit the spectral learnability of delay-based physical unclonable functions (PUFs). We ask whether that promise survives access matching, a strong classical comparator, and oracle synthesis. Three gates structure the evaluation. Structure: low degree is not small support at reachable challenge lengths; for 4-XOR at n=14, degree le d_f(0.1) admits 91% of all 2^n characters and the median 90%-mass set spans a third of the spectrum. Algorithmics: constructing the phase oracle logically implies classical membership access, making Kushilevitz--Mansour the correct baseline; across 45 tasks it exhausts each finite domain, and no 4-XOR ideal-sampling case reaches 90% mass within 2^n calls. A quantum-kernel diagnostic appears more favorable, with geometric difference rising to 2.151 at N=512 challenges, but it correlates 0.991 with 1/sqrt{lambda_{min}(K_C)} for the classical Gram matrix K_C, and the 4-XOR label-complexity ratio does not exceed a balance-preserving permutation null (p=0.930). Trace-normalized geometric difference can therefore grow through classical ill-conditioning alone, without task-label alignment. Implementation: a simulator-validated fixed-point phase oracle based on the quantum Fourier transform admits an 18.9% routed-depth reduction, yet the least certified precisions have estimated durations of 1.18--1.55imes the median dephasing time T_2 of the mapped qubits on a static backend snapshot, without hardware execution. We find no end-to-end advantage in the evaluated regime, although ideal sampling does use fewer coherent calls on the thresholded task. The contribution is the Three-Gate Quantum Audit Protocol: a reproducible procedure separating an ideal query advantage from a realizable security benefit. This is not a claim about deployed silicon and not an impossibility result.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.02636) | 2026-10-05
