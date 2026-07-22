---
title: "SoK: Adversarial Robustness of the Variational Quantum Eigensolver via Red-Teaming"
date: "2026-07-22"
updated: "2026-07-22"
source: "agent"
category: "chemistry"
tags: [chemistry, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.19318"
summary: "arXiv:2607.19318v1 Announce Type: new Abstract: The Variational Quantum Eigensolver (VQE) is a leading algorithm for estimating molecular ground-state energies on near-term quantum hardware, with appl"
last_verified: "2026-07-22"
review_by: "2026-10-20"
stale: false
---

arXiv:2607.19318v1 Announce Type: new Abstract: The Variational Quantum Eigensolver (VQE) is a leading algorithm for estimating molecular ground-state energies on near-term quantum hardware, with applications spanning quantum chemistry, materials science, and drug discovery. As VQE workloads are increasingly deployed through cloud-based ``VQE-as-a-service'' pipelines, they become exposed to adversaries such as compromised service components, malicious co-tenants, or insiders in the transpilation stack, any of which can corrupt results before they reach the user. A range of attacks on variational quantum circuits has been proposed, but each has been studied in isolation: some on quantum classifiers with accuracy-based metrics, others on variational quantum algorithms with energy-error metrics. This lack of a common evaluation setup makes their relative severity difficult to compare and leaves the security of VQE poorly characterized. In this work, we present extbf{VQE-AdvBench}, the first unified red-teaming benchmark for the Variational Quantum Eigensolver, systematizing these attacks under a single evaluation protocol to rigorously assess VQE's adversarial robustness. We organize attacks along a black-, gray-, and white-box access taxonomy, and evaluate seven representative attack scenarios -- the QTrojan circuit backdoor, the QDoor parameter backdoor, parameter-space adaptations of FGSM and PGD, and three QNBAD noise-induced variants -- over a fixed molecule-ansatz-backend-metric configuration, on H_2 and H_3^+ across five noise-calibrated IBM backends. Our results reveal a clear severity ordering: noise-induced attacks that manipulate the Zero-Noise Extrapolation (ZNE) pipeline are the most damaging (up to 8.84imes error amplification), followed by the QTrojan circuit-level backdoor (7.52imes), while the QDoor parameter-level backdoor is the least effective, yielding only marginal amplification (up to 1.37imes).

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.19318) | 2026-07-22
