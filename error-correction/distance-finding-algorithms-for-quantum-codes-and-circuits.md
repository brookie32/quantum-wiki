---
title: "Distance-Finding Algorithms for Quantum Codes and Circuits"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2603.22532"
summary: "arXiv:2603.22532v2 Announce Type: replace Abstract: The distance of a classical or quantum code is a key figure of merit which reflects its capacity to detect errors. Quantum LDPC code families have c"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2603.22532v2 Announce Type: replace Abstract: The distance of a classical or quantum code is a key figure of merit which reflects its capacity to detect errors. Quantum LDPC code families have considerable promise in reducing the overhead required for fault-tolerant quantum computation, but calculating their distance is challenging with existing methods. We generally assess the performance of a quantum code under circuit level error models, and for such scenarios the circuit distance is an important consideration. Calculating circuit distance is in general more difficult than finding the distance of the corresponding code as the detector error matrix of the circuit is usually much larger than the code's check matrix. In this work, we benchmark a wide range of distance-finding methods for various classical and quantum code families, as well as syndrome-extraction circuits. We consider both exact methods (such as Brouwer-Zimmermann, connected cluster, SAT and mixed integer programming) and heuristic methods which have lower run-time but can only give a bound on distance (examples include random information set, syndrome decoder algorithms, and Stim undetectable error methods). We further develop the QDistEvol algorithm and show that it performs well for the quantum LDPC codes in our benchmark. The algorithms and test data have been made available to the community in the codeDistance Python package.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2603.22532) | 2026-08-17
