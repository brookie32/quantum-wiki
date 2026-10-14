---
title: "On the Hardness of Finding Permutation Automorphisms of Linear Codes"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2476"
summary: "We study the hardness of finding permutation automorphisms of linear codes. We look into three main problems: mathsf{AUT}, mathsf{AUT}-mathsf{Gen} and mathsf{AUT}-mathsf{Count} which, respectively, as"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

We study the hardness of finding permutation automorphisms of linear codes. We look into three main problems: mathsf{AUT}, mathsf{AUT}-mathsf{Gen} and mathsf{AUT}-mathsf{Count} which, respectively, ask to find a non-trivial automorphism, a generating set and the order of the automorphism group. We give polynomial time reductions from mathsf{AUT} to mathsf{ISO} (the problem of finding a permutation isomorphism between two linear codes), and from mathsf{ISO} to mathsf{AUT}-mathsf{Gen} and mathsf{AUT}-mathsf{Count}. This shows that mathsf{AUT}-mathsf{Gen} and mathsf{AUT}-mathsf{Count} are unlikely to be easy in the worst case, since all known solvers for mathsf{ISO} take exponential time if the hull dimension (the subspace given by the intersection between the code and its dual) is large enough. Furthermore, we give a reduction from mathsf{AUT}-mathsf{Gen} to the problem of finding generators for the automorphism group of a graph, which we refer to as mathsf{GraphAUT}-mathsf{Gen}. Up to some polynomial factors, the reduction runs in time O(n^{h}), with n being the code length and h the hull dimension: for h = Oig(log(n)ig), this implies that mathsf{AUT}-mathsf{Gen} can be solved in worst case quasi-polynomial time. We also give a simpler version of the reduction, running in time which is exponential in the worst case (arguably, only for rather contrived codes), even for small h. However, heuristically, the algorithm is on average extremely efficient for small h. We use it as a concrete solver and show that a proof-of-concept implementation is significantly faster than the built-in implementations of Leon's and Feulner's algorithms provided by exttt{Magma} and exttt{Sagemath}.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2476) | 2026-10-14
