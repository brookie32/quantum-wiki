---
title: "Accordion: Efficient Batch Proving via Algebraic Folding"
date: "2026-09-22"
updated: "2026-09-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2160"
summary: "We present mathsf{Accordion}, a new proof system that works in two steps: - extit{Accumulate}: The first building block is a multi-folding scheme that efficiently accumulates k different instances of "
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

We present mathsf{Accordion}, a new proof system that works in two steps: - extit{Accumulate}: The first building block is a multi-folding scheme that efficiently accumulates k different instances of a degree-d polynomial relation into a single accumulated instance, without using recursion. Our scheme builds on the Protostar [Bünz & Chen, ASIACRYPT '23] and Protogalaxy [Eagen & Gabizon, ePrint 2023/1106] line of work, improving further the verifier efficiency. It supports the same expressive class of relations, arbitrary-degree polynomial constraints, enabling efficient folding for CCS, Plonkish constraints, and even custom gates. - extit{Decide}: The second block is a SNARK decider for the folding scheme, which efficiently proves the validity of the resulting accumulated instance using off-the-shelf optimized building blocks. We give a concrete instantiation consisting of a Plonk-based proof plus an additional KZG polynomial commitment opening. This design is especially attractive in batch-aggregation settings where a prover collects many independent witnesses, folds them into a single accumulator, and then runs one succinct decider to certify the entire batch. Our scheme avoids costly recursion overheads. We implement mathsf{Accordion} and evaluate it against a highly optimized Plonk proving pipeline (exttt{midnight-zk}). For k=64 instances, mathsf{Accordion} is up to 2.5imes faster than computing k Plonk proofs for SHA-256 preimages, with a 3imes faster verifier and 4imes smaller proofs. Its prover is also an order of magnitude faster than using IVC to aggregate the k proofs.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2160) | 2026-09-22
