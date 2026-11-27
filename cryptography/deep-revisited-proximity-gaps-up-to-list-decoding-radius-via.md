---
title: "DEEP Revisited: Proximity Gaps up to List-Decoding Radius via Out-of-Domain Samples"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3053"
summary: "We revisit the use of out-of-domain samples for proximity gaps, introduced in DEEP-FRI. Over sufficiently large fields, multiple samples yield proximity gaps for linear codes at any list-decodable rad"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

We revisit the use of out-of-domain samples for proximity gaps, introduced in DEEP-FRI. Over sufficiently large fields, multiple samples yield proximity gaps for linear codes at any list-decodable radius below the code’s minimum distance. For general linear codes, this extends the proximity-gap guarantee from the one-and-a-half Johnson bound to the full Johnson bound using a constant number of out-of-domain samples. With a constant fraction of agreement loss and field size q at least the blocklength, the error is O(1/q), yielding roughly 20 to 30 additional bits of soundness in typical hash-based SNARK settings. For Reed-Solomon codes, the bounds apply beyond the Johnson radius even when the list size L is much larger than 2^lambda. When the field is sufficiently large for the target error, O(log L / lambda) out-of-domain samples suffice to achieve error 2^{-lambda}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3053) | 2026-11-26
