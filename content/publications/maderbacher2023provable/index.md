---
title: 'Provable Correct and Adaptive Simplex Architecture for Bounded-Liveness Properties'
authors:
  - Benedikt Maderbacher
  - admin
  - Ezio Bartocci
  - Roderick Bloem
  - Dejan Nickovic
  - Bettina Könighofer
publication_types: ["conference"]
publication: "International Symposium on Model Checking Software"
summary: ""
abstract: "We propose an approach to synthesize Simplex architectures that are provably correct for a rich class of temporal specifications, and are high-performant by optimizing for the time the advanced controller is active. We achieve provable correctness by performing a static verification of the baseline controller. The result of this verification is a set of states which is proven to be safe, called the recoverable region. During runtime, our Simplex architecture adapts towards a running advanced controller by exploiting proof-on-demand techniques. Verification of hybrid systems is often overly conservative, resulting in over-conservative recoverable regions that cause unnecessary switches to the baseline controller. To avoid these switches, we invoke targeted reachability queries to extend the recoverable region at runtime.

Our offline and online verification relies upon reachability analysis, since it allows observation-based extension of the known recoverable region. However, detecting fix-points for bounded liveness properties is a challenging task for most hybrid system reachability analysis tools. We present several optimizations for efficient fix-point computations that we implemented in the state-of-the-art tool HyPro that allowed us to automatically synthesize verified and performant Simplex architectures for advanced case studies, like safe autonomous driving on a race track."
publishDate: "2023-01-01T00:00:00Z"
year: "2023"
pages: "141--160"
hugoblox:
    ids:
        doi: "10.1007/978-3-031-32157-3_8"
---
