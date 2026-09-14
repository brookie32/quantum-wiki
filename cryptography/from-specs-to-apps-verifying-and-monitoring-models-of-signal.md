---
title: "From Specs to Apps: Verifying and Monitoring Models of Signal and WhatsApp"
date: "2026-09-11"
updated: "2026-09-14"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1979"
summary: "The Signal protocol is a prominent messaging protocol that se- cures communication for billions of users. It powers WhatsApp, the most widely used messaging application worldwide, and the Signal app, "
last_verified: "2026-09-14"
review_by: "2026-12-13"
stale: false
---

The Signal protocol is a prominent messaging protocol that se- cures communication for billions of users. It powers WhatsApp, the most widely used messaging application worldwide, and the Signal app, popular among privacy-conscious users. Extensive re- search in the computational and Dolev-Yao settings provides strong formal security guarantees for the protocol itself. However, a gap remains between the guarantees of the protocol specification and the implementation’s actual behavior at runtime. In this work, we bridge this gap by applying SpecMon, a recently proposed runtime monitor, to check whether observed executions conform to formal protocol models. To this end, we instrument two applications (WhatsApp Web and Signal Desktop) to capture their interactions with the network and the cryptographic components. Using this instrumentation, we develop two multiset-rewrite models that are compatible with Tamarin, thus enabling verification. We derive the first model of WhatsApp Web’s implementation of the Signal protocol and the most detailed model to date of Signal’s original protocol. Monitoring establishes that observed executions conform to these models, relative to the trusted event extraction and the symbolic abstraction. For the core components of the Signal protocol, we verify authentication and secrecy properties. Finally, monitoring reveals previously undocumented differences between the original libsignal library and WhatsApp’s fork. We evaluate our methodology and demonstrate its reproducibil- ity. Developing the WhatsApp Web model, instrumenting the app, adding fuzzing, and running the experiments took three person- weeks. We also demonstrate efficient monitoring of real-world applications and detection of deliberately injected security faults, with low overhead in our measured setting.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1979) | 2026-09-11
