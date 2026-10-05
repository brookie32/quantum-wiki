---
title: "Explicit Nonlinear Functions beyond the Fourier bound"
date: "2026-10-03"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2320"
summary: "We study the problem of constructing highly nonlinear vectorial maps F: F_2^n o F_2^m. Concretely, we want an F and an A = A(m,n)>0 as small as possible, so that for every affine map L: F_2^n o F_2^m "
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

We study the problem of constructing highly nonlinear vectorial maps F: F_2^n o F_2^m. Concretely, we want an F and an A = A(m,n)>0 as small as possible, so that for every affine map L: F_2^n o F_2^m (of the form L(x) = Mx + b) we have: $ operatorname{agree}(F,L) := |{x in F_2^n mid F(x) = L(x)}| leq A. Such questions have been studied by Nyberg [1991, 1993], Carlet and Ding [2004, 2007], Liu, Mesnager and Chen [2017], Nagy [2025], and Biryukov, Turecek, and Udovenko [2026]. There is a classical method of constructing such functions from bent-functions and Fourier analytic ideas; the best bound achievable by this method is: A(m,n) = Theta(2^{n-m} + 2^{n/2}), and in particular, is never smaller than 2^{n/2}. In this work, we show how to construct highly nonlinear functions beyond this Fourier bound. Concretely, we show how to construct for every gamma>0, a function F: F_2^n o F_2^m with m = O_{gamma}(n), achieving A(m,n) leq (1+gamma)^n. Surprisingly, we even achieve the same quantitative behavior for the much harder question of having low agreement with m-tuples of degree d polynomials Q: F_2^n o F_2^m, with m = O_{gamma,d}(n). Here the previously best bounds were of the form A(m,n) = O(2^{-frac{n}{2^{d+1}}} dot 2^n) of Ben-Sasson and Kopparty [Kopparty's thesis, 2010], based on Gowers-norm-type arguments. All our results generalize to all finite fields F_q in place of F_2$. Our methods are based on a new connection to classical results on counting solutions to systems of polynomial equations via algebraic methods. This connection brings us to basic questions in combinatorics, about graphs and hypergraphs with simultaneously a small number of edges and independent sets.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2320) | 2026-10-03
