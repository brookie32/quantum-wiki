---
title: "HELLO, GOODBYE: Concurrent General Composition From Super-Rushing Security"
date: "2026-10-26"
updated: "2026-10-26"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2651"
summary: "Kushilevitz, Lindell, and Rabin (STOC `06, SIAM Journal on Computing `10), in their seminal result, showed that any standalone-secure synchronous multiparty computation (MPC) protocol can be compiled "
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

Kushilevitz, Lindell, and Rabin (STOC `06, SIAM Journal on Computing `10), in their seminal result, showed that any standalone-secure synchronous multiparty computation (MPC) protocol can be compiled into one secure under concurrent general composition, by adding a synchronisation step after every round; thereby, at least doubling the round complexity. We show that for protocols that are secure against super-rushing adversaries, introduced by Asharov, Chandramouli, Cohen, and Ishai (EuroCrypt `25), two synchronisation rounds suffice. Specifically, for an R-round protocol that is secure against super-rushing adversaries with a black-box, straight-line simulator, adding a round of start synchronisation (saying ``HELLO'') and a round of end synchronisation (saying ``GOODBYE'') yields security under concurrent general composition with selective abort in R+2 rounds. If the end synchronisation is over a broadcast channel, the security is upgraded to unanimous abort. Both compilers incur no loss in the security reduction and preserve the flavour of security (perfect, statistical, or computational) of the underlying synchronous protocol. Moreover, combining with the sufficient conditions of Asharov et al. for perfect security, and the round-preserving super-rushing compilers of Ciampi, Ravi, and Zou (Cryptology ePrint Archive 2026/1745) for statistical and computational security, yields compilers from rushing security to security under concurrent general composition, with an additive overhead of at most 2 rounds. We further extend our compilers to protocols with a trusted setup, such as a common reference string or a public-key infrastructure, which is necessary in the dishonest majority setting. We require two conditions. First, every execution of the protocol uses its own stateless copy of the setup, whose responses to the adversary do not depend on the interactions of the honest parties. In particular, this rules out setups that are shared across executions, such as a global common reference string or a single public-key infrastructure used by every execution. Second, the underlying protocol is secure against super-rushing adversaries with adaptive inputs, that is, even when the inputs are chosen after interacting with the setup. Under these conditions, the same compilers yield security under concurrent general composition. We also show that adaptive inputs cannot be relaxed to the usual notion of security in the setup-hybrid model. Specifically, we give a protocol that is statistically secure against super-rushing adversaries with guaranteed output delivery under the standard hybrid model, but is insecure under concurrent general composition after adding start and end synchronisation, even with selective abort.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2651) | 2026-10-26
