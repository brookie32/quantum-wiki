---
title: "Composing Detector Error Models"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.13087"
summary: "arXiv:2609.13087v1 Announce Type: new Abstract: Fault-tolerant quantum programs thread together reusable logical operations, yet correcting errors requires comparing measurements across operation boun"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2609.13087v1 Announce Type: new Abstract: Fault-tolerant quantum programs thread together reusable logical operations, yet correcting errors requires comparing measurements across operation boundaries. Correlations tie each operation's error analysis to the computation around it. Adaptive computation makes this a runtime challenge: measurement results determine which operation comes next, so the error analysis must keep pace with execution. We introduce extended detector error models (EDEMs), which compose in sequence and in parallel, mirroring the composition of physical realizations and their detector contracts. We prove how detectors, the measurement parities used to diagnose errors, can be split across circuit boundaries, and establish conditions under which composition recovers the assembled circuit's detector error model. This structure supports symbolic precompilation and analysis of entire families of circuits. It also defines error models for decoding windows and the boundary information through which committed corrections affect subsequent windows. The same interface thus connects the design of individual logical operations to the decoding of an unfolding quantum program.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.13087) | 2026-09-14
