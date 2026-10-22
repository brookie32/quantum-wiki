---
title: "Graphs and cycles in curve-based collision walks"
date: "2026-10-20"
updated: "2026-10-22"
source: "agent"
category: "cryptography"
tags: [cryptography, iacr-eprint-archive]
url: "https://eprint.iacr.org/2026/2560"
summary: "In this work, we look at collision-based attacks both for elliptic curve and isogeny problems. Our main focus is on attacks in the multi-user setting, i.e., where one tries to recover all secret keys "
last_verified: "2026-10-22"
review_by: "2027-01-20"
stale: false
---

In this work, we look at collision-based attacks both for elliptic curve and isogeny problems. Our main focus is on attacks in the multi-user setting, i.e., where one tries to recover all secret keys of a large set of L public keys simultaneously, in a faster way than the total time required to attack each key individually. We consider three different problems: (1) the discrete logarithm problem on elliptic curves, (2) the isogeny pathfinding problem on supersingular F_{p^2}-curves, (3) the isogeny pathfinding problem on supersingular F_p-curves. We first survey the existing van Oorschot and Wiener style attacks on these three problems. Then we propose versions of the pseudorandom walks that are better suited for isogeny pathfinding problems without additional restrictions. We then apply these new walks to the multi-user setting and analyse which properties we can achieve compared to the discrete logarithm case where we show that we can extract all L public keys with L useful collisions and without an infiltrator (a user for which we know the secret key). Specifically, for (2) we can extract L public keys with approximately L + log(L) useful collisions and no infiltrator needed. Our analysis shows however that heuristic and infiltrator-aided strategies are more efficient while enjoying practically similar gains. For (3) we can extract approximately 0.75L public keys with L useful collisions, but with an infiltrator.

**Source:** [IACR ePrint Archive](https://eprint.iacr.org/2026/2560) | 2026-10-20
