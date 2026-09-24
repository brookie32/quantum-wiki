---
title: "Batch IT-MAC: Program the Randomness in Succinct VOLE"
date: "2026-09-22"
updated: "2026-09-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2159"
summary: "Many cryptographic protocols rely on affine message authentication tags of the form ({oldsymbolsigma}=Delta{oldsymbol x}+{oldsymbol k}), the batch version of information-theoretic MAC. Generating the "
last_verified: "2026-09-24"
review_by: "2026-12-23"
stale: false
---

Many cryptographic protocols rely on affine message authentication tags of the form ({oldsymbolsigma}=Delta{oldsymbol x}+{oldsymbol k}), the batch version of information-theoretic MAC. Generating the tags for a long message vector typically requires communication linear in its length. Recent chosen-input VOLE protocols achieve succinct communication, but do not allow the authenticator’s key k to be fixed in advance. We introduce mathit{batchext{-}MAC}, a primitive that authenticates a chosen message vector in two messages while allowing the authenticator’s key vector to be generated beforehand from a short seed. For a vector of length (m), we construct batch-MACs with (O(m^{2/3}lambda)) communication under the decisional composite residuosity (DCR) assumption and (operatorname{poly}(log m,lambda)) communication under the learning with errors assumption. Both constructions require a common reference string (CRS). We find applications in constrained pseudorandom functions, 2-message 2PC, and succinct zero-knowledge arguments.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2159) | 2026-09-22
