---
title: "On Aborts in Differential Privacy"
date: "2026-09-16"
updated: "2026-09-18"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2059"
summary: "There is a growing literature on differential privacy (DP) in multiparty protocols, enabling use in distributed settings and reduced trust assumptions. A largely overlooked aspect of such protocols is"
last_verified: "2026-09-18"
review_by: "2026-12-17"
stale: false
---

There is a growing literature on differential privacy (DP) in multiparty protocols, enabling use in distributed settings and reduced trust assumptions. A largely overlooked aspect of such protocols is the extent to which an adversary can undermine the DP guarantees by making the protocol abort. Another is the DP properties of the honest parties' outputs. We initiate the study of both these issues. First, we propose an idealized model of aborts, where an aborter is leaked some information about a DP mechanism execution and then chooses whether or not to let an independent malicious analyst learn the mechanism output. We bound the effects of aborts according to what information (the database, randomness, output, or any combination of these) is leaked. These bounds are not only applicable to multiparty DP via general-purpose multiparty computation (MPC) but may also be used in the analysis of other methods to certify DP properties of a protocol. Second, we apply these bounds to analyze ideal protocol executions in MPC. We show, for the first time, that the ideal execution with fairness gives strictly stronger DP guarantees than that for security-with-abort, for the outputs to the honest parties. Further, solitary-output functionalities satisfy guarantees similar to those of the execution with fairness. Finally, we analyze multiparty protocols with respect to the way in which they realize the respective ideal functionalities. We show that partially fair and fully fair protocols have very similar DP guarantees. Since partial fairness, as opposed to full fairness, can be achieved in dishonest-majority settings, and in particular the two-party setting, this opens up for enhanced DP guarantees in two-party computation.



## Related
- [[one-proof-to-rule-them-all-practical-sublinear-verification-|One Proof to Rule Them All: Practical, Sublinear Verification for Actively Secure MPC on Z_{2^k} with Dishonest Majority and a Dealer (Full Version)]]
- [[its-not-just-a-phase-understanding-function-dependence-in-mp|It's Not Just a Phase: Understanding Function Dependence in MPC Preprocessing]]

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2059) | 2026-09-16
