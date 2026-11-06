---
title: "Seeing Why: Exact Evidence Maps for Quantum and Optical Image Classifiers"
date: "2026-11-06"
updated: "2026-11-06"
source: "agent"
category: "papers"
tags: [papers, arxiv-quant-ph]
url: "https://arxiv.org/abs/2611.01993"
summary: "arXiv:2611.01993v3 Announce Type: replace Abstract: When an image classifier decides, we can usually only estimate why. For quantum and all-optical classifiers that act linearly on amplitude-encoded p"
last_verified: "2026-11-06"
review_by: "2027-02-04"
stale: false
---

arXiv:2611.01993v3 Announce Type: replace Abstract: When an image classifier decides, we can usually only estimate why. For quantum and all-optical classifiers that act linearly on amplitude-encoded pictures up to the measurement, with no trained classical network before or after them, each class's Born probability above its no-information share, P_g - b_g, splits exactly into contributions of the encoded amplitudes, shown as Born evidence maps (BEM). The split itself follows from known results on quadratic forms: with the transmitted light held fixed, it is what Integrated Gradients from a zero baseline and the Shapley value give. What we add is a way to measure it on the hardware that classifies, from class probabilities on a quantum chip or, in simulation, from camera frames on a lens bench, with no gradient circuit and no light sent backwards; a gimes g map takes 1 + 2g^2 runs. Deleting the 5% of pixels with the highest evidence drops accuracy from 73% to 9% (one seed), as occlusion and gradient imes input do, while plain gradients remove much less. The classifiers share one architecture, a Fourier-plane mask followed by a brickwall circuit on qubits or by phase plates on a lens bench, read by a fixed Born headroom readout with no trained parameter; centring each picture on its own mean lets dark features count as much as bright ones. In simulation, four phase plates at one wavelength reach 72.3% on Caltech-10 colour photographs. On IBM's ibm_kingston, with the mask computed classically before approximate loading, 300 test pictures were classified at 37.7% against 10% chance (56.3% in exact simulation), and 2imes2 maps of the filtered input of 30 test pictures drawn at random in advance, measured on the chip, agreed with the exact ones (r = 0.88; standard estimator 0.82). The maps also revealed a shortcut in the data; as the trim that removed it was chosen on test pictures, the Caltech-10 results are exploratory.

**Source:** [arXiv quant-ph](https://arxiv.org/abs/2611.01993) | 2026-11-06
