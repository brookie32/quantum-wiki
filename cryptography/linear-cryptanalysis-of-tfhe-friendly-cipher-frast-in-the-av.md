---
title: "Linear Cryptanalysis of TFHE-Friendly Cipher FRAST in the Average Key Setting"
date: "2026-10-22"
updated: "2026-10-25"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2599"
summary: "In the average key setting, a linear attack of Bak et al. on the TFHE-friendly stream cipher FRAST let wrong guesses pass, which they left as an open problem. The S-boxes of FRAST are public and rando"
last_verified: "2026-10-25"
review_by: "2027-01-23"
stale: false
---

In the average key setting, a linear attack of Bak et al. on the TFHE-friendly stream cipher FRAST let wrong guesses pass, which they left as an open problem. The S-boxes of FRAST are public and random for every keystream block. For the mask on the least significant bit, we show that key differences fall into five indistinguishable classes per round. The filter of Bak et al. gives some wrong classes of the right parity a nonzero expected score. We compute the trail correlation exactly through the real cipher and bound the success of our statistic for every fixed master key. We bound its false alarms for a fixed master key with the last round kept and no filter, and for every attack against an ideal keystream. With known XOF inputs, our algorithm Contract recovered the classes of a branch pair of 15 rounds and the master key of ten rounds. A cost model gives class recovery for every sampled key at 26 rounds with known inputs and for a third at 38 rounds with chosen inputs. In the accounting of Bak et al., it reaches full FRAST on weak master keys of density 2^{-11.8} to 2^{-5.4} within the claimed security. A distinguisher of full FRAST has a proved advantage on these keys, and its time over the advantage stays below the claimed security as well. Independent branch S-boxes remove the cheap classes at a cost in TFHE.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2599) | 2026-10-22
