---
title: "Beyond Stepwise Transformation: MILP Model for Low-Area Implementations of Linear Layers"
date: "2026-11-27"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3077"
summary: "Low-area linear layers play an important role in lightweight symmetric-key cryptography. Across gate libraries, multi-input XOR gates are effective in reducing the area of linear layers, but finding l"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Low-area linear layers play an important role in lightweight symmetric-key cryptography. Across gate libraries, multi-input XOR gates are effective in reducing the area of linear layers, but finding lower-area implementations using XOR gates of different input sizes remains challenging. At ToSC 2022, Liu et al. proposed a heuristic stepwise framework that constructs lower-area implementations with (n+1)-input XOR gates from given implementations with (n)-input XOR gates. However, we observe that such a stepwise strategy may restrict the search space and fail to find lower-area implementations. To address this limitation, we propose a mixed-integer linear programming (MILP)-based model that starts from a given XOR2 circuit and searches for lower-area implementations with two-, three-, and four-input XOR gates within a prescribed candidate space. It jointly selects candidate coefficient vectors and admissible XOR implementations to form a valid acyclic circuit that preserves the required outputs and minimizes the area under the given gate costs. Using the proposed MILP-based model, we first re-evaluate the implementations reported by Liu et al. and obtain lower-area implementations for most of the representative linear layers. For AES MixColumns, we obtain an implementation requiring 236.99 gate equivalents (GE) in the STM 130 nm library, improving upon the previous result of 243 GE. We then evaluate the MILP model on a set of more than 5000 (32 imes 32) maximum distance separable (MDS) matrices proposed by Li et al. at ToSC 2019 and reduce their average area by up to about 28% over the initial XOR2 circuits and 8% over previous stepwise multi-input XOR implementations. These results indicate that jointly optimizing two-, three-, and four-input XOR gates within the prescribed search space can be more effective than stepwise transformation in obtaining lower-area implementations of linear layers.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3077) | 2026-11-27
