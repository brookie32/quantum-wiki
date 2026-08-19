---
title: "Verifiable Compression of Images"
date: "2026-08-17"
updated: "2026-08-19"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/1717"
summary: "AI image generation has made image misinformation a serious concern. To address this issue, the Coalition for Content Provenance and Authenticity (C2PA) standard adopts digital signatures to attest th"
last_verified: "2026-08-19"
review_by: "2026-11-17"
stale: false
---

AI image generation has made image misinformation a serious concern. To address this issue, the Coalition for Content Provenance and Authenticity (C2PA) standard adopts digital signatures to attest that an image originates from an authorized source, such as an attested camera or authorized AI provider. In practice, however, raw images are rarely published directly: photos are typically compressed before publication, which invalidates any C2PA signature. Recent works have proposed the use of zero-knowledge proofs (zk-SNARKs) to prove that only allowed edits were applied to a C2PA-signed original image. Unfortunately, prior works only support simple edits (e.g. cropping, blurring, and resizing) and do not support lossy image compression like JPEG, which is ubiquitous. The purpose of compression is to save communication. Therefore, unlike other edits, it cannot be verified directly, requires small proof sizes, and is unsuitable to outsourcing. To address these limitations, we present SPEG, the first practical proof system that supports the full image-transmission pipeline on personal devices. We present two protocols that support JPEG compression, while proving validity of the C2PA signature on the original image. The two modes are incomparable: the first is compatible with an arbitrary hashing algorithm (we use Poseidon for efficiency), whereas the second is significantly faster but requires the C2PA to use a polynomial commitment (e.g., KZH) instead of a conventional hash. Our key optimizations are handling the non-algebraic JPEG Encoding outside the proving circuit, and avoiding range checks in our floating-point arithmetic. We can prove the JPEG compression of an FHD(1080p) image in 47s in the Poseidon mode and in 2s in the fast mode. The fastest prior work (VerITAS) which only handles simple resizing, requires 227s on the same consumer hardware. Additionally, we identify a security gap in VIMz (PETS 25) that enables forgery of proofs for unauthorized images and provide a fix. We also prove that we can securely use the popular powers-of-tau SRS with the polynomial commitment scheme KZH.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/1717) | 2026-08-17
