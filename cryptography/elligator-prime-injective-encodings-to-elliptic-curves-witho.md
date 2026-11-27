---
title: "Elligator Prime: Injective Encodings to Elliptic Curves Without Torsion Assumptions"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3058"
summary: "extit{Encoding functions} map finite-field elements to rational points on elliptic curves and are used in many cryptographic protocols. Injective encodings with efficient inversion are of particular i"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

extit{Encoding functions} map finite-field elements to rational points on elliptic curves and are used in many cryptographic protocols. Injective encodings with efficient inversion are of particular interest, since they allow elliptic curve points to be transmitted as strings indistinguishable from uniformly random ones, as in extit{Elligator}. However, existing injective encodings rely on rational points of small order, which excludes important families of curves, notably those of prime order. Constructing efficient injective encodings to curves of prime order has thus remained a challenging open problem for more than a decade. Classical deterministic encodings based on Ska{l}ba's equality apply to all curves, but this equality only guarantees that some candidate abscissa is valid and does not control the fibres of the encoding. In this paper, we introduce Elligator Prime, which takes a new direction in the design of encoding functions by replacing Ska{l}ba's equality with an odd-parity identity on four injective Mobius branches, arranged as two pairs exchanged by a fixed-point-free involution. Exactly one pair then contains exactly one valid abscissa, and the sign of the resulting point identifies that pair. This yields uniform 2{:}1 encodings whose fibres are the orbits of the involution; choosing one representative per orbit gives an injective encoding with efficient inversion, without any rational torsion point of a prescribed order. In characteristic p>3, it covers every curve with j(E)notin{0,1728}, in particular every curve of prime order with j(E)neq0, and the curves with j(E)in{0,1728} that have a nonzero rational 2-torsion point. It also covers all ordinary elliptic curves in characteristic~3 and all ordinary binary elliptic curves y^2+xy=x^3+ax^2+b with bneq1, closing a gap left by earlier constructions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3058) | 2026-11-26
