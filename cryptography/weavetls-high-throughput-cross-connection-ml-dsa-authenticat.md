---
title: "WeaveTLS: High-Throughput Cross-Connection ML-DSA Authentication in Mutual TLS"
date: "2026-08-28"
updated: "2026-08-30"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1828"
summary: "Mutual TLS (mTLS) authenticates both peers and therefore incurs post-quantum signature costs on every connection. Concurrent handshakes expose independent ML-DSA operations, but executing them jointly"
last_verified: "2026-08-30"
review_by: "2026-11-28"
stale: false
---

Mutual TLS (mTLS) authenticates both peers and therefore incurs post-quantum signature costs on every connection. Concurrent handshakes expose independent ML-DSA operations, but executing them jointly is difficult: signing is rejection-divergent, verification uses heterogeneous keys, and synchronous TLS APIs expose authentication work one connection at a time. We present WeaveTLS, a wire-transparent architecture that executes ML-DSA authentication across concurrent TLS connections. Its primitive interface combines rejection-aware slot refill with per-request expanded-key handles, supporting both unrelated client keys and shared issuer keys. A stackless OpenSSL continuation lets an nginx worker suspend authentication, expose work from other connections, and execute compatible operations through optimized single-request, four-request, or eight-request AVX-512 kernels without fibers or cross-thread handoff. WeaveTLS preserves the TLS authentication barrier, certificate validation, and wire protocol. On an AMD Ryzen 9 9950X3D, WeaveTLS improves one-core nginx mTLS throughput by 2.81-4.31imes over OpenSSL's default ML-DSA path and by 2.19-3.29imes over a synchronous reference-C control in the same provider across ML-DSA-44/65/87. At the primitive boundary, expanded-key eight-request verification is 1.65-2.23imes faster than matched cached AVX2, and rejection-aware refill makes ML-DSA-65 signing 1.90imes faster than otherwise identical lockstep scheduling. Cohort publication also weakens client-visible rejection timing under load, reducing attempt-count/latency correlation to 0.063 at concurrency 16 and 0.008 at 64; singleton execution retains the signal.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1828) | 2026-08-28
