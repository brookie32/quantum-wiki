---
title: "Chosen Commitments and Certified Decoding Regions in the Adaptive Threshold Schnorr Attack"
date: "2026-10-24"
updated: "2026-10-26"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2632"
summary: "Crites and Stewart reduce an adaptive forgery attack on threshold Schnorr signatures with N parties and threshold au to one call to a sparse linear search oracle, which they show to be bounded distanc"
last_verified: "2026-10-26"
review_by: "2027-01-24"
stale: false
---

Crites and Stewart reduce an adaptive forgery attack on threshold Schnorr signatures with N parties and threshold au to one call to a sparse linear search oracle, which they show to be bounded distance decoding of a diagonally scaled Reed–Solomon code and whose sparse answer, a witness, names the parties to corrupt. Their analysis samples the coefficient vector behind the adversary's commitment uniformly at random and leaves open whether a chosen vector does better. We bound the success of an adversary that follows their template with a chosen vector and recovers witnesses only inside regions built from the radii that seven decoding theorems, three for Reed–Solomon and four for folded Reed–Solomon codes, certify under their own setup hypotheses. When the commitment is fixed through a known coefficient vector before a fresh hash challenge, the attack target is, conditional on the history that fixed the vector, a uniform point of a line. For distinct nonzero Shamir points, our main theorem shows that every such line contains at most M targets with a witness in a finite collection of coordinate and block weight regions fixed before the targets, each permitting fewer than au nonzero coordinates, for an explicit integer M depending only on N, au and the collection. We call the adversary the wrapper when it makes at most Q fresh challenges and no signing query, chooses each coefficient vector from its history before the challenge and keeps it afterwards, and lets its solvers make no further signature hash queries. It accepts only a witness of the same target and representation that lies in the regions of the collection within its corruption cap, corrupts parties only once it holds such a witness, and then forges from that witness and stops. Hence the wrapper succeeds with probability at most QM/p, with p the group order, even if its solvers recover every witness in the regions at no cost. On the six pairs (N,au) of the original attack, fixed collections built from partitions into consecutive blocks contain all seven certified regions and have M below 2^{24}, so at the field size proxy p = 2^{252} the bound stays below 2^{-100} after 2^{128} challenges. For uniform targets we prove much smaller bounds on the witness probability in these regions. For the folded Guruswami–Wang and Ashvinkumar–Habib–Srivastava block regions on partitions into consecutive blocks fixed before the target, this probability is negligible for polynomially many parties, exponentially large fields and au/N bounded away from zero. These results also classify the studied decoder theorems. The hardness of the oracle, the success of other strategies and the adaptive security of threshold Schnorr schemes are open.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2632) | 2026-10-24
