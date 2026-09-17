---
title: "Leopard: A High-Performance Framework for Updatable Private Set Intersection"
date: "2026-09-14"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2027"
summary: "Updatable Private Set Intersection (UPSI) extends conventional PSI protocols to dynamic scenarios, where input sets evolve over time. A straightforward approach is to rerun the entire PSI protocol aft"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Updatable Private Set Intersection (UPSI) extends conventional PSI protocols to dynamic scenarios, where input sets evolve over time. A straightforward approach is to rerun the entire PSI protocol after each update, incurring redundant computational and communication overhead. Although several UPSI schemes have been proposed to enable updates without full protocol re-execution, existing constructions remain impractical. Building on the high efficiency of unbalanced PSI designs, this work introduces Leopard---a general framework that leverages unbalanced PSI to realize UPSI without complete re-execution, while handling both insertions and deletions. Leopard is compatible with any unbalanced PSI protocol and achieves further performance gains by reusing internal data structures across updates. Specifically, we observe that certain data structures in unbalanced PSI can be incrementally updated instead of fully rebuilt. We provide an FHE-based instantiation of Leopard that demonstrates substantial performance improvements through such data structure reuse. Through comprehensive experiments, we evaluate Leopard's performance. Compared to Badrinarayanan et al. (ASIACRYPT 2024) and Alborch et al. (ACNS 2026), our instantiations reduce computational cost by up to 111.28× and at least 1.48×, and communication cost by up to 118.97× and up to 522.01×, respectively.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2027) | 2026-09-14
