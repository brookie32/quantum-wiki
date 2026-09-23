---
title: "A Syndrome-Extraction Framework for Distributed Lattice Surgery on Arbitrary Rotated Surface-Code Layouts"
date: "2026-09-23"
updated: "2026-09-23"
source: "agent"
category: "error-correction"
tags: [error-correction, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.26736"
summary: "arXiv:2609.26736v1 Announce Type: new Abstract: Modular quantum computing is a leading candidate for scalable fault tolerant quantum computation. Performing lattice surgery using surface code patches "
last_verified: "2026-09-23"
review_by: "2026-12-22"
stale: false
---

arXiv:2609.26736v1 Announce Type: new Abstract: Modular quantum computing is a leading candidate for scalable fault tolerant quantum computation. Performing lattice surgery using surface code patches in different modules requires the use of inter-module gates that are noisier than the local gates. Furthermore, the merged layouts during lattice surgery expose multiple directions in which hook errors can propagate to reduce the fault distance. Existing hook-avoiding schedules either increase the syndrome extraction circuit depth, or let link faults propagate into the bulk. We introduce a seam construction that allows splitting arbitrary merged rotated surface code layout into smaller patches with uniform boundaries that could keep their own hook-avoiding N/Z shaped schedule. At the seam we split weight-4 stabilizers into pairs of weight-2 stabilizers that are mediated through a Bell pair and measured within a CNOT depth of 4. We also employ the use of three-qubit exttt{CXX} gates for parity measurements at the seam to maintain the minimum CNOT depth. Through this seam construction, we confine the elevated link error at the seam, protecting the bulk from higher error rate. We also give a custom detector annotator for such seams that can find the detector space, annotate detectors in the Stim circuits, and ensure that they are suitable to use by matching decoders. We implement our construction for the logical Pauli-XX measurement lattice surgery and a cross-shaped spatial junction and sweep the link error rate from 10 times to 100 times a fixed bulk error rate, and show that our construction gives the lowest and most stable logical error rate than the other frameworks compared here.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.26736) | 2026-09-23
