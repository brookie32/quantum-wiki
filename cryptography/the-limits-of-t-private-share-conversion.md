---
title: "The Limits of t-Private Share Conversion"
date: "2026-08-23"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1780"
summary: "Private information retrieval (PIR) protocols allow a user to retrieve an entry from a database held by several servers without revealing any information about the index to any individual server. Stat"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

Private information retrieval (PIR) protocols allow a user to retrieve an entry from a database held by several servers without revealing any information about the index to any individual server. State-of-the-art information-theoretic PIR protocols are based on a combination of matching vectors over the ring Z_m and decoding polynomials (Efremenko, SICOMP 2012; Dvir and Gopi, STOC 2015; Ghasemi, Kopparty, and Sudan, STOC 2025). Decoding polynomials are sparse polynomials over a field F_q, where q is a prime power coprime to m, that evaluate to a nonzero value at 1 and to 0 on a certain set of inputs determined by m. The properties of decoding polynomials were abstracted by Beimel, Ishai, Kushilevitz, and Orlov (CCC 2012) through the notion of share conversions. Share conversions allow a set of parties to locally convert a secret shared under one scheme into a related secret shared under another scheme. They constructed a share conversion from Z_m to F_{q} for various values of m and prime-powers q. More recent PIR protocols by Dvir and Gopi and by Ghasemi et al. were abstracted by Alon, Beimel, and Lasri (TCC 2025). The share conversion they considered transforms shares from the ring Z_m to a finite field F_q, where q is a prime-power coprime to m. We observe that if the initial conversion is based on a t-private secret-sharing scheme, then the resulting PIR protocol of Alon et al. is also t-private: no set of t servers learns any information about the user's index. We call such share conversions t-private share conversions. Moreover, the resulting PIR protocol could potentially achieve communication complexity better than that of the best-known t-private PIR protocols, due to Woodruff and Yekhanin (CCC 2005) and Barkol, Ishai, and Weinreb (APPROX-RANDOM 2007). This raises the natural question of whether t-private share conversions exist. We show that there is no t-private share conversion from Z_m to F_q when tgeq 2 and q is coprime to m. As a result, the PIR framework of Alon et al. cannot be instantiated in a way that yields a t-private PIR protocol. We further generalize the result to conversions whose output is in the ring Z_{m'}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1780) | 2026-08-23
