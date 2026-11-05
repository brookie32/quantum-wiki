---
title: "Affine Advantage in Guess-type Attacks on Goldreich’s PRGs: Generalization, Characterization and Countermeasures"
date: "2026-11-04"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2757"
summary: "The recent guess-type attack (Eurocrypt'26) on Goldreich's pseudorandom generators exploits the strong bias toward constants that can arise when some inputs of majority-based predicates are fixed. Thi"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

The recent guess-type attack (Eurocrypt'26) on Goldreich's pseudorandom generators exploits the strong bias toward constants that can arise when some inputs of majority-based predicates are fixed. This attack has demonstrated substantial effectiveness against several concrete parameter instances (Eurocrypt'24&'25, Asiacrypt'24). In this paper, we generalize this attack paradigm to arbitrary affine approximations, characterize its capabilities, and develop a new predicate as a countermeasure. We introduce a guess-and-affine-approximation (GAA) attack framework that generalizes existing guess-type attacks from constant approximations to arbitrary affine approximations of residual nonlinear predicates. To characterize the capacity of GAA attack, we introduce the bit-fixing affine advantage operatorname{adv}_{b'}(M_b), defined as the maximum affine advantage of a b-ary nonlinear predicate M_b over all residuals with b' unfixed inputs. For polynomial stretch m=n^s and logarithmic nonlinear arity b=gammalog_2 n, we obtain the optimal attack complexities C^star linking bit-fixing affine advantages: (1) C^star>2^{cn} for every c<2^{-(s-1)/gamma} iff operatorname{adv}_{heta b}(M_b)o 0 for every constant hetain(0,1]; (2) C^star=2^{o(n)} iff fixing only o(b) predicate inputs can yield a residual with affine advantage frac{1}{2}-o(1), and the sufficient direction also holds for b=Omega(log n). In particular, if operatorname{adv}_{b-r}(M_b) =frac12- Oleft(frac{log n}{n}right) for rle s-1, then C^star can further decrease to n^{O(1)}. These results complement prior analyses for arities O(1), omega(1)ap O(log n), and Omega(n^{1/s}). Guided by the results above, we introduce the XOR_a--MODtwelve_b family as a predicate candidate. We prove that every b'-input residual of its nonlinear component retains algebraic degree and algebraic immunity Theta(b'), matching the asymptotic orders of MAJ (STOC'16). Moreover, its bit-fixing affine advantage is at most 2^{-Omega(b')}, whereas operatorname{adv}_{heta b}(MAJ_b)approx frac12 for every fixed hetain(0,1). Analysis shows that, for n=1024, m=n^2, and b=54, XOR--MODtwelve can achieve log C^star approx 737, while XOR--MAJ and XOR--MODthree have cost exponents of only 182 and 599, respectively, under the specified attack. Furthermore, our experiments show that MODtwelve offers stronger resistance to belief-propagation-based attacks.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2757) | 2026-11-04
