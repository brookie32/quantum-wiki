---
title: "Sybil-Proofness of Generalized Adaptive Clinching and Implications for Blockchain Mechanism Design"
date: "2026-10-29"
updated: "2026-10-31"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2674"
summary: "The adaptive clinching auction of Dobzinski, Lavi, and Nisan (FOCS'08) is a cornerstone of mechanism design with budget-constrained bidders, and it has since inspired a broad range of extensions to su"
last_verified: "2026-10-31"
review_by: "2027-01-29"
stale: false
---

The adaptive clinching auction of Dobzinski, Lavi, and Nisan (FOCS'08) is a cornerstone of mechanism design with budget-constrained bidders, and it has since inspired a broad range of extensions to substantially richer market settings. Adaptive clinching enjoys compelling guarantees: it is Pareto optimal, and truthful bidding is a dominant strategy whenever budgets cannot be overreported. In many real-world environments, however, identities are cheap to create, making resilience to Sybil attacks an additional requirement. Whether the guarantees of adaptive clinching survive when a bidder can split its budget across fake identities has remained open. We introduce a generalized framework for adaptive clinching and prove that it satisfies Sybil-robust incentive compatibility: a bidder cannot benefit from splitting into any finite number of identities with arbitrary value reports, provided their aggregate reported budget does not exceed the bidder's enforceable true budget. Sybil resilience thus joins the list of ideal properties of adaptive clinching. Our work is motivated by practical mechanism-design problems in blockchain-based decentralized finance, where two-asset automated market makers (AMMs) are among the most widely used applications. We design a new AMM adaptive clinching mechanism that extends classical adaptive clinching in two ways: it supports a two-sided market and protects against two-sided strategies, and it allows the supply function to depend on the auction state. Its one-sided special case is captured by our generalized adaptive clinching framework, and we further extend our proof techniques to show that the full two-sided mechanism simultaneously satisfies Sybil-robust incentive compatibility and a relaxed notion of Pareto optimality. In light of known impossibility results, together with a new impossibility proved in this paper, we argue that these guarantees are essentially the best possible. More broadly, our work reveals new connections between classical algorithmic game theory and modern decentralized blockchains.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2674) | 2026-10-29
