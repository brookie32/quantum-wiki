---
title: "Faulting the Proof: Key Recovery Attacks on MQOM, SDitH and FAEST"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3064"
summary: "MQOM, SDitH and FAEST are three candidates in the third round of NIST’s additional call for post-quantum signature schemes. The signature in all of them is a proof of knowledge of the secret key. We s"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

MQOM, SDitH and FAEST are three candidates in the third round of NIST’s additional call for post-quantum signature schemes. The signature in all of them is a proof of knowledge of the secret key. We study their resistance to faults during the computation of this proof and present practical key-recovery attacks on all three schemes. Our attacks exploit a common feature among them: a value that is omitted from the signature to reduce its size is still bound through a hash. We show how an attacker can use this hash to test guesses about secret key material from faulty signatures. This yields new attacks on all three schemes and corrects an earlier analysis of fault attacks on MQOM, which assumed that the omitted value is available to the attacker. We demonstrate the attacks with clock glitches on an STM32F405 microcontroller running code from the round-3 reference implementations. The validated attacks recover the full secret key of all three schemes. These results show that the proof evaluation is a practical fault target in signature schemes based on the MPC-in-the-head and VOLE-in-the-head paradigms.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3064) | 2026-11-26
