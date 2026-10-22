---
title: "Optimal Proofs of Sequential Work"
date: "2026-10-20"
updated: "2026-10-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2569"
summary: "In a proof of sequential work (PoSW), introduced by Mahmoody, Moran and Vadhan [MMV'13], a verifier can be convinced that a prover performed a computation of T sequential steps. Such a proof is (elta,"
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

In a proof of sequential work (PoSW), introduced by Mahmoody, Moran and Vadhan [MMV'13], a verifier can be convinced that a prover performed a computation of T sequential steps. Such a proof is (elta, lambda)-sound if a malicious prover making at most (1-elta)T sequential steps can produce a valid proof only with probability 2^{-lambda}, even when using massive parallelism. Besides time-lock puzzles (TLPs) and verifiable delay functions (VDFs), PoSW are one of the central primitives in timed cryptography. Unlike TLPs or VDFs, PoSW can be constructed just from hash functions, with a security proof in the random oracle model. Existing PoSW are based on graph labeling: the prover must sequentially compute a labeling of a graph of T nodes, where each node's label is the hash of its parents' labels. The [MMV'13] construction uses node-depth-robust graphs. A simple and much more efficient construction was later given by Cohen and Pietrzak [CP'18]. In the [CP'18] PoSW, getting (elta, lambda) soundness requires transmitting Omega((lambdalog T)/elta) hash outputs. The underlying graph has average in-degree Theta(log T), so labeling takes Theta(Tlog T) total hash inputs. Our first result is a lower bound: any efficient graph-labeling-based PoSW that is (elta, lambda)-sound requires the prover to send Omega((lambdalog T)/elta) labels. To prove this result, we relate PoSW soundness to a cut-depth game and bound this game using a refinement of Valiant's depth-reduction argument. This shows that [CP'18] achieves asymptotically optimal communication and verifier hash-input complexity, while leaving open whether its Theta(log T) average indegree (and thus Theta(Tlog T) prover hash-input complexity) is necessary. Our second result is a new PoSW that matches these lower bounds up to constant factors and has maximum indegree two. In particular, it reduces the honest prover's total hash-input complexity from Theta(Tlog T) to Theta(T) while retaining O((lambdalog T)/elta) communication and verifier hash-input complexity.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2569) | 2026-10-20
