---
title: "Exact and fast series expansions for quantum models with long-range interactions"
date: "2026-09-17"
updated: "2026-09-17"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.18761"
summary: "arXiv:2609.18761v1 Announce Type: cross Abstract: Over the past decade, high-order series expansions based on linked-cluster methods have become an important tool for studying low-energy properties of"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

arXiv:2609.18761v1 Announce Type: cross Abstract: Over the past decade, high-order series expansions based on linked-cluster methods have become an important tool for studying low-energy properties of gapped quantum systems with long-range interactions. We introduce a deterministic framework that removes a central computational bottleneck of this method. Our graph zeta method replaces the costly and statistically noisy Monte Carlo (MC) evaluation of high-dimensional lattice sums by a systematic, high-precision computation that delivers series coefficients within minutes on standard desktop hardware. The full momentum-dependent series is obtained in a single calculation, enabling high-resolution excitation spectra throughout the Brillouin zone. Building on the companion paper [1], the method reformulates graph-embedding sums as graph zeta functions and decomposes them into blocks classified by their treewidth tw. Low-treewidth blocks (twleq2) admit closed expressions based on Epstein zeta functions, while higher-treewidth blocks (tw>2) are evaluated using tensor-network bucket elimination. We benchmark the approach for transverse-field Ising models with power-law interactions in 1d, 2d, and 3d, reproducing previous MC results at a fraction of the computational cost while enabling substantially denser parameter sampling. An open-source implementation makes the method directly applicable to general interactions and large parameter scans. As an application, we compare microscopic interaction models for the stacked quasi-2d transverse-field Ising triangular-lattice antiferromagnet KTmSe_2 and find that a model including dipolar interactions best describes existing experimental data. The graph zeta method thus turns high-order linked-cluster expansions into a practical and deterministic tool for fast quantitative momentum-resolved modeling of short- and long-range quantum matter.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.18761) | 2026-09-17
