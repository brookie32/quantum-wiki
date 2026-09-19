---
title: "Revisiting Malicious Private Aggregation: Formalization, Weaknesses, and Enhancements"
date: "2026-09-17"
updated: "2026-09-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2074"
summary: "Private aggregation schemes enable aggregation of sensitive data across clients without leaking any individual client's input. Their applications include privacy-preserving federated learning, private"
last_verified: "2026-09-19"
review_by: "2026-12-18"
stale: false
---

Private aggregation schemes enable aggregation of sensitive data across clients without leaking any individual client's input. Their applications include privacy-preserving federated learning, private heavy hitters, and anonymous systems. Many private aggregation schemes assume two non-colluding servers and aim to guarantee privacy even when one server is malicious, i.e., the malicious server learns an aggregation result that includes all honest client inputs. However, many private aggregation schemes in the literature fail to achieve privacy, which we believe is in large part due to a lack of formalism for the nuanced variations of privacy guarantees. In this work, we present ideal functionalities for several variants of private aggregation. We also formalize a common paradigm underlying most prior private aggregation schemes. The formal treatment helps us identify security flaws or underspecifications in existing private aggregation schemes. We then present modular modifications or fill in critical details to help prior schemes in the share-aggregate paradigm securely realize the private aggregation functionalities we formally define, including in settings where clients may have unreliable networks.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2074) | 2026-09-17
