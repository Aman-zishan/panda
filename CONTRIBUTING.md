# Updating the documentation

Edit or add Markdown files under `docs/`. Pages, sidebar navigation, search and
links between documents are generated automatically with Material for MkDocs.
Use relative Markdown links such as `[Focus](focus-experience.md)` so they work
both in GitHub and on the website. No HTML wrapper or navigation entry is needed
for a new page. Add a descriptive first heading to name it. New pages appear under
“More docs” until placed in one of the ordered sections in `mkdocs.yml`.

The product homepage lives in `site/`. Documentation is published at `/panda/docs/`;
the old `docs.html` address redirects there. Keep drafts labelled as drafts.
Local experiments and private working notes belong in ignored `notes/`, not `docs/`.

## Build locally

```sh
python3 -m venv .venv-docs
.venv-docs/bin/python -m pip install -r requirements-docs.txt
.venv-docs/bin/python scripts/build_site.py
```

The complete Pages artifact is written to ignored `build/site/`. The build fails
on documentation warnings, including broken Markdown links. Dependencies are
installed into the local environment, not the system Python.

For live Markdown editing, run `.venv-docs/bin/mkdocs serve`. This previews the docs;
the product-home link and shared logo use their published GitHub Pages addresses.

## Publishing

Push changes to `main`. The existing Pages workflow builds the homepage and Markdown
documentation together and deploys them to GitHub Pages. Pull requests run the same
build as a check without deploying. Review a successful workflow run before calling
a change live.

Use `mkdocs.yml` for theme settings and the sidebar's section order. The navigation
hook automatically includes Markdown pages not yet assigned to a section. Keep
assets under `docs/` only if they are intended for public distribution.
