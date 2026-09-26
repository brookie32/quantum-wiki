---
title: "A Black-Box Impossibility Result for Threshold Signing Standard Hash-Based Signatures"
date: "2026-09-23"
updated: "2026-09-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2194"
summary: "Hash-based signature schemes present an appealing proposition: they are broadly regarded as the most conservative in terms of assumptions, and their efficiency profiles suit many applications. However"
last_verified: "2026-09-26"
review_by: "2026-12-25"
stale: false
---

Hash-based signature schemes present an appealing proposition: they are broadly regarded as the most conservative in terms of assumptions, and their efficiency profiles suit many applications. However, little is known about their compatibility with threshold signing, which is common practice today in domains like digital asset security. Especially in the context of an impending migration to post-quantum cryptography, this gap in the literature leaves uncertain what hash-based standards would imply for applications that rely on threshold signing. In this work, we develop a new framework by which to analyze such hash-based schemes, and prove inherent barriers to designing an entire class of efficient (fully distributed) threshold signing protocols. Our framework is simple, and yet powerful. Our results encompass standard schemes such as XMSS and SLH-DSA. Our approach is to connect hash-based signatures to the literature on straight-line extraction in the random oracle model. We then apply and build upon techniques from the recent work of Doerner et al. (Crypto '24) to show that threshold signing protocols for hash based schemes must—beyond a certain number of signers—use the circuit representation of the hash function, i.e. it can not use the hash function as a black box. We then give a more fine-grained analysis for the specific case of the Winternitz signature scheme—a building block of both NIST standards—and show that it can not permit even two-party signing with blackbox use of the hash function.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2194) | 2026-09-23
