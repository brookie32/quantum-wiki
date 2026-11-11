---
title: "On Composing Oracle Separations"
date: "2026-11-09"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2845"
summary: "Black-box separations constitute very powerful technical barriers against constructing primitives from specific building blocks. However, they give surprisingly little indication on the usefulness of "
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

Black-box separations constitute very powerful technical barriers against constructing primitives from specific building blocks. However, they give surprisingly little indication on the usefulness of combining several such building blocks in a single construction. We propose a set of technical conditions, under which (fully) black-box separations compose with each other. That is, if two black-box separations P_1 stackrel{BB}{nRightarrow} Q and P_2 stackrel{BB}{nRightarrow} Q satisfy our conditions, then Q is also separated from black-box combinations of P_1 and P_2. When applicable, these conditions can be established without unpacking the full technical details of the base separations. As our main application, we show that combining indistinguishability obfuscation (iO) with collision resistant hash functions is unlikely to yield hard problems in the complexity class SZK, and thus unlikely to suffice for primitives such as lossy functions or fully homomorphic encryption. Previous lower bounds on iO only applied to combinations of iO with one-way permutations (Asharov-Segev, FOCS '15 and Bitansky-Degwekar-Vaikuntanathan, SIAM Journal on Computing '21).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2845) | 2026-11-09
