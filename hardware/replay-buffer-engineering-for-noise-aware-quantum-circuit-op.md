---
title: "Replay-buffer engineering for noise-aware quantum circuit optimization"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.21863"
summary: "arXiv:2604.21863v2 Announce Type: replace Abstract: Deep reinforcement learning for quantum circuit optimization faces three bottlenecks: replay buffers that overlook temporal difference (TD) target r"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

arXiv:2604.21863v2 Announce Type: replace Abstract: Deep reinforcement learning for quantum circuit optimization faces three bottlenecks: replay buffers that overlook temporal difference (TD) target reliability, curriculum-based architecture search requiring a full quantum-classical evaluation after every edit, and the discard of noiseless trajectories when retraining under hardware noise. We address these limitations by treating replay as a central algorithmic lever. We introduce ReaPER+, an annealed replay rule that transitions from TD-error prioritization to reliability-aware sampling as value estimates mature. ReaPER+ achieves up to 4x higher sample efficiency than fixed PER, ReaPER, and uniform replay, while matching prior on-policy solution quality with up to 32x fewer interactions At 12 qubits, fixed ReaPER reaches the lowest energy error in the fewest steps, while PER and uniform replay find more compact circuits at higher error. On tasks scaling to 20 qubits, ReaPER+ retains its advantage, demonstrating that reliability-aware annealing extends beyond small-system benchmarks. LunarLander-v3 confirms that the ReaPER+ is domain-agnostic, it improves success rates by up to 26.8% over PER and 21.8% over fixed ReaPER, with a 3% AUC gain over both. We further introduce OptCRLQAS, which amortizes quantum-classical evaluations across multiple architectural edits, reducing training wall-clock time by up to 67.5% on 12-qubit without degrading solution quality. Finally, lightweight replay-buffer transfer warm-starts noisy optimization from noiseless trajectories, without weight transfer or epsilon-greedy pretraining, reducing steps to chemical accuracy by 85-90% and final energy error by up to 90% relative to from-scratch learning. Transfer gains increase with system size. Together, these results establish experience storage, sampling, and transfer as decisive levers for sample efficient, noise-aware quantum circuit optimization.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.21863) | 2026-09-30
