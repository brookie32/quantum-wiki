---
title: "On Succinct Obfuscation via Propositional Proofs"
date: "2026-09-13"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2009"
summary: "A central line of inquiry in the study of indistinguishability obfuscation (IO) is to minimize the size of the obfuscation. Today we know how to obfuscate programs represented as Turing machines, wher"
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

A central line of inquiry in the study of indistinguishability obfuscation (IO) is to minimize the size of the obfuscation. Today we know how to obfuscate programs represented as Turing machines, where the size of the obfuscation grows only with the input size and not with the machine's running time. Jain and Jin [FOCS 2022] showed how to remove the dependency on the input size for functionally equivalent programs where equivalence can be proven in Cook's theory PV. In this work we investigate the limits of the pursuit of succinct obfuscation. We consider the task of obfuscating a program with a large description, most of which can be made public while some portion of the description is secret. We put forth a new notion of fully succinct IO where the size of the obfuscated program only grows with the size of the program's secret part and not with the public part or with the input size. Starting with input-succinct IO for PV-equivalent machines, which is known from super-polynomially hard IO for circuits and LWE, we construct fully succinct IO for the same class of programs. We refer to such an obfuscation as fully succinct pv-IO. Next, we show how to bootstrap our fully succinct pv-IO to achieve full IO security. Our bootstrapping theorems are based on succinct cryptographic primitives with seemingly weaker functionality: either succinct witness encryption or SNARGs for NP with unique proofs. We also require that the correctness of these primitives can be proven in theory PV. We show that these assumptions are sufficient and necessary. We demonstrate several applications of fully succinct IO and pv-IO: (i) We give the first IO construction where the size of the obfuscated program is less than twice the size of the original program for a large class of useful programs. (ii) We show how to avoid padding the program before obfuscating it—a step often necessitated by security analysis—by replacing the padding with a public random string. (iii) We give the first construction of succinct computational secret sharing for access structures represented by polynomial-size monotone circuits where the share size does not grow with the size of the access structure.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2009) | 2026-09-13
