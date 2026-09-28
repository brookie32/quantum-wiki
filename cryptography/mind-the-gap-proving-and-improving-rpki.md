---
title: "Mind the Gap: Proving and Improving RPKI"
date: "2026-09-27"
updated: "2026-09-28"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2233"
summary: "We present the first rigorous security analysis of the Resource Public Key Infrastructure (RPKI), an IETF standard for protecting inter-domain routing from basic yet effective attacks: prefix and subp"
last_verified: "2026-09-28"
review_by: "2026-12-27"
stale: false
---

We present the first rigorous security analysis of the Resource Public Key Infrastructure (RPKI), an IETF standard for protecting inter-domain routing from basic yet effective attacks: prefix and subprefix hijacks. Existing evaluations of RPKI's security focus on empirical studies: adoption measurements, simulations evaluating the security provided by different adoption levels, and identification of implementation and specification flaws. In contrast, we focus on rigorous, modular security specifications and analysis of RPKI, including its interactions with the Border Gateway Protocol (BGP) and the Internet Protocol (IP). We identify sufficient conditions for RPKI to provably achieve its goals (requirements), under explicit, well-defined assumptions (models). We show that existing RPKI deployments do not always meet these conditions, e.g., because of circular dependencies, and propose standard-compliant improvements that restore them.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2233) | 2026-09-27
