---
title: "Proper Agnostic Learning of Matrix Product States and Tree Tensor Networks"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.30148"
summary: "arXiv:2609.30148v1 Announce Type: new Abstract: We establish proper agnostic learning of matrix product states and tree tensor networks. Given copies of an arbitrary quantum state rho, our algorithms "
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.30148v1 Announce Type: new Abstract: We establish proper agnostic learning of matrix product states and tree tensor networks. Given copies of an arbitrary quantum state rho, our algorithms return a state |psirangle of chosen bond dimension such that langlepsi| rho |psirangle is within arepsilon of the optimum over the model class, without assuming that rho itself belongs to or is well approximated by that class. The main idea is to use improper learning to compress the mixed-state objective, reducing proper agnostic learning to optimization against a finite collection of explicitly specified pure states. We then introduce a comparator-dual compression procedure that reduces the bond dimension of these targets while uniformly preserving their overlaps with all bounded-bond comparators, with an error independent of system size. For matrix product states, this gives polynomial copy complexity in the system size, local dimension, bond dimension, and 1/arepsilon, together with polynomial runtime in the system size for fixed local dimension, bond dimension, and accuracy. The same framework yields proper agnostic learning of tree tensor networks on bounded-degree trees, with both copy complexity and runtime polynomial in the system size when the remaining parameters are fixed.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.30148) | 2026-09-25
