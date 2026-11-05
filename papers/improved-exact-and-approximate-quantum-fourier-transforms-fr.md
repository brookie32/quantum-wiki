---
title: "Improved Exact and Approximate Quantum Fourier Transforms from Multiplication"
date: "2026-11-05"
updated: "2026-11-05"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.06341"
summary: "arXiv:2611.06341v1 Announce Type: new Abstract: In the world of quantum computing, quantum Fourier transform (QFT) has been one of the most important subroutines for quantum algorithms, as exemplified"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

arXiv:2611.06341v1 Announce Type: new Abstract: In the world of quantum computing, quantum Fourier transform (QFT) has been one of the most important subroutines for quantum algorithms, as exemplified by Shor's factoring algorithms and phase estimation (which in itself has been used as a primitive in various quantum algorithms). In fact most of the well known quantum algorithms can be divided into two classes, QFT based algorithms and search based algorithms. The usual circuit for QFT (covered in almost every basic quantum algorithms course) needs O(q^2) gates (and O(q) qubits) to perform the exact Fourier transform over F_{2^q}. Cleve and Watrous (FOCS 2000) improved this gate count to O(q (log q)^2 (log log q)) using the integer multiplication algorithm in O(n (log n) (log log n)) time for two n-bit integers (best known at that time). Our first main result shows that this gate count can be improved to O(q (log q)). In fact, if there is a multiplication circuit, to multiply two n-bit integers, with O(n (log n)^{alpha}) gates; we get a QFT circuit with O(q (log q)^{alpha}) gates (improving upon O(q (log q)^{alpha + 1})) gates from the construction of Cleve and Watrous). Given the recent claim by OpenAI about integer multiplication, this opens up the possibility of having a QFT circuit with o left( q (log q)right) gates. On approximating the QFT over ZZ/(2^q ZZ), the result of Ahokas, Cleve and Hales (ERATO 2003) showed that an approximating circuit can be built with O left( q (log log(q/arepsilon))^{alpha+1} right) gates, where epsilon is the approximating parameter. Our second main result again improves this to O left( q (log log(q/arepsilon))^{alpha} right) gates.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.06341) | 2026-11-05
