---
title: "Quantum Vault: Symmetric No-Cloning Protection for Token Issuer and User (Benchmarked on IBMQ)"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.03564"
summary: "arXiv:2605.03564v2 Announce Type: replace Abstract: Quantum tokens are underlying primitives for quantum money and network proposals, which leverage the no-cloning theorem to realize unforgeable authe"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2605.03564v2 Announce Type: replace Abstract: Quantum tokens are underlying primitives for quantum money and network proposals, which leverage the no-cloning theorem to realize unforgeable authentication. A relevant but overlooked type of attack to such architectures is one in which a hacker steals the classical side information about the token states from the issuing agent (e.g., a bank), enabling the forgery of fake tokens without violating the no-cloning theorem. Our proposal addresses this threat by removing the classical side information about the token states, where instead a copy of the token is stored at the bank, i.e. a quantum vault. This copy can be accessed by anyone to perform authentication, consuming the token pair in the process. We benchmark the protocol and identify quality parameters within a hardware agnostic framework employing IBMQ processors, such that the protocol is applicable to arbitrary quantum platforms. By comparing the efficiency with which genuine tokens are produced and authenticated against a possible estimate-and-forge attack, we quantify the security of the protocol. We achieve probabilities lower than 10^{-4} for false-negative errors (Type 1) and 10^{-10} for successful attacks (Type 2) when considering quantum bills composed of 200 tokens, even in the worst performing processor and most conservative uncertainty estimate. The quantum vault not only protects both user and bank symmetrically with the same quantum principles, but provides a step towards public key authentication, since any untrusted party can have access granted by the bank to the tokens' authentication interface without being able to clone them. Besides this bank-mediated form of publicly accessible verifiability, our proposal achieves traceability and revocability, since the bank retains the vault copy of the tokens.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.03564) | 2026-09-15
