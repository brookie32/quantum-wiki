---
title: "RECOB: Reliable Benchmarking of Experimental Optimization in Chemistry and Materials Science"
date: "2026-09-21"
updated: "2026-09-21"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2609.20891"
summary: "arXiv:2609.20891v1 Announce Type: new Abstract: Optimization methods for experimental science are often evaluated on synthetic functions that are reproducible but omit important characteristics of rea"
last_verified: "2026-09-21"
review_by: "2026-12-20"
stale: false
---

arXiv:2609.20891v1 Announce Type: new Abstract: Optimization methods for experimental science are often evaluated on synthetic functions that are reproducible but omit important characteristics of real experiments. We introduce RECOB (REliable Chem Optimization Benchmark, Github repository: hyperlink{https://github.com/XieZikai/RECOB}{https://github.com/XieZikai/RECOB}), a black-box optimization benchmark constructed exclusively from data generated through physical experiments in chemistry and materials science. The suite contains 14 single-objective and two multi-objective tasks spanning chemical reactions, material formulations, electrochemical systems, continuous-flow processes, and automated laboratories. Each task provides a machine-readable specification of its decision variables, feasible domain, physical constraints, objective direction, and experimental provenance. Continuously queryable learned oracles are screened using repeated holdout validation and prespecified admission criteria, while measured-table replay enables evaluation using the original experimental responses. Under a common paired evaluation protocol, we compare ten single-objective and eight multi-objective optimization methods. HEBO achieves the best aggregate single-objective rank, while qNEHVI leads the multi-objective comparison. Model-based methods generally outperform non-adaptive baselines, although their computational overhead varies substantially. We further assess benchmark reliability using independent oracle retraining and measured-table replay. Aggregate optimizer rankings remain highly consistent across retrained oracles, while replay preserves the broad performance hierarchy using only physically measured responses. Together, these results show that RECOB can reproducibly distinguish optimizer performance as an experimentally grounded and reliability-tested benchmark for black-box optimization in chemistry and materials science.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2609.20891) | 2026-09-21
