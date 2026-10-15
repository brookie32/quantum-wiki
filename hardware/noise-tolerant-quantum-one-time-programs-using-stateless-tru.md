---
title: "Noise-Tolerant Quantum One-Time Programs Using Stateless Trusted Hardware, Revisited"
date: "2026-10-15"
updated: "2026-10-15"
source: "agent"
category: "hardware"
tags: [hardware, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2498"
summary: "A quantum one-time program scheme is a functionality-preserving compiler that transforms a program into a quantum state that can be used to obtain only one output of the program. Our goal is to design"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

A quantum one-time program scheme is a functionality-preserving compiler that transforms a program into a quantum state that can be used to obtain only one output of the program. Our goal is to design quantum one-time programs that can be realized on existing quantum technologies. Our contributions are two-fold: 1. We design a BB84 state-based quantum one-time program scheme in the stateless trusted hardware model that is resilient to single-qubit corruption errors and detectable erasure errors. To illustrate, under independent noise with a 90% detectable erasure rate and a 3% Pauli Y-error rate on surviving qubits, a signature token of 39,801 BB84 qubits achieves forging probability at most small 2^{-128} against at most small 2^{32} classical verification queries, with honest failure probability below small 10^{-6}. Prior to our work, [Behera, Sattath, and Shinar TQC'22] studied a BB84 state-based quantum one-time program scheme resilient to independent single-qubit corruption errors; our construction treats detectable erasures separately. 2. We give two extensions to our scheme. First, we study the setting wherein the same trusted hardware can be reused across different independently generated quantum one-time programs. Second, we study the setting wherein multiple trusted hardware devices are used and the security holds as long as at least one of them is not compromised.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2498) | 2026-10-15
