---
title: "Unveiling the Cost: Gas-Efficient Output-Private Distributed VRFs on Ethereum"
date: "2026-10-14"
updated: "2026-10-15"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2484"
summary: "Unbiased and publicly verifiable randomness is a fundamen- tal component of Web3 security, and output-private distributed verifiable random functions (DVRFs) extend this guarantee by keeping the gener"
last_verified: "2026-10-15"
review_by: "2027-01-13"
stale: false
---

Unbiased and publicly verifiable randomness is a fundamen- tal component of Web3 security, and output-private distributed verifiable random functions (DVRFs) extend this guarantee by keeping the gener- ated randomness hidden from chain observers until the requester chooses to reveal it. Two constructions currently realize output privacy under dif- ferent algebraic regimes: FlexiRand, whose on-chain verification rests on bilinear pairings, and IcyVeil, a pairing-free design whose verification re- duces to a constant number of group operations. While it is folklore that pairing-free verification should be cheaper on the Ethereum Virtual Ma- chine (EVM), the actual on-chain cost of output-private randomness has never been measured for either scheme. In this paper, we present the first EVM implementations of both constructions. Both verifiers are served by a single coordinator contract realizing the common blind–evaluate–pre- verify lifecycle, so that every measured difference is attributable solely to the verification arithmetic. The isolated verification is 57% cheaper in execution gas for the pairing-free scheme (51,561 against 118,541 gas); over the full request lifecycle, whose remaining stages are shared, the ad- vantage is about 11%. This on-chain saving comes with a cost off chain: the pairing-free scheme’s distributed evaluation requires roughly 2.5 to 8.2 times more aggregate committee compute across committee configu- rations (n, t), a gap absorbed comfortably by Ethereum’s block time and one that narrows further once the committee executes concurrently. We report both axes, separating one-time distributed key generation (DKG) cost from IcyVeil’s consumable preprocessing, and reconcile the on-chain and off-chain ratios, which point in opposite directions. All contracts, harnesses, and raw measurements are publicly available.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2484) | 2026-10-14
