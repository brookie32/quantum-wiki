---
title: "Rotten CHERIs - A Comprehensive Study of Faults in CHERI RISC-V"
date: "2026-11-26"
updated: "2026-11-27"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/3063"
summary: "The relentless stream of exploits based on memory vulnerabilities has prompted hardware developers to engineer new solutions that prevent these vulnerabilities at a deep hardware level. One such solut"
last_verified: "2026-11-27"
review_by: "2027-02-25"
stale: false
---

The relentless stream of exploits based on memory vulnerabilities has prompted hardware developers to engineer new solutions that prevent these vulnerabilities at a deep hardware level. One such solution is CHERI (Capability Hardware Enhanced RISC Instructions), which has attracted significant interest from academia and industry. While CHERI has proven effective at mitigating memory-safety vulnerabilities under its architectural threat model, real-world environments often expose devices to advanced attack strategies. In particular, physical attackers can launch fault attacks that greatly exceed the fault model assumed during CHERI's development. Although memory and fault attacks are vastly different, the question arises whether CHERI's memory-protection guarantees hold under a fault attack model. To address this issue, we conduct the first fault analysis of CHERI on RISC-V systems. We analyze the impact of faults on capabilities and capability management instructions. Our threat analysis reveals opportunities and limitations for attackers, showing that CHERI raises the bar for meaningful fault attacks, but does not prevent them entirely. In order to evaluate fault attacks on generic CHERI-RISC-V systems, we have developed a functional, Spike-based fault simulator. We demonstrate successful fault attacks that can still violate CHERI's memory-safety guarantees and evaluate and discuss potential countermeasures.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/3063) | 2026-11-26
