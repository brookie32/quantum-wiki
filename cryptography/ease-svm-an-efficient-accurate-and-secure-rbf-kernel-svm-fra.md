---
title: "EASE-SVM: An Efficient, Accurate, and Secure RBF Kernel SVM Framework for Medical IoT"
date: "2026-11-23"
updated: "2026-11-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3003"
summary: "The increasing use of machine learning in Internet of Things (IoT) environments facilitates more intensive data exchange, raising growing concerns about data privacy. Secure computation techniques add"
last_verified: "2026-11-25"
review_by: "2027-02-23"
stale: false
---

The increasing use of machine learning in Internet of Things (IoT) environments facilitates more intensive data exchange, raising growing concerns about data privacy. Secure computation techniques address these concerns by enabling collaborative machine learning without revealing raw data. However, they often incur substantial overhead compared to plaintext computation, hindering their practical deployment. We propose EASE-SVM, an efficient, accurate, and secure RBF kernel SVM framework based on multi-party computation techniques for medical IoT, covering both training and inference phase. For training, we exploit the fixed-value update property of PEGASOS to design an efficient two-party MPC-based kernel SVM training protocol that avoids generic secure multiplication. Under the evaluated settings, EASE-SVM achieves a 1.22imes-7.25imes speedup over the prior work of Mo et al. in the iterative training phase with a precomputed kernel matrix. For inference, we develop a privacy-preserving RFF-based framework that enables RBF kernel SVMs jointly trained by multiple parties to be distributed and shared without exposing their support vectors. To improve inference efficiency, we first develop an RFF parameter optimization method that allows both parties to optimize the RFF parameters locally using kernel values, reducing the feature dimension while maintaining approximation accuracy and classification performance. We also provide an optional decision-oriented variant that directly optimizes the approximation of the trained SVM decision function while incurring explicitly specified additional leakage. Additionally, we design a lightweight period-aligned two-party secure cosine protocol, achieving a 2.21imes-2.41imes speedup over the cosine protocol of Guo et al. (USENIX Security '26).

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3003) | 2026-11-23
