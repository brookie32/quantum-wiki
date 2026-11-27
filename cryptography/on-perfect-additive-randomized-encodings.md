---
title: "On Perfect Additive Randomized Encodings"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3070"
summary: "An Additive Randomized Encoding (ARE) for f(x_1,ldots,x_n) reduces the task of securely computing f to computing the sum of locally encoded inputs. Concretely, an ARE for f over an Abelian group mathb"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

An Additive Randomized Encoding (ARE) for f(x_1,ldots,x_n) reduces the task of securely computing f to computing the sum of locally encoded inputs. Concretely, an ARE for f over an Abelian group mathbb G randomly encodes each input x_i into ilde x_iinmathbb G, such that from sum_{i=1}^n ilde x_i one can decode f(x_1,ldots,x_n) (correctness) but cannot learn anything else about the inputs (security). Previous works constructed AREs for simple functions such as sf{OR} with perfect security and imperfect correctness (namely, the decoder's output is incorrect with a small probability), and AREs for general functions with imperfect correctness and security, where imperfect security was shown to be inherent. This leaves open the existence of ARE for nontrivial functions with perfect correctness. We make progress on this question, obtaining the following negative results. ullet Ruling out a perfect ARE for {sf OR}: We rule out the existence of a perfect ARE, namely ARE satisfying both perfect security and perfect correctness, for {sf OR}(x_1,x_2)=x_1ee x_2 over any finite Abelian group. We also rule out any perfect ARE for {sf XOR}(x_1,x_2)=x_1oplus x_2 over mathbb Z_p, for any prime p>2, assuming that the encoding probabilities are rational. ullet Towards ruling out perfectly correct AREs: We partially rule out AREs for {sf OR} that have perfect correctness and imperfect security, under some natural restrictions on the ARE that are met by existing constructions. Concretely, assuming that the input 0 is always encoded as 0, we rule out perfectly correct AREs whose security error is negligible in the bit-length of group elements. If the encodings of 1 are also uniform over their supports, we rule out security error at most 10^{-5}. Finally, we rule out perfectly secure AREs with nontrivial correctness error for {sf OR} and {sf XOR} over histograms, i.e., elements hinmathbb N^mathbb N whose support is finite. This also rules out perfectly secure protocols with the same correctness guarantee for {sf OR} and {sf XOR} in the (non-interactive) shuffle model, a popular model in the differential privacy literature, where parties can broadcast anonymous messages from which the output is computed.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3070) | 2026-11-26
