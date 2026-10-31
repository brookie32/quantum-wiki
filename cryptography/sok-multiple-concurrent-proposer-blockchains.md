---
title: "SoK: Multiple Concurrent Proposer Blockchains"
date: "2026-10-29"
updated: "2026-10-31"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2684"
summary: "Multiple concurrent proposer (MCP) protocols let several parties contribute transactions to the same ledger update. They can distribute communication and reduce one proposer's control over inclusion a"
last_verified: "2026-10-31"
review_by: "2027-01-29"
stale: false
---

Multiple concurrent proposer (MCP) protocols let several parties contribute transactions to the same ledger update. They can distribute communication and reduce one proposer's control over inclusion and order, but these benefits depend on how the contributions are combined. We describe a common architecture from transaction receipt through proposal formation, agreement, data recovery, ordering, execution, and state finality. Within it, we identify four direct MCP families: fixed proposal vectors, selected proposal collections, persistent proposal streams, and causal proposal DAGs. We compare them with constrained assembly, where several parties restrict a block assembled by one party. Across 39 configurations, we distinguish agreement and progress from service for a particular transaction, and compare hiding, ordering, communication, throughput, and latency at explicitly named endpoints. The comparison shows why additional proposers alone do not guarantee inclusion, why hiding does not settle who can react last, and why parallel disseminations need not improve useful execution. It also identifies the recovery, payment, and organizational assumptions needed to turn independent proposal rights into reliable transaction service.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2684) | 2026-10-29
