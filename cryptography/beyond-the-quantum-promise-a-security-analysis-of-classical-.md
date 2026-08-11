---
title: "Beyond the Quantum Promise: A Security Analysis of Classical Control in Quantum Key Distribution"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.07626"
summary: "arXiv:2608.07626v1 Announce Type: new Abstract: Quantum Key Distribution (QKD) protocols provide information-theoretic security by using quantum mechanical principles. Yet QKD is fundamentally a hybri"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.07626v1 Announce Type: new Abstract: Quantum Key Distribution (QKD) protocols provide information-theoretic security by using quantum mechanical principles. Yet QKD is fundamentally a hybrid protocol: its security depends on the correct integration of the quantum phase with classical post-processing. While ETSI and ITUT specifications standardize QKD architectures and interfaces, they evaluate protocol security in isolation, leaving cross-layer interactions as an underexplored attack surface. This paper introduces a formal verification framework that holistically models QKD protocols based on ETSI and ITUT QKD specifications. Our model is the first hybrid QKD protocol model that supports automated analysis of protocollevel security focusing on how classical operations influence the security guarantees provided by the quantum phase of the QKD protocol. We formalize a comprehensive symbolic model of QKD protocols, based on ETSI and ITU-T QKD specifications, in Tamarin, an automated protocol verifier. Applying this framework, we obtain formal evidence of three specification-level vulnerabilities in ETSI- and ITU-T-grounded protocol models under adversary Eve+: subverted entanglement injection, basis-deferred measurement, and message reflection. Each arises from a classical control-plane omission in the procedure text and is established under a symbolic abstraction rather than as a claim about all practical deployments. We introduce two protocol improvements: measurement commitment and identitybound message authentication codes (MACs). Tamarin verification confirms that these countermeasures eliminate the identified vulnerabilities under Eve+. We have communicated our results and recommendations to relevant standardization organizations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.07626) | 2026-08-11
