---
title: "Randomness-Anchored Runtime Discovery of Cryptographic Operations on Linux Using eBPF"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2345"
summary: "Migration to post-quantum cryptography requires knowing not only which cryptographic libraries are present on a system, but which algorithms are actually executed at runtime. Static binary analysis an"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Migration to post-quantum cryptography requires knowing not only which cryptographic libraries are present on a system, but which algorithms are actually executed at runtime. Static binary analysis answers the former question; the latter requires dynamic observation. We present a runtime cryptographic discovery system for Linux, built on eBPF user-space probes, that detects classical and post-quantum operations as they execute. Because key generation and encapsulation consume fresh randomness, the system treats randomness observations as temporal anchors and correlates them with the cryptographic calls that follow in the same process, producing a stream of confidence-scored events for a runtime cryptographic inventory. An ablation over three detection configurations shows that randomness alone is not a sound detector, while API detection reaches perfect precision and recall on classical and ML-KEM workloads with no false positives on random-only negatives, and the randomness anchor raises the confidence of those detections without adding any. A single probe set also covers native post-quantum support in current OpenSSL releases. Median detection latency is 28 μs (P99 48 μs), largely insensitive to a four-round tuning sweep, with overhead of 14–18% on a key-generation-bound workload, full detection under sustained and concurrent load, and stable behavior over a one-hour run. A case study across nine application cases drawn from or paired with the QED datasets shows where static and runtime views agree and how probe coverage determines what runtime discovery can observe.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2345) | 2026-10-05
