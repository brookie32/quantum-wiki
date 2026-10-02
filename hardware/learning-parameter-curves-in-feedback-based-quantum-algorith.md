---
title: "Learning parameter curves in feedback-based quantum algorithms"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2601.08085"
summary: "arXiv:2601.08085v2 Announce Type: replace Abstract: Feedback-based quantum algorithms (FQAs) operate by iteratively growing a quantum circuit to optimize a given task. At each step, feedback from qubi"
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2601.08085v2 Announce Type: replace Abstract: Feedback-based quantum algorithms (FQAs) operate by iteratively growing a quantum circuit to optimize a given task. At each step, feedback from qubit measurements is used to inform the next quantum circuit update. In practice, the sampling cost associated with these measurements can be significant. Here, we ask whether FQA parameter sequences can be predicted using classical machine learning, obviating the need for qubit measurements altogether. To this end, we train a teacher-student model to map problem instances to associated FQA parameter curves in a single classical inference step. We first study weighted MaxCut problem instances, where numerical experiments show that this machine learning model can accurately predict FQA parameter curves across a range of problem sizes, including sizes not seen during model training. We then extend the analysis to transverse-field Ising models on graphs, and analyze how this learning strategy performs and generalizes beyond the original MaxCut setting. To evaluate performance, we compare the predicted parameter curves in simulation against FQA reference curves and linear quantum annealing schedules. We observe similar results to the former and performance improvements over the latter. These results suggest that machine learning can offer a heuristic, practical path to reducing sampling costs and resource overheads in quantum algorithms.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2601.08085) | 2026-10-02
