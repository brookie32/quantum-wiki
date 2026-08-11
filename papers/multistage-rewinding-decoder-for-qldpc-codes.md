---
title: "Multistage Rewinding Decoder for QLDPC Codes"
date: "2026-08-11"
updated: "2026-08-11"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2608.07783"
summary: "arXiv:2608.07783v1 Announce Type: new Abstract: In this paper, we propose a multistage decoding framework that leverages internal information produced by an underlying message-passing decoder. The pro"
last_verified: "2026-08-11"
review_by: "2026-11-09"
stale: false
---

arXiv:2608.07783v1 Announce Type: new Abstract: In this paper, we propose a multistage decoding framework that leverages internal information produced by an underlying message-passing decoder. The proposed method targets the failure dynamics caused by both classical trapping sets and degenerate errors supported on symmetric stabilizers, which are among the primary limitations of iterative decoding for QLDPC codes. To identify unreliable variable nodes, we introduce a heuristic metric that combines several dynamical features of the decoder, including variable-node log likelihood reliabilities, hard-decision oscillations, the number of adjacent unsatisfied checks, and the soft information contributed by unsatisfied checks. Based on this ranking metric, the decoder performs guided rewinds by selectively forcing the initial log likelihood ratio values of the most suspicious variable nodes and restarting the message-passing decoder under the corresponding forced configuration. To manage the combinatorial growth of candidate configurations, the search is formulated within a beam- search framework with controlled beam width. In addition, we introduce a pruning metric based on the combination of the residual syndrome weight and a posteriori reliability of the decoder output, thereby retaining only the most promising search paths. Logical error rate results demonstrate that the proposed decoder significantly outperforms the normalized min- sum decoder and achieves competitive performance with belief propagation enhanced by order-10 ordered statistics decoding.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2608.07783) | 2026-08-11
