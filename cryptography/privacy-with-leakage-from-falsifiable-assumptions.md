---
title: "Privacy with Leakage from Falsifiable Assumptions"
date: "2026-10-19"
updated: "2026-10-20"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2551"
summary: "An inherent challenge in cryptography is finding realistic and meaningful models and assumptions. Such assumptions must be fal- sifiable. For symmetric-key cryptography in the standard model (i.e., bl"
last_verified: "2026-10-20"
review_by: "2027-01-18"
stale: false
---

An inherent challenge in cryptography is finding realistic and meaningful models and assumptions. Such assumptions must be fal- sifiable. For symmetric-key cryptography in the standard model (i.e., black-box without leakage), it is conjectured that we have identified the right assumptions: pseudorandom functions and permutations (PRFs and PRPs). However, when considering side-channel attacks (SCAs) that exploit physical side-channel leakage, the answer is less clear. Moreover, the requirements for integrity and privacy may differ in the leakage-aware SCA setting. For integrity: due to advances in the so-called unbounded leakage model, it is sufficient to claim integrity based only on black-box properties by instantiating a single strongly unpredictable-with-leakage (tweakable) block cipher. For privacy: one approach relied on simulatabil- ity, proposed by Yu and Standaert at CRYPTO 2013. That is, it should be possible to simulate leakage traces without access to the underlying secret key. Unfortunately, simulating the leakage behavior of a complex electronic system and arguing that distinguishing simulation from reality is hard has proved highly challenging (e.g., Galea et al., ASIACRYPT 2014, and Deperz et al., Cascade 2026). In this paper, we propose a new model and assumption. We isolate a key component, namely the key-refreshing process, and provide a security definition for it that is both falsifiable in practice and usable in security proofs: secure refreshing. Like simulatability, this assumption is designed to capture the security of the key-refreshing process. Rather than re- lying on a simulator, however, we formalize security through a direct refreshing experiment that can be practically falsified by evaluation lab- oratories. Therefore, our approach avoids many of the concrete problems and challenges associated with previous models. Furthermore, inspired by this new assumption (and its accompanying model), and to provide an additional security assumption for the strongly SCA-protected leak- free component, we introduce strongly protected secure refreshing. As one concrete example, using these assumptions, we prove the privacy of the well-known PSV encryption scheme. We provide the first privacy proof based only on falsifiable assumptions and, importantly, without assuming that the strongly protected component is leak-free which can effectively translate to significant computational cost reduction.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2551) | 2026-10-19
