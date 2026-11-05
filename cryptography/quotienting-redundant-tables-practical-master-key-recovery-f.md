---
title: "Quotienting Redundant Tables: Practical Master-Key Recovery from WBSLT White-Box AES"
date: "2026-11-03"
updated: "2026-11-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2729"
summary: "Enlarging lookup-table addresses does not hide smaller selectors when the complete public table factors through a core with distinct rows and distinct columns. We demonstrate this condition in WBSLT, "
last_verified: "2026-11-05"
review_by: "2027-02-03"
stale: false
---

Enlarging lookup-table addresses does not hide smaller selectors when the complete public table factors through a core with distinct rows and distinct columns. We demonstrate this condition in WBSLT, a white-box AES design presented at NDSS 2026 that reports resistance to several structural attacks. In the released general generator, the joint output of each group of four first-round TypeII tables has an exact 16 × 16 quotient of its 64 × 64 address space. Mapping its row and column classes to observed addresses recovers the original nibble partition of each AES input byte. Public tables implementing encoded XOR supply compatible output coordinates. Under the generator’s strictly linear input decoder, two 16-point restrictions of each keyed AES S-box then identify its embedded key byte; independent exhaustive checks confirm this property for all 256 byte keys. Using public tables and traces of chosen encoded inputs, we recover every key in 200 general instances that passed 200,000 reference AES block tests, after a median of 146 and at most 221 inputs. Separate 200-instance cohorts of the released optimized C source and its one-line functional repair also yield every key; only the repair passes the AES tests. An adjacent-round adaptation recovers 20/20 exact keys on a paired cohort without reconstructing the nibble partition. On those instances, our first-round route uses fewer live trace queries and less public table data. The exact quotient provides a concrete test for selector partitions that survive address enlargement.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2729) | 2026-11-03
