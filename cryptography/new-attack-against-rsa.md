---
title: "New Attack Against RSA"
date: "2026-09-28"
updated: "2026-09-28"
source: "agent"
category: "cryptography"
tags: [cryptography, schneier-on-security]
url: "https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html"
summary: "ArsTechnica is reporting on a “new” attack against RSA, one that bypasses factoring. First, this attack isn’t new. The original research is from 2007. What is new is the implementation. Second, it is "
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

ArsTechnica is reporting on a “new” attack against RSA, one that bypasses factoring. First, this attack isn’t new. The original research is from 2007. What is new is the implementation. Second, it is a forgery attack. It allows an attacker to forge digital signatures. It does not recover the private key from the public key. Third, the attack only works against pure signatures. That is, signatures without any formatting or padding. This is not generally how we use RSA in practice. Fourth, speed is all relative. This is not a polynomial-time algorithm; it’s a subexponential-time algorithm. But it is somewhat faster than factoring. The authors were able to forge messages for 1024-bit RSA with 1380 CPU core-years (over five real-world months)...

**Source:** [Schneier on Security](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html) | 2026-09-28
