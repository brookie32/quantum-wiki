---
title: "Auditing an AI-Generated Mathematical Proof: A Correction to a Greedy Conditioning Lemma in Quantum Parallel Repetition"
date: "2026-08-18"
updated: "2026-08-18"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.14673"
summary: "arXiv:2608.14673v1 Announce Type: cross Abstract: Chapter 6 of OpenAI's *Ten Advances in Mathematics and Theoretical Computer Science* claims an exponential parallel-repetition theorem for all finite "
last_verified: "2026-08-18"
review_by: "2026-11-16"
stale: false
---

arXiv:2608.14673v1 Announce Type: cross Abstract: Chapter 6 of OpenAI's *Ten Advances in Mathematics and Theoretical Computer Science* claims an exponential parallel-repetition theorem for all finite two-player, one-round entangled games. Early in the proof, the chapter uses a quantitative greedy conditioning lemma. The lemma is meant to select a small set of coordinates (D) such that, after conditioning on winning every coordinate in (D), a randomly chosen remaining coordinate is won with average probability at least (1-elta). The statement is correct, but the proof as printed contains a polarity error. Its continuation test is written in terms of average success, while the next step requires a coordinate with a large conditional failure probability. That implication is false, and even simple examples can leave the printed procedure without a valid next move. This note gives an explicit counterexample, identifies the intended continuation condition, and supplies a complete corrected proof. The repair is local: it leaves the statement of the lemma and the parameters used later in the chapter unchanged. It should not, however, be read as an independent verification of the main parallel-repetition theorem. More broadly, the example shows how a mathematically plausible AI-generated argument can hide a small but decisive reversal between complementary events.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.14673) | 2026-08-18
