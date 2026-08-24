---
title: "Efficient Additive Randomized Encodings for String Oblivious Transfer: A Core Primitive for General Functions"
date: "2026-08-23"
updated: "2026-08-24"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1781"
summary: "Additive Randomized Encodings (AREs) provide a lightweight route to non-interactive secure computation: each party locally produces a randomized encoding of its input, and an evaluator learns only the"
last_verified: "2026-08-24"
review_by: "2026-11-22"
stale: false
---

Additive Randomized Encodings (AREs) provide a lightweight route to non-interactive secure computation: each party locally produces a randomized encoding of its input, and an evaluator learns only the function value from the sum of these encodings. Prior frameworks for constructing AREs for general functions ultimately hinge on an efficient ARE for string oblivious transfer (SOT), making SOT the core efficiency bottleneck. We revisit this final step and present improved ARE constructions for SOT. First, we streamline the recent PKE-based approach by directly constructing the required one-sided ARE (OSARE) for SOT. This yields a perfectly correct, statistically one-sided secure OSARE for SOT of size O(lambda), improving the intermediate overhead and, consequently, the overall size of the resulting PKE-based ARE. Second, we give a pairing-free ARE for SOT under the Squaring DDH assumption. Our construction is compatible with Halevi et al.'s efficient equality-to-SOT methodology: we build an ARE for Rabin-OT that embeds a message in the equality-checking procedure and then transform it to SOT while incurring only constant-factor communication overhead and no additional correctness error. The resulting ARE for SOT has size O(lambda) and negligible correctness error.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1781) | 2026-08-23
