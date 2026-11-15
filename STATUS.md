# Delivery status

## Implemented locally
- Independent Git repository; 60-minute meeting package with six-slide editable source
  and PDF, speaker notes, bilingual worksheet and a 12-minute demonstration guide.
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
Notebook execution records are in validation/notebook_execution.json. These are fresh
local Python executions, not authenticated Google Colab sessions. Browser layout and
download checks are in validation/browser_checks.json. Unit checks cover the agenda,
known-answer neighbour/MI controls, empty student results, site asset links and pinned
source hashes. The rehearsal procedure is reproducible through tools/rehearse_demo.py.

## Requires external account access or a human check
- Create/configure the remote and GitHub Pages, then verify deployment and backup.
- Authenticated live Colab save/reopen/share and mentor feedback using the actual
  accounts. Local execution cannot certify these Google-account operations.
- Mentor review account and private submission channel: configure or announce in class.
- Classroom projector/pacing check and actual student access check.
- Obtain official Alpha proposal requirements; they were not supplied in the email.

No student personal information, real submissions or private feedback are included.
Mentor answers in a public source repository remain readable even though excluded from
the student website. The public content consists of generic teaching guidance.
