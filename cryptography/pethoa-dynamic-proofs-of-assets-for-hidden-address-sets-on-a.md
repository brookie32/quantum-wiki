---
title: "Pethoa: Dynamic Proofs of Assets for Hidden Address Sets on Account-Based Blockchains"
date: "2026-11-22"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2982"
summary: "Proofs of solvency allow custodians to demonstrate that their assets cover their liabilities, but conventional Proofs of Assets (PoA) often require publicly disclosing reserve addresses, exposing fina"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Proofs of solvency allow custodians to demonstrate that their assets cover their liabilities, but conventional Proofs of Assets (PoA) often require publicly disclosing reserve addresses, exposing financial activities and enabling long-term transaction tracing. While zero-knowledge proofs can hide reserve addresses and prove asset ownership and balances against a public blockchain state, generating proofs for evolving blockchain states remains computationally expensive, particularly for chains with proof-unfriendly state structures. We introduce Dynamic Private Proof of Assets (DPoA), a framework for efficiently updating proofs of assets over hidden sets of on-chain addresses. Our construction separates asset-proof generation into an expensive initialization phase and lightweight incremental updates. During initialization, the prover establishes ownership and state membership for the reserve addresses. Subsequently, for each epoch, the prover locally updates its proof state based on newly finalized blocks and generates a zero-knowledge proof to demonstrate the correctness of the update, avoiding the need to regenerate the entire asset proof from scratch. Experimental results demonstrate the efficiency of our approach: generating a conventional static proof for thousands of addresses takes several minutes on an NVIDIA RTX 5090 GPU, whereas our dynamic update requires only a few seconds per block and runs entirely on a 14-core CPU.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2982) | 2026-11-22
