---
title: "Trainable Quantum-Native Language Models: Dissipative Memory, Capacity Limits, and Hardware Validation"
date: "2026-10-12"
updated: "2026-10-12"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.12806"
summary: "arXiv:2610.12806v1 Announce Type: new Abstract: We study byte-level autoregressive language models whose hidden state is a small quantum register, whose transitions are learned token-conditioned quant"
last_verified: "2026-10-12"
review_by: "2027-01-10"
stale: false
---

arXiv:2610.12806v1 Announce Type: new Abstract: We study byte-level autoregressive language models whose hidden state is a small quantum register, whose transitions are learned token-conditioned quantum channels, and whose next-byte probabilities come directly from Born-rule measurements without a learned classical vocabulary projection or softmax. In the fixed-width recurrent setting, unitary dynamics cannot contract or reset stored distinctions; experimentally, unitary recurrence loses to its retrained one-token control in every tested variant. Introducing learned dissipation, then token-conditioned dissipative gating, yields useful memory beyond one token. The gated model improves test negative log-likelihood by 0.20 +/- 0.03 nats/byte over retrained parameter-matched one-token controls at context length 12, and by 0.29-0.33 at longer contexts, but never beats retrained two-token controls. A key-value recall benchmark shows a width-dependent threshold: one stored pair meets the pre-registered accuracy bar at 4-5 memory qubits, two pairs at 6-7, and three pairs remain unsolved. This is consistent with, but does not establish, a capacity explanation for the short effective memory horizon. As a secondary result, one-qubit models reach lower stationary memory entropy than a heuristically optimized classical predictive frontier at matched error in 9/9 seeds. On IBM Heron hardware, computational-basis memory-register distributions show signal against a uniform null in 12/12 circuits across prefixes of up to 12 tokens, next-bit probabilities pass pre-registered accuracy bars at four-token prefixes, and bytes are generated autoregressively by sampling physically measured bit probabilities. The tested models are classically simulable and substantially worse than classical n-gram baselines. We claim no computational quantum advantage.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.12806) | 2026-10-12
