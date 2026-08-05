---
title: "Improving initial-state-dependent quantum circuit optimization by introducing state labels"
date: "2026-08-05"
updated: "2026-08-05"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2509.04761"
summary: "arXiv:2509.04761v4 Announce Type: replace Abstract: While the capabilities of quantum hardware have significantly advanced in recent years, executing quantum algorithms as quantum circuits at the lowe"
last_verified: "2026-08-05"
review_by: "2026-11-03"
stale: false
---

arXiv:2509.04761v4 Announce Type: replace Abstract: While the capabilities of quantum hardware have significantly advanced in recent years, executing quantum algorithms as quantum circuits at the lowest possible cost remains crucial, regardless of the hardware progress. We are developing a quantum-state-dependent circuit optimizer called AQCEL. Our guiding principle, implemented as the AQCEL optimization protocol, is to optimize quantum circuits by measuring the states of the control qubits to identify and eliminate unnecessary control operations. In this paper, we introduce two key improvements: the state label manager that reduces unnecessary state measurements and the CX-pair removal process that eliminates redundant gate pairs. These enhancements significantly reduce the number of two-qubit gates, improving the fidelity of quantum circuits executed on quantum hardware. To demonstrate the effectiveness of our method, we apply AQCEL to quantum circuits for the quantum parton shower algorithm. Experimental results using the IBM quantum computer show a substantial reduction in gate counts and an improvement in fidelity compared to the conventional optimization technique as well as the original AQCEL protocol. Our findings highlight the potential of state-dependent circuit optimization for enhancing the performance of quantum algorithms on near-term quantum devices.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2509.04761) | 2026-08-05
