---
title: "MPCTM: MPC-Based Trajectory Matching on Unmanned Autonomous Systems"
date: "2026-11-09"
updated: "2026-11-11"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2840"
summary: "Emerging technologies such as Unmanned Autonomous Systems (UASs) are increasingly being deployed across several application domains. Their deployment, however, introduces safety risks, especially when"
last_verified: "2026-11-11"
review_by: "2027-02-09"
stale: false
---

Emerging technologies such as Unmanned Autonomous Systems (UASs) are increasingly being deployed across several application domains. Their deployment, however, introduces safety risks, especially when unmanned vehicles operate in shared operational spaces (e.g., air, land, or maritime) and may follow collision-prone paths. This creates the need for solutions that can detect possible collisions among pre-planned trajectories, thereby improving operational safety and reducing risk. At the same time, revealing trajectories in plaintext leaks sensitive information, such as traversal patterns, deployment and infrastructure locations, and potentially private user data. In this paper, we present a privacy-preserving trajectory matching protocol based on Multi-Party Computation (MPC). We introduce an end-to-end secure scheme for collision detection that reveals no information beyond the prescribed output. Our solution models the behaviour of UASs along their paths, accurately capturing collisions that may occur between discretely sampled points. We further propose a lightweight, MPC-friendly model and discuss the trade-off between accuracy and efficiency for the two approaches. We provide a proof-of-concept implementation of our scheme and compare it to the closest state-of-the-art solution. Our evaluation shows that our work MPCTM, in the dealer mode, improves the online latency upon previous work by over 2x in our modelled protocol and by 8x in our lightweight protocol. In autonomous mode, our protocol results in a slow-down of 2.5-3x, while providing a more expressive model with no false negatives and fully preserving privacy of the trajectory data.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2840) | 2026-11-09
