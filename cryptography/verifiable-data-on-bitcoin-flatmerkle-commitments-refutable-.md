---
title: "Verifiable Data on Bitcoin: FlatMerkle Commitments, Refutable Proofs, and FlatChecks"
date: "2026-11-01"
updated: "2026-11-04"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2717"
summary: "We give a method to publish data on Bitcoin and to verify properties of that data on Bitcoin itself, against a publisher who may lie. The data is a FlatMerkle file – a structured byte string whose ord"
last_verified: "2026-11-04"
review_by: "2027-02-02"
stale: false
---

We give a method to publish data on Bitcoin and to verify properties of that data on Bitcoin itself, against a publisher who may lie. The data is a FlatMerkle file – a structured byte string whose ordinary SHA-256 supports logarithmic inclusion proofs and logarithmic proofs of malformation – placed in a transaction's annex or, at four times the cost but relayable by Bitcoin Core, in an output. We show that the publisher's ordinary Taproot signature, with a suitably chosen signature-hash type, binds the publisher to the published data in a form that a dispute can authenticate with a single SHA-256 compression plus the signature check, or with three compressions when no annex is used. Claims about the data, and claims about such claims, are published as proof messages in two formats: a plain encoding, refuted by revealing it whole, and a traced encoding that stores the verifier's output after each level, so that any false message is refuted by revealing at most five of its elements. The format, chosen by a cost model that weighs challenge bytes against published bytes, is fixed by public context so that no message can be read in two formats; chains of claims about claims settle at four logical elements. A dispute thus reduces to a few dozen SHA-256 compressions and one Schnorr verification per commitment – too large for Bitcoin Script, but small enough to adjudicate with an interactive bisection game, a chunked script in the manner of BitVM2, or a garbled circuit. The same technique verifies any locally refutable verifier, one whose every rejection is witnessed by a single check over a few words of a canonical trace. In a FlatCheck, the prover publishes only the proof; the trace, the verifier's intermediate values, is published only if a challenger asks for it, and the dispute then examines the single check he names. When the verifier splits into groups that each read a few parts of the proof, a challenge forces the trace of one group only. We give two examples: a toy L2 of signed transfers, whose 512-transfer batches cost 12,200 vbytes to claim, and a Bitcoin header-chain light client verified on Bitcoin itself, which claims a retarget period of 2,016 headers in 45,200 vbytes; a dispute over a local check costs about 37,500 and 49,200 vbytes, and one over a malformed trace about 77,100 and 99,800, independently of the number of groups. Verifying STARK proofs is another application. We also remove FlatMerkle's restriction to power-of-two sizes without padding.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2717) | 2026-11-01
