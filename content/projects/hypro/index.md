---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "HyPro"
summary: "A Toolbox for the Reachability Analysis of Hybrid Systems using Geometric Approximations"
authors: []
tags: []
categories: []
date: 2020-03-08T21:59:51+01:00

# Optional external URL for project (replaces project detail page).
external_link: "https://ths.rwth-aachen.de/research/projects/hypro/"

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_code: "https://github.com/hypro/hypro"
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: ""
---

In this project we considered systems, which are hybrid in the sense that their behaviour is a mixture of continuous evolution as well as instantaneous (discrete) changes of the system state. For such systems, we are interested in their formal safety analysis, i.e., in the development, implementation and application of rigorous methods that are able to take such a hybrid system, a set of initial states and a set of unsafe states as input, and determine whether the system can reach any of the unsafe states from any of the initial states. Our focus lies on hybrid systems, whose continuous evolution (dynamics) can be described by linear (ordinary) differential equations, and a special technique of reachability analysis using ﬂowpipe construction. For a given hybrid system and a given set of initial states, such methods over-approximate the set of all reachable states (within certain bounds on the execution length) by “paving” the set of all system trajectories by a ﬁnite number of state sets. These computations use different geometric and symbolic representations for state sets as datatypes. The choice of the state set representation has a strong impact on the approximation error and on the running time of the analysis method. Additionally, numerous further parameters and heuristics inﬂuence the analysis outcome. Well-chosen parameter values, achieving a good balance between efﬁciency and precision, are needed for conclusive veriﬁcation results, proving that no unsafe states are reachable. However, due to over-approximative computations, when one of the computed state sets has a non-empty intersection with the unsafe state set then there is the possibility to reach a target state. If such a counterexample is detected then the analysis in inconclusive, since we do not know whether the target state is indeed reachable or the counterexample is just spurious, i.e. caused by over-approximation. In most approaches parameter values are static, such that the only way to prove safety is to re-start the veriﬁcation process with different parameter values. In this project we investigated the inﬂuence and optimal usage of such veriﬁcation parameters. Firstly, we developed a general framework that allows dynamically changing parameter conﬁgurations; this can be useful for example to chose optimal analysis methods under different types of dynamics or to increase the precision for discrete-event detection. In a second step, we instantiated this framework to a counterexample-guided abstraction reﬁnement (CEGAR) approach, which allows to dynamically change parameter conﬁgurations to achieve conclusive safety veriﬁcation: we start with fast but imprecise computations and stepwise increase the precision along counterexample trajectories until they can be refuted as spurious. However, since more precise computation are computationally more involved, we minimise the effort invested in such reﬁnements by re-using as much of the previous computation results as possible. In a third step, we further increased the applicability of our dynamically conﬁgured veriﬁcation approach by an elegant parallelisation approach. The idea is to decompose the search space and to replace computationally expensive high-dimensional computations by cheaper computations in lowerdimensional subspaces, on the cost of a relatively small increment in over-approximation. We provide automation for the check of application conditions and for the decomposition itself, and use our dynamic framework to integrate context-dependent analysis methods for subspace computations. All results are implemented in our open-source C++ programming library named HyPro, which is publicly available under https://github.com/hypro/hypro.
