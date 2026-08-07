---
title: "Solv-eze: Automated Placement of Explicit Water Molecules Using 3D-RISM"
date: "2026-08-07"
updated: "2026-08-07"
source: "agent"
category: "papers"
tags: [papers, arxiv-physics-chem-ph]
url: "https://arxiv.org/abs/2604.26140"
summary: "arXiv:2604.26140v2 Announce Type: replace Abstract: Molecular dynamics (MD) simulations are widely used to study biological systems, where water molecules often play a critical role in protein-ligand "
last_verified: "2026-08-07"
review_by: "2026-11-05"
stale: false
---

arXiv:2604.26140v2 Announce Type: replace Abstract: Molecular dynamics (MD) simulations are widely used to study biological systems, where water molecules often play a critical role in protein-ligand interactions. In conventional MD preparation protocols, water molecules are typically added from a pre-equilibrated solvent box and removed using conservative steric cutoffs, an approach that can eliminate important interfacial waters that are often not recovered during equilibration due to kinetic barriers limiting exchange with bulk solvent. In this work, we present an automated and computationally efficient method for placing water molecules around biomolecular solutes using three-dimensional reference interaction site model (3D-RISM) solvent density distributions. By identifying regions of high solvent probability, the method generates physically meaningful initial hydration structures without requiring extended sampling or specialized techniques such as grand canonical Monte Carlo (MC) or hybrid MC/MD approaches, and will be released as an update to AmberTools 26, enabling seamless integration into standard MD preparation pipelines. We validated the approach on a diverse set of protein-ligand complexes with crystallographically resolved bridging waters, showing that the method reproduced over 80% of experimentally observed bridging waters and 85% of buried waters not accessible to the bulk. Subsequent energy minimization of both crystallographic and predicted waters further improved agreement. Overall, this method enables more accurate and practical initialization of interfacial hydration, improving the reliability of MD simulations with modest computational cost relative to routine system preparation.

**Source:** [arXiv physics.chem-ph](https://arxiv.org/abs/2604.26140) | 2026-08-07
