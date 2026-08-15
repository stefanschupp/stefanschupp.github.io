---
title: 'Maximizing Reachability Probabilities in Rectangular Automata with Random Events'
authors:
  - Joanna Delicaris
  - Anne Remke
  - Erika Ábrahám
  - admin
  - Jonas Stübbe
publication_types: ["journal"]
publication: ""
summary: ""
abstract: "This paper introduces two stochastic variants of rectangular automata. First, rectangular automata with random events (RAE) are introduced, which semantically embed random events. Second, in rectangular automata with random clocks (RAC), the dynamics of random events are explicitly modeled as stopwatches which are called random clocks. We show that RAE can be transformed into RAC maintaining time- and jump-bounded reachability. Both modeling variants incorporate time-induced nondeterminism on discrete behavior and nondeterminism in the dynamic behavior. The difference between RAE and RAC lies in the modeling of the random events: while RAE semantically ensure that random events are correctly handled via stochastic guards, in RAC it is the responsibility of the modeler to ensure, e.g., that random clocks are enabled and disabled such that the resulting random delay correctly models the desired random event. However, the advantage of RAC is that existing methods for nonstochastic rectangular automata can directly be applied to RAC to compute the reachable state space. We then propose an algorithm to maximize reachability probabilities for RAC with history-dependent prophetic scheduling. Specifically, we use a backward refinement approach to identify the maximum prophetic scheduler and prove the correctness of the proposed method. The feasibility of the presented approach is illustrated on a scalable model and the results computed with our tool RealySt are validated against the tool ProHVer."
publishDate: "2025-01-01T00:00:00Z"
year: "2025"
volume: "240"
pages: "103213"
hugoblox:
    ids:
        doi: "10.1016/j.scico.2024.103213"
---
