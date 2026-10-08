---
title: "Differential-Neural Cryptanalysis of ChaCha and Related ARX Stream Ciphers"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2382"
summary: "The paper presents the first-ever differential neural cryptanalysis of the Latin Dances family of Salsa, ChaCha, and Forró. First, we provide a systematic differential-neural study of the ARX stream c"
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

The paper presents the first-ever differential neural cryptanalysis of the Latin Dances family of Salsa, ChaCha, and Forró. First, we provide a systematic differential-neural study of the ARX stream cipher ChaCha. We train and compare six neural architectures, viz.: Gohr's residual network, DBitNet, an Inception network, an MLP-ResNet, an SE-ResNet, and a self-attention network on a 3-round reduced version of ChaCha. We train in both the classical single-pair setting and a multi-pair setting that combines up to sixteen ciphertext pairs through a log-odds rule. We extend the study for breadth to other ARX ciphers, Salsa, *ChaCha, and Forró. We provide the first-ever distinguisher for 4.5 rounds of Salsa with accuracy of 0.53 for one pair and 0.60 for 16 pairs. Also, for Forró the first-ever distinguisher for 1.25 rounds of Salsa with accuracy of 1 for single and multiple pairs. We also introduce a family of experimental round-1-XOR variants (XOR-1) that isolate the contribution of the first round's diffusion to distinguishability. Finally, we investigate the trained 3-round ChaCha distinguisher with four explainability experiments and show that, although the output difference is its dominant feature, it is not a pure differential distinguisher: its decision is interpretable as a learned mixture of round-1 truncated differentials, five of which already account for 99% of the high-confidence ciphertext pairs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2382) | 2026-10-06
