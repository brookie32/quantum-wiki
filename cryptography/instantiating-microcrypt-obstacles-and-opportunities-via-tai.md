---
title: "Instantiating Microcrypt: Obstacles and opportunities via tailored state certification"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2185"
summary: "Recent work has introduced the Hamiltonian phase state (HPS) assumptions, which postulate that Hamiltonian phase states can be used to instantiate pseudorandom and one-way state generators. Additional"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

Recent work has introduced the Hamiltonian phase state (HPS) assumptions, which postulate that Hamiltonian phase states can be used to instantiate pseudorandom and one-way state generators. Additionally, it has been conjectured that these assumptions can be true, even if one-way functions do not exist. This is exciting, because if true, then the HPS assumptions provide a route to the instantiation of Microcrypt. In this work we falsify this conjecture, by proving that if the HPS assumptions are true, then one-way functions exist. While this removes the possibility of instantiating genuine Microcrypt cryptography with Hamiltonian phase states, it shows that the HPS assumptions provide novel inherently quantum assumptions for the construction of classical cryptography. Technically we achieve this via a method for the construction of one-way puzzles from one-way state generators and tailored "measure first, ask later" state certification protocols. This generalizes prior constructions of one-way puzzles from one-way state generators via classical shadows and allows us to relate properties of the one-way puzzle to properties of the state certification protocol used in the construction. Specifically, if the state certification protocol admits efficient classical post-processing then one obtains an efficiently verifiable one-way puzzle, and if the state certification protocol can be efficiently classically simulated in a certain sense, then one obtains a classical one-way puzzle, which implies one-way functions. The latter observation allows us to prove that the HPS assumptions imply one-way functions, by exploiting properties of state certification protocols for phase states. The former observation provides a new toolbox for the construction of efficiently verifiable one-way puzzles by exploiting tailored state certification protocols for pseudorandom and one-way state generators.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2185) | 2026-09-23
