---
title: "Hiding Capabilities in AI Models"
date: "2026-10-27"
updated: "2026-10-27"
source: "agent"
category: "cryptography"
tags: [cryptography, schneier-on-security]
url: "https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html"
summary: "Interesting research: “AI Models Can Provably Hide Arbitrary Capabilities” Abstract: Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on"
last_verified: "2026-10-27"
review_by: "2027-01-25"
stale: false
---

Interesting research: “AI Models Can Provably Hide Arbitrary Capabilities” Abstract: Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under cryptographic assumptions, even given full access to model weights, extending prior work from hiding fixed strings to arbitrary computations. We implement our proof of concept constructions in PyTorch and evaluate elicitation through fine-tuning, weight noising, gradient-based trigger search, and latent adversarial training, using a small chemical reaction prediction task as a proxy for CBRN-relevant capabilities. Our results demonstrate resistance to these methods and, together with our cryptographic guarantees, reveal a limit of elicitation-based capability audits. We release our models to support the improvement of defenses...

**Source:** [Schneier on Security](https://www.schneier.com/blog/archives/2026/10/hiding-capabilities-in-ai-models.html) | 2026-10-27
