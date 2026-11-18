# Delivery status

## Published
- Source and history: https://github.com/yaminbens/alpha-mentorship
- Student book: https://yaminbens.github.io/alpha-mentorship/
- GitHub Actions build and deployment succeeded on 2026-11-15.
- Colab launch links now point to the public repository templates.

## Implemented
- Student tasks now have numbered steps, sentence starters, completion checklists and
  matching fill-in notebook/document templates. Task 2 includes raw-export averaging,
  four explicit result rows and graph/CSV downloads. Hebrew instructions match.
- Independent Git repository; 60-minute meeting package with twelve Hebrew slides
  (six research slides, three activity slides and three scientific appendix slides), editable Markdown, standalone
  HTML and PDF. Detailed Hebrew facilitator plan for 2026-11-18, speaker notes,
  bilingual worksheet and a 12-minute demonstration guide.
- Mentor facilitation, background, answers, assessment, troubleshooting, communications,
  program requirements, review workflow and blank private-record templates.
- Reading guides, bilingual questions/glossary, references and source/license register.
- Eight self-contained notebooks: classroom introduction; later simulation, export
  analysis, neighbour persistence; two optional controls; two homework records.
- Eight-page responsive student book, notebook downloads and configurable Colab links.
- GitHub Pages workflow publishing only the built student site.
- Browser rehearsal: exact initial/final states, actual measurement files, screenshots,
  accelerated recording and worked example. No equilibrium phase claim.
- Research question options, provisional plan, proposal/report/poster templates and timeline.

## Validation
On 2026-11-18, fixed source-page links that incorrectly pointed to generated HTML
inside GitHub (for example site/pages/task-0.html). Source pages now link to actual
Markdown and repository assets; the site builder maps these to published paths.
All eight notebooks and the README now include direct Colab launch links. Added
regression checks for source links, notebook buttons and matching downloads.
Only the first Markdown cell changed in each notebook; code and remaining cells
are unchanged. Five relevant checks and 16 browser/page layout checks passed.

The revised presentation distinguishes saved particle coordinates from synthetic
neighbour diagrams. Font provenance and license are in vendor/fonts/. Scientific
plots remain available in the appendix. No new simulation was run for the redesign.

Live Pages checks passed for all eight pages at desktop and mobile widths. All
eight hosted notebook downloads match the source files. Repository-specific Colab
launch links were verified; this does not test Google sign-in or sharing. See
validation/github_pages.json.

Notebook execution records are in validation/notebook_execution.json. These are fresh
local Python executions, not authenticated Google Colab sessions. Browser layout and
download checks are in validation/browser_checks.json. Unit checks cover the agenda,
known-answer neighbour/MI controls, empty student results, site asset links and pinned
source hashes. The rehearsal procedure is reproducible through tools/rehearse_demo.py.

## Requires external account access or a human check
- Authenticated live Colab save/reopen/share and mentor feedback using the actual
  accounts. Local execution cannot certify these Google-account operations.
- Mentor review account and private submission channel: configure or announce in class.
- Classroom projector/pacing check and actual student access check.
- Obtain official Alpha proposal requirements; they were not supplied in the email.

No student personal information, real submissions or private feedback are included.
Mentor answers in a public source repository remain readable even though excluded from
the student website. The public content consists of generic teaching guidance.
