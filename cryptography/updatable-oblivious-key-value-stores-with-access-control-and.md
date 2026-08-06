---
title: "Updatable Oblivious Key Value Stores with Access Control and Application to Multi Key Searchable Encryption"
date: "2026-08-03"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1590"
summary: "Oblivious Key-Value Stores (OKVS) (Garimella et al., CRYPTO 2021), once encoded, provide indistinguishability over keys and random values. This is an important property in many secure computation appl"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Oblivious Key-Value Stores (OKVS) (Garimella et al., CRYPTO 2021), once encoded, provide indistinguishability over keys and random values. This is an important property in many secure computation applications, such as private set intersection and multi-key searchable encryption. We introduce an Updatable Oblivious Key-Value Store with access control (UOKVS), a dynamic extension of OKVS that supports insertions over time. We provide meaningful security in the presence of updates by equipping UOKVS with fine-grained access control. As a building block in UOKVS, we provide the first analysis of oblivious insertions for Cuckoo hashing, which may be of independent interest. We show the application of UOKVS to multi-key searchable encryption where a data owner wishes to share parts of a multimap with multiple clients. We construct an oblivious multimap with insertions from UOKVS and private information retrieval (PIR). Unlike prior multi-key searchable encryption schemes, our construction supports sharing without replicating data across authorized users, substantially reducing storage costs in addition to stronger privacy guarantees. We implement our multi-key searchable encryption construction on a dataset containing up to 24 million entries using the Enron email dataset. For keywords matching 100 documents on a WAN, query processing completes in 0.6 seconds using FrodoPIR as the underlying PIR protocol. By comparison, the scheme of Wang and Papadopoulos (Cloud Computing 2023) achieves a query time of 0.6 seconds and also incurs data replication and leaks access patterns. Our construction reduces leakage, maintains performance, and only requires a 3.1x storage overhead.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1590) | 2026-08-03
