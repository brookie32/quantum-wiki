---
title: "Multiparty Homomorphic Secret Sharing From Distributed Discrete Logarithm"
date: "2026-10-02"
updated: "2026-10-05"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2308"
summary: "Homomorphic secret sharing (HSS) enables non-interactive distributed evaluation of functions on secret-shared inputs. While two-party HSS is well understood, multiparty constructions remain limited in"
last_verified: "2026-10-05"
review_by: "2027-01-03"
stale: false
---

Homomorphic secret sharing (HSS) enables non-interactive distributed evaluation of functions on secret-shared inputs. While two-party HSS is well understood, multiparty constructions remain limited in expressiveness and efficiency. We present a general framework for constructing multiparty HSS from two-party semi-private HSS (which in turn can be instantiated using distributed discrete logarithms) via a new party virtualization paradigm. In a semi-private HSS, some designated inputs may be fully known to specific servers, while the remaining inputs remain hidden. Starting from two-party semi-private schemes, we obtain N-party semi-private HSS supporting compositions of polynomial computations and restricted multiplication straight-line programs, for N = O(log lambda / log log lambda). We further upgrade semi-private HSS to fully private HSS for functions of polynomial degree and polynomially bounded Waring rank. As a consequence, we obtain multiparty distributed point functions with key size polynomial in lambda and log |D|, for a domain D of superpolynomial size. When the underlying two-party scheme supports offline/online sharing, the resulting multiparty DPFs are programmable. Our framework admits instantiations under standard assumptions including DCR and class-group assumptions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2308) | 2026-10-02
