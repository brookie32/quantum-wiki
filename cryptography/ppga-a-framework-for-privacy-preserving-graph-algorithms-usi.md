---
title: "PPGA: A Framework for Privacy-Preserving Graph Algorithms using the Prepare/Propagate/Gather/Apply Paradigm"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2550"
summary: "Privacy-preserving graph computation enables the secure analysis of graphs modeling social interactions and networks, financial transactions, etc., while keeping the graph private. One approach is to "
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Privacy-preserving graph computation enables the secure analysis of graphs modeling social interactions and networks, financial transactions, etc., while keeping the graph private. One approach is to use secure multiparty computation (MPC), allowing different clients to contribute parts of a graph without need of disclosure, and multiple MPC protocols have been proposed for running message-passing-based graph analysis. Yet, existing public implementations are prototypes for fixed analysis functions that require substantial MPC expertise to modify and extend. We present PPGA, a practical framework based on the MultiCent protocol (PETS'25). PPGA lets users define their custom message-passing graph algorithms with a high-level interface, clients input parts of the graph, and then runs the algorithm in MPC. It significantly improves performance compared to MultiCent's implementation, running BFS on a graph of size |V|+|E|=30 million in 23 minutes without leaking the graph topology.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2550) | 2026-10-19
