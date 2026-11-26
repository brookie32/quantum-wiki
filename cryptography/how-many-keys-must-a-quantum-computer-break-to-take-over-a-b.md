---
title: "How Many Keys Must a Quantum Computer Break to Take Over a Blockchain? A Quantum Nakamoto Coefficient for Fifteen Proof-of-Stake Networks"
date: "2026-11-26"
updated: "2026-11-26"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.33413"
summary: "arXiv:2611.33413v1 Announce Type: new Abstract: Blockchains that run on proof of stake, among them Ethereum and Solana, are secured by a vote: a transaction becomes irreversible once computers holding"
last_verified: "2026-11-26"
review_by: "2027-02-24"
stale: false
---

arXiv:2611.33413v1 Announce Type: new Abstract: Blockchains that run on proof of stake, among them Ethereum and Solana, are secured by a vote: a transaction becomes irreversible once computers holding two thirds of the deposited money have signed it. Each signature is made with a secret key whose public counterpart is permanently visible, and a large quantum computer could compute the secret from the public key. We ask a simple question: how many such keys would it have to break to take over the vote? We call the answer the quantum Nakamoto coefficient and measure it on live data from fifteen networks, collected on 15 November 2026. For fourteen of them, 2 to 18 keys are enough to break the network's security guarantee and 7 to 77 to control it outright; at one key every 12 minutes, the pace implied by recent resource estimates, a single quantum computer would defeat the guarantee of any of these networks in less than four hours and take full control in less than sixteen hours. Ethereum is far more robust, but a 2025 change that lets operators merge their deposits into fewer keys has cut the number of keys at its first threshold from about 465,000 to 7,682, a factor of 60. We derive a simple formula for this effect, and another for the small rotating committee on which wallets rely, and confirm both on the data. For fourteen of the fifteen networks, the first large quantum computer would be less than a day away from total control. Their validator signatures should therefore be migrated to post-quantum schemes before such a machine exists, since once it does, the time to respond is measured in hours.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.33413) | 2026-11-26
