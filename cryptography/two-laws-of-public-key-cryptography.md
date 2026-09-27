---
title: "Two Laws of Public-Key Cryptography"
date: "2026-09-24"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2207"
summary: "We discover two laws governing public-key key exchange and public-key encryption. The first states that a non-interactive key-exchange scheme is secure only if it is kleptographically insecure. The se"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

We discover two laws governing public-key key exchange and public-key encryption. The first states that a non-interactive key-exchange scheme is secure only if it is kleptographically insecure. The second states that a public-key encryption scheme is secure only if it is kleptographically insecure. They give two impossibility results: no kleptographically secure non-interactive key exchange with pseudorandom shared keys exists, and no kleptographically secure public-key encryption with pseudorandom ciphertexts exists. More precisely, no non-interactive key-exchange scheme can simultaneously establish pseudorandom shared keys and support black-box execution in which the user observes only the public keys and the final shared keys output by the black box, and no public-key encryption scheme can simultaneously have pseudorandom ciphertexts and support black-box execution in which the user observes only the public keys and plaintexts input to the black box and the ciphertexts output by it. Our argument turns the very shield of a primitive into a spear against itself, showing that the security guarantee of the primitive is precisely what enables a kleptographic attack. We instantiate the laws with two post-quantum schemes: CSIDH and Regev encryption.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2207) | 2026-09-24
