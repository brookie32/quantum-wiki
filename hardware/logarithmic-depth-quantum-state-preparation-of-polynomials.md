---
title: "Logarithmic-depth quantum state preparation of polynomials"
date: "2026-10-19"
updated: "2026-10-19"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.16527"
summary: "arXiv:2603.16527v4 Announce Type: replace Abstract: Quantum state preparation is a central primitive in many quantum algorithms, yet it is generally resource intensive, with efficient constructions kn"
last_verified: "2026-10-19"
review_by: "2027-01-17"
stale: false
---

arXiv:2603.16527v4 Announce Type: replace Abstract: Quantum state preparation is a central primitive in many quantum algorithms, yet it is generally resource intensive, with efficient constructions known only for structured families of states. This work introduces a method for preparing quantum states whose amplitudes are given by a degree-d polynomial, using circuits with logarithmic depth in the number n of qubits and only mathcal O(n) ancilla qubits, improving previous approaches that required linear-depth circuits. The construction first relies on a block-encoding of an affine diagonal operator based on its Pauli-basis decomposition, which involves only n terms. A modified linear-combination-of-unitaries (LCU) technique is introduced to implement this decomposition in logarithmic depth, together with a novel circuit for the EXACT-one oracle that flags basis states in which exactly one qubit is in the state |1rangle. It then uses a generalized quantum eigenvalue transformation (GQET) to promote this affine operator to an arbitrary degree polynomial. Theoretical analysis and numerical simulations are reported along with a proof-of-principle implementation on a trapped-ion quantum processor using 14 qubits and more than 500 primitive quantum gates. Because polynomial approximations are ubiquitous in scientific computing, this construction provides a scalable and resource-efficient approach to quantum state preparation, further improving the potential of quantum algorithms in fields such as chemistry, physics, engineering, and finance.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.16527) | 2026-10-19
