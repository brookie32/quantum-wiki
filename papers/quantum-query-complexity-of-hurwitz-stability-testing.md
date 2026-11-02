---
title: "Quantum query complexity of Hurwitz stability testing"
date: "2026-11-02"
updated: "2026-11-02"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.41180"
summary: "arXiv:2610.41180v1 Announce Type: new Abstract: Determining whether every trajectory of the linear system ot{x}=Ax converges to zero (or, equivalently, whether A is Hurwitz stable) is a fundamental pr"
last_verified: "2026-11-02"
review_by: "2027-01-31"
stale: false
---

arXiv:2610.41180v1 Announce Type: new Abstract: Determining whether every trajectory of the linear system ot{x}=Ax converges to zero (or, equivalently, whether A is Hurwitz stable) is a fundamental problem in control theory. It arises, for example, in verifying the stability of feedback controllers and state observers, as well as of linearized dynamical models. We study the quantum query complexity of deciding whether a matrix AinC^{nimes n} is Hurwitz stable, given an exact normalized block-encoding of A. The query complexity is characterized in terms of the system dimension n and a supplied lower bound 0<nuleq omega_A on the imaginary-axis distance omega_A:=min_{tinR}sigma_{min}(A-itI), where sigma_{min}(A) is the smallest singular value of A. We prove a query-complexity lower bound of Omega(sqrt{n}/nu), which holds even when A is restricted to be real and diagonal. For general matrices with nonzero omega_A, we encode an approximation of the right-half-plane spectral projector operatorname{sign}^+(A):=(I+operatorname{sign}(A))/2 as a block of a matrix inverse, where A is Hurwitz if and only if the projector is zero. To test this, we produce a quantum algorithm which determines if a (eta,b,1/(4sqrt{n}))-block-encoded projector matrix (like operatorname{sign}^+(A)) is zero or not; for constant success probability, it has complexity Theta(etasqrt{n}). When the zero test is applied to specific approximations of operatorname{sign}^+(A), this yields an upper bound of O(sqrt{n}nu^{-2}log(sqrt{n}/nu)) queries in the general case, and O(sqrt{n}nu^{-1}log n) when A is Hermitian or normal. The latter upper bound matches the lower bound up to a logarithmic factor. Thus the dimension dependence of quantum Hurwitz testing is nearly optimal, while the remaining factor in the non-normal case isolates an open conditioning gap.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.41180) | 2026-11-02
