---
title: "Removing the Human, Keeping the Doors Unlocked: A Cross-Tool Formal Analysis of GSMA SGP.32 eSIM IoT Provisioning"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2020"
summary: "GSMA SGP.32 manages eSIM profiles for unattended IoT devices by replacing the local user confirmation of consumer eSIM provisioning (SGP.22) with the signature of a remote manager, the eIM. The device"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

GSMA SGP.32 manages eSIM profiles for unattended IoT devices by replacing the local user confirmation of consumer eSIM provisioning (SGP.22) with the signature of a remote manager, the eIM. The device segment is forecast at 1.5 billion units in 2026. We present the first formal security analysis of SGP.32 and the first vulnerability-class account of the RSP family across its three generations. Modeling the v1.3 management plane in Tamarin and ProVerif, we witness six specification-level attacks, among them a 10-step management-plane takeover that chains two unauthenticated local operations. The protocol's resistance to network adversaries verifies cleanly. A requirement audit shows the attacks violate SGP.31's own SHALL for association integrity; the companion NOTE defers the mechanism to implementation. A twin model of SGP.22 shows the vulnerable interface was inherited while the human who compensated for it was not. Of the 26 local operations, 40% carry real card-side authentication, and every unauthenticated one is local. Two fixes that reuse mechanisms the specification already contains are proved effective and add no steady-state overhead, and the same join-hard, leave-soft shape recurs across zero-touch standards. All 24 verdicts are machine-checked and the models are open.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2020) | 2026-09-14
