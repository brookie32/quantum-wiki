---
title: "Optimal Distributed Similarity Estimation of Quantum Channels"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "networking"
tags: [networking, arxiv-quant-ph]
url: "https://arxiv.org/abs/2512.10465"
summary: "arXiv:2512.10465v5 Announce Type: replace Abstract: We study the query complexity of estimating the similarity of two unknown quantum channels available at separated devices. For channels E and F on a"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2512.10465v5 Announce Type: replace Abstract: We study the query complexity of estimating the similarity of two unknown quantum channels available at separated devices. For channels E and F on a d-dimensional system, the target functional is the normalized Choi overlap {rm Tr}[J_{E} J_{F}]/d^2, where J_{E} and J_{F} are unnormalized Choi operators. We call this task distributed similarity estimation of quantum channels (DSEC). Our main result is a tight characterization: estimating this overlap to additive error arepsilon with constant success probability requires and is achievable with egin{align*} Theta!left(maxleft{frac{sqrt d}{arepsilon},frac{1}{arepsilon^2}right}right) end{align*} queries to each channel. The lower bound holds even for the most general model considered here, allowing arbitrary ancillas, coherent adaptive access, quantum memory within each laboratory, and multi-round classical communication. The dimension-dependent term follows from a shared-versus-independent Haar-unitary testing problem, while the arepsilon-dependence is obtained through a random-phase channel construction. Conversely, we give a non-adaptive, ancilla-free, incoherent randomized-measurement protocol for arbitrary channels that attains the same scaling. The protocol uses only shared classical randomness to coordinate local state preparations and measurement bases. For unitary channels, our protocol reduces the dimension-dependent upper bound from d/arepsilon for independent coherent shadows to sqrt d/arepsilon. These results identify the optimal information-theoretic cost of distributed Choi overlap estimation and clarify the role of public classical randomness in distributed quantum channel learning.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2512.10465) | 2026-11-06
