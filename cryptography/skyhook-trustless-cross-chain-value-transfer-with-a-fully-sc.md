---
title: "Skyhook: Trustless Cross-Chain Value Transfer with a Fully Scriptless Pool"
date: "2026-09-25"
updated: "2026-09-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2210"
summary: "Facilitating value transfers with a scriptless chain is a longstanding problem in cryptography. We present a cross-chain messaging and value transfer protocol that maintains game-theoretic atomicity e"
last_verified: "2026-09-27"
review_by: "2026-12-26"
stale: false
---

Facilitating value transfers with a scriptless chain is a longstanding problem in cryptography. We present a cross-chain messaging and value transfer protocol that maintains game-theoretic atomicity even when one party is operating on a chain which is fully scriptless, such as shielded Zcash, which has no scripting capabilities at all and requires transactions to be virtually identical. The observation is that consensus protocols which utilise segregated witness schemes to ensure transaction ID unmalleability (such as ZIP244 in Zcash, SegWit in Bitcoin), segregate transaction data from transaction witness component (which is the part that is actually signed). The transaction identifier is, therefore, a virtually collision-resistant commitment to the effects intended by the transaction, computable before signing, and in many chains, even without the knowledge of the signer. We then use this primitive to build a non-interactive zero-knowledge argument (NIZK) to prove that a given future transaction ID reliably commits to a specific effect, often without revealing the sender, confidential data, or requiring the recipient to sign. Combined with an SPV light client on the Turing-complete chain, this yields fully trustless verification that a shielded transaction occurred with a reliable guarantee, with no requirements of a validator consortium or multisig that can be hacked or stalled.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2210) | 2026-09-25
