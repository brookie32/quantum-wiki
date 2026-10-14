---
title: "Accelerating Pollard Rho with GPU Field Arithmetic on NVIDIA Blackwell"
date: "2026-10-14"
updated: "2026-10-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2469"
summary: "We show how far Pollard rho can be accelerated on current NVIDIA GPUs by rebuilding its field arithmetic around the hardware, with the Certicom challenge ECC2K-130, the Koblitz curve y^2+xy=x^3+1 over"
last_verified: "2026-10-14"
review_by: "2027-01-12"
stale: false
---

We show how far Pollard rho can be accelerated on current NVIDIA GPUs by rebuilding its field arithmetic around the hardware, with the Certicom challenge ECC2K-130, the Koblitz curve y^2+xy=x^3+1 over F_{2^{131}} with an expected cost of 2^{60.9} iterations, as the benchmark. None of the speedup comes from changing the algorithm. It comes from a packed normal-basis representation in which every Frobenius power is a permutation network instead of a chain of squarings; from the carry-less multiply that CUDA 13.3 exposes in PTX (clmad), which forms a 131-bit product in six instructions; from three-input logic instructions for everything around it; and from a batch size, launch geometry and compact tiled state chosen by measurement against the pipes they load. Across sixteen paired steps, each held to a rule written down before it ran, these take one RTX PRO 6000 Blackwell from a 0.85 billion iterations per second bitsliced control to 14.64 in the audited campaign build, a 17.2imes gain (representation and arithmetic 6.3imes, geometry 1.5imes, memory layout 1.3imes, clmad 1.2imes), and a later build reaches 15.88. That is about 230 times the best published 2010 GPU kernel per card and puts the whole challenge under five GPU-years: five cards expect a solution within a year, a thousand in about three days. The gains depend on the die. clmad issues ten to eighteen times faster per SM-clock on the data-centre parts than on the workstation part, so the same change can win on one Blackwell part and lose on another; we report twelve GPUs from Turing to Blackwell per card, per SM and per dollar, and the CPU instruction sets that play the same role. Upper bounds derived from measured pipe rates leave about 1.5imes of headroom on one RTX PRO 6000, at 24–26 billion iterations per second for any walk with one addition per step. The same levers applied to Pollard rho on NIST P-256 and P-384 on the same card give 1.52imes and 2.61imes, to 1.632 and 0.548 billion iterations per second, which still leaves P-256 about 6dot10^{21} card-years away. We also separate the sigma-walk from a table walk whose 20.08 was measured under a cycle rule later found unsound (the exact rule runs at 8.24), measure the walk constant at 2^{60.91}–2^{60.92} iterations, and report an FPGA engine at 8.25 billion iterations per second on one AWS F2 and a campaign that walked 2^{56.68} iterations, 5.4% of the expected work. Every number cites an evidence record; the code, data, evidence and a Dockerfile whose image starts the ECC2K-130 walk are at https://github.com/aburan28/rho-blackwell. None of this improves on the generic-group bound, and we do not claim that it does.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2469) | 2026-10-14
