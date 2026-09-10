---
title: "AIPA: Anonymous Image Provenance Authentication in Online Social Networks via Unlinkable Pseudonym Certificates and zk-SNARKs"
date: "2026-09-07"
updated: "2026-09-10"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1914"
summary: "Generative AI has made high-fidelity deepfakes easy to produce, and online social networks (OSNs) spread them widely across users and platforms. Publicly verifying an image's provenance, i.e., where a"
last_verified: "2026-09-10"
review_by: "2026-12-09"
stale: false
---

Generative AI has made high-fidelity deepfakes easy to produce, and online social networks (OSNs) spread them widely across users and platforms. Publicly verifying an image's provenance, i.e., where an image came from and what edits it has undergone, can help combat deepfakes. The Coalition for Content Provenance and Authenticity (C2PA) offers an industry-standard framework, but depends on trusted software and hardware environments. Cryptographic image authentication eliminates the reliance on trusted editors through signatures and zero-knowledge proofs. However, deploying such schemes in OSNs faces three problems: preserving signer privacy, maintaining provenance authenticity across edits, and ensuring efficient verification. To ensure signer anonymity in image provenance, we propose an unlinkable pseudonym certificate scheme (UPCS) based on anonymous credentials. UPCS provides fast signing and X.509 compatibility, with signing taking only 0.017 ms in our experiments. Building on UPCS, zk-SNARKs, and hash chains, we present an anonymous image provenance authentication (AIPA) scheme, ensuring the authenticity of provenance and editing history of an image as it propagates across mutually untrusted editors, while preserving signer privacy. To achieve efficient verification in OSNs, we propose VIMz-Loua, an image proof system featuring GPU acceleration, constant-size proofs, and low verification overhead, with support for proving JPEG compression, where each proof is only 448 B and is verified in 12 ms in our experiments. We formally prove the security of UPCS and AIPA, and implement an end-to-end workflow in a simulated OSN environment, where the full multi-edit provenance lineage is only 40.2 KB and is verified in 4.28 s.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1914) | 2026-09-07
