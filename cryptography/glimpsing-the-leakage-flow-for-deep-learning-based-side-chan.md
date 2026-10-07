---
title: "Glimpsing the Leakage Flow for Deep Learning-Based Side-Channel Analysis using Stochastic Leakage Model"
date: "2026-10-05"
updated: "2026-10-07"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2358"
summary: "Deep learning has become the dominant method for profiled Side-Channel Analysis (SCA), successfully recovering secret keys even in the presence of strong countermeasures. Despite its efficacy, Deep Ne"
last_verified: "2026-10-07"
review_by: "2027-01-05"
stale: false
---

Deep learning has become the dominant method for profiled Side-Channel Analysis (SCA), successfully recovering secret keys even in the presence of strong countermeasures. Despite its efficacy, Deep Neural Networks (DNNs) are predominantly black-box in nature. Evaluators do not know what information leakages are extracted and utilized across the network's layers. Yet, understanding this leakage flow is vital for designing more resilient cryptographic implementations. Existing explainability techniques often do not provide any explanation of the leakages at specific points within a layer's feature representation. In this work, we introduce GlimpseDNN, a novel model-agnostic framework designed to provide layer-by-layer visualizations that reveal how DNNs process physical leakage traces to achieve secret key recovery. GlimpseDNN utilizes the stochastic leakage model to provide characterization of the underlying leakage in the intermediate features of each layer. A key advantage of the stochastic leakage model is its dual capability: it can learn complex leakage models and is inherently interpretable through its learned weights. We validate the GlimpseDNN framework on a simulated traces and various public datasets, including ASCADf, ASCADr, ASCADf_desync50 and ASCADf_desync100. In particular, we show that even when leakages fail to be captured in the original traces, the GlimpseDNN framework manages to find these leakages by considering the deeper layers of the well-trained DNN. This provides evaluators an alternative to glimpse the underlying leakage for identifying specific implementation vulnerabilities used by DNN, ultimately aiding in the design of more robust, side-channel-resistant hardware.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2358) | 2026-10-05
