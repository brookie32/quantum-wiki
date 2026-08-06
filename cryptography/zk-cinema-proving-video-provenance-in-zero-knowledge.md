---
title: "zk-Cinema: Proving Video Provenance in Zero Knowledge"
date: "2026-08-04"
updated: "2026-08-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1598"
summary: "Video provenance is an important problem on the modern internet. In response, the Coalition for Content Provenance and Authenticity (C2PA) has developed a standard for verifying video and image proven"
last_verified: "2026-08-06"
review_by: "2026-11-04"
stale: false
---

Video provenance is an important problem on the modern internet. In response, the Coalition for Content Provenance and Authenticity (C2PA) has developed a standard for verifying video and image provenance where cameras sign captured videos with an on-device secret key. Since videos are generally edited and resized before be- ing posted, the C2PA signature from a camera cannot be used as is to verify provenance of published videos. Prior work has developed zero-knowledge techniques for verifying provenance of edited im- ages and videos. In this work, we develop new efficient techniques for producing such zero-knowledge proofs. First, we show how to represent common video edits as matrix multiplications in a form that is particularly friendly for zero-knowledge provers and enables a number of optimizations. Second, we develop a SNARK-friendly video representation, which we call sfvr, that reduces prover work for video editing. Third, we design new efficient methods for incor- porating signed data into a SNARK proof. To evaluate our designs, we built an end-to-end system for proving edits to a signed video. In our end-to-end system, we optimize the NeutronNova folding scheme for high-arity folding. To scale the size of our Neutron- Nova proofs, we implement a “Read-Write Streaming” version of NeutronNova to take advantage of high-performance storage and parallel computing resources. Our system achieves competitive performance and scale relative to prior work.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1598) | 2026-08-04
