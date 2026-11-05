---
title: "Fine-Grained Proof Complexity for Elementary Arithmetic in Extended Frege"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2758"
summary: "Proof complexity has historically focused on qualitative results, such as whether natural mathematical statements (e.g. the Pigeonhole Principle) admit polynomial-size proofs in certain proof systems "
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Proof complexity has historically focused on qualitative results, such as whether natural mathematical statements (e.g. the Pigeonhole Principle) admit polynomial-size proofs in certain proof systems (e.g. Resolution or Frege). In contrast to the rich theory of algorithm design, there is little understanding of how to design quantitatively efficient proofs. We initiate the study of fine-grained propositional proof complexity. Our motivation comes from an emerging line of cryptographic constructions such as the elegant work of Jain and Jin (2022), in which the efficiency of the resulting scheme is governed by the size of the underlying Extended Frege proofs. Our main result is that the basic laws of integer arithmetic —commutativity and associativity of addition and of multiplication, together with distributivity — admit Extended Frege proofs of quasi-linear size, when addition is implemented by the schoolbook algorithm and multiplication by an FFT-based algorithm. This seemingly elementary result turns out to be surprisingly non-trivial: the natural paper-and- pencil arguments for distributivity and for associativity of multiplication translate into Extended Frege proofs of quadratic size. To reach quasi-linear size, we develop a technique we call index generalization, which we believe will find wide application in the design of efficient propositional proofs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2758) | 2026-11-04
