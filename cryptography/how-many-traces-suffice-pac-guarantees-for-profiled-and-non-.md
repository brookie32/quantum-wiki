---
title: "How Many Traces Suffice? PAC Guarantees for Profiled and Non-profiled Side-Channel Analysis"
date: "2026-08-21"
updated: "2026-08-23"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1770"
summary: "Side-channel analysis (SCA) is commonly evaluated by reporting the number of traces required to reduce the rank of the correct key. Still, such evaluations remain empirical and do not explain how many"
last_verified: "2026-08-23"
review_by: "2026-11-21"
stale: false
---

Side-channel analysis (SCA) is commonly evaluated by reporting the number of traces required to reduce the rank of the correct key. Still, such evaluations remain empirical and do not explain how many traces suffice for reliable recovery, how profiling and attack data contribute separately, or when additional traces cannot overcome weak key distinguishability. We address these questions through a Probably Approximately Correct (PAC) formulation of profiled and non-profiled SCA. Our framework treats candidate-key scores as the common cryptanalytic object and separates finite-sample estimation from the intrinsic separation between the correct key and competing hypotheses. This distinction enables confidence guarantees for key rank and helps determine whether an attack failure is due to insufficient data or an inherently weak attack score. We instantiate the framework with representative profiled and non-profiled attacks chosen for their analytical tractability. Experiments on ASCAD-f and ASCAD-r show that this analytical tractability does not come at the cost of impractical attack performance. The profiled attack achieves exact recovery with tens of attack traces, whereas the non-profiled single-attack rank certificate guarantees exact recovery with about 1,000 traces. These results are competitive with recent ASCAD attacks and, in the non-profiled setting, substantially below the smallest trace counts identified in prior studies, while additionally providing finite-sample guarantees on key rank. More generally, the same finite-sample rank analysis can be adapted to other learners and distinguishers by deriving the corresponding score-gap guarantees. Overall, the framework turns trace complexity from an empirical attack observation into a reusable finite-sample criterion for key recovery.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1770) | 2026-08-21
