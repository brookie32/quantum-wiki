---
title: "Fuzzy Private Set Intersection with Large Databases via Locality-Sensitive Hashing"
date: "2026-11-19"
updated: "2026-11-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2953"
summary: "Many query workloads require privacy-preserving similarity joins: parties, each holding a private database, may want to learn which of their records are close to records in the other party's database "
last_verified: "2026-11-22"
review_by: "2027-02-20"
stale: false
---

Many query workloads require privacy-preserving similarity joins: parties, each holding a private database, may want to learn which of their records are close to records in the other party's database under a distance metric, without leaking anything beyond this information. Fuzzy private set intersection (fuzzy PSI) is a cryptographic primitive that addresses this problem. In this setting, a client and a server hold sets X and Y, respectively, and the client learns the subset of points in X that are "close" to points in Y. Fuzzy PSI has many use cases, including biometric authentication, password breach monitoring, contact tracing, regional-outbreak monitoring, and machine-learning label matching. Despite growing interest in fuzzy PSI, many existing schemes still require communication costs and client computation linear in the server's set size |Y|. Consequently, these protocols do not scale well to the unbalanced setting, where |X| ll |Y|, as is common in many client-to-server applications. In this work, we propose an efficient fuzzy PSI protocol for the unbalanced setting. At its core is a fuzzy probabilistic data structure (fuzzy PDS), which generalizes prior work by combining locality-sensitive hashing (LSH) with compact filters, enabling tunable false-positive and false-negative rates while ensuring efficient queries. Building on techniques from unbalanced PSI, we combine oblivious pseudorandom functions and private information retrieval with our fuzzy PDS to support private and communication-efficient approximate matching. We instantiate the protocol with an LSH for the L_2 metric and evaluate it on two real-world workloads: regional-outbreak monitoring and machine-learning label matching. Our results show significant reductions in communication and runtime compared with state-of-the-art fuzzy PSI schemes, with gains that increase as the server database size |Y| grows.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2953) | 2026-11-19
