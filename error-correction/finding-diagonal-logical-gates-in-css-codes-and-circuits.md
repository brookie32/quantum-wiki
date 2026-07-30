---
title: "Finding diagonal logical gates in CSS codes and circuits"
date: "2026-07-30"
updated: "2026-07-30"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2607.26477"
summary: "arXiv:2607.26477v1 Announce Type: new Abstract: Finding efficient schemes for non-Clifford logic or magic state preparation is one of the central challenges on the way to fault-tolerant quantum comput"
last_verified: "2026-07-30"
review_by: "2026-10-28"
stale: false
---

arXiv:2607.26477v1 Announce Type: new Abstract: Finding efficient schemes for non-Clifford logic or magic state preparation is one of the central challenges on the way to fault-tolerant quantum computation. Many of the proposed schemes rely on diagonal non-Clifford logical gates acting on CSS codes in space or decorating CSS-type syndrome-extraction circuits in spacetime. Here we propose and implement efficient algorithms to find all (spacetime) logical gates of a given CSS code (circuit) composed from a prescribed set of ansatz gates. Depending on the choice of ansatz gates, this means finding transversal gates, more general locality-preserving logical circuits, folding gates, or similar. While we focus on qubit diagonal gates in the Clifford hierarchy, we also discuss the generalization to arbitrary diagonal non-hierarchy gates, certain non-diagonal gates, as well as prime and composite-dimensional qudits. Our method works by rephrasing code-space preserving gates as the kernel of the ``pullback'' of the X check matrix onto phase functions, which maps between finite abelian 2-groups. We implement a fast ``filtration'' method to find this kernel. The runtime for finding fault-tolerant logical gates in a qLDPC code with O(n) qubits or a circuit with O(n) gates in a naive dense implementation is O(n^3), with potential for improvement making use of sparsity.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2607.26477) | 2026-07-30
