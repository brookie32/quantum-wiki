---
title: "Differentially Oblivious Resizing for Group-By Aggregations"
date: "2026-09-17"
updated: "2026-09-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2065"
summary: "Systems for private group-by aggregation (e.g., computing histograms, min/max values, or averages) let a confidential virtual machine (CVM) generate statistics from streaming user data. A particular c"
last_verified: "2026-09-19"
review_by: "2026-12-18"
stale: false
---

Systems for private group-by aggregation (e.g., computing histograms, min/max values, or averages) let a confidential virtual machine (CVM) generate statistics from streaming user data. A particular challenge in such systems is ensuring that the CVM's memory-access patterns do not reveal (too much) private information to the untrusted host. While it is possible to rely on oblivious RAM (ORAM), doing so imposes a significant performance penalty and requires allocating sufficient memory to handle a worst-case data stream. We introduce ROGA, a scheme for Resizable Oblivious Group-by Aggregation. ROGA uses an extension of oblivious single-access machines and thus improves performance, both asymptotically and concretely, relative to using ORAM. It also incorporates a novel, differentially oblivious resizing mechanism that ensures the allocated memory is within a constant factor of the memory used by a non-oblivious solution. ROGA also parallelizes cleanly across multiple cores for improved performance. We implement ROGA in Rust and use Binsec/Rel to verify trace noninterference of its compiled fixed-capacity operations, resize estimator, and fixed-work noise sampler, showing that executions with equal public parameters have identical branch-target and memory-address traces for all secret inputs. The only data-dependent branch is the differentially private resize decision. Compared to state-of-the-art oblivious schemes for confidential analytics (which do not support private resizing), ROGA is up to 50.4imes faster when sharded across 64 logical cores, and private resizing cuts memory by up to 14imes compared to domain-provisioned instances. In a case study, ROGA using 16 cores processes the standard network statistics of a 277-million-packet backbone trace with 5.3imes end-to-end overhead over a non-oblivious pipeline while exactly matching the reference output.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2065) | 2026-09-17
