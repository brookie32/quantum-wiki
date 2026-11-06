---
title: "Can Fully Homomorphic Encryption on Public Blockchains Protect Sensitive Medical Consultations? A Security and Privacy Assessment"
date: "2026-11-04"
updated: "2026-11-06"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2771"
summary: "%===================================================================== egin{abstract} People seeking care for stigmatised conditions often delay treatment because they fear exposure, yet digital healt"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

%===================================================================== egin{abstract} People seeking care for stigmatised conditions often delay treatment because they fear exposure, yet digital health services routinely expose user data and metadata. Fully homomorphic encryption (FHE) now allows smart contracts on public blockchains to hold encrypted data whose decryption is governed by contract rules. This paper assesses whether this approach can protect sensitive medical consultations. We present ConfidentialCare, a prototype built on Zama's fhEVM and the Ethereum Sepolia testnet, in which patients' symptoms are encrypted in the browser and only an authorised doctor may decrypt them. We evaluated three versions of the system through metadata inspection, access-control tests and attack experiments, asking what FHE protects and whether access to patient data can be controlled. Consultation content remained confidential in all tested cases, and the design collects no names, emails or accounts. However, public on-chain metadata revealed which wallet consulted which doctor, the doctor's specialty, when, and the approximate length of each message, and this history would be exposed permanently if the wallet were ever linked to the patient. We also found that a doctor granted access could re-share a patient's encrypted data, both through a confused-deputy flaw in the application contract, which we fixed, and directly through fhEVM's access control list, and that neither withdrawing access nor closing a consultation removed it. A redesign based on time-limited, revocable delegation prevented re-sharing, and Zama's live service enforced its revocation and expiry immediately. On Sepolia, Zama's key-management service refused decryption without a valid delegation, and revocation took effect within the same block in all six trials. We conclude that FHE protects what patients disclose, but not the fact or context of seeking care, and that in fhEVM a permission to decrypt is also a permission to share. end{abstract}

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2771) | 2026-11-04
