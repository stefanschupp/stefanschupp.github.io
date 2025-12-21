---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ''
      # Show a call-to-action button under your biography? (optional)
      #button:
      #  text: Download CV
      #  url: uploads/resume.pdf
      headings:
        about: ''
        education: ''
        interests: ''
    design:
      # Apply a gradient background
      # css_class: hbx-bg-gradient
      # Avatar customization
      avatar:
        size: large # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: rounded # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: 'About me'
      subtitle: ''
      text: |-
        My main interest is centered around formal methods, formal verification, and applications thereof. Early contact with SMT solvers and interval constraint propagation as a theory-solver during my master's degree has pushed me toward theoretical computer science. The development of HyPro and the work on reachability analysis for linear hybrid systems during my Ph.D. equipped me with experience in both, tool/library design (c/c++/cmake/git/ci ...) as well as the realization of theoretical concepts ready to be used by practitioners. Bringing formal methods to students as part of my teaching duties was another insightful experience that I enjoyed very much. 

        Later working together with the group at WWU opened up a perspective on uncertainty in hybrid systems that raises further requirements on analysis methods. During that time I also started to help organize the ARCH competition subgroup on stochastic hybrid models.

        My work at TU Vienna opened up various new opportunities to learn and explore new fields such as IoT and GPU programming (during teaching) as well as simplex architectures (together with TU Graz) and statistical model checking of hyperproperties (together with University of Michigan, ongoing work).

        I enjoy new challenges and the discourse and discussion on how to solve the induced problems. The time during my Ph.D. made me sensible of the beauty of algorithms and structured approaches in formal methods. My view for details allowed me to fine-tune those approaches and identify sub-classes of problems and specialize dedicated methods aiming at those sub-classes

        While working at Apple I strive to extend my toolbox to further applications and approaches in formal verification to broaden my view and to open up for appplications of learnt techniques across fields.

    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: Featured Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2


---
