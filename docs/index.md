# Cookiecutter Sphinx Documentation Template

## Overview

### About

Only HTML or HTML-based builders.

### Quickstart

You will need two Python tools:

- Copier to create project from the template
- Nox to "use" (generate docs) from the projected

The recommended way to install and running is [uv](https://docs.astral.sh/uv/). Uv can even install Python for you, if you don't have it already.

See [Copier docs](https://copier.readthedocs.io/) and [Nox docs](https://nox.thea.codes/) for other instalation options.

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/) for your environment.

1. Open the terminal, choose a destination folder (use `.` for current), and follow the wizard. E.g.,:

   ```
   uv run copier copy --trust https://github.com/documatt/cookiecutter-sphinx-docs-template my-documentation
   ```

1. A new shiny folder, e.g., `my-documentation`, with a Sphinx doc project has been created for you.

1. Install nox, the task runner. The generated Sphinx project has noxfile.py which contains common tasks as a "build HTML", "preview", etc.

   With uv with `uv tool install nox`.

1. Build the docs. For example, to build the docs for default language and format, `cd` to just created folder and run `nox -s build`.

   Because you have uv installed, you can use it to install and launch Nox in one command with `uvx`.

   ```
   cd my-documentation
   nox -s build
   ```

   The example output:

   ```
   nox > Running session build
   nox > Creating virtual environment (virtualenv) using python3.11 in .nox/build
   nox > python -m pip install sphinx==8.1.3 myst-parser==4.0.0 linkify-it-py==2.0.3 sphinx-design==0.6.1 sphinx_copybutton==0.5.2 sphinxcontrib.mermaid==1.0.0 sphinx-reredirects==0.1.5 sphinx-sitemap==2.6.0
   nox > sphinx-build -b html source build/html/en -j auto -T -q -D language=en -t language_en -W
   nox > Session build was successful.
   ```

   The Nox will handle of everything - installing Sphinx and its extensions and trigger Sphinx build.

1. Enjoy. See other all the cool [features](#features) provided by the template.

### Features

TODO: include to z README (kde features označit komentářemi)

## Structure

Driven

### File layout

{{ project }} follows failry specific project layout and structure. This standarized structure eases maintenance and switching between multiple projects. Also, all actions in `noxfile.py` assumes this structure like [preview with automatic refresh on change](#preview-nox--s-preview).

```
pycounts
├── CHANGELOG.md               ┐
├── CONDUCT.md                 │
├── CONTRIBUTING.md            │
├── docs                       │ Package documentation
│   └── ...                    │
├── LICENSE                    │
├── README.md                  ┘
├── pyproject.toml             ┐
├── src                        │
│   └── pycounts               │ Package source code, metadata,
│       ├── __init__.py        │ and build instructions
│       ├── moduleA.py         │
│       └── moduleB.py         ┘
└── tests                      ┐
    └── ...                    ┘ Package tests
```

## Usage (CLI)

### Build HTML (nox -s build)

### Preview (nox -s preview)

### Localize

## VS Code goodies

---

## Deployment

- published at root / (not subfolder)

## File system organization

## Sphinx configuration

html_baseurl = 'https://documatt.com/blog'

## Nox configuration

### Supported builders

### Supported languages

### Building docs

Default builder/langauge

```
nox -s build
```

Specify builder/language

```
nox -s build -- html cs
```

### Build all builders/languages

```
nox -s build_all
```

### Redirect to default language

```
nox -s build_all redirect
```

```
nox -s build_all redirect                                ⏱ 10:25:14
nox > Running session build_all(language='en', builder='html')
nox > Creating virtual environment (virtualenv) using python in .nox/build_all-language-en-builder-html
nox > python -m pip install sphinx==8.1.3 myst-parser==4.0.0 linkify-it-py==2.0.3 sphinx-design==0.6.1 sphinx_copybutton==0.5.2 sphinxcontrib.mermaid==1.0.0 sphinx-reredirects==0.1.5 sphinx-sitemap==2.6.0
nox > sphinx-build -b html source build/html/en -j auto -T -q -D language=en -t language_en -W
nox > Session build_all(language='en', builder='html') was successful.
nox > Running session build_all(language='cs', builder='html')
nox > Creating virtual environment (virtualenv) using python in .nox/build_all-language-cs-builder-html
nox > python -m pip install sphinx==8.1.3 myst-parser==4.0.0 linkify-it-py==2.0.3 sphinx-design==0.6.1 sphinx_copybutton==0.5.2 sphinxcontrib.mermaid==1.0.0 sphinx-reredirects==0.1.5 sphinx-sitemap==2.6.0
nox > sphinx-build -b html source build/html/cs -j auto -T -q -D language=cs -t language_cs -W
nox > Session build_all(language='cs', builder='html') was successful.
nox > Running session build_all(language='ua', builder='html')
nox > Creating virtual environment (virtualenv) using python in .nox/build_all-language-ua-builder-html
nox > python -m pip install sphinx==8.1.3 myst-parser==4.0.0 linkify-it-py==2.0.3 sphinx-design==0.6.1 sphinx_copybutton==0.5.2 sphinxcontrib.mermaid==1.0.0 sphinx-reredirects==0.1.5 sphinx-sitemap==2.6.0
nox > sphinx-build -b html source build/html/ua -j auto -T -q -D language=ua -t language_ua -W
nox > Session build_all(language='ua', builder='html') was successful.
nox > Running session build_all(language='en', builder='dirhtml')
nox > Creating virtual environment (virtualenv) using python in .nox/build_all-language-en-builder-dirhtml
nox > python -m pip install sphinx==8.1.3 myst-parser==4.0.0 linkify-it-py==2.0.3 sphinx-design==0.6.1 sphinx_copybutton==0.5.2 sphinxcontrib.mermaid==1.0.0 sphinx-reredirects==0.1.5 sphinx-sitemap==2.6.0
nox > sphinx-build -b dirhtml source build/dirhtml/en -j auto -T -q -D language=en -t language_en -W
nox > Session build_all(language='en', builder='dirhtml') was successful.
nox > Running session build_all(language='cs', builder='dirhtml')
nox > Creating virtual environment (virtualenv) using python in .nox/build_all-language-cs-builder-dirhtml
nox > python -m pip install sphinx==8.1.3 myst-parser==4.0.0 linkify-it-py==2.0.3 sphinx-design==0.6.1 sphinx_copybutton==0.5.2 sphinxcontrib.mermaid==1.0.0 sphinx-reredirects==0.1.5 sphinx-sitemap==2.6.0
nox > sphinx-build -b dirhtml source build/dirhtml/cs -j auto -T -q -D language=cs -t language_cs -W
nox > Session build_all(language='cs', builder='dirhtml') was successful.
nox > Running session build_all(language='ua', builder='dirhtml')
nox > Creating virtual environment (virtualenv) using python in .nox/build_all-language-ua-builder-dirhtml
nox > python -m pip install sphinx==8.1.3 myst-parser==4.0.0 linkify-it-py==2.0.3 sphinx-design==0.6.1 sphinx_copybutton==0.5.2 sphinxcontrib.mermaid==1.0.0 sphinx-reredirects==0.1.5 sphinx-sitemap==2.6.0
nox > sphinx-build -b dirhtml source build/dirhtml/ua -j auto -T -q -D language=ua -t language_ua -W
nox > Session build_all(language='ua', builder='dirhtml') was successful.
nox > Running session redirect(builder='html')
nox > Creating virtual environment (virtualenv) using python in .nox/redirect-builder-html
nox > Session redirect(builder='html') was successful.
nox > Running session redirect(builder='dirhtml')
nox > Creating virtual environment (virtualenv) using python in .nox/redirect-builder-dirhtml
nox > Session redirect(builder='dirhtml') was successful.
nox > Ran multiple sessions:
nox > * build_all(language='en', builder='html'): success
nox > * build_all(language='cs', builder='html'): success
nox > * build_all(language='ua', builder='html'): success
nox > * build_all(language='en', builder='dirhtml'): success
nox > * build_all(language='cs', builder='dirhtml'): success
nox > * build_all(language='ua', builder='dirhtml'): success
nox > * redirect(builder='html'): success
nox > * redirect(builder='dirhtml'): success
```

### Clean build dir

```
nox -s clean
```

```
nox -s clean build
```

### Live preview

Default builder and language

```
nox -s preview
```

Pass builder and language on commandline

```
nox -s preview -- dirhtml cs
```
