---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "State Set Representations and Their Usage in the Reachability Analysis of Hybrid Systems"
authors:
  - admin
date: 2019-09-25T23:56:10+01:00
doi: "10.18154/RWTH-2019-08875"
featured: true

# Schedule page publish date (NOT publication's date).
publishDate: 2020-03-07T23:56:10+01:00

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['thesis']

publication: State Set Representations and Their Usage in the Reachability Analysis of Hybrid Systems
publication_short: Thesis.


# Custom links
#links:
#  - type: pdf
#    url: ""
#  - type: code
#    url: https://github.com/HugoBlox/hugo-blox-builder
#  - type: dataset
#    url: https://github.com/HugoBlox/hugo-blox-builder
#  - type: slides
#    url: https://www.slideshare.net/
#  - type: source
#    url: https://github.com/HugoBlox/hugo-blox-builder
#  - type: video
#    url: https://youtube.com

# Publication name and optional abbreviated publication name.
abstract: "Hybrid systems in computer science are systems with combined discrete-continuous behavior. This work presents results obtained in the field of safety verification for linear hybrid systems whose continuous behavior can be described by linear differential equations. We focus on a special technique named flowpipe-construction-based reachability analysis, which over-approximates the reachable states of a given hybrid system as a finite union of state sets. In these computations we can use different geometric and symbolic representations for state sets as datatypes.The choice of the state set representation has a strong impact on the precision of the approximation and on the running time of the analysis method. Additionally, numerous further parameters and heuristics influence the analysis outcome. In this work we investigate on the influence and optimal usage of these parameters.Our results are collected in a publicly available open-source C++ programming library named HyPro. The major contributions of this work are threefold: 1) We present our HyPro library offering implementations for several state set representations that are commonly used in flowpipe-construction-based reachability analysis. A unified interface in combination with reduction and conversion methods supports the fast implementation of versatile analysis methods for linear hybrid systems. 2) We put our library to practice and show its applicability by embedding a flowpipe-construction-based reachability analysis method in a CEGAR-based abstraction refinement framework. The parallelization of this approach further increases its performance. 3) We introduce methods to decompose the search space and replace high-dimensional computations by computations in lower-dimensional subspaces.This method is applicable under certain conditions. An automated check of these conditions, an automated decomposition, and the integration of dedicated analysis methods for subspace computations extend our approach."

# Summary. An optional shortened abstract.
summary: "This work presents results obtained in the field of safety verification for linear hybrid systems via flow pipe construction-based reachability analysis."

tags: []
categories: []


# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
  - hypro 

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
