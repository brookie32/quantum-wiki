---
title: "ZK-JPEG: Zero-knowledge Image Editing and Compression"
date: "2026-09-15"
updated: "2026-09-17"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2039"
summary: "Tools for generating deep fake photographs are proliferating with greater ease of use and prominence in pop culture. Image authentication tools can defeat these deceitful developments by verifying tha"
last_verified: "2026-09-17"
review_by: "2026-12-16"
stale: false
---

Tools for generating deep fake photographs are proliferating with greater ease of use and prominence in pop culture. Image authentication tools can defeat these deceitful developments by verifying that a digital image was actually produced by a physical camera. The challenge is that these tools must be robust to desirable image transformations. Camera attestation uses digital signatures to prove an image's provenance from a camera. Lossy compression makes minute changes in order to reduce an image's size, and blurring or redacting regions of an image can protect its subjects. These changes invalidate an image's signature. Prior works use zero-knowledge (ZK) to prove a published image's edit history, but they do not survive lossy encoding such as the JPEG format. We present zkjpeg, a cryptographic tool for JPEG compression that proves an image was correctly compressed from a secret, committed input. In addition, our tool can verify a large family of image transformations by integrating them into JPEG compression with minimal cost. Our system is fast, flexible, and can be instantiated from off-the-shelf ZK tools. We use PicoZK to convert Python image editing code into a ZK circuit for the line-point zero knowledge (LPZK) proof system.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2039) | 2026-09-15
