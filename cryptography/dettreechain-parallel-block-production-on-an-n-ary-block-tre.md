---
title: "DetTreeChain: Parallel Block Production on an N-ary Block Tree with Bounded Lane Divergence"
date: "2026-11-10"
updated: "2026-11-12"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2855"
summary: "Nakamoto-style blockchains append one block at a time to a single chain, and raising the block rate increases forking and weakens security. We present DetTreeChain, a ledger in which up to N blocks ar"
last_verified: "2026-11-12"
review_by: "2027-02-10"
stale: false
---

Nakamoto-style blockchains append one block at a time to a single chain, and raising the block rate increases forking and weakens security. We present DetTreeChain, a ledger in which up to N blocks are produced in parallel and placed without later merging or reordering. Blocks form an N-ary tree in which each block's slot follows from its parent and its lane. A locally derived Parent Queue Pool lets only two consecutive parents receive children, so lanes never drift more than one parent apart, and links between consecutive blocks of a lane make each lane a hash chain. As in several earlier designs, transactions are routed by what they spend, here a hash of the spent locking scripts, so blocks of different lanes cannot conflict and payments to other lanes need no cross-lane protocol. The rules are consensus-agnostic. Under proof of work, miners choose their lane, and an adversary with more than 1/(N+1) of the total hash power can outpace one lane. In a 25-minute run of our Rust prototype, six nodes converged on identical trees and difficulty targets, and 65% of slots were filled against 63% predicted. In simulation with delays of 5% of the lane interval, a single chain at the same block rate wasted 1.7 to 3.3 times as much work as 2 to 8 lanes, although nodes more often held later-discarded blocks. Among Bitcoin transactions whose spent scripts could be rebuilt, about 95% kept their inputs in one lane, mostly because they spend a single output.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2855) | 2026-11-10
