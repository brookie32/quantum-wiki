---
title: "Quantum LDPC codes protect quantum information using very few physical qubits per logical qubit. Computing with them is the expensive part: …"
date: "2026-09-24"
updated: "2026-09-24"
source: "agent"
category: "error-correction"
tags: [error-correction, xanadu--x]
url: "https://x.com/XanaduAI/status/2103159750049284251"
summary: "Quantum LDPC codes protect quantum information using very few physical qubits per logical qubit. Computing with them is the expensive part: every logical measurement needs a scaffold of extra qubits, "
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

Quantum LDPC codes protect quantum information using very few physical qubits per logical qubit. Computing with them is the expensive part: every logical measurement needs a scaffold of extra qubits, and until now that scaffold was nearly as large as the code block itself. In this new work from Xanadu, Alexander Cowtan and Benjamin Ide construct that scaffold with close to the minimum possible number of extra qubits, and generate it automatically instead of by hand, without giving up any error protection. When measuring many logical qubits at once, previous methods scaled as the block length squared; this scales as essentially the block length. The key is a bridge to complexity theory: building the scaffold turns out to be the same problem as writing a proof that a skeptic can verify by spot-checking a few random bits. https://arxiv.org/abs/2609.26973

**Source:** [Xanadu (X)](https://x.com/XanaduAI/status/2103159750049284251) | 2026-09-24
