---
title: "Distill and Conquer: Cryptanalytic Extraction of Local Rules in the Hard-Label Setting"
date: "2026-11-02"
updated: "2026-11-04"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2723"
summary: "Cryptanalytic extraction can expose proprietary neural network parameters, but unknown architectures and large parameter counts complicate recovery under hard-label access. Local class-pair rules offe"
last_verified: "2026-11-04"
review_by: "2027-02-02"
stale: false
---

Cryptanalytic extraction can expose proprietary neural network parameters, but unknown architectures and large parameter counts complicate recovery under hard-label access. Local class-pair rules offer a narrower target by making class-switching conditions explicit and predicting nearby labels under a specified sampling law. Distillation methods mainly return substitute models rather than explicit rules whose local agreement has been tested against the victim. We propose Distill–Probe–Extract to produce such rules without first identifying the victim architecture. Verified boundary events guide student training, and student gradients propose directions at boundary anchors refined through victim queries. Fresh hard-label queries then test the proposed rules, retaining validation inputs and victim labels for each accepted rule. On a digits multilayer perceptron and pooling convolutional networks, fixed-candidate comparisons isolate the savings from replacing victim-normal estimation with student gradients. For the multilayer perceptron, median recorded online cost decreases from 246 to 118 queries per attempt after student preparation. With preparation and failures counted, full Fashion-MNIST sessions produce 2.03–2.23 times Direct's accepted-rule count under the original validation gate at 320,000-call caps. At 320,000 calls, a separate student-level test on trained Blended watermarks yields 99.99% trigger agreement and 91.79% clean agreement, with all three seeds passing joint verification.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2723) | 2026-11-02
