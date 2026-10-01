---
title: "Parallel classical simulation of noisy shallow circuits: no quantum advantage in 1D"
date: "2026-10-01"
updated: "2026-10-01"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.39448"
summary: "arXiv:2609.39448v1 Announce Type: new Abstract: We consider quantum circuits consisting of d layers of nearest-neighbor two-qubit gates acting on n qubits arranged on a line, where every qubit is inde"
last_verified: "2026-10-01"
review_by: "2026-12-30"
stale: false
---

arXiv:2609.39448v1 Announce Type: new Abstract: We consider quantum circuits consisting of d layers of nearest-neighbor two-qubit gates acting on n qubits arranged on a line, where every qubit is independently depolarized with a constant probability before each layer. We describe a randomized parallel algorithm which samples from the output distribution of any such circuit to within total variation error elta, with parallel runtime 2^{O(d)}loglog(n/elta) and n 2^{O(d)} elementary real-arithmetic operations. Without noise, the same approach gives an exact sampler with parallel runtime O(log n). For constant depth, we further show that the input/output behavior of the noisy quantum circuit is reproduced up to a constant error by a randomized mathsf{AC}^0-circuit, that is, a Boolean circuit of polynomial size and constant depth with unbounded fan-in AND and OR gates and NOT gates. Consequently, every relation problem solved by a noisy constant-depth quantum circuit in one dimension is also solved, with essentially the same success probability, by a randomized mathsf{AC}^0-circuit. This rules out, for noisy circuits in one dimension, the unconditional quantum advantage established for noisy shallow circuits in two and three dimensions, where polynomial-size classical circuits over the same gate set require depth Omega(log n/loglog n). Our algorithm exploits the fact that depolarizing noise cuts a one-dimensional circuit into independent pieces of logarithmic width, each of which can be sampled exactly in parallel.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.39448) | 2026-10-01
