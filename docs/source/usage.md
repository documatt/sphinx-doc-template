# Usage

The generated template is regular [Sphinx project](https://www.sphinx-doc.org). You can configure it with `conf.py` and build the docs with `sphinx-build`, etc.

Some tasks are just simple command, but other like preview or translate requires series of operations, including installing dependencies, copying files, etc. These tasks are scripted and centralized in a single file `noxfile.py`. This file is read by [Nox] tool. With running these complex scripts is just `nox -s <task>`, e.g. `nox -s build`.

The following page is reference of configuration variables and tasks in `noxfile.py`.

[Nox]: https://nox.thea.codes/

```{topic} Install Nox globally
If you have uv installed, run `uvx nox -s <task>`. But the `uv tool install nox` will install Nox globally and you can type only `nox -s <task>`.
```

## Configuration

At the beginning of `noxfile.py` is a few configuration variables which influence most of bellow descibed tasks.

```{confval} INDIR
Directory containing Markdown or reStructuredText document sources. By default `source`.
```

```{confval} OUTDIR
Base output directory for builds. By default `build`. But actual output will be in `<outdir>/<builder>/<language>/`, e.g. `build/html/en/`. See [](#outdir-structure).
```

```{confval} DEFAULT_SPHINX_OPTS
Default list of [`sphinx-build` arguments](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) passed to every build task.
```

```{confval} BUILDERS
List of Sphinx builders, i.e. formats, which will be builded by [](#build_all) task. E.g., `["html", "dirhtml"]`.
```

```{confval} DEFAULT_BUILDER
Default builder for [](#nox-build) and [](#nox-preview) tasks.
```

```{confval} LANGUAGES
List of all supported languages, if you want to translate your documentation.By default `[]` (an empty list). E.g., `['es', 'fr', 'de']`. See [list of Sphinx supported languages](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language).
```

```{confval} DEFAULT_LANGUAGE
Default language for [](#nox-build) and [](#nox-preview) tasks.
```

{#nox-tasks}

## Tasks

The generated `noxfile.py` offers the following tasks. You can invoke a task with `nox -s <task>` or multiple tasks with `nox -s <task1> <task2>...`. (In Nox terminology, they are called _sessions_, therefore `-s`.)

{#nox-build}

### build

Build single builder and language. If not specified in commandline argument, default builder and language.

Build to default builder and language:

```
nox -s build
```

Pass build builder/language on commandline:

```
nox -s build -- dirhtml cs
```

### build_all

Build all builders and langauges configured. Creates a `<builder>/<language>/` folder for each builder and language as described in [](#outdir-structure).

```
nox -s build_all
```

### redirect

Create a HTML redirect from the root (`/`) to the default language (e.g., `/en/`).

```
nox -s redirect
```

For example, for html builder, and languages en, cs and he, the following folder and files are created (irrelevant files omitted):

```
├── build
    └── html
        ├── cs
        │   ├── index.html
        │   ├── settings.html
        │   └── ...
        ├── en
        │   ├── index.html
        │   ├── settings.html
        │   └── ...
        └── he
            ├── index.html
            ├── settings.html
            └── ...
```

When you deploy `html/` at e.g., `https://docs.example.com`, it will cause 404 error, because actual URLs to pages are `https://docs.example.com/he/settings.html`, etc.

The task redirect will create the `index.html` at the builder root (`html/`) that redirect visitors to `en/index.html` (if en is default language).

### clean

Deletes {confval}`OUTDIR` directory.

Usually used before other task. E.g., clean and build:

```
nox -s clean build
```

{#nox-preview}

### preview

Build and serve the docs with automatic reload on change. If not specified on commandline, uses default builder and language.

Preview allows see immedially changes made to documents. It starts webserver (by default at http://localhost:8000) and watch for changes. If document is edited, preview will rebuild docs and refresh the webpage.

Preview the default builder and language:

```
nox -s preview
```

Pass preview builder/language on commandline:

```
nox -s preview -- dirhtml cs
```

The output is similar to:

```
nox > Running session preview
nox > Re-using existing virtual environment at .nox/preview.
nox > python -m pip install sphinx==8.1.3 myst-parser==4.0.0 linkify-it-py==2.0.3 sphinx-design==0.6.1 sphinx_copybutton==0.5.2 sphinxcontrib.mermaid==1.0.0 sphinx-reredirects==0.1.5 sphinx-sitemap==2.6.0 furo sphinx-autobuild==2024.10.3
nox > rm -rf build
nox > sphinx-autobuild -b html source build/html/en -j auto -T -q -D language=en -t language_en
[sphinx-autobuild] Starting initial build
[sphinx-autobuild] > python -m sphinx build -b html source build/html/en -j auto -T -q -D language=en -t language_en
[sphinx-autobuild] Serving on http://127.0.0.1:8000
[sphinx-autobuild] Waiting to detect changes...
```

The preview is based on [sphinx-autobuild](https://pypi.org/project/sphinx-autobuild/) tool. Nox installs and runs it for you.

### gettext

Gettext task extracts text strings from documents to message templates (`.pot` files) and create/update existing messages (`.po`).

In multi-lingual documentation, the gettext task should be performed after every document change.

```
nox -s gettext
```

After completion, POT files are temporary stored at `<OUTDIR>/gettext/` and PO files at `source/locales/`. For example, for {confval}`LANGUAGES` set to `["cs", "he"]` the following messages are created:

```
source
└── locales
    ├── cs
    │   └── LC_MESSAGES
    │       ├── demo.po
    │       ├── index.po
    │       ├── sample.po
    │       └── sections.po
    └── he
        └── LC_MESSAGES
            ├── demo.po
            ├── index.po
            ├── sample.po
            └── sections.po
```

```{seealso}
Learn more about [PO/POT formats](https://documatt.com/blog/21/gettext-po-format/) and [gettext translation process](https://documatt.com/blog/21/gettext-translation/) at Tech writer at work blog.
```
