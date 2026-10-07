---
title: "Output Policies for Anomaly Detection with Homomorphic Encryption: Threshold Resolution, Decision Preservation, and Numerical Stability"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2349"
summary: "Homomorphic encryption computes anomaly scores without exposing inputs, but released scores and decisions can reveal a private threshold. We evaluate whether output policies limit numerical threshold "
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Homomorphic encryption computes anomaly scores without exposing inputs, but released scores and decisions can reveal a private threshold. We evaluate whether output policies limit numerical threshold information while preserving existing decisions, and whether this limitation also impedes decision prediction on other inputs. Policies distinguish internal-score and released-score decisions and share decision-loss and score-distortion constraints. Thresholds were estimated in all 45 plaintext experiments combining three intrusion-detection datasets, three scoring models, and five seeds. All 45 CKKS experiments combining the same datasets, five autoencoder seeds, and three independent keys yielded threshold-containing intervals after revalidating supplied starting intervals. A 16-query cap stopped every plaintext baseline search but served only 16 of 512 separate usage requests, reducing availability. Under random splitting, released-score quantization preserved 99.864% of decisions on average while limiting numerical threshold precision. Surrogates trained on 128 decision-only responses achieved mean balanced accuracy 0.817. With training-only preprocessing and a CIC-IDS2017 weekday split, model-wise balanced accuracies were 0.816–0.911. Separating time and Flow IDs across five resampled evaluations reduced model-wise means to approximately 0.5, showing that prediction transfer depends on data splitting. Threshold-dependent reselection of quantization width changed responses that matched under fixed widths. Selected CKKS boundary tests yielded one released-decision mismatch in 57 queries. Numerical threshold information and service decision prediction therefore require separate protection goals. Output policies must assess decision preservation and response rate alongside policy selection, data splitting, and numerical boundary conditions.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2349) | 2026-10-05
