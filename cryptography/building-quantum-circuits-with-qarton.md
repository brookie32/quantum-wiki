---
title: "Building Quantum Circuits with Qarton"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2191"
summary: "In order to estimate accurately the impact of large-scale computing devices, one requires a precise resource estimate of quantum algorithms for cryptographic problems. As a start, these algorithms can"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

In order to estimate accurately the impact of large-scale computing devices, one requires a precise resource estimate of quantum algorithms for cryptographic problems. As a start, these algorithms can be described as quantum circuits. One then estimates the number of gates, qubits, and circuit depth that they require, as a first step towards physical resource estimates. In order to simplify this task, different quantum programming languages have been used, targeting different circuit sizes and abstraction levels. Quantum cryptanalysis is indeed a domain in which one may consider both medium-scale circuits with fine-grained optimizations (such as optimizations of Shor's algorithm) and very large-scale circuits with well-defined building blocks (such as exhaustive key search on block ciphers using Grover's algorithm). This paper presents Qarton, a python library to represent logical quantum circuits, focused on quantum cryptanalysis. It allows to study very large-scale circuits like Grover searches, to simulate classical or ``almost'' classical circuits such as the arithmetic building blocks of Shor's algorithm, and to analyze trade-offs between qubit and gate count when switching between different implementations of arithmetic operations. Qarton is equipped with a library of around 300 circuits and examples from different areas of quantum symmetric and asymmetric cryptanalysis.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2191) | 2026-09-23
