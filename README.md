# Alpha molecular simulation mentorship

A complete introductory teaching package for high-school students: a one-hour
meeting, a guided particle simulation, Colab practice and independent work at home.

**[Student website](https://yaminbens.github.io/alpha-mentorship/)** · **[GitHub repository](https://github.com/yaminbens/alpha-mentorship)**

## Start here
- [Mentor facilitation guide](mentor/facilitation_guide.md)
- [60-minute agenda](meetings/01_introduction/agenda.md)
- [Presentation PDF](meetings/01_introduction/slides.pdf) and [editable source](meetings/01_introduction/slides.md)
- [Guided simulation](meetings/01_introduction/demonstration.md) and [exact browser procedure](simulation/browser_guide.md)
- [Student website source](site/pages/index.md)
- [Reading guide](readings/reading_guide.md) and [first assignment](assignments/01_first_experiment/task.md)
- [Review workflow](mentor/review_workflow.md)
- [Delivery status and remaining account checks](STATUS.md)
- [Detailed implementation checklist](IMPLEMENTATION_PLAN.md)

## First meeting
8 minutes introductions, 10 minutes research, 12 minutes mentor-led simulation,
20 minutes Colab and 10 minutes homework/submission walkthrough. Students need a
laptop, browser, internet and access to Colab. The full experiment is homework.

## Student work
The website explains tasks. Students save personal Colab copies in Drive, preserve
separate data files, share with the designated mentor account and send their link
through the agreed private channel. The website does not store or submit answers.
No GitHub account is required for students using the public notebook templates.
The instructor sets the mentor account/channel in site/config.json or gives them
privately in class; no personal account is inferred from Git configuration.

## Build and preview
```sh
python -m pip install -r requirements.txt
python tools/build_site.py
python -m http.server 8000 --directory dist
```
Open http://localhost:8000. The site is a static, book-style guide with Markdown
sources and an explicit public-content allowlist. No backend or API key is needed.

```sh
python tools/make_notebooks.py
python tools/build_slides.py
python -m pytest tests -q
python tools/check_notebooks.py
```
Optional browser checks: install Playwright and Chromium, then run
`python tools/check_browser.py`. See [contributing](CONTRIBUTING.md).

## Hosting and backup
The source and full Git history are backed up in
[yaminbens/alpha-mentorship](https://github.com/yaminbens/alpha-mentorship).
The [student book](https://yaminbens.github.io/alpha-mentorship/) is deployed through
GitHub Actions. Pushing `main` rebuilds and publishes the student site. Notebook
buttons open the corresponding public GitHub templates in Colab.

For a separate copy, configure `repository` in site/config.json and use
`python tools/publish_github.py --owner OWNER --name REPOSITORY` after GitHub CLI
sign-in. The helper creates a public repository and does not replace unrelated
remote history.

This repo is independent of GNN and lives in its ignored workstreams/ directory.
It must be committed/backed up separately. It uses no GNN datasets, server or GPU.
See [third-party attribution](THIRD_PARTY.md) and [license](LICENSE).
Student records belong outside tracked history; mentor answer keys here are generic
and visible to anyone who can access the source repository.
