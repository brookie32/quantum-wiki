---
title: "Universally Composable Reverse Firewalls for Oblivious Linear Evaluation and Applications"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2012"
summary: "Secure multi-party computation (MPC) traditionally assumes that parties execute protocols on trustworthy machines. This assumption fails under machine subversion, where compromised devices may leak se"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Secure multi-party computation (MPC) traditionally assumes that parties execute protocols on trustworthy machines. This assumption fails under machine subversion, where compromised devices may leak sensitive information through manipulated protocol transcripts. Reverse Firewalls (RFs), introduced by Mironov and Stephens-Davidowitz, counter this threat by externally sanitizing messages in a functionality-preserving manner, without trusting the internal execution environment. Prior RF constructions are limited to Boolean-circuit-based MPC using oblivious transfer (OT) and garbled circuits (GC). In contrast, many high-performance MPC protocols are predominantly arithmetic, relying on Oblivious Linear Evaluation (OLE) as a core primitive. Achieving subversion resilience in this setting requires sanitizing OLE, a problem that has remained open. We initiate a systematic study of subversion-resilient arithmetic MPC in the universally composable (UC) framework against semi-honest adversaries. We formalize a sanitizable OLE functionality FsOLE, prove a two-round impossibility for a natural class of additive homomorphic encryption (AHE)-based protocols, and present a UC-secure three-round construction from key-malleable AHE. To recover the full expressiveness of plain OLE, we further introduce wrapped sanitizing OLE under a covert adversary model, yielding an efficient UC-secure two-round protocol. Both constructions are instantiated using a key-malleable AHE scheme from class groups that we construct. Using OLE as a black box, we obtain the first subversion-resilient UC-secure protocols for Oblivious Polynomial Evaluation (OPE), Oblivious Polynomial Addition (OPA), and Private Set Intersection (PSI), achieving optimal communication for PSI. A full end-to-end implementation demonstrates that RF protection incurs only a 1.5--3X overhead, showing that practical subversion-resilient MPC is attainable.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2012) | 2026-09-14
