# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add VS Code support (sample settings and recommended extensions)
- Add "no other languages" error to gettext task and reduce repeating
- Use dynamic year in conf.py copyright

### Changed

- Explicitly declare dev deps in generated pyproject.toml (nox, sphinx-autobuild, ...)
- Use uv as nox default backend in generated projects
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
