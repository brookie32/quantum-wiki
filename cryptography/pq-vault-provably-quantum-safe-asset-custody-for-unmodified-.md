---
title: "PQ-Vault: Provably Quantum-Safe Asset Custody for Unmodified Ethereum"
date: "2026-10-22"
updated: "2026-10-22"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.29230"
summary: "arXiv:2610.29230v1 Announce Type: new Abstract: A quantum computer could recover the key of any Ethereum account whose public key appears on chain. We prove that no sidechain or bridge that leaves Eth"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

arXiv:2610.29230v1 Announce Type: new Abstract: A quantum computer could recover the key of any Ethereum account whose public key appears on chain. We prove that no sidechain or bridge that leaves Ethereum's rules unchanged can protect such accounts: their funds must move into a contract whose release condition relies only on quantum-safe primitives. We design PQ-Vault, a custody system for unmodified Ethereum combining this vault, a quantum-safe proof-of-stake sidechain whose checkpoints carry compact certificates, and an optimistic dispute protocol. We give the first security proof of compact certificates against quantum attackers and a matching attack: with classically chosen parameters, the guarantee falls from 128 to about 60 bits, and a simple rule restores it. We show that a common seed-update rule in hash-chain proof of stake lets an attacker steer chosen slots and profit from splitting its stake, and give an election whose steering gain and inclusion delay are provably bounded against quantum attackers. Since compressing certificates with a pairing-based SNARK breaks quantum security, we use fraud proofs that need a single signature check. For 65,536 validators, a certificate is 0.8 MB, 260 times smaller than all signatures, and verifies in about 20 ms; the vault accepts a checkpoint for about 420,000 gas.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.29230) | 2026-10-22
