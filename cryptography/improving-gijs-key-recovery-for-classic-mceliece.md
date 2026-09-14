---
title: "Improving GIJS Key Recovery for Classic McEliece"
date: "2026-09-11"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1984"
summary: "Ghoshal, Ishai, Jain and Sun (GIJS) recently gave the first distinguisher for Classic McEliece public keys that is cheaper than generic decoding. They estimate its cost at 2^{114} to 2^{124} bit opera"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

Ghoshal, Ishai, Jain and Sun (GIJS) recently gave the first distinguisher for Classic McEliece public keys that is cheaper than generic decoding. They estimate its cost at 2^{114} to 2^{124} bit operations for the five NIST candidate parameter sets, and have since extended it to a key-recovery algorithm. The distinguisher is one large sparse linear-algebra computation. We show that this computation already contains the secret key, and we give two ways to extract it. The first method uses the polynomials that the distinguisher computes. For each column of the public key, their gradients span a subcode of the public code, and we prove which subcode this is. Once the subcode is known for every column, the support and the Goppa polynomial follow by linear algebra. The cost is that of about 100 to 1400 runs of the distinguisher, depending on the parameter set. The second method builds on the key-recovery algorithm of GIJS and reads the whole support from a single run. We also lower the cost estimate of the distinguisher itself by about 20 bits. This uses two facts about binary Goppa codes that we prove and two heuristic assumptions that we test. In the cost model of GIJS, key recovery then costs 2^{94} to 2^{102} bit operations, or 2^{114} to 2^{124} if every condition and formula of GIJS is kept unchanged. Information-set decoding costs 2^{151} to 2^{287}. As a demonstration, we ran the single-run attack on the highest-numbered instance of the TII McEliece key-recovery challenges (label 253: m=8, t=9, n=214), which had not been solved, and recovered its secret key. This took two sparse kernel computations with about 10^7 unknowns each, at about 700 core-hours each on one server. None of the Classic McEliece computations is close to practical, and several ingredients are heuristic. We state each heuristic as an explicit assumption. We test each one by running the attacks end to end on small keys and, for the parts that do not need the expensive run, at full Classic McEliece size.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1984) | 2026-09-11
