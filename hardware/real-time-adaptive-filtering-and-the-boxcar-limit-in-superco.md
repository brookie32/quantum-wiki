---
title: "Real-Time Adaptive Filtering and the Boxcar Limit in Superconducting Qubit Readout"
date: "2026-10-02"
updated: "2026-10-02"
source: "agent"
category: "hardware"
tags: [hardware, arxiv-quant-ph]
url: "https://arxiv.org/abs/2610.00783"
summary: "arXiv:2610.00783v1 Announce Type: new Abstract: In dispersive readout of superconducting qubits, the common baseline is a boxcar averager: a uniformly weighted average over a fixed window followed by "
last_verified: "2026-10-02"
review_by: "2026-12-31"
stale: false
---

arXiv:2610.00783v1 Announce Type: new Abstract: In dispersive readout of superconducting qubits, the common baseline is a boxcar averager: a uniformly weighted average over a fixed window followed by threshold-based state assignment. We ask when additional digital processing improves fidelity. We evaluated an adaptive finite-impulse-response (FIR) filter trained in real time by the least-mean-squares (LMS) algorithm on an FPGA quantum controller, and analyzed measured readout shots offline to compare the frozen filter with boxcar averaging and to test per-sample weighting and sequential detection. For the fixed FIR filters tested, summing the filtered samples gives the boxcar sum multiplied by one complex number, apart from a small edge correction (the kernel collapse). This scales state separation and noise equally, so discrimination cannot improve (the boxcar limit). The frozen LMS filter reduces trace noise without a resolved fidelity improvement at the tested readout lengths. Replayed on the same shots offline, each filtered shot carries 99.4% of the boxcar shot's discrimination signal-to-noise ratio at the 8 mus operating point of the 2D transmon qubit (Q1). On Q1, optimizing the readout window's start and duration improves contrast readout fidelity by +2.4% to +5.6% across four readout lengths. Per-sample weighting adds up to +3.0% over full-window integration, and only +0.33% beyond the tuned window at 8 mus. Remaining results are from a 3D ancilla qubit (Q2), which sits above the early-decision crossover that Q1 sits below. Hardware sweeps locate the crossover window near 1 mus. Offline, the sequential test decided most shots early, with fidelity within 0.5 percentage points of the boxcar. About 30 labeled shots per class build a matched-filter template nearly as good as one from hundreds. The results form an operating-point record that separates waveform denoising from decision improvement.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2610.00783) | 2026-10-02
