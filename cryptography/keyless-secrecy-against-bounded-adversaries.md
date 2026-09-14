---
title: "Keyless secrecy against bounded adversaries"
date: "2026-09-14"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.12251"
summary: "arXiv:2609.12251v1 Announce Type: new Abstract: We introduce a keyless coding/cryptographic primitive that asks for two guarantees at once: the receiver is never fooled into accepting a message other "
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

arXiv:2609.12251v1 Announce Type: new Abstract: We introduce a keyless coding/cryptographic primitive that asks for two guarantees at once: the receiver is never fooled into accepting a message other than the one sent, and the adversary learns nothing about the message unless the receiver aborts. Neither the sender nor the receiver holds a secret key, and no computational hardness is assumed. The only restriction is on the adversary's online computation: the receiver aborts if nothing arrives by a fixed deadline, so the adversary must forward something before it, and her map in that window is computed by a circuit of size (or depth) at most p; before and after, she is unbounded. For every polynomial p we construct such an efficient quantum scheme, encoding k-bit messages into n = O(k) qubits with circuits of size poly(n,p). No classical scheme achieves this type of everlasting security, at any choice of parameters. Our techniques also resolve open questions about universal tamper detection against families restricted in cardinality rather than in circuit size. We settle a question of Broadbent, Kapshikar and Rochette on relaxed tamper detection. As a corollary, we obtain the first efficient non-malleable code secure against global quantum tampering, with no split-state restriction, whereas the current constructions in the literature require the codeword to be split into non-communicating shares.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.12251) | 2026-09-14
