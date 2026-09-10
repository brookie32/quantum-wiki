---
title: "Computing 256-bit elliptic curve discrete logarithms in 26 days on a fault-tolerant trapped-ion quantum computer with 20,000 qubits"
date: "2026-09-08"
updated: "2026-09-10"
source: "agent"
category: "error-correction"
tags: [error-correction, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1916"
summary: "One of the strengths of our recently proposed Walking Cat Architecture for a trapped-ion quantum computer is that it is straightforward to extend and optimize for a specific application. As a proof-of"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

One of the strengths of our recently proposed Walking Cat Architecture for a trapped-ion quantum computer is that it is straightforward to extend and optimize for a specific application. As a proof-of-concept, here we present such optimizations for solving the 256-bit elliptic curve discrete logarithm problem (ECDLP) on mathtt{secp256k1}, which is the elliptic curve used by blockchain technologies such as Bitcoin, using Shor's algorithm. We optimize the circuits from Schrottenloher's recent work and arrive at a logical quantum circuit for solving the ECDLP using about 1450 qubits and 40dot 10^6 Toffoli gates, with a rigorous lower bound on the logical-level success probability that holds with confidence at least 1-2^{-128}, as well as a heuristic estimate thereof. Using our compilation toolchain in combination with manual optimization of the logical layout and integrated routing, we produce estimates for the logical measurement depth and the required number of physical qubits by compiling all components to measurement schedules that obey the architectural constraints. A key ingredient is a fast CCZ magic-state factory and a depth-one CCZ state injection, reducing the execution time of CCZ gates by a factor of 31. We increase the logical-measurement parallelism using non-overlapping cat-based measurements in parallel, and we leverage the recently proposed logical CliNR protocol to speed up Clifford operations. To reduce the qubit overhead, we introduce a more efficient loss correction protocol, design a layout that allows us to recycle the CliNR ancilla qubits, and provision reusable cat-state resources according to the circuit's peak measurement parallelism. All results and optimizations combined, we conclude that a trapped-ion quantum computer based on our architecture would be able to solve the ECDLP on mathtt{secp256k1} in approximately 25.7 days using 19{,}397 physical qubits with an estimated success probability of 63%.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1916) | 2026-09-08
