# Quickstart

## Setup

[Copier]: https://copier.readthedocs.io/
[Nox]: https://nox.thea.codes/
[uv]: https://docs.astral.sh/uv/

You will need Python and two Python tools:

- [Copier]: scaffolding tool that will generate from this template a Sphinx project on your disk
- [Nox]: automation tool for easier building docs from a project sources

The recommended way to install and running is using the [uv] tool. The uv can even install Python for you, if you don't have it already.

1. [**Install uv**](https://docs.astral.sh/uv/getting-started/installation/) for your environment.

   ```{seealso}
   See [Copier docs][Copier] and [Nox docs][Nox] for other instalation options, if uv is not suitable for you.
   ```

## Tutorial

1. **Answer questions.** Open the terminal, choose a destination folder (use `.` for current), and follow the wizard. E.g.,:

   ```
   uvx --with jinja2-time copier copy --trust https://github.com/documatt/copier-sphinx-docs-template my-documentation
   ```

   This a bit lenghty command handles everything. It will install Copier, its `jinja2-time` dependency and call Copier with `--trust` to allow use `jinja2-time`.

1. **Examine the template.** A new shiny folder, e.g., `my-documentation`, with a Sphinx doc project has been created for you.

   ```
   $ cd my-documentation
   $ tree
   .
   ├── CHANGELOG.md
   ├── LICENSE
   ├── noxfile.py
   ├── package-lock.json
   ├── package.json
   ├── pyproject.toml
   └── source
       ├── _static
       │   ├── favicon.svg
       │   └── logo.svg
       ├── _templates
       ├── conf.py
       ├── demo.rst
       ├── index.md
       ├── robots.txt
       ├── sample.md
       └── sections.md
   ```

   Learn more about template's [file structure](#file-structure).

1. **Examine `noxfile.py`.** This file is read by [Nox] tool and contains common tasks as a "build HTML", "preview", etc.

   Some tasks are just simple command, but preview or translate requires series of operations, including installing dependencies, copying files, etc. With Nox will run these complex scripts with just `nox -s <task>` command.

   Learn more about available Nox tasks in [](usage.md).

1. **Build the docs.** For example, to build the docs for default language and format, `cd` to just created folder and run `nox -s build`.

   Because you have uv installed, you can use it to install and launch Nox with `uvx`:

   ```
   cd my-documentation
   uvx nox -s build
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

1. **Enjoy.** See other all the cool [features](features.md) provided by the template.
