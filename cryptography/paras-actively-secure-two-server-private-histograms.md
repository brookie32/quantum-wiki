---
title: "Paras: Actively Secure Two-Server Private Histograms"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1600"
summary: "Private histogram computation is a fundamental building block for many data analytics tasks, enabling frequency analysis without revealing individual inputs. Existing protocols achieving robustness ag"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Private histogram computation is a fundamental building block for many data analytics tasks, enabling frequency analysis without revealing individual inputs. Existing protocols achieving robustness against malicious clients and servers typically require three servers with limited adversarial tolerance, restricting practicality. In this work, we present Paras, the first two-server protocol for private histogram computation that achieves robustness against collusion between a malicious server and arbitrarily many malicious clients. Paras builds upon distributed point function-based approaches and introduces novel consistency checks leveraging vector oblivious linear evaluation (VOLE) to enforce both input correctness and output integrity. To realize these checks, we design two new cryptographic primitives: (1) aBV, an authenticated bit verification protocol that ensures VOLE committed shares correspond to valid bits, and (2) adIPA, an authenticated double inner product argument that enables secure consistency checks across two different VOLE sessions. These primitives may be of independent interest for other secure computation tasks. We show that Paras is highly efficient and scalable: clients incur minimal cost independent of domain size, while servers achieve low per-client runtime, communication, and storage even at scale. For example, with 8192 clients over a domain of 128 inputs, each server requires only 14 ms runtime and 24 KB communication per client.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1600) | 2026-08-04
