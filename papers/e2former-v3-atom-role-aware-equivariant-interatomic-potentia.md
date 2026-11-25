---
title: "E2Former-V3: Atom-Role-Aware Equivariant Interatomic Potentials"
date: "2026-11-23"
updated: "2026-11-23"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2611.27111"
summary: "arXiv:2611.27111v1 Announce Type: new Abstract: Machine-learned interatomic potentials approach density-functional accuracy, but explicit-solvent atom counts are dominated by hydrogens and water. Unif"
last_verified: "2026-11-23"
review_by: "2027-02-21"
stale: false
---

arXiv:2611.27111v1 Announce Type: new Abstract: Machine-learned interatomic potentials approach density-functional accuracy, but explicit-solvent atom counts are dominated by hydrogens and water. Uniform equivariant architectures still give every atom the same latent width and number of expensive block updates. To our knowledge, no prior method reallocates capacity by chemical role while retaining every atom and its first-principles force. We introduce E2Former-V3, which treats capacity as an atom-level resource: a static chemical role, assigned before the backbone runs, sets each atom's latent width and update count. No atom is removed, no coordinate is integrated out, and every force remains the gradient of one conservative energy. Standard reduces only the update count, sending hydrogen through half as many full-width block updates; on OMol25 validation it reaches a force mean absolute error (MAE) of 8.146 meV/Angstrom, against E2Former-V2's published 8.38, at 1.75-1.84x V2's throughput with lower peak memory on one H200. Flash also narrows the low-resolution stream to one eighth of the high-resolution width (32 vs 256 channels) and routes water oxygen with hydrogen, reaching 4.00-4.88x on three solvated systems (up to 5.85x in the pure-water all-low-resolution limit) at 11.272 meV/Angstrom, trading force accuracy for speed. Across 54 20 ps MD legs, a 100 ps NVE check, and a 1 ns NVT run on a 32,437-atom solvated protein, all runs complete; the MD legs show no non-finite values, clashes, or water fusion, and water O-O and Na-O RDF peak positions match experiment within 0.04 Angstrom. E2Former-V3 therefore moves the accuracy-throughput frontier for all-atom, conservative simulation, not a uniform accuracy win: Standard is worse on biomolecules and metals, better on electrolytes and organics; energy MAE is higher than E2Former-V2's; and water densities remain about 7.5% too high. Code: https://github.com/IQuestLab/UBio-MolFM.



## Related
- [[unconstrained-learning-of-equivariant-atomistic-properties|Unconstrained learning of equivariant atomistic properties]]
- [[dpa4-pushing-the-accuracy-cost-frontier-of-interatomic-poten|DPA4: Pushing the Accuracy-Cost Frontier of Interatomic Potentials with EMFA SO(2) Convolution]]
- [[nemora-neural-equivariant-multipole-operators-for-long-range|NEMORA: Neural Equivariant Multipole Operators for Long-Range Atomistic Learning]]
- [[fast-and-accurate-foundation-models-for-equivariant-machine-|Fast and Accurate Foundation Models for Equivariant Machine-Learned Interatomic Potentials]]
- [[branchip-learning-adaptive-equivariant-computation-for-inter|BranchIP: Learning Adaptive Equivariant Computation for Interatomic Potentials]]

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2611.27111) | 2026-11-23
