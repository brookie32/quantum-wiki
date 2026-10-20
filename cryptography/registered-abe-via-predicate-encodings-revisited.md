---
title: "Registered ABE via Predicate Encodings, Revisited"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2558"
summary: "Predicate encodings, proposed by Wee (TCC'14), are a simple framework that abstracts a variety of attribute-based encryption (ABE) schemes. Zhu et al. showed how to apply predicate encodings to regist"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

Predicate encodings, proposed by Wee (TCC'14), are a simple framework that abstracts a variety of attribute-based encryption (ABE) schemes. Zhu et al. showed how to apply predicate encodings to registered ABE (Reg-ABE) using the same definition as in vanilla ABE (Asiacrypt'23). We provide a new definition of predicate encodings that is more suitable for registered ABE and allows us to obtain more efficient Reg-ABE schemes than those by Zhu et al. for predicates captured by predicate encodings. Notably, we obtain egin{itemize} item the first Reg-ABE scheme for (non-)zero inner product with O(log L) -size ciphertexts, item the first Reg-ABE scheme for conjunctions/disjunctions with O(log L) -size ciphertexts, item the first registered broadcast encryption scheme with O(log L) -size ciphertexts, end{itemize} under the standard k -Lin assumption, where L denotes the maximum number of users. Prior to our work, Reg-ABE schemes for (non-)zero inner product, conjunctions, and disjunctions require O(elllog L) -size ciphertexts where ell is the vector length or the policy size, and registered broadcast encryption schemes rely on the generic group model.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2558) | 2026-10-19
