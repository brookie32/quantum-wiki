---
title: "Probabilistic Polynomial Time is a healer: Consensus with Mobile-Omission Faults"
date: "2026-11-22"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2990"
summary: "We study synchronous Byzantine agreement (BA) with t adaptive Byzantine corruptions and mobile, arbitrarily overlapping send and receive omission sets of per-round sizes s and r. The adversary can sel"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

We study synchronous Byzantine agreement (BA) with t adaptive Byzantine corruptions and mobile, arbitrarily overlapping send and receive omission sets of per-round sizes s and r. The adversary can selectively drop outgoing (respectively, incoming) messages for send omissions (respectively, receive omissions). Mobile means the adversary can choose a set of fresh send/receive omissions for each round. A well-known lower bound of Santoro and Widmayer (STACS 1989) establishes that time, by itself, is not a healer: any c-round agreement protocol with even a single mobile fault must incur an error of 1/[2(2n)^c]. Yet, while this rules out deterministic protocols, to date, no randomized protocol (even with higher probability of error) is known. This is all the more true when considering a model in which mobile omission faults are mixed with t (permanent) Byzantine faults. Assuming 2t+s+r<n, we provide the first protocols for and clean formal models for the mixed model with mobile omission faults. This matches the resilience of existing works in this area which consider non-mobile omission faults. We then build a player-replaceable BA protocol with subquadratic communication complexity, under the stronger assumption that 2t+s+rleq (1-arepsilon)n.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2990) | 2026-11-22
