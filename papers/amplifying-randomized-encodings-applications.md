---
title: "Amplifying Randomized Encodings & Applications"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2505.21442"
summary: "arXiv:2505.21442v3 Announce Type: replace-cross Abstract: A randomized encoding for a promise problem is a randomized reduction whose outcome distribution on input x can be simulated within some dista"
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2505.21442v3 Announce Type: replace-cross Abstract: A randomized encoding for a promise problem is a randomized reduction whose outcome distribution on input x can be simulated within some distance d, called privacy, using only one bit of information about x: whether it is a YES or NO instance. The encoding is one-sided if this holds only for YES instances. Our main contribution is showing that (classical and quantum) one-sided randomized encodings have privacy and correctness amplification: any problem with an encoding with privacy 1-1/poly(n) and error 1/2-1/poly(n) also has one with negligible privacy and error. We use this result to show: - NISZK, the class of problems with non-interactive (statistical) zero-knowledge proofs, has strong zero-knowledge amplification: every problem with such a proof with zero-knowledge error 1-1/poly(n) also has one with negligible zero-knowledge error. This solves a problem open since Goldreich, Sahai, and Vadhan (CRYPTO '99). - The worst-case hardness of a problem with a perfect (zero-error) one-sided encoding implies one-way functions (OWFs), and, if the encoding is quantum, one-way state generators (OWSGs). We then conclude that removing the error from one-sided randomized encodings would make the worst-case hardness of SZK sufficient for OWFs. - Weak and imperfect indistinguishability obfuscation (iO) implies OWFs assuming the Polynomial Hierarchy does not collapse to its third level. Here, weak means the computational distance between the obfuscated and original circuits is 1-1/poly(n), and imperfect means the error is 1/2-1/poly(n). To achieve this amplification, we study randomized encodings through the lens of lossy reductions (Ball et al. ITCS 2020): we introduce an extended, flexible notion of lossy reductions and show it is equivalent to randomized encodings. This equivalence underlies our main results and may be of independent interest.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2505.21442) | 2026-09-23
