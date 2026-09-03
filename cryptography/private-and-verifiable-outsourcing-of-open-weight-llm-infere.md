---
title: "Private and Verifiable Outsourcing of Open-Weight LLM Inference"
date: "2026-08-31"
updated: "2026-09-03"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1849"
summary: "Open-weight models allow clients to run LLMs locally, thus keeping their data private from untrusted providers. However, running large models requires massive hardware and storage resources (especiall"
last_verified: "2026-09-03"
review_by: "2026-12-02"
stale: false
---

Open-weight models allow clients to run LLMs locally, thus keeping their data private from untrusted providers. However, running large models requires massive hardware and storage resources (especially challenging on resource-constrained devices like smartphones), limiting local execution to smaller models. This leaves clients with a frustrating compromise: settle for a less-capable model that can be run locally, or sacrifice privacy by sending queries to an external server. We present an efficient protocol that allows a client to privately and verifiably outsource LLM inference of an open-weight model to a pair of malicious (but non-colluding) servers. Privacy implies that neither server learns anything about the client's queries. At the same time, the client can verify the claimed result using information posted by the model owner along with the model weights. Compared to prior state-of-the-art for private LLM inference (SIGMA, PETS' 24) -- which does not provide verifiability -- our protocol is approx11--14imes faster while imposing no overhead at the servers (beyond the cost of inference in the original model). Our protocol also scales to larger models not supported by prior work: for example, with our protocol a client can run the Llama 2-70B model using just 179~MB of local storage (instead of the 140~GB required to run the model locally).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1849) | 2026-08-31
