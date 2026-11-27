---
title: "End-to-End Framework for  Maliciously Secure Threshold Homomorphic Encryption"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3042"
summary: "We study t-out-of-n threshold homomorphic encryption (ThHE) and its instantiation as a maliciously secure multiparty computation (MPC) protocol. We observe that recent ThHE constructions often focus o"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

We study t-out-of-n threshold homomorphic encryption (ThHE) and its instantiation as a maliciously secure multiparty computation (MPC) protocol. We observe that recent ThHE constructions often focus on individual phases, such as distributed key generation or distributed decryption, rather than providing an end-to-end protocol with a comprehensive security analysis. Furthermore, most existing constructions either consider only passive security or address malicious security at a theoretical level, without providing concrete instantiations or evaluating the associated overhead. Consequently, there remains a lack of practical ThHE constructions that can serve as a drop-in replacement for an MPC functionality while achieving malicious security without relying on additional ideal functionalities for key generation or secure decryption, such as a trusted dealer or an external MPC functionality. In this work, we address these limitations by constructing a ThHE scheme and its associated secure computation protocol in an end-to-end manner, covering all phases from distributed key generation to distributed decryption. We provide a comprehensive security analysis of the resulting protocol against malicious adversaries within the universal composability framework. Furthermore, we quantify the concrete overhead of achieving malicious security by instantiating and benchmarking all the required zero-knowledge arguments of knowledge for verifying the well-formedness of cryptographic materials generated throughout the protocol execution. Our benchmarks demonstrate the practicality of our proof system instantiations, with proving times typically around 5 seconds per phase for a small parameter setting with ring degree 2^{13} and a 200-bit ciphertext modulus, and around one minute per phase even for a large parameter setting with ring degree 2^{15} and an 800-bit ciphertext modulus, using only a single thread. Furthermore, the resulting proof sizes remain practical, reaching at most 10 MiB per phase, while the public key materials can be as large as 90 MiB.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3042) | 2026-11-25
