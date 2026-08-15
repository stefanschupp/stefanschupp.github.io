---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Spread the Work: Multi-threaded Safety Analysis for Hybrid Systems"
authors: 
  - admin
  - Erika Ábrahám
date: 2018-05-30T21:11:11+01:00
doi: "10.1007/978-3-319-92970-5_6"

# Schedule page publish date (NOT publication's date).
publishDate: 2020-03-08T21:11:11+01:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["Conference paper"]

# Publication name and optional abbreviated publication name.
publication: "Sorftware Engineering for Formal Methods"
publication_short: "SEFM"

abstract: "We consider a method for the bounded safety analysis of hybrid systems, whose continuous behaviour is intertwined with discrete execution steps. The method computes a tree of state sets, which together over-approximate reachability by bounded-length executions. If none of the state sets intersects with a given set of unsafe states then we have proven bounded safety. Otherwise, we iteratively repeat parts of the computations with locally refined search parameters, in order to reduce the over-approximation error. In this paper we present a parallelization technique for the above method. We identify independent computations that can be carried out by different threads/processes concurrently, and examine how to achieve work-balance between the threads at low communication cost. Furthermore, we discuss how to assure mutually exclusive node access during refinement computations, without high synchronization costs. We evaluate our proposed solutions experimentally on some benchmarks."

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
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
