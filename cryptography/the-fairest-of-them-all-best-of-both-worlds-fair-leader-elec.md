---
title: "The Fairest of Them All: Best-of-Both-Worlds Fair Leader Election"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2738"
summary: "Fair leader election is the problem of sampling an unbiased random party out of a set of n parties. The seminal impossibility result of Cleve (STOC 1986) applies to this setting, and shows that the re"
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Fair leader election is the problem of sampling an unbiased random party out of a set of n parties. The seminal impossibility result of Cleve (STOC 1986) applies to this setting, and shows that the result of the election cannot be unbiased against a dishonest majority. Recent work has achieved the weaker property of game-theoretic fairness, where behaving dishonestly cannot improve one’s chances of being elected. However, such protocols allow even a single corrupt party to bias the outcome. In this work, we introduce best-of-both-worlds (BoBW) fairness, where a small number t_S of corrupt parties cannot bias the result, and even a larger number t_{GT} of corrupt parties still cannot improve their collective election chances (CSP-fairness) nor hurt the election chances of any given honest party (MM-fairness). We present a protocol for BoBW fair leader election for t_S + t_{GT} < n. We then prove a generalization of Cleve’s impossibility, and show that this protocol is optimal. Next, in the setting of statistical security we find that BoBW fairness is uninteresting, as it is only possible for an honest majority, where we can get also unbiased leader election. Finally, in the setting of perfect security, we present a BoBW protocol achieving CSP-fairness and strong fairness for t_S + 1 = t_{CSP} = frac{n}{3}, and prove that this is also optimal.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2738) | 2026-11-03
