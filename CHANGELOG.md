# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add Prettier Jinja plugin to template
- Enable `strikethrough` MyST extension to template conf.py
- Enable `colon_fence` MyST extension to template conf.py
- Ask to generate flat structure (everything in root instead of `source/`)
- Ask if generate LICENSE file from template
- Add VS Code support (sample settings and recommended extensions) to template
- Add "no other languages" error to gettext task and reduce repeating in template
- Use dynamic year in conf.py copyright in template

### Changed

- Change default builder to dirhtml of template
- Explicitly declare dev deps in template pyproject.toml (nox, sphinx-autobuild, ...)
- Use uv as nox default backend in template
- Ask for year used in copyright, license, etc. (remove dependency on Jinja time)
- Rename project to sphinx-doc-template (instead of copier-sphinx-docs-template)
- Reduce repating code in noxfile.py
- Don't run clean from preview task

### Deprecated

### Removed

- Stop generating CHANGELOG.md

### Fixed

- Fix typo in noxfile.py

### Security

## [0.2.0]

- feat: add sphinx-copybutton extension
- docs: improve docs

## [0.1.0]

Initial version.
