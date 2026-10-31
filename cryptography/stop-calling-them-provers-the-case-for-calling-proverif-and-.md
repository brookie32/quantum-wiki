---
title: "Stop Calling Them Provers: The Case for Calling ProVerif and Tamarin Symbolic Protocol Analyzers"
date: "2026-10-29"
updated: "2026-10-31"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2683"
summary: "A claim that a cryptographic protocol has been proved secure depends on the theory, the analysis software, the protocol model, and the security property being checked. I examine each of these for ProV"
last_verified: "2026-10-31"
review_by: "2027-01-29"
stale: false
---

A claim that a cryptographic protocol has been proved secure depends on the theory, the analysis software, the protocol model, and the security property being checked. I examine each of these for ProVerif and Tamarin. An audit of their published soundness arguments finds false statements, missing proofs, and gaps between the procedures justified on paper and those the tools run. I also reproduce previously reported bugs that cause Tamarin to accept false claims about the submitted models. ProVerif supplies no certificate for its full analysis, while Tamarin replays its proof tree with its own solver, leaving the correctness of that code to be trusted. A correct symbolic result can still fall short of the security claim made for a protocol. Models can omit behavior in parsers and state machines; secrecy queries can allow information to leak; and equations for cryptographic primitives need justification before they support computational guarantees. Better models, stronger queries and computational soundness arguments can address these problems, but someone must establish that they apply to the protocol at hand. For these reasons and more, I argue that calling ProVerif and Tamarin "provers" is misleading: we should call them symbolic protocol analyzers and report their results with the models, assumptions and evidence that support them. They remain useful for finding attacks and establishing symbolic properties, including for unbounded sessions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2683) | 2026-10-29
