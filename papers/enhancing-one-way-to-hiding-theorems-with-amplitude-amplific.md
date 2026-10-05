---
title: "Enhancing One-Way to Hiding Theorems with Amplitude Amplification"
date: "2026-10-04"
updated: "2026-10-05"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2331"
summary: "The one-way to hiding (O2H) theorem and its variants, which bound the distinguishing advantage in terms of the one-way advantage, are widely used in security proofs in the quantum random oracle model "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

The one-way to hiding (O2H) theorem and its variants, which bound the distinguishing advantage in terms of the one-way advantage, are widely used in security proofs in the quantum random oracle model (QROM), particularly for key encapsulation mechanisms (KEMs). However, existing O2H bounds typically incur a security loss depending on the adversary's oracle query depth d (i.e. the number of sequential layers of parallel queries), which can make both computational and information-theoretic bounds in KEM security proofs less tight. In this work, we establish a generic amplitude-amplification-based technique to many O2H variants to remove their depth-dependent factors by these theorems in the advantage bounds.This covers the Semi-Classical O2H (SC-O2H) [Ambainis et al., CRYPTO 2019] and Measure-Rewind-Extract O2H (MRE-O2H) [Ge et al., ASIACRYPT 2024] theorems, in which the constructed one-way adversaries have access to an indicator oracle mathbf{1}_S that checks whether the input is a valid solution to the one-way game. We identify conditions under which our enhanced O2H theorems can replace the original O2H theorems in existing security proofs. These conditions hold for a range of security proofs, including IND-CCA security proofs for KEMs obtained from variants of the U transformation in the Fujisaki-Okamoto (FO) framework. Applying our enhanced theorems in these proofs yields the following improvements in the depth dependence of security bounds: - When the one-way advantage is bounded information-theoretically, our technique eliminates the depth-dependent factors with only a constant-factor loss in the security bound. - When the one-way advantage is bounded by computational hardness assumptions, our technique eliminates the depth-dependent factors d for SC-O2H and sqrt{d} for MRE-O2H, at the cost of increasing the constructed one-way adversary's running time by a factor that is only of the order of the square roots of the eliminated losses, namely O(sqrt{d}) for SC-O2H and O(sqrt[4]{d}) for MRE-O2H.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2331) | 2026-10-04
