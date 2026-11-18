# Contributing

## Edit the site

- Edit the product homepage in `site/` and documentation in `docs/`. Label drafts and keep private working notes in the ignored `notes/` directory.
- Give each Markdown page a descriptive first heading. Use relative links such as `[Focus](focus-experience.md)` so links work on GitHub and the published site.
- MkDocs generates pages, navigation and search. New pages appear under **More docs** automatically. To place a page in an ordered section or change the theme, edit `mkdocs.yml`.
- Include only assets intended for public distribution in `docs/`.

## Build and preview

```sh
python3 -m venv .venv-docs
.venv-docs/bin/python -m pip install -r requirements-docs.txt
.venv-docs/bin/python scripts/build_site.py
```

The build writes the homepage and docs to `build/site/` and fails on MkDocs warnings,
including broken Markdown links. For live documentation previews, run
`.venv-docs/bin/mkdocs serve`. The product-home link and shared logo use their published URLs.

## Publishing

Pull requests build both parts of the site. Pushes to `main` also deploy to GitHub Pages.
Check the workflow run before reporting a change live. Documentation is served at
`/panda/docs/`, and the old `docs.html` address redirects there.
