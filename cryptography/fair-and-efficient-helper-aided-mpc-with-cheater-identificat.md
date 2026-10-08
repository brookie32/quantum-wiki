---
title: "Fair and Efficient Helper-Aided MPC with Cheater Identification"
date: "2026-10-07"
updated: "2026-10-08"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2392"
summary: "Secure multi-party computation (MPC) enables privacy-preserving tasks such as auctions and voting. In practice, more than half of the parties may collude, making security against a dishonest majority "
last_verified: "2026-10-08"
review_by: "2027-01-06"
stale: false
---

Secure multi-party computation (MPC) enables privacy-preserving tasks such as auctions and voting. In practice, more than half of the parties may collude, making security against a dishonest majority desirable. Unfortunately, dishonest-majority MPC suffers from high communication and can achieve only abort security. For instance, in an auction, an adversary may abort after learning the outcome and rerun the protocol with a higher bid. Helper-aided MPC mitigates these limitations by introducing a semi-honest, non-colluding helper, a model that naturally fits settings with a central governing or coordinating entity and provides strong guarantees even when up to n-1 parties are malicious. The model assumes that the adversary can either semi-honestly corrupt the helper or maliciously corrupt up to n-1 parties (excluding the helper). While existing helper-aided protocols are fair i.e. either all parties receive the output or none do; they still allow the adversary to abort without any penalty and deny output to all parties. This behavior is undesirable in practice, as parties may incur the cost of computation without receiving the output. In this work, we design efficient helper-aided MPC protocols that achieve identifiable fairness: either all parties obtain the output, or—if an abort occurs—no party receives the output, and the honest parties identify at least one common cheater. We propose two protocols, mathsf{Alhena} for synchronous networks and mathsf{Wasat} for asynchronous networks which provide the stronger guarantee of identifiable fairness compared to the state-of-the-art fair protocols mathsf{Asterisk} (Kamarkar et al. IEEE S&P 2024) and mathsf{Castor} (Kamarkar et al. IEEE S&P 2026) in the respective network settings. Our experiments show that, in the online phase, mathsf{Alhena} and mathsf{Wasat} achieves speedups of 4-12.5imes and 2.5-5imes over mathsf{Asterisk} and mathsf{Castor} respectively. Furthermore, in the preprocessing phase, mathsf{Wasat} exhibits speedup of approx 3imes over mathsf{Castor}. Notably, our protocols are designed in such a way that the online performance remains unaffected by active misbehaviour.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2392) | 2026-10-07
