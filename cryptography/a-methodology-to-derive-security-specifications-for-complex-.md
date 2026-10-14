---
title: "A methodology to derive security specifications for complex electronic systems"
date: "2026-10-12"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2447"
summary: "Modern electronic systems are becoming increas- ingly complex and must satisfy demanding performance, power, and area (PPA) constraints. Consider for instance artificial intelligence chips, aiming at "
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

Modern electronic systems are becoming increas- ingly complex and must satisfy demanding performance, power, and area (PPA) constraints. Consider for instance artificial intelligence chips, aiming at datacenters running LLMs or at automotive perception, which manipulate massive data streams. Beyond performance considerations, these systems must also provide increasingly strong security and dependability guaran- tees. Indeed, when electronic systems are based on chiplets, for instance, the supply chain gets longer and therefore brings a larger number of threats. Also, those systems are very versatile, in that they can run varied multi-tenant applications. Therefore, defining what security features are required in this context with numerous stakes is not trivial. Existing scholarly research is very relevant when the security problem is well defined. The resulting scientific papers accord- ingly dig very deep: this modus operandi has proved productive in exploring new problems, and actually allowed to come up with innovative solutions. For instance, in the field of side-channel attacks, varied mitigations alongside with metrics to evaluate them have been devised. Increasing sophistication resulted from this research, as external considerations have been injected into the problem (typically, aspects such as attack order, impact of combinatorial glitches, etc.). Therefore, we face today the question of selecting the most suitable technology amongst the proliferation of state-of-the-art techniques. In addition, in complex systems, we encounter another prob- lem, namely that of defining the security problem(s). A fruitful approach in this respect is a risk based approach. Specifically, the application of a risk-oriented methodology allows to reason on the security rationale. It proceeds as follows. First, the system missions are listed. Then for each of them, the necessary assets are deduced. A threat analysis allows to identify how assets are threatened, and eventually, security requirements can be enunciated. At this stage, the task of matching relevant countermeasures becomes straightforward. This paper illustrates the methodology by deriving security specifications for datacenter and automotive chiplets. The considered missions are (secure) provisioning, trimming, debugging, booting, and remote attestation.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2447) | 2026-10-12
