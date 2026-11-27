---
title: "TB-IOPP: Repair-Group-Local IOPs of Proximity for Tamo–Barg Codes"
date: "2026-11-25"
updated: "2026-11-27"
source: "agent"
category: "papers"
tags: [papers, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3043"
summary: "Reed-Solomon IOPPs underpin transparent succinct arguments but inherently lack small-locality symbol repair: by the MDS barrier, reconstructing missing queries requires global recovery, creating a fun"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

Reed-Solomon IOPPs underpin transparent succinct arguments but inherently lack small-locality symbol repair: by the MDS barrier, reconstructing missing queries requires global recovery, creating a fundamental structural mismatch in distributed, authenticated, and data-availability settings. We introduce TB-IOPP, the first repair-group-local IOP of proximity for locally recoverable Tamo-Barg codes. TB-IOPP delegates global proximity testing to an arbitrary Reed-Solomon backend via full-rank matrix folding while strictly confining every query to the committed original oracle within a fiber, an individual local repair group. The central technical challenge is cross-fiber stitching, where locally valid repair groups fail to combine into a globally consistent codeword. We resolve this by proving a robust anti-stitching theorem that bounds distance to the code in the fiber metric, showing that our original-oracle query complexity is optimal up to a constant factor in the ideal-IOPP model. Furthermore, we establish round-by-round knowledge soundness assuming only round-by-round soundness and efficient witness decoding of the backend, and compile the protocol under BCS into a non-interactive argument whose extraction guarantee binds directly to the published commitment. Finally, we establish a correlated-agreement theorem directly in the fiber metric to enable batched verification, and construct a splicing-resistant repairable proximity certificate tailored for authenticated distributed storage.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3043) | 2026-11-25
