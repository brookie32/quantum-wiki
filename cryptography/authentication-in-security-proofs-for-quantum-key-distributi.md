---
title: "Authentication in Security Proofs for Quantum Key Distribution"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.17960"
summary: "arXiv:2601.17960v2 Announce Type: replace Abstract: Quantum Key Distribution (QKD) protocols rely on authenticated classical communication. Typical QKD security proofs are carried out in an idealized "
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

arXiv:2601.17960v2 Announce Type: replace Abstract: Quantum Key Distribution (QKD) protocols rely on authenticated classical communication. Typical QKD security proofs are carried out in an idealized setting where authentication is assumed to behave honestly: it never aborts, and all classical messages are delivered faithfully with their original timing preserved. Authenticated channels that can be constructed in practice have different properties. Most critically, such channels may abort asymmetrically, such that only the receiving party may detect an authentication failure while the sending party remains unaware. Furthermore, an adversary may delay, reorder, or block classical messages. This discrepancy means that existing security proofs under honest authentication do not directly establish security in the practical authentication setting. We address this gap using an existing security definition from the literature that permits asymmetric aborts while retaining secrecy of any key produced and agreement of the keys whenever both parties accept. Our main result is a reduction theorem showing that, under mild and easily satisfied protocol conditions, any QKD protocol proven secure under the honest authentication setting, for the standard security definition with symmetric aborts, remains secure under a practical authentication setting, for the weaker security definition that allows for asymmetric aborts. This result allows all existing QKD proofs to be retroactively lifted to the practical authentication setting (with asymmetric aborts) with a minor protocol tweak.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.17960) | 2026-10-26
