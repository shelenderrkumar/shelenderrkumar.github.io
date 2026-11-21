# shelenderrkumar.github.io

[![Check](https://github.com/shelenderrkumar/shelenderrkumar.github.io/actions/workflows/check.yml/badge.svg)](https://github.com/shelenderrkumar/shelenderrkumar.github.io/actions/workflows/check.yml)
[![Deploy](https://github.com/shelenderrkumar/shelenderrkumar.github.io/actions/workflows/static.yml/badge.svg)](https://github.com/shelenderrkumar/shelenderrkumar.github.io/actions/workflows/static.yml)

Source of my personal site, [shelenderrkumar.github.io](https://shelenderrkumar.github.io/).

One hand-written page: `index.html` and `assets/style.css`, with no build step, framework or
tracking. It follows the system light/dark setting, with a toggle. Every push to `main` is
deployed by `.github/workflows/static.yml`.

To preview locally: `python -m http.server` and open http://localhost:8000.

`python3 scripts/check_site.py` checks that every local link and asset exists (also run in CI).

Code is MIT-licensed (see `LICENSE`).
