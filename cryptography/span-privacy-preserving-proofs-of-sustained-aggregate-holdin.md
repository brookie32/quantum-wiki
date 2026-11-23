---
title: "SPAN: Privacy-Preserving Proofs of Sustained Aggregate Holdings in UTXO Privacy Pools"
date: "2026-11-21"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2978"
summary: "Privacy pools are expanding from private transfers to tokenized real-world assets and holding-dependent rewards. These applications motivate evidence of sustained holdings across note replacements. We"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Privacy pools are expanding from private transfers to tokenized real-world assets and holding-dependent rewards. These applications motivate evidence of sustained holdings across note replacements. We define a privacy-preserving interval proof of holding (PP-IPoH) scheme and present SPAN for arbitrary-value unspent transaction output (UTXO) pools. Two incrementally verifiable computations (IVCs) authenticate selected records and establish spend completeness, certifying a balance lower bound after every finalized transaction. An independent zero-knowledge succinct argument proves that this bound meets a threshold throughout an interval and supports subsequent queries over the same certified history. We prove completeness, knowledge soundness, and privacy under the stated component and ledger conditions. Experiments show linear proving time, adding about 2.9 seconds per additional transaction, and essentially constant maximum memory usage near 3.8 GB.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2978) | 2026-11-21
