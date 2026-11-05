---
title: "From Claws to Conferences: Device-Independent Key Agreement Beyond Non-Signaling"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.05509"
summary: "arXiv:2611.05509v1 Announce Type: new Abstract: Device-independent conference key agreement (DI-CKA) allows a group of users to establish a common secret key without trusting the internal operation of"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.05509v1 Announce Type: new Abstract: Device-independent conference key agreement (DI-CKA) allows a group of users to establish a common secret key without trusting the internal operation of their quantum devices. Existing DI-CKA protocols derive their security from multipartite Bell tests and therefore require the device components not to communicate during each round. We present, to the best of our knowledge, the first DI-CKA protocol that removes this non-signaling assumption: all interfaces and their mutual communication are treated as one untrusted device, which only has to be quantum polynomial-time while the protocol runs. Assuming that the Learning With Errors (LWE) problem is hard for quantum algorithms with quantum advice during the execution, we prove finite-size security against coherent attacks, in which the device may keep quantum memory and correlate and adapt its behavior across rounds. For two parties the protocol is a computational DI-QKD protocol with an explicit finite-size proof against coherent attacks. Technically, we lift the claw state underlying the classical-verifier test of Brakerski et al. (FOCS 2018) to multipartite entanglement, obtaining a GHZ-correlated claw state. %that is prepared with one coherent claw-free function evaluation and N-1 CNOT gates. We then introduce the collective adaptive hardcore bit, a multiparty generalization of the adaptive hardcore bit of Brakerski et al. and show that it follows from the original property by a tight reduction. Combined with Jordan's lemma, an entropic uncertainty relation, and entropy accumulation, this certifies smooth min-entropy of the key against an external quantum adversary. Our protocol achieves everlasting security: LWE needs to hold only during the execution, because the final key is statistically secure and its secrecy persists even if LWE is broken after the protocol ends.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.05509) | 2026-11-05
