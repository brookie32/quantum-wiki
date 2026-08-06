---
title: "Baker: A Privacy-Preserving, NIZK-free and Efficient Payment Channel Hub Supporting Bidirectional Channels"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1596"
summary: "Payment Channel Hub (PCH) improves blockchain scalability by enabling off-chain transactions via an untrusted intermediary known as the tumbler. However, existing PCHs either fail to guarantee the unl"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Payment Channel Hub (PCH) improves blockchain scalability by enabling off-chain transactions via an untrusted intermediary known as the tumbler. However, existing PCHs either fail to guarantee the unlinkability privacy or rely on inefficient non-interactive zero-knowledge (NIZK) proofs. Recently, Ge et al. proposed Accio, a privacy-preserving PCH that eliminates the need for NIZK proofs. Nevertheless, Accio only supports unidirectional channels which results in high on-chain costs and routing inefficiencies. In this paper, we present Baker, the first bidirectional payment channel hub that operates without NIZK proofs and guarantees unlinkability. Unlike prior PCH solutions that maintain channel balance using a single state, Baker introduces a novel design in which each non-tumbler user maintains two separate pockets to record the channel balance. To ensure payment atomicity, Baker further designs a novel cryptographic primitive named Aggregatable Adaptor Signature (AAS) to enable atomic signature exchanges and signature aggregation. We implement Baker and empirically demonstrate its advantages over state-of-the-art protocols. Compared to BlindHub, which relies on NIZK proofs for privacy, Baker reduces off-chain communication overhead to 0.0036%. Moreover, the off-chain computation overhead of Baker is 7% of that of BlindHub and 40% of TBPChannel. Relative to Accio, Baker incurs only 80% of its on-chain cost and enjoys a 25% higher average transaction success rate.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1596) | 2026-08-04
