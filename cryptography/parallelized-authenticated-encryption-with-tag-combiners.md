---
title: "Parallelized Authenticated Encryption with Tag Combiners"
date: "2026-09-11"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1981"
summary: "When looking at authenticated encryption schemes, we have schemes that process the input data by having serial calls to their underlying building blocks, like duplex-based constructions, and schemes t"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

When looking at authenticated encryption schemes, we have schemes that process the input data by having serial calls to their underlying building blocks, like duplex-based constructions, and schemes that allow for parallel calls to their underlying building blocks, like the Galois Counter Mode (GCM). Naturally, one can parallelize a serial scheme by distributing the data to encrypt over different calls to the serial scheme. However, there are many different choices to be made, like how to choose the nonce for the different instances, or if and how to combine the multiple tags into a single one. In this paper, we investigate different possible choices providing proofs for their security. Interestingly, we see a huge variance in the provable properties and hence, the security in making a serial scheme parallel. Or, motivating the problem more generally, we are investigating tag combiners, where the single tags to be combined are secret to the adversary.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1981) | 2026-09-11
