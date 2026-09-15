---
title: "Scaling Hindi Quantum Natural Language Processing through Automatic Pregroup Supertagging"
date: "2026-09-15"
updated: "2026-09-15"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2609.13721"
summary: "arXiv:2609.13721v1 Announce Type: cross Abstract: Quantum Natural Language Processing (QNLP) uses pregroup grammars to translate grammatical structure into diagrammatic representations and quantum cir"
last_verified: "2026-09-15"
review_by: "2026-12-14"
stale: false
---

arXiv:2609.13721v1 Announce Type: cross Abstract: Quantum Natural Language Processing (QNLP) uses pregroup grammars to translate grammatical structure into diagrammatic representations and quantum circuits. Recent Hindi QNLP work has shown that Hindi-specific pregroup grammars can support grammar-sensitive compositional models, but grammatical type assignment is still largely manual, limiting scalability. This paper formulates automatic Hindi pregroup supertagging as a token-level classification task. Using a manually annotated corpus of 380 Hindi sentences, we evaluate lexical, contextual, prompting-based, lexical-repair, and suffix/morphology-aware methods. Results show that simple lexical and contextual models are strong in this low-resource setting: contextual backoff achieves the best completed accuracy of 64.56%, while raw Qwen2.5 prompting reaches only 11.65%. Lexical repair raises LLM-assisted prediction to 64.08%, demonstrating the value of constraining generative outputs with symbolic grammar knowledge. Diagnostic analysis further shows that seen and unambiguous tokens are much easier than unseen tokens, and suffix/morphology features improve karaka-token accuracy but not overall performance. These results show that automatic Hindi pregroup assignment is feasible and can reduce reliance on manual annotation in future multilingual QNLP pipelines.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2609.13721) | 2026-09-15
