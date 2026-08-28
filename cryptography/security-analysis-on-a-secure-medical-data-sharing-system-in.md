---
title: "Security Analysis on a Secure Medical Data Sharing System in Digital Twin Environments"
date: "2026-08-26"
updated: "2026-08-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1801"
summary: "Gao et al. (IEEE Internet of Things Journal, 2025) proposed a medical data sharing system for digital twin environments using identity-based encryption (IBE), public-key encryption with keyword search"
last_verified: "2026-08-28"
review_by: "2026-11-26"
stale: false
---

Gao et al. (IEEE Internet of Things Journal, 2025) proposed a medical data sharing system for digital twin environments using identity-based encryption (IBE), public-key encryption with keyword search (PEKS), and blockchain technologies. In this short note, we show that Gao et al.'s system allows unauthorized users to access other patients' medical data. We further show that the search server can obtain information about the queried keywords from the trapdoors (search queries). In addition, we analyze the procedure used to retrieve, from the blockchain, the IPFS (InterPlanetary File System) addresses storing encrypted medical data and encrypted keywords. Since these addresses are derived from labels that can be computed solely from public information and keywords, and because the keywords themselves are provided to the search server, we demonstrate that searchable encryption is unnecessary in the first place. Based on our security analysis, we argue that the proposed system requires a fundamental redesign.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1801) | 2026-08-26
