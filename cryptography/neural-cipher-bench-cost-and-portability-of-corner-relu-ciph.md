---
title: "Neural Cipher Bench: Cost and Portability of Corner-ReLU Cipher Implementation"
date: "2026-11-10"
updated: "2026-11-12"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2850"
summary: "Edge and Internet of Things (IoT) devices run neural networks on GPUs, neural processing units (NPUs), and microcontrollers (MCUs) through machine learning (ML) runtimes. Deep Neural Cryptography (DNC"
last_verified: "2026-11-12"
review_by: "2027-02-10"
stale: false
---

Edge and Internet of Things (IoT) devices run neural networks on GPUs, neural processing units (NPUs), and microcontrollers (MCUs) through machine learning (ML) runtimes. Deep Neural Cryptography (DNC, EUROCRYPT 2026) expressed AES as a bit-exact ReLU network with fixed weights, using a corner-ReLU construction that keeps the cipher inside the affine+ReLU operators such runtimes execute. What this construction costs on edge and IoT hardware, and whether real ML backends execute it correctly, had not been measured. We implement SM4, ARIA, Camellia, and ChaCha20 (spanning substitution–permutation, Feistel, and add–rotate–XOR structures) alongside AES on a shared corner-ReLU core under one construction policy, derive a cost model for width, depth, and neuron count, and measure five execution paths on four platforms. All ciphers admit bit-exact networks whose width and depth diverge with cipher structure, and the model's width predicted where GPU throughput drops. Every configuration passing the correctness check fell below its classical baseline (best 0.80×, SM4 on the GPU), by hundreds to thousands of times for the S-box ciphers on the MCU, and keeping the activations on chip through fusion raised throughput 1.4–3.5× and moved the peak past the predicted cache limit without closing the gap. Some AES configurations on the Apple Neural Engine returned valid-looking but incorrect outputs with no error or warning, a failure reproduced in a minimal graph without project code. Mathematical bit-exactness therefore does not guarantee backend-level bit-exactness, and exact workloads offloaded to edge NPUs require output validation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2850) | 2026-11-10
