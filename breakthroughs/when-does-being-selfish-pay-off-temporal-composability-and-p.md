---
title: "When Does Being Selfish Pay Off? Temporal Composability and Profitability in Selfish Mining"
date: "2026-08-06"
updated: "2026-08-09"
source: "agent"
category: "breakthroughs"
tags: [breakthroughs, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1629"
summary: "Selfish mining undermines incentive compatibility of proof-of-work blockchains, letting a miner earn disproportionate rewards at a hashrate lower than the majority threshold. A decade of work has aske"
last_verified: "2026-08-09"
review_by: "2026-11-07"
stale: false
---

Selfish mining undermines incentive compatibility of proof-of-work blockchains, letting a miner earn disproportionate rewards at a hashrate lower than the majority threshold. A decade of work has asked whether a strategy is profitable, however, far less is understood about when it becomes profitable. Timing is critical since selfish mining operates at a loss before it turns a profit, typically requiring tens of weeks to break even in the classic case. In this paper, we present a holistic study of the time-to-profitability (TTP) of existing selfish mining strategies structured around four contributions. First, in the single-attacker setting, we characterize TTP across the full strategy space and find that TTP-minimizing and profit-maximizing strategies frequently diverge, making attack horizon a critical metric. In particular, under realistic fee dynamics, the use of incentive transactions to recruit honest-but-rational miners enable incentivized strategies to reach profitability up to 15imes faster than classic selfish mining at the same hash rate. Second, we explore TTP for the first time in the multi-attacker setting, showing that the difference in strategies between opposing attackers has a dramatic impact on joint-profitability lag. Third, we generalize intermittent selfish mining by exploring temporal composition over the full strategy space and show that its purported benefits are largely overstated. That is, alternating strategies rarely outperform the best static strategy in terms of either TTP or long-term profits. Finally, and building off our earlier findings, we explore adaptive, state-conditioned strategy selection at the difficulty adjustment period (DAP) level. We compare a general-purpose LLM agent against a fixed decision-tree selector, both implementing the same selection criteria. We find that both selectors reliably identify profit-maximizing strategies from observed network conditions, at a low operating cost, lowering the expertise barrier to exploiting adaptive selfish mining.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1629) | 2026-08-06
