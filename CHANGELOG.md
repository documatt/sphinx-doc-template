# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2025-04-25

### Added

- Add optional VS Code recommended settings and extensions
- Add common substitutions, like `|project|`, for RST (MD already has it)
- Add Prettier Jinja plugin to template
- Add `strikethrough` MyST extension to generated `conf.py`
- Add `colon_fence` MyST extension to generated `conf.py`
- Add optional `LICENSE` file generation

### Changed

- Move favicon and logo to `_static/images/`
- Update sphinx-reredirect to 0.1.6
- Ask if create `package.json`
- Replace triple backticks with triple colon (colon fences) in sample MD files
- Ask if copy sample documents to the project
- Change `pyproject.toml` project name to `<project_slug>-docs` to prevent conflicts with main project
- Ask to generate flat structure (everything in root instead of `source/`)
- Change default builder to dirhtml
- Use gh:namespace/project instead of full URL in docs
- Use uv as Nox default backend in `noxfile.py`
- Use dynamic year in `conf.py` copyright
- Ask for year (it allowed to remove dependency on jinja time extension)
- Refactor `noxfile.py` to reduce repeating

### Removed

- Stop generating `CHANGELOG.md`

### Fixed

- Fix URLs in `sitemap.xml`
- Search and genindex are not ignored in sitemap for dirhtml
- Missing `_build` in `conf.py` exclude_patterns
- Duplicate dependency in `pyproject.toml`
- Fix typo in `noxfile.py`
- "No other languages" error to gettext Nox task

## [0.2.0] - 2025-02-O3

- feat: add sphinx-copybutton extension
- docs: improve docs

## [0.1.0] - 2025-01-19

Initial version.
