---
title: "Separating Quantum Indistinguishability Obfuscation from Falsifiable Assumptions"
date: "2026-08-27"
updated: "2026-08-27"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.25195"
summary: "arXiv:2608.25195v1 Announce Type: new Abstract: Quantum indistinguishability obfuscation (qIO) aims to make a quantum circuit unintelligible while preserving its functionality. It serves as a foundati"
last_verified: "2026-08-27"
review_by: "2026-11-25"
stale: false
---

arXiv:2608.25195v1 Announce Type: new Abstract: Quantum indistinguishability obfuscation (qIO) aims to make a quantum circuit unintelligible while preserving its functionality. It serves as a foundational primitive for advanced applications, such as witness encryption (WE) for QMA, non-interactive zero-knowledge arguments for QMA, and attribute-based encryption for BQP. Despite its importance, constructing qIO from standard assumptions remains a major open problem. In this work, we prove that the security of WE for QMA cannot be based on any falsifiable cryptographic assumption via a restricted class of quantum black-box reductions. Because qIO for null quantum circuits implies WE for QMA, this also separates null-qIO from falsifiable assumptions. Since almost all standard cryptographic assumptions are falsifiable, our result presents a barrier to basing qIO on standard cryptographic assumptions. The reductions we rule out are restricted: the reduction must query the adversary classically, non-adaptively, at the same security parameter, and only on honestly generated ciphertexts. Moreover, our impossibility applies only to WE with classical ciphertexts, and therefore does not rule out qIO with obfuscators whose output is a quantum state. Ruling out more general reductions, as well as more general forms of WE and qIO, remains open. Our impossibility relies on the existence of a QMA-QCIP[2] gap problem, an average-case assumption postulating a QMA language that cannot be verified with two messages of classical communication.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.25195) | 2026-08-27
