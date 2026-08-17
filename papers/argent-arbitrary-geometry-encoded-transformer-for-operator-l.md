---
title: "ArGEnT: Arbitrary Geometry-encoded Transformer for Operator Learning"
date: "2026-08-17"
updated: "2026-08-17"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2602.11626"
summary: "arXiv:2602.11626v3 Announce Type: replace-cross Abstract: Learning solution operators on arbitrary geometries remains a central challenge in scientific machine learning, especially for many-query simu"
last_verified: "2026-08-17"
review_by: "2026-11-15"
stale: false
---

arXiv:2602.11626v3 Announce Type: replace-cross Abstract: Learning solution operators on arbitrary geometries remains a central challenge in scientific machine learning, especially for many-query simulation, physics-informed learning, and evolving geometries requiring accurate, geometry-aware predictions at arbitrary spatial locations. Existing operator-learning methods often rely on structured discretizations, explicit geometry parameterizations, or point-cloud formulations that couple geometric representation with solution-query sampling, limiting flexibility on irregular and non-parameterized domains. We propose the Arbitrary Geometry-encoded Transformer (ArGEnT), a geometry-conditioned attention framework that decouples geometry encoding from query-point evaluation. We develop three variants: self-attention, cross-attention, and hybrid-attention. ArGEnT can be used independently or integrated with neural operators to incorporate non-geometric physical inputs. In the cross-attention variant, geometry is represented by an independently sampled point cloud used to construct keys and values, while arbitrary solution-query points construct queries. This design enables mesh-independent field prediction, reduces sensitivity to query-point distribution, and allows compact geometric representations to condition large-scale solution evaluations. Across benchmarks in fluid dynamics, solid mechanics, and electrochemical systems, ArGEnT consistently improves accuracy and generalization over standard DeepONet, point-cloud-based operator learning, and geometry-aware transformer baselines. In several cases, it reduces prediction errors by more than an order of magnitude while requiring substantially lower training cost than transformer-based baselines. These results demonstrate that decoupled geometry-query attention provides an accurate, scalable, and flexible framework for operator learning on arbitrary geometries.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2602.11626) | 2026-08-17
