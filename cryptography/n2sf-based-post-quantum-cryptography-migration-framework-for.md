---
title: "N2SF-Based Post-Quantum Cryptography Migration Framework for Data in National and Public Institutions"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2353"
summary: "This paper proposes post-quantum cryptography (PQC) migration decision criteria for data in national and public institutions, based on the protection requirements of the National Network Security Fram"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

This paper proposes post-quantum cryptography (PQC) migration decision criteria for data in national and public institutions, based on the protection requirements of the National Network Security Framework (N2SF) and the cryptographic dependencies and operational states of data. The criteria distinguish payload retention, key rewrapping, re-encryption, communication migration, and signature renewal. Required actions are separated from decisions to allow, defer, or deny execution. Completion requires consistent results for the same object and version, recovery of registered copies, and current authority. A reference implementation examined these decisions under supported conditions. In 225 policy trials, completion/read rechecking and per-stage rechecking exhibited none of the unauthorized completions or reads observed with initial-decision reuse. Nine interruption trials confirmed resumption by reconciling artifacts with records. These results support the feasibility of the criteria in the local reference environment; institutional approval, production key management, and long-term preservation continuity remain unvalidated.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2353) | 2026-10-05
