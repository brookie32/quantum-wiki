---
title: "A Crypto-Agile Mixed-Radix NTT Accelerator for Negacyclic and Trinomial Rings"
date: "2026-10-23"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2610"
summary: "Hardware accelerators for lattice-based post-quantum cryptography (PQC) have largely converged on the radix-2 number-theoretic transform (NTT). The spectrum of standards that crypto-agility must accom"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

Hardware accelerators for lattice-based post-quantum cryptography (PQC) have largely converged on the radix-2 number-theoretic transform (NTT). The spectrum of standards that crypto-agility must accommodate, however, extends beyond NIST. In response to advances in cryptanalysis and to reduce the attack surface, national authorities are standardizing or recommending lattice-based algorithms with alternative algebraic structures, as well as schemes built on entirely different primitives. For instance, NTRU+, selected in the Korean PQC competition and currently undergoing standardization, is defined over a trinomial ring whose degree is divisible by three and thus requires a mixed-radix NTT comprising both radix-2 and radix-3 layers, whereas SMAUG-T employs an NTT-unfriendly modulus. Support for heterogeneous algebraic structures is therefore no longer optional but a prerequisite for crypto-agile design; existing radix-2-centric accelerators, however, fail to meet this requirement. In this paper, we present a crypto-agile mixed-radix NTT accelerator that performs transforms over both negacyclic and trinomial rings on a single datapath. Our contributions are threefold. First, we design a unified butterfly unit that integrates two parallel radix-2 butterflies, one radix-3 butterfly, and the trinomial transform on shared arithmetic resources, in which a generic 17-bit Montgomery path and an ML-DSA-specific 23-bit reduction path share the same two DSPs. Second, we propose a conflict-free memory mapping that guarantees in-place parallel access across all mixed-radix layers with a single 1-bit bank-selection function, namely address parity for radix-2 and a fixed address bit for radix-3, and requires neither mapping tables, nor coefficient reordering, nor additional BRAMs. Third, we introduce a generalized modular constant division that combines the multiple alignment of Montgomery reduction with the quotient estimation of Barrett reduction to perform the 3^{-1} scaling of the radix-3 inverse NTT without any DSP. Implemented on an Artix-7 FPGA, the proposed core supports all security levels of ML-KEM, ML-DSA, HAETAE, SMAUG-T, and NTRU+ using 5,279 LUTs, 4 DSPs, and 9 BRAMs at 141.5~MHz. For NTRU+, it achieves a 4.1--13.0imes improvement in area-time product (ATP) over approaches that resort to radix-2-only cores via degree lifting, and new moduli of up to 17 bits can be integrated at the cost of fewer than 20 LUTs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2610) | 2026-10-23
