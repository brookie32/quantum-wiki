---
title: "Efficient Quantum Fully Homomorphic Encryption"
date: "2026-04-28"
updated: "2026-04-28"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2604.23490"
summary: "arXiv:2604.23490v1 Announce Type: new Abstract: Quantum fully homomorphic encryption (QFHE) promises secure delegated quantum computation but has been impeded by the prohibitive quantum resource deman"
last_verified: "2026-04-28"
review_by: "2026-07-27"
stale: false
---

arXiv:2604.23490v1 Announce Type: new Abstract: Quantum fully homomorphic encryption (QFHE) promises secure delegated quantum computation but has been impeded by the prohibitive quantum resource demands of existing constructions. This paper introduces a unified framework that achieves an extbf{exponential improvement} in efficiency by synergistically integrating three theoretical tools: extbf{modular arithmetic programs (MAP)}, the extbf{garden-hose model}, and extbf{measurement-based quantum computation (MBQC)}. Our central innovation is a novel MAP tailored to the algebraic structure of Learning-with-Errors (LWE) decryption. Unlike generic approaches that incur exponential overhead, our MAP computes the inner product langle oldsymbol{sk}, oldsymbol{c} rangle mod q by tracking a partial sum modulo q, requiring only O(log q) bits of state width. This yields branching programs of width O(log lambda) and length O(lambda log lambda), thereby reducing the size of the essential quantum gadget from O(lambda^{2.58}) to O(lambda log^2 lambda) EPR pairs -- a concrete improvement factor of 2^{15} to 2^{18} for standard security parameters. Critically, we demonstrate that LWE decryption is not a extbf{symmetric function}, necessitating our specialized MAP design beyond prior symmetric-function optimizations. The framework provides a direct mapping from the MAP to an efficient gadget via the garden-hose model, with MBQC furnishing the deterministic control flow for homomorphic evaluation. The resulting QFHE scheme supports extbf{fully classical clients}, relies solely on the extbf{classical LWE assumption} (avoiding circular security or quantum hardness assumptions), and maintains compactness. This work dramatically lowers the quantum resource barrier for practical QFHE, paving the way for realistic privacy-preserving quantum cloud computing.



## Related
- [[demonstration-of-a-quantum-c-not-gate-in-a-time-multiplexed-|Demonstration of a quantum C-NOT Gate in a Time-Multiplexed fully reconfigurable photonic processor]]
- [[a-fully-quantum-algorithm-for-image-edge-detection|A Fully Quantum Algorithm for Image Edge Detection]]
- [[beyond-monolithic-scaling-modularity-and-heterogeneity-as-an|Beyond Monolithic Scaling: Modularity and Heterogeneity as an Architectural Imperative for Utility-Scale Quantum Computing]]
- [[diffqec-a-versatile-diffusion-model-for-quantum-error-correc|DiffQEC: A versatile diffusion model for quantum error correction]]

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2604.23490) | 2026-04-28
