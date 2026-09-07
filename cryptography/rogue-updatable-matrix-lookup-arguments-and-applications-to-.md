---
title: "Rogue: Updatable Matrix Lookup Arguments and Applications to Verifiable Databases"
date: "2026-09-04"
updated: "2026-09-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1890"
summary: "Proving the correctness of computations over a large dataset via succinct non-interactive arguments of knowledge (SNARKs) entails the large overhead of ``loading'' the dataset in the SNARK. However, c"
last_verified: "2026-09-07"
review_by: "2026-12-06"
stale: false
---

Proving the correctness of computations over a large dataset via succinct non-interactive arguments of knowledge (SNARKs) entails the large overhead of ``loading'' the dataset in the SNARK. However, certain computations may only need to access a small fraction of the dataset (e.g., a database query that only accesses a subset of table rows and then computes an aggregation function). The standard way of efficiently proving such computations is to use lookup arguments with sublinear prover complexity to load only necessary data to the SNARK. Unfortunately, all prior schemes are static: even a single change to the dataset forces the prover to re-run an expensive pre-processing step, linear to the dataset size. The only exemption is the recent work of Dutta et al., (CCS'24) that proposed a lookup argument with amortized sublinear updates---based on re-running the pre-processing phase periodically, when too many changes have been accumulated. In this work, we present Rogue, the first lookup argument with sublinear prover time and updates that always take time proportional only to the number of incurred changes. Indeed, Rogue is actually a matrix lookup argument, supporting entire row lookups in time proportional to the number of rows (and independent of their size)! It has very good practical performance, e.g., for a 2^{20}imes 2^7 matrix and 2^{10} row accesses, Rogue achieves imes 21-942 and imes 76-30000 faster lookups and updates, respectively, compared to prior works. We then use Rogue to build RogueDB, the first verifiable database system for arbitrary SQL queries that supports authenticated indexes, hence achieves prover time sublinear to the database. Compared with prior schemes with succinct proofs, vSQL (Zhang et al., IEEE S&P'17) and PoneglyphDB (Gu et al., SIGMOD'25), we get imes 42.8-imes 8624.1 and imes 149.6-imes 11362.4 faster prover times, for various SQL queries from the TPC-H benchmark.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1890) | 2026-09-04
