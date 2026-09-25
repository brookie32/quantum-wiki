---
title: "On the numerical limitations of dual Koopman von Neumann embeddings for solving conservative nonlinear ordinary differential equations on quantum computers"
date: "2026-09-25"
updated: "2026-09-25"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.28999"
summary: "arXiv:2609.28999v1 Announce Type: new Abstract: The simulation of nonlinear ordinary differential equations on quantum computers is inherently challenging, as quantum gates are linear operators on qub"
last_verified: "2026-09-25"
review_by: "2026-12-24"
stale: false
---

arXiv:2609.28999v1 Announce Type: new Abstract: The simulation of nonlinear ordinary differential equations on quantum computers is inherently challenging, as quantum gates are linear operators on qubit states. In this paper, we put forth a Koopman-von Neumann (KvN) operator based algorithm for solving nonlinear ordinary differential equations on a quantum computer which overcomes the innate limitations of quantum operations. In this approach, a Liouville probability density is embedded into a wavefunction, the evolution of which is governed by an operator dual to the Koopman operator. The trajectories corresponding to the nonlinear differential equations are reconstructed from the average value of Koopman observables evaluated through quantum measurements. We specifically evaluate the computational limitations of solving nonlinear equations within this Liouville embedding framework. An Ehrenfest-type estimate is derived that relates the reconstruction error to the covariance of the transported density, highlighting the competition between linear stretching and Hessian-induced folding.This leads to a key stability criterion, which depends on the local Ehrenfest-Reynolds number. We discuss the effects of measurement-induced errors including those due to Hadamard-test sampling, amplitude estimation, and bias due to covariance in probabilistic Grover-type inference on the evaluation of trajectories. The limiting bounds on the accuracy of quantum computations are numerically verified for the Lotka-Volterra system and for the quartic oscillator. We observe a rapid growth in computational errors when the Ehrenfest-Reynolds number approaches the predicted threshold. The bounds resulting from our analysis provide key guidelines for selecting the width of the initial Gaussian probability distribution associated with a system of nonlinear ordinary differential equations.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.28999) | 2026-09-25
