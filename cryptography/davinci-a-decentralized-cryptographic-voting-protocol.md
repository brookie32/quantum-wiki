---
title: "DAVINCI: A Decentralized Cryptographic Voting Protocol"
date: "2026-09-30"
updated: "2026-10-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2282"
summary: "We present DAVINCI, a decentralized end-to-end verifiable voting protocol with no trusted coordinator. The protocol is structured as a zero-knowledge (ZK) rollup: the election is a ZK-verified state m"
last_verified: "2026-10-03"
review_by: "2027-01-01"
stale: false
---

We present DAVINCI, a decentralized end-to-end verifiable voting protocol with no trusted coordinator. The protocol is structured as a zero-knowledge (ZK) rollup: the election is a ZK-verified state machine in which every transition, from ballot submission to final tallying, is encoded as a circuit constraint, so that no actor can force the protocol into an invalid state without breaking the underlying proof system. A decentralized set of sequencers handles ballot validation and aggregation off-chain, while Ethereum serves as a public bulletin board and a data-availability layer via EIP-4844 blobs. For ballot secrecy, DAVINCI uses threshold ElGamal with distributed key generation; for receipt-freeness, sequencers re-encrypt ciphertexts before storing them, and voters may revote at any time. To make revoting effective against bribery and coercion, DAVINCI introduces silent revoting on every state update, sequencers also re-randomize a random subset of stored ballots, and we quantify how well this hides overwrites among routine refreshes. Our open-source implementation shows that DAVINCI supports large-scale elections with succinct on-chain verification and ballot proofs generated on commodity devices, under the honest-device assumption shared by several deployed verifiable-voting systems.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2282) | 2026-09-30
