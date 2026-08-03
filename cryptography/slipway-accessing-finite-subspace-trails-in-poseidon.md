---
title: "Slipway: Accessing Finite Subspace Trails in Poseidon"
date: "2026-08-02"
updated: "2026-08-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1579"
summary: "Poseidon is an algebraic permutation designed for efficient use in proof systems. Its nonlinear layer consists of power-map S-boxes. In a full round, the S-box is applied to every state coordinate; in"
last_verified: "2026-08-03"
review_by: "2026-11-01"
stale: false
---

Poseidon is an algebraic permutation designed for efficient use in proof systems. Its nonlinear layer consists of power-map S-boxes. In a full round, the S-box is applied to every state coordinate; in a partial round, it is applied to only one coordinate, reducing the arithmetization cost. Each round also applies an MDS linear layer to diffuse information across the state. To study algebraic degree, we let the input depend on variables and follow the resulting family of states through the permutation. If the coordinate entering a partial-round S-box is constant across that family, the S-box adds no degree in the family variables. Directions with this property over several consecutive partial rounds form finite subspace trails. Such trails exist for every linear layer, but their existence does not by itself explain how a constrained family can pass through the preceding full rounds and enter them without first acquiring high degree. We address this reachability problem by constructing a constrained input family and a round-constant-dependent MDS matrix together. The prescribed matrix images carry the family through the four initial full rounds and into a chosen finite trail. After an explicit change of variable, the state at the end of the full-round prefix is linear in the new root variable, so the prefix acts as a controlled reparametrization rather than as a source of degree growth. We call this effect full-round absorption. For the KoalaBear instance ((t,alpha,R_F,R_P)=(16,3,8,20)), we construct a two-parameter family whose first two input coordinates are zero. On this family, the four initial full rounds act as a reparametrization and deliver the variable directions into a two-dimensional trail, so those four rounds and the next fourteen partial S-boxes add no degree. For the exhibited control, the polynomials representing the first two output coordinates have exact degree (3^{R_F+R_P-4-14}=3^{10}), rather than the expected degree (3^{R_F+R_P}=3^{28}). We exhibit a common base-field root, yielding a complete CICO-2 solution for the full-round Poseidon instance. The resulting matrices are MDS and satisfy the relevant matrix checks prescribed by the Poseidon designers, yet they make a finite trail reachable through the full-round prefix. We generalize the construction to CICO-(k), derive the corresponding trail-dimension and matrix-image bounds, and provide a concrete MDS matrix that meets the CICO-3 matrix-image bound with equality.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1579) | 2026-08-02
