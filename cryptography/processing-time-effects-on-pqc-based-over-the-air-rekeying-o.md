---
title: "Processing-Time Effects on PQC-Based Over-the-Air Rekeying over CCSDS TC/TM Links"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2354"
summary: "When post-quantum cryptography (PQC)-based over-the-air rekeying (OTAR) is evaluated over CCSDS Telecommand (TC) and Telemetry (TM) links, omitting endpoint processing time can change not only the fin"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

When post-quantum cryptography (PQC)-based over-the-air rekeying (OTAR) is evaluated over CCSDS Telecommand (TC) and Telemetry (TM) links, omitting endpoint processing time can change not only the final transport outcome but also the protocol execution path shaped by COP-1 retransmission and CLCW return feedback. This study instantiates the P1–P2–P3 exchange of a PQC-based Space Data Link Security (SDLS) key update over a CCSDS TC/TM transport model and performs paired comparisons between a zero-processing baseline, T₀, and a processing-aware model, T₁, whose service times are measured at seven logical stages of a study-specific Triple-KEM reference implementation. The two models are compared at three observation levels—final transport outcome, canonical event path, and continuous timing—while varying processing scale, finite contact time, direction-specific loss, and schedule phase. Under the canonical schedule with measured processing at αs = 1, no final-transport-outcome discordance is observed in the evaluated BCH and LDPC(512,256) TC-only or TM-only conditions, although some paired trials follow different canonical event paths. At some predefined TM-only processing-scale points, bidirectional final-outcome discordance is observed between success and P2-stage failure. The agreement state also varies with the evaluated finite contact time, and a schedule-phase case exhibits a larger transport-completion timing difference aligned with the TM slot structure. Under the evaluated conditions, the effect of omitting processing time therefore cannot be characterized by success or failure alone and must be interpreted together with event-path, timing, contact-time, and schedule conditions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2354) | 2026-10-05
