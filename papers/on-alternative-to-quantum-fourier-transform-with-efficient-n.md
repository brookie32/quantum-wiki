---
title: "O(n) alternative to Quantum Fourier Transform with efficient neural net classical post-processing"
date: "2026-09-16"
updated: "2026-09-16"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.16998"
summary: "arXiv:2605.16998v2 Announce Type: replace Abstract: The Quantum Fourier Transform (QFT) is employed by hidden subgroup problem (HSP) algorithms, including Shor's algorithm for factoring. The circuit d"
last_verified: "2026-09-16"
review_by: "2026-12-15"
stale: false
---

arXiv:2605.16998v2 Announce Type: replace Abstract: The Quantum Fourier Transform (QFT) is employed by hidden subgroup problem (HSP) algorithms, including Shor's algorithm for factoring. The circuit depth of the QFT remains challenging for near-term hardware. To find shallower alternatives we identify two properties that are exploited by the QFT to enable HSP. Firstly, the shift invariance of the QFT allows for the removal of a random overall shift. Secondly, the QFT retains information about the hidden subgroup generator accessible in the measurement outcomes. We quantify that information via the discrete Fisher information. We construct a family of shallow circuits using Hadamards and controlled-Phase gates, HP-L circuits, that we prove preserve shift invariance. Numerical analysis shows these circuits retain exponentially growing Fisher information. The O(n) HP-1 is employed in place of the O(n^2) QFT in our numerical implementation of Shor's algorithm. An efficient neural network is used for the corresponding classical post-processing.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.16998) | 2026-09-16
