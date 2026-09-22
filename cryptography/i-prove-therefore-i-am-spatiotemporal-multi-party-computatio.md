---
title: "I Prove, Therefore I Am: Spatiotemporal Multi-Party Computation"
date: "2026-09-20"
updated: "2026-09-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2118"
summary: "Secure multiparty computation (MPC) enables mutually distrustful parties to compute on private digital inputs. We initiate the study of mathbf{spatiotemporal} mathbf{MPC}, extending this paradigm to f"
last_verified: "2026-09-22"
review_by: "2026-12-21"
stale: false
---

Secure multiparty computation (MPC) enables mutually distrustful parties to compute on private digital inputs. We initiate the study of mathbf{spatiotemporal} mathbf{MPC}, extending this paradigm to functionalities whose inputs additionally depend on physical facts such as the parties' locations, times, or trajectories. Such protocols must simultaneously hide spatiotemporal information and ensure its physical consistency: a malicious party should not be able to make the functionality operate on a spatiotemporal input inconsistent with its actual physical state. The main conceptual challenge is to formulate extraction of spatiotemporal information within the simulation-based security framework. We introduce mathbf{arguments} mathbf{of} mathbf{spatiotemporal} mathbf{knowledge}, following the principle "I prove, therefore I am:" rather than defining physical presence directly through a mathematical relation, we define it operationally through the ability to complete a sound spatiotemporal verification protocol. Accordingly, an extractor recovers a spatiotemporal point from a successful prover and certifies its physical validity by using the extracted prover to succeed in an auxiliary spatiotemporal verification protocol. Building on this notion, we define universally composable (UC) security for spatiotemporal MPC, capturing privacy, physical consistency, and composability. We provide constructions achieving this new MPC notion. We first construct UC-secure commit-and-prove protocols for spatiotemporal knowledge: in the CRS model under LWE against quantum provers without pre-shared entanglement, and in the QROM against quantum provers with unbounded pre-shared entanglement. Using these protocols, we obtain general-purpose UC-secure spatiotemporal MPC from semi-honest post-quantum MPC. We also extend our framework to UC-secure spatiotemporal multiparty quantum computation over private quantum inputs and classical spatiotemporal information.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2118) | 2026-09-20
