---
title: "The Tower of Babel: Large Language Models for Side-channel Analysis"
date: "2026-09-26"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2224"
summary: "Deep learning-based side-channel analysis (DLSCA) is dominated by CNNs and from-scratch Transformer architectures, while pretrained Large Language Models (LLMs) as side-channel distinguishers remain l"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Deep learning-based side-channel analysis (DLSCA) is dominated by CNNs and from-scratch Transformer architectures, while pretrained Large Language Models (LLMs) as side-channel distinguishers remain largely unexplored. We present the first systematic study of seven off-the-shelf pretrained LLMs (DeepSeek, Falcon, GPT-J, GPT-2, GPT-2m, Qwen2, T5) on three masked AES datasets, i.e., ASCADf, ASCADv, and eShard. With lightweight fine-tuning and no architectural redesign of the backbone, Falcon and GPT-2m reach GE=1 on ASCADf in only 12 to 16 traces (16, 12 and 12 traces for Falcon and 15, 14 and 13 for GPT-2m on desync0, desync50 and desync100) and uniquely sustain this trace count under desynchronization, an order of magnitude below the best prior desynchronized results. The strongest reported alternatives, EstraNet (13 traces) and Order-vs-Chaos (1 trace), are bespoke architectures trained from scratch and report only synchronized results, while other CNN- and Transformer-based baselines degrade substantially under desynchronization. The pretrained LLMs additionally extract exploitable leakage from all 16 first-round AES key bytes, the first such result outside of multi-task CNNs trained from scratch. We further provide the first per-share evaluation and the first interpretability analysis of LLM-based SCA using Effective Perceived Information (EPI), revealing a correlation between the models' leakage extraction capability and their attack performance. Strikingly, randomly initialized backbones perform on par with their pretrained counterparts, indicating that much of the advantage is architectural rather than derived from language pretraining. Our findings establish LLM architectures as unexpectedly powerful, robust, and reusable side-channel distinguishers whose inductive bias yields very low trace complexity and strong robustness to desynchronization.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2224) | 2026-09-26
