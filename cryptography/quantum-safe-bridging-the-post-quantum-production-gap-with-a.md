---
title: "quantum-safe: Bridging the Post-Quantum Production Gap with a Hybrid-by-Default Python Cryptography Library"
date: "2026-10-07"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, arxiv-quant-ph]
url: "https://arxiv.org/abs/2605.17061"
summary: "arXiv:2605.17061v2 Announce Type: replace-cross Abstract: FIPS 203, 204 and 205 closed the algorithmic gap in post-quantum cryptography (PQC); the production gap -- hybrid combiners, conformance evide"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

arXiv:2605.17061v2 Announce Type: replace-cross Abstract: FIPS 203, 204 and 205 closed the algorithmic gap in post-quantum cryptography (PQC); the production gap -- hybrid combiners, conformance evidence, migration tooling, stateful signing, protocol helpers -- remains open. A methodology that scores it must not choose its own dimensions, so we anchor nine to external requirements (CNSA 2.0, CMVP, the TNO CADI survey, the IETF hybrid draft). We present quantum-safe, a hybrid-by-default Python library built against this rubric, and an audit of nine PQC libraries (September 2026). The exercise can lower our own score, and it does. Hybrid combiners exist in three of six verifiable libraries, not the one a March-2026 snapshot found. Discovery and inventory tooling is the sharper gap: none of seven audited libraries has it; quantum-safe adds a CycloneDX CBOM. Only Bouncy Castle holds a CMVP FIPS 140-3 certificate; quantum-safe reports 225/225 runnable ACVP known-answer cases, which is conformance evidence, not validation. Bouncy Castle also supports LMS and XMSS where quantum-safe has LMS only, and quantum-safe's defaults sit below the CNSA 2.0 parameter sets; we score both against ourselves. Every benchmark figure is computed from archived raw runs (bootstrap intervals over 15 runs). A full X25519 + ML-KEM-768 handshake takes a median of 231 microseconds under Docker/Linux (95% interval 218-250), 5.3x an X25519-only handshake and 0.46-2.3% of a typical TLS 1.3 budget. Throughput is flat from 100 to 5,000 threads but below the single-thread rate: threads do not speed up the hybrid path, although liboqs does release the GIL in longer calls (ML-DSA-65 signing scales 2.6x on four threads). Timing side channels are treated in a companion paper.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2605.17061) | 2026-10-07
