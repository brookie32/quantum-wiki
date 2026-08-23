---
title: "Pilaf: Fully Tight Two-Round Threshold Signatures with Adaptive Corruptions"
date: "2026-08-21"
updated: "2026-08-23"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1762"
summary: "Threshold signatures are deployed in settings where an adversary may run many concurrent signing sessions and corrupt signers adaptively. Two-round schemes make this especially delicate. Their first-r"
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

Threshold signatures are deployed in settings where an adversary may run many concurrent signing sessions and corrupt signers adaptively. Two-round schemes make this especially delicate. Their first-round messages are independent of the signed message and can be preprocessed offline, so a later corruption must reveal randomness that is consistent with commitments already published in prior transcripts. Existing adaptive constructions address this tension by adding rounds, relying on algebraic or knowledge assumptions, or paying non-tight losses from guessing the corruption pattern, the decisive session, or the final transcript. We construct mathsf{TPilaf}, the first two-round threshold signature scheme that combines partially non-interactive signing with a fully tight proof against adaptive corruptions. The scheme is pairing-free and is built in prime-order groups from the mathsf{MDDH} assumption in the random-oracle model. Its first-round messages can be generated offline, and any threshold set of signers can aggregate their second-round shares into a single publicly verifiable signature. The proof combines two ingredients. First, we introduce a linearly homomorphic dual-mode commitment with targetable opening. This lets the simulator open an already fixed commitment to the aggregate target imposed by a later Fiat-Shamir challenge. Second, we use profile-wise zero-sum masking with posterior completion. Corruption openings and signing responses are therefore sampled from the exact conditional law while values already visible to the adversary remain cached. Together, these tools enable a delayed branch-decision argument. The reduction waits until the adversary's own queries determine the last touched coordinate, completes only latent state, and then binds the forged hidden branch. The final bound has no combinatorial loss in the number of users, threshold, sessions, or corruption patterns, and contains only the explicit bad-event and assumption terms appearing in the theorem.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1762) | 2026-08-21
