---
title: "Privacy-Preserving Counterfactual Explanations for Federated AI"
date: "2026-07-21"
updated: "2026-07-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1488"
summary: "As the usage of Artificial Intelligence (AI) for sensitive purposes increases, there is a growing need for privacy-aware explainable AI (XAI) tools. In this paper, we present a privacy-preserving coun"
last_verified: "2026-07-24"
review_by: "2026-10-22"
stale: false
---

As the usage of Artificial Intelligence (AI) for sensitive purposes increases, there is a growing need for privacy-aware explainable AI (XAI) tools. In this paper, we present a privacy-preserving counterfactual explanation algorithm. Our starting point is a decision-support model that is able to operate on vertically partitioned datasets, meaning that each party holds a different subset of datapoint attributes. The goal of a counterfactual algorithm is to find, given an observation, a datapoint from the (virtual) dataset that is closest to the observation but has a different label. Our algorithm fully preserves the privacy of the n datapoints belonging to the different parties by combining the strengths of homomorphic encryption and secret sharing. Through a number of experiments, we demonstrate the added value of combining multiple datasets in a realistic scenario and show that the privacy-preserving solution does not affect the accuracy. We fully implement our solution and demonstrate that it scales as to thousands of datapoints.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1488) | 2026-07-21
