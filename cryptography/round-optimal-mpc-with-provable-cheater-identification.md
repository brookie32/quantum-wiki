---
title: "Round Optimal MPC With Provable Cheater Identification"
date: "2026-10-07"
updated: "2026-10-09"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2393"
summary: "Secure multiparty computation with provable identifiable selective abort (PISA), introduced by Kondi and Ravi (CCS 2025), guarantees that every honest party either obtains the computation output or a "
last_verified: "2026-10-09"
review_by: "2027-01-07"
stale: false
---

Secure multiparty computation with provable identifiable selective abort (PISA), introduced by Kondi and Ravi (CCS 2025), guarantees that every honest party either obtains the computation output or a certificate that convinces any external auditor that a specific party cheated. Crucially, honest parties need not agree: some may get output while others receive evidence of cheating. In contrast, secure computation with identifiable abort (IA) requires just such unanimity; however, in the event that an honest party doesn't get output, it need merely be able to point to a cheater - not to prove their guilt. Secure computation with IA classically requires broadcast. Kondi and Ravi demonstrated that secure computation with PISA, on the other hand, can be built over point-to-point channels alone. While PISA is feasible exactly when guaranteed output delivery is, i.e. for t < n / 2, the best known construction over point-to-point channels requires six rounds. We settle the round complexity of PISA for all but a narrow band of thresholds. We prove that two rounds are impossible for t geq n /3, even with arbitrary setup and computational assumptions; we give a three-round protocol for any t < n/2, which is therefore round-optimal for n / 3 leq t < n/2; and we give a two-round protocol for t < n/4. The two-round protocol introduces a new primitive called one-or-nothing secret sharing with omissions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2393) | 2026-10-07
