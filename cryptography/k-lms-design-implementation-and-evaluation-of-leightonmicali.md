---
title: "K-LMS: Design, Implementation, and Evaluation of Leighton–Micali Signatures with Korean Cryptographic Primitives"
date: "2026-10-06"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2372"
summary: "Hash-based signatures are the most conservative post- quantum signature family, and the stateful schemes XMSS and LMS are both standardized by NIST. Prior work has instantiated XMSS and SPHINCS+ with "
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

Hash-based signatures are the most conservative post- quantum signature family, and the stateful schemes XMSS and LMS are both standardized by NIST. Prior work has instantiated XMSS and SPHINCS+ with Korean cryptographic primitives, but no comparable Korean-primitive study exists for LMS. We fill that gap with K-LMS, an experimental variant that preserves the full LMS structure and domain separation and replaces only the hash. The substituted hashes are the Korean hash function LSH-256, in both its reference and its vectorized implementation, and a Tandem-DM double-block-length construction over the Korean block ciphers CHAM, LEA, and ARIA. A non-invasive bridge over the reference LMS implementation realizes eight interchange- able backends without editing a line of it. We evaluate key generation, signing, and verification latency, key and signature sizes, peak memory, a sweep over tree height and the Winternitz parameter, and implemen- tation complexity. Hash substitution leaves key and signature sizes, and the memory requirement of the LMS data structures, unchanged. We also isolate two measurement pitfalls that can distort such comparisons: a vector dispatch wrapper that re-runs its capability check on every digest, which costs an order of magnitude on our virtualized host, and the choice of software or hardware-accelerated SHA-256 as the baseline, which shifts any LSH vs. SHA-2 conclusion by a factor of about six. Profiling shows that LMS is dominated by 55-byte one-shot hashes (about 94 % of all calls), so scheme-level ranking cannot be extrapolated from long-message hash benchmarks. Against a fair software baseline, LSH-256 K-LMS signing is on par with SHA-256 LMS (0.84×), while hardware acceleration retains a ∼3.6× advantage where it is available. On the same host and with identical LSH-256 code, K-LMS runs 3.3– 3.9× faster than the published K-XMSS implementation, because LMS needs one hash call per Winternitz chain step where XMSS needs three.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2372) | 2026-10-06
