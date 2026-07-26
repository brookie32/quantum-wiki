---
title: "Efficient Unclonable Encryption from Pauli Eigenstates"
date: "2026-07-23"
updated: "2026-07-26"
source: "agent"
category: "hardware"
tags: [hardware, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1509"
summary: "We give, to our knowledge, the first plain-model, one-time information-theoretically secure, efficient unclonable encryption scheme for one classical bit. Previous work by Bhattacharyya and Culf (Natu"
last_verified: "2026-07-26"
review_by: "2026-10-24"
stale: false
---

We give, to our knowledge, the first plain-model, one-time information-theoretically secure, efficient unclonable encryption scheme for one classical bit. Previous work by Bhattacharyya and Culf (Nature Physics, 2026) and Bhattacharyya, Broadbent, and Culf (arXiv:2603.08916) either only showed 1/mathsf{poly}(lambda) security loss or required inefficient encryption/decryption operations. We avoid both of these caveats; in doing so, we obtain (to our knowledge) the first plain-model construction of many-time secure 1 o 2 unclonable encryption for arbitrary polynomial-length messages, assuming the existence of pseudorandom function-like states (Bartusek and Goldin, arXiv:2605.27647). The key is a uniformly random non-identity phase-free Pauli on n qubits, and bit a is encrypted as a random (-1)^a eigenstate of that Pauli. Encryption and decryption use O(n) single-qubit operations and O(n) time classical computation; key generation uses only O(n) time classical computation. The scheme is exponentially secure; we prove that the probability that both receivers recover the bit is at most frac{1}{2}+frac{1}{2}sqrt{{2^n}/({4^n-1})} = frac{1}{2} + Oleft(2^{-n/2}right). By a lower bound due to Broadbent, Culf, and Rochette, this is the best probability bound achievable with n-qubit ciphertexts (up to the constant hidden in the O(dot)). The main conceptual idea is to leverage, in a precise spectral sense, the balanced commutation-anticommutation structure of the Pauli group. The proof is intricate but completely elementary and makes use of standard spectral bound techniques. The main technical workhorse is a standalone linear-algebraic lemma which we present in its own section: informally, it relates the positivity of two different operators, each capturing the intuition that if the two receivers can individually decrypt unusually often then they must also disagree often. GPT-5.6 Sol Ultra found this proof in an extended conversation with the author and drafted a preliminary version of this paper. The author is fully accountable for the correctness of this paper.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1509) | 2026-07-23
