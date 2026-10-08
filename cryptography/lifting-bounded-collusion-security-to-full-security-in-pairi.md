---
title: "Lifting Bounded-Collusion Security to Full Security in Pairing-Based Encryption Schemes"
date: "2026-10-07"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2389"
summary: "Notions like identity-based encryption (IBE) and attribute-based encryption (ABE) augment public-key encryption to provide fine-grained access control to encrypted data. In these settings, there is a "
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

Notions like identity-based encryption (IBE) and attribute-based encryption (ABE) augment public-key encryption to provide fine-grained access control to encrypted data. In these settings, there is a single master public key that anyone can encrypt to. Users in turn possess different secret keys that determine which ciphertexts they can decrypt. The standard, or full, security notion for these schemes stipulates that a ciphertext computationally hides the message if the adversary does not possess a key that is allowed to decrypt. A relaxed notion of security that is often much easier to achieve is bounded-collusion security, where we only require security against adversaries that have an a priori bounded number of keys (and the scheme parameters can grow with this bound). For instance, it is known that vanilla public-key encryption implies bounded-collusion IBE (and ABE) whereas there is a black-box separation between public-key encryption and fully secure IBE. In this work, we develop a general methodology to upgrade a pairing-based encryption scheme with bounded-collusion security into one that is fully secure. We illustrate our methodology by applying it to two main applications: batched IBE and multi-authority ABE. First, in the case of batched IBE, we obtain the first pairing-based construction of batched IBE where there are no tag restrictions (in the generic bilinear group model). All previous pairing-based batched IBE schemes require attaching a tag to ciphertexts and secret keys, and moreover, restrict the adversary to an a priori bounded number of secret keys for each tag. Second, we use our techniques to obtain a multi-authority ABE scheme that supports conjunction policies in the generic bilinear group model. This is the first pairing-based scheme that makes fully black-box use of the group. Previous pairing-based multi-authority ABE schemes require a random oracle whose output is a group element (which implicitly assumes the underlying group supports a procedure for explainable oblivious sampling).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2389) | 2026-10-07
