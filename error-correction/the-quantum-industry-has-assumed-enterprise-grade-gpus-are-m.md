---
title: "The quantum industry has assumed enterprise-grade GPUs are mandatory for quantum error correction. We measured it. 👇 With an FPGA controlle…"
date: "2026-09-30"
updated: "2026-09-30"
source: "agent"
category: "error-correction"
tags: [error-correction, xanadu--x]
url: "https://x.com/XanaduAI/status/2105296682678104550"
summary: "The quantum industry has assumed enterprise-grade GPUs are mandatory for quantum error correction. We measured it. 👇 With an FPGA controller submitting a 128-bit payload over RDMA across roughly a mil"
last_verified: "2026-09-30"
review_by: "2026-12-29"
stale: false
---

The quantum industry has assumed enterprise-grade GPUs are mandatory for quantum error correction. We measured it. 👇 With an FPGA controller submitting a 128-bit payload over RDMA across roughly a million samples: 2.3 µs mean end-to-end to a stock AMD Ryzen Threadripper PRO CPU, 4.4 µs to an AMD Instinct MI210 GPU. The commodity CPU cleared the co-processing budget with room to spare. For workloads that don't require heavy parallel GPU processing, that takes the GPU off the critical path — no accelerator allocation to wait on, and no specialized system mandating shared CPU/GPU memory. We built Backline for photonic timing budgets, one of the tightest of any modality. Infrastructure built for photonics means over-specified for many others. Learn more: https://xanadu.ai/docs/backline-whitepaper.pdf

**Source:** [Xanadu (X)](https://x.com/XanaduAI/status/2105296682678104550) | 2026-09-30
