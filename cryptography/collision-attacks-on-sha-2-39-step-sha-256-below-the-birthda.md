---
title: "Collision Attacks on SHA-2: 39-Step SHA-256 below the Birthday Bound"
date: "2026-11-11"
updated: "2026-11-13"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2867"
summary: "SHA-2 is the most widely deployed family of hash functions, and its security margin is measured by the number of steps collision attacks reach. Li et al. gave the first classical collision attack on 3"
last_verified: "2026-11-13"
review_by: "2027-02-11"
stale: false
---

SHA-2 is the most widely deployed family of hash functions, and its security margin is measured by the number of steps collision attacks reach. Li et al. gave the first classical collision attack on 38-step SHA-256, with an estimated complexity of 2^{104.3}. The challenge is to extend the attack to more steps while retaining its advantage over generic collision search. In this paper, we show that collisions for 39-step SHA-256 can be found at an estimated cost below the 2^{128} birthday bound. We keep the published 39-step characteristic and change how its conditions are satisfied. We introduce joint message-word pinning, a technique that fixes two expanded message words, W_{16} and W_{17}, to the values prescribed by the characteristic. For each chaining value, we solve for assignments to two state words that carry no direct condition, and every assignment returned gives both message words their prescribed values. To find these assignments, we first fix the value of a function with a small image and then solve the coupled equations for W_{16} and W_{17} in sequence. On 39-step SHA-256, pinning W_{16} alone gives an estimated cost of 2^{123.4} scalar compressions per expected collision, and pinning both words reduces it by 14.6 bits to 2^{108.8}. Under the uniform-chaining-value model, the measured probabilities and the cost of processing one first block give an upper bound of approximately 2^{124.6} on the expected cost of finding the first collision, even under worst-case clustering. For 38-step SHA-256, we reduce the estimated cost per expected collision from 2^{104.3} to 2^{90.9} by using a new differential characteristic and pinning W_{16} alone. On SHA-512, pinning W_{16} alone reduces this cost from 2^{125.4} to 2^{100.7} for 38 steps and from 2^{178} to 2^{131.3} for 39 steps.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2867) | 2026-11-11
