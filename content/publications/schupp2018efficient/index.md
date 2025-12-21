---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Efficient Dynamic Error Reduction for Hybrid Systems Reachability Analysis"
authors: 
  - admin 
  - Erika Ábrahám
date: 2018-04-14T00:05:52+01:00
doi: "10.1007/978-3-319-89963-3_17"

# Schedule page publish date (NOT publication's date).
publishDate: 2020-03-08T00:05:52+01:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["Conference paper"]

# Publication name and optional abbreviated publication name.
publication: ""
publication_short: ""

abstract: "To decide whether a set of states is reachable in a hybrid sys-
tem, over-approximative symbolic successor computations can be used,
where the symbolic representation of state sets as well as the successor
computations have several parameters which determine the efficiency
and the precision of the computations. Naturally, faster computations
come with less precision and more spurious counterexamples. To remove
a spurious counterexample, the only possibility offered by current tools
is to reduce the error by re-starting the complete search with different
parameters. In this paper we propose a CEGAR approach that takes as
input a user-defined ordered list of search configurations, which are used
to dynamically refine the search tree along potentially spurious coun-
terexamples. Dedicated datastructures allow to extract as much useful
information as possible from previous computations in order to reduce
the refinement overhead."

# Summary. An optional shortened abstract.
summary: ""

tags: []
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_code:
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:

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
