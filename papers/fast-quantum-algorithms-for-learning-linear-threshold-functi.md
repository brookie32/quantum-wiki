---
title: "Fast Quantum Algorithms for Learning Linear Threshold Functions"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.40331"
summary: "arXiv:2609.40331v1 Announce Type: new Abstract: Linear threshold functions are f_{w,heta}(x)=ext{sign}(langle x,w rangle -heta), where the weight vector winR^n is a unit vector, hetainmathbb R is a th"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.40331v1 Announce Type: new Abstract: Linear threshold functions are f_{w,heta}(x)=ext{sign}(langle x,w rangle -heta), where the weight vector winR^n is a unit vector, hetainmathbb R is a threshold, and typically xinR^n or xin{-1,1}^n. When heta=0, the LTF is called homogeneous, and we write f_w:=f_{w,0}. Such functions are among the most important objects in machine learning, since they serve to linearly discriminate positive and negative examples. We give three positive results about learning LTFs: 1. Suppose we can make real-domain queries, meaning we can compute f_{w,heta}(x) at any xinR^n of our choice. We give a quantum algorithm that learns f_{w,heta} up to Euclidean error~epsilon using O(log(n/epsilon)) membership queries and widetilde{O}(n) other gates. Then we have also learned f_{w,heta} up to error O(epsilon) when x is Gaussian. Classical algorithms need Omega(nlog(1/epsilon)) queries. 2. A homogeneous LTF f_w on domain {-1,1}^n where w has only k nonzero entries of the same value, is the Majority function on the support of w. Belovs gave a bounded-error quantum algorithm that identifies the hidden support exactly (and hence learns f_w) using O(k^{1/4}) queries. We give an exponential improvement, using O(log k) queries. 3. Suppose we have a unitary U that can produce (discretized) quantum examples under Gaussian measure, corresponding to int_x sqrt{gamma_n(x)}|xrangle |f_w(x)rangle dx. This is a weaker access model than membership queries. We give a quantum algorithm based on the efficient Hermite transform of Jain et al. to learn homogeneous LTFs~f_w with error~epsilon under the Gaussian distribution, using O(n^{1/4}/sqrt{epsilon}) applications of U and U^agger and widetilde{O}(n^2/epsilon^4) other gates.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.40331) | 2026-10-01
