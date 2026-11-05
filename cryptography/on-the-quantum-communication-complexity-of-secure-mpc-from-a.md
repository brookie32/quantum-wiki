---
title: "On the (Quantum) Communication Complexity of Secure MPC from a Random Oracle"
date: "2026-11-02"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2727"
summary: "Information-theoretic MPC among n parties with t corruptions can securely evaluate a circuit C with O(|C| dot t/(n-t)) online communication in the preprocessing model and O(|C| dot t/(n-2t)) communica"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Information-theoretic MPC among n parties with t corruptions can securely evaluate a circuit C with O(|C| dot t/(n-t)) online communication in the preprocessing model and O(|C| dot t/(n-2t)) communication in the honest majority setting. Damg{aa}rd, Larsen and Nielsen (CRYPTO 2019) showed that both communication bounds are tight for inner products. Fully homomorphic encryption and other assumptions known to imply public-key cryptography beat both communication bounds, but the communication complexity with symmetric-key cryptography alone is less understood. For MPC with preprocessing, we prove that the same Omega(|C| dot t/(n-t)) lower bound holds in the random oracle model, so a random oracle cannot reduce the online communication. For honest majority MPC relative to a random oracle, we present an Omega(|C|) communication lower bound that is matched by a new construction for degree-2 polynomials (including inner products) when n = O(log lambda), beating the information-theoretic bound. We also study quantum MPC. First, we prove that information-theoretic protocols with quantum communication (and preprocessing) cannot reduce communication compared to their classical counterparts. Furthermore, we extend our lower bound for MPC with preprocessing to protocols with a quantum-accessible random oracle, but use only classical communication. In contrast, with both quantum communication and a post-quantum one-way function, we present a simple two-party protocol that evaluates the two-party instance of these circuits with mathsf{poly}(lambda, log |C|) communication, beating these lower bounds. Finally, such communication savings do not come for free. We prove that there exist circuits C such that every blackbox protocol with o(|C|) quantum communication must perform Omega(|C|) cryptographic operations.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2727) | 2026-11-02
