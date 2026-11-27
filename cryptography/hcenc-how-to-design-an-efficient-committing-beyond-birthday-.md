---
title: "HCENC: How to Design an Efficient Committing Beyond-Birthday-Bound Accordion from a Block Cipher with n-Bit Blocks and Keys"
date: "2026-11-27"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3078"
summary: "Many accordions, that is, tweakable encryption modes for inputs of variable length, offer security beyond the birthday bound, but they differ in cost and in how they obtain key commitment (CMT-1) or f"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Many accordions, that is, tweakable encryption modes for inputs of variable length, offer security beyond the birthday bound, but they differ in cost and in how they obtain key commitment (CMT-1) or full commitment (CMT-4). Practical deployment needs inexpensive schemes that follow well-established design criteria and proof methods, use standardized primitives, and have small overheads for each master key and message. We introduce HCENC, a generalization of HCTR built from a block cipher with n-bit blocks and keys, an n-bit AXU hash function, and the keystream generator of CENC, that is, a simply masked counter mode. We prove that in the ideal-cipher model it is a strong tweakable pseudorandom permutation up to about 2^n/w blocks, where w is the frame width of the keystream, for every key derivation that satisfies three weak conditions. We show that with the block cipher alone, CMT-1 stays at the birthday bound for every key derivation that computes unrelated derived keys from different master keys. To achieve beyond the birthday bound we admit a second block cipher with longer keys. In concrete instantiations, with HCENC on AES-128 and the transform UCX with a Feistel concealer on AES-256, we obtain CMT-1 and CMT-4 of 116 bits, at a cost of two AES-256 calls for each message, and of one hash evaluation and one AES-256 key expansion more for CMT-4. Among the accordions with a complete proof of security beyond the birthday bound using a single 2n-bit master key, HCENC has among the smallest overheads for each master key and each message. NOTE: The formal proofs are embedded in the PDF file. They can be downloaded from the PDF by clicking on "attached to this PDF" in the paragraph "Machine-checked proofs." This works with many PDF viewers and browsers, but, curiously, not Preview under macOS. Under macOS, use PDFcraft, Adobe Acrobat (Reader), Firefox or Chrome.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3078) | 2026-11-27
