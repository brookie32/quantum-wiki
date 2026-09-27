---
title: "Communication Preserving SFE from Obfuscation"
date: "2026-09-25"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2214"
summary: "The communication complexity of computing a function in the two party setting can be much smaller than requiring one of the parties to send its input. We revisit how this communication complexity must"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

The communication complexity of computing a function in the two party setting can be much smaller than requiring one of the parties to send its input. We revisit how this communication complexity must change if the function must be computed securely. Hubáček and Wichs show that any protocol for computing a function securely must communicate at least as many bits as the length of the function's output. However, all positive results in this direction require much more communication than optimal. In particular, the state of the art for general protocols requires a extit{multiplicative} overhead polynomial in the security parameter, achieving only ''rate 0'' asymptotically. We show that, assuming the existence of input-succinct indistinguishability obfuscation for Turing machines, it is possible to achieve constant rate for this task. This compiler works even when the original protocol communicates single bits in each round, which is the main obstacle in prior works, and necessitates the use of obfuscation. The compiler can be based on standard non-succinct indistinguishability obfuscation for circuits (instead of Turing machines) in the common random string or random oracle models.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2214) | 2026-09-25
