---
title: "Nearly Optimal Hardness for CVP and NCP with Preprocessing"
date: "2026-10-25"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2634"
summary: "The closest vector problem(CVP)and the nearest codeword problem (NCP) are fundamental computational problems with connections to learning, coding theory, and cryptography. We study hardness of approxi"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

The closest vector problem(CVP)and the nearest codeword problem (NCP) are fundamental computational problems with connections to learning, coding theory, and cryptography. We study hardness of approximation in the preprocessing model: an algorithm receives the lattice or code in advance, may perform unrestricted computation to produce polynomial-size advice, and must then solve the problem on any target in polynomial time. Unless mathsf{NP} subseteq mathsf{P/poly}, no such algorithm achieves an approximation factor of ullet M^{1−arepsilon} for NCP over any fixed finite field, or ullet M^{1/min{p,2}−arepsilon} for CVP in any ell_p norm, for every fixed arepsilon > 0, where M denotes the code block length or lattice dimension, respectively. We improve the subpolynomial factors of Khot, Popat, and Vishnoi [KPV14]to polynomial ones, matching the exponents that Song [Son26] proved without preprocessing for binary codes and the ell_2 norm. We further extend Song’s evaluation tables to every fixed prime characteristic and the lattice reduction to ell_p with p > 2. Our main technical contribution is an extension of the moment method, introduced in an OpenAI report [Ope26] and improved by Song [Son26], to the preprocessing setting. In addition, we give a direct reduction from probabilistically checkable proofs (PCPs) whose query locations and families of possible predicates do not depend on the formula. The resulting factor of M^{Omega(1/(log log M)^2)} is already larger than that of [KPV14], and the reduction may be of independent interest.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2634) | 2026-10-25
