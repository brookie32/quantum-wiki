---
title: "Post-Quantum Self-Updatable Pseudonyms for Conditional Privacy-Preserving Authentication in VANETs From Lattice-Based Credentials"
date: "2026-11-22"
updated: "2026-11-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2981"
summary: "Authentication in vehicular networks must hide the sender and still allow an authority to identify it when needed. Schemes in which a vehicle derives its own pseudonyms avoid authority contact after r"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

Authentication in vehicular networks must hide the sender and still allow an authority to identify it when needed. Schemes in which a vehicle derives its own pseudonyms avoid authority contact after registration, but known constructions rest on assumptions that quantum computers break. We present L-SUPA, a lattice-based scheme of this kind. The credential contains a binary key, and the pseudonym of an epoch is a vector of rounded inner products of that key with public pseudo-random vectors; because the rounding is an exact integer relation, the statement that a pseudonym is the rounding of the signed key fits, together with possession of a credential, inside the presentation proof of a practical lattice anonymous-credential system. Messages are signed with a fresh FN-DSA-512 key bound to the pseudonym, and a tracing authority separate from the issuer identifies a sender by scanning stored keys. The relation raises the presentation proof from 79.6 to 81.4 KiB and its verification time by about 3%; on one desktop core a presentation verifies in 0.15 s, the time of about 4500 message-signature verifications, and a message signature verifies in 0.033 ms. A presentation adds 0.32% to the message bytes of a one-hour epoch at 10 Hz for 722-byte messages, the most favorable rate, and messages of one vehicle are linkable within an epoch. The analysis states, goal by goal, whether we have a reduction, a conditional reduction, or a sketch; under the generic hybrid the presentation-layer M-LWE and LWR terms leave margins of about 80 and 176 bits for 2^{30} vehicles over ten years (no claim of 128-bit anonymity).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2981) | 2026-11-22
