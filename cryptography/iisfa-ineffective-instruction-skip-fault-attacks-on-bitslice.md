---
title: "IISFA: Ineffective Instruction-Skip Fault Attacks on Bitslice Implementations"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2536"
summary: "Redundancy countermeasures prevent differential fault analysis by withholding faulty ciphertexts. Ineffective fault analysis and statistical ineffective fault attacks exploit executions in which an in"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Redundancy countermeasures prevent differential fault analysis by withholding faulty ciphertexts. Ineffective fault analysis and statistical ineffective fault attacks exploit executions in which an injected fault leaves the result unchanged, using constraints on intermediate values or statistical bias to recover keys. In this paper, we present an Ineffective Instruction-Skip Fault Attack (IISFA) on bitsliced implementations protected by redundancy. A bitsliced instruction processes m S-boxes simultaneously. Skipping it leaves the group unchanged exactly when all m S-box inputs belong to its ineffective set, which we compute from the implementation. Each ciphertext output by the device therefore restricts all m n-bit subkeys to candidates whose S-box inputs belong to that set. The ineffective probability specifies how often a uniformly random S-box input makes the skip ineffective, and its m-th power gives the ciphertext output probability for independent inputs. We determine which key candidates remain indistinguishable under a single target instruction. We give key-recovery procedures for both known and chosen plaintexts and combine different target instructions across queries, with one instruction skipped per execution. We calculate expected injection counts or enclosing intervals for the known- and chosen-plaintext procedures from the ineffective sets and use them to reduce the search for efficient target sequences. We evaluate five bitsliced implementations of GIFT, SKINNY and PIPO on an 8-bit AVR microcontroller under a redundancy countermeasure using clock glitches. All measured key-recovery campaigns succeed in every trial.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2536) | 2026-10-19
