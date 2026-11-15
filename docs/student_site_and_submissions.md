# Student website and saved work

## Proposed workflow

Use a book-style GitHub Pages site for instructions and downloadable notebooks.
Students open each assignment in Colab, save their own copy in Google Drive and
share it with the mentor for feedback. The initial course requires no student
GitHub account or Git commands.

GitHub Pages hosts static content. A published book does not by itself provide
authenticated student accounts, durable server-side answer storage or a mentor
submission inbox. A browser-local draft would not be visible to the mentor and
would not be a submitted assignment. For the first version, keep answers in Colab
and provide a clear sharing/submission checklist on every task page.

Sources: [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
and [Colab saving and sharing](https://research.google.com/colaboratory/faq.html).

## Student pages to implement

1. **Start here:** project question, first meeting, required access and help.
2. **Task 0 — My first notebook:** save a copy, run a cell, write an answer, make
   an example plot and reopen the saved notebook. Begin this in class.
3. **Task 1 — Explore atomic motion:** reproduce the guided demonstration at home,
   state a prediction and record settings and observations.
4. **Task 2 — Make a controlled comparison:** three energy levels at fixed particle
   count and box size, measured temperatures, a repeat, screenshots and a plot.
5. **Reading and questions:** selected portions of the existing reading list,
   questions and terminology.
6. **Save and submit:** naming, saving, data persistence, sharing permissions,
   review links, revision and backup instructions.

Task 1 and Task 2 divide the existing first experiment into manageable steps;
they do not add a separate simulation campaign. Use a matching notebook for each
task so students need not transfer answers between a web form and Colab.

Each task page needs its purpose, approximate workload, prerequisites, numbered
steps, expected output, Open in Colab button, notebook download, saving reminder
and submission checklist. Provide previous/next navigation and Hebrew prompts.

## Saving and submitting

1. Open the notebook template and choose **Save a copy in Drive** before editing.
2. Name it with the assignment identifier and an agreed student code.
3. Write predictions, answers and small observation tables directly in the saved
   notebook. Retain plot outputs for review.
4. Explicitly save exported data files to Drive or download them. Files stored only
   in the Colab runtime can disappear; sharing the notebook does not share those
   files automatically. Do not assume uploaded screenshots persist unless embedded
   in the saved notebook or separately shared.
5. Save and reopen the notebook to verify that answers and outputs are present.
6. Share with the mentor's designated Google account, normally with Commenter
   permission. Keep general access restricted to the intended recipients.
7. Send the notebook link through the agreed program communication channel.
   Giving access and submitting the link are distinct steps.
8. For review, include any separate data/image files with matching access. Keep
   a dated downloaded notebook as a submission snapshot if a fixed version is
   needed; the shared working copy can continue to change.
9. Read feedback and revise the same notebook, adding a short revision note.

Notebook contents, saved outputs and comments are shareable; the runtime state
and its custom files are not included automatically. See the
[Colab FAQ](https://research.google.com/colaboratory/faq.html).

## Mentor review

Keep a private review tracker with student code, task, submission link, receipt
date, access check, feedback and next action. Never publish that tracker in the
course website or a public repository. In the first meeting, verify a practice
submission from each student before assigning the at-home experiment.

Before class, choose the mentor Google account and the program's link-submission
channel. If school-account restrictions prevent sharing, use a downloaded notebook
and data files through the program's approved channel. The mentor reviews the
notebook rather than relying on a student having left a runtime open.

## Website implementation

- Keep the book source under `site/` with an explicit list of student pages.
  A documentation/book generator should render Markdown and link notebooks.
- Build and deploy only the student site through GitHub Actions. Do not publish
  the whole repository as the site artifact.
- Include notebooks and small public example files in the built download assets.
- Configure repository and branch once a GitHub owner/remote has been chosen;
  derive Colab links from that configuration and check project-site base paths.
- Exclude mentor answer keys and student work from the published site. Excluding
  a file from the site does not hide it in a public source repository; keep any
  private mentor material outside public tracked history.
- Provide a local preview command, record dependencies and check links, navigation,
  notebook downloads and phone/laptop layouts before deployment.
- Test the complete path: website → personal Colab copy → saved answers → mentor
  access → feedback → student revision. Also verify runtime-file persistence.

Expected address after hosting is configured:
`https://<owner>.github.io/alpha-mentorship/`. This is a template, not a live URL.

## Later alternatives

Private GitHub assignment repositories and pull-request feedback are possible if
students later learn GitHub. Direct answer saving inside the book would require
an authenticated storage/submission service or an explicit export/upload workflow.
Neither is necessary for the initial Colab route. Do not add a Save button that
only stores local browser data while implying that the mentor has received it.

## Current status

The site, task notebooks, download assets and deployment workflow are implemented.
Local execution and browser checks are recorded under validation/. Remote creation
and publication require GitHub API authentication; real student/mentor Colab sharing
requires an account-access check. See ../STATUS.md for current delivery status.
