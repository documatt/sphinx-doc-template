# Usage

The generated template is regular [Sphinx project](https://www.sphinx-doc.org). You can configure it with `conf.py` and build the docs with `sphinx-build`, etc.

Some tasks are simple commands, but others, like preview or translate, require a series of operations, including installing dependencies, copying files, etc. These tasks are scripted and centralized in a single file `noxfile.py`. This file is read by the [Nox] tool. Running these complex scripts is just `nox -s <task>`, e.g. `nox -s build`.

The following page is the reference of configuration variables and tasks in `noxfile.py`.

[Nox]: https://nox.thea.codes/

:::{topic} Install Nox globally
If you have uv installed, run `uvx nox -s <task>`. But the `uv tool install nox` will install Nox globally, and you can type only `nox -s <task>`.
:::

## Configuration

At the beginning of `noxfile.py` are a few configuration variables that influence most of the below described tasks.

:::{confval} INDIR
Directory containing Markdown or reStructuredText document sources. By default, `source`.
:::

:::{confval} OUTDIR
Base output directory for builds. By default, `build`. But the actual output will be in `<outdir>/<builder>/<language>/`, e.g. `build/html/en/`. See [](#outdir-structure).
:::

:::{confval} DEFAULT_SPHINX_OPTS
Default list of [`sphinx-build` arguments](https://www.sphinx-doc.org/en/master/man/sphinx-build.html) passed to every build task.
:::

:::{confval} SPHINX_AUTOBUILD_OPTS
List of [`sphinx-autobuild` arguments](https://github.com/sphinx-doc/sphinx-autobuild) passed to the [](#nox-preview) task.

For example, `--port 0` to use first found free port instead of default 8000.
:::

:::{confval} BUILDERS
List of Sphinx builders, i.e., formats, which will be built by [](#build_all) task. E.g., `["html", "dirhtml"]`.
:::

:::{confval} DEFAULT_BUILDER
Default builder for [](#nox-build) and [](#nox-preview) tasks.
:::

:::{confval} LANGUAGES
List of all supported languages if you want to translate your documentation.By default, `[]` (an empty list). E.g., `['es', 'fr', 'de']`. See [list of Sphinx supported languages](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language).
:::

:::{confval} DEFAULT_LANGUAGE
Default language for [](#nox-build) and [](#nox-preview) tasks.
:::

{#nox-tasks}

## Tasks

The generated `noxfile.py` offers the following tasks. You can invoke a task with `nox -s <task>` or multiple tasks with `nox -s <task1> <task2>...`. (In Nox terminology, they are called _sessions_, therefore `-s`.)

{#nox-build}

### build

Build single builder and language. If not specified on the commandline, it uses default builder and language. Creates a `<builder>/<language>/` folder for each builder and language as described in [](#outdir-structure).

Build to default builder and language:

```
nox -s build
```

Pass build builder/language on commandline:

```
nox -s build -- dirhtml cs
```

Will fail on error to prevent dead links and other problems.

### build_all

Build all builders and languages configured. Creates a `<builder>/<language>/` folder for each builder and language as described in [](#outdir-structure).

If you have no multiple languages and builders, it will do the same as [](#nox-build) task.

```
nox -s build_all
```

Will fail on error to prevent dead links and other problems.

### redirect

Create an HTML redirect from the root (`/`) to the default language (e.g., `/en/`).

```
nox -s redirect
```

For example, for html builder and languages en, cs and he, the following folder and files are created (irrelevant files omitted):

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

When you deploy `html/` at e.g., `https://docs.example.com`, it will cause a 404 error because the actual URLs to pages are `https://docs.example.com/he/settings.html`, etc.

The task redirect will create the `index.html` at the builder root (`html/`) that redirects visitors to `en/index.html` (if en is the default language).

### clean

Deletes {confval}`OUTDIR` directory.

Usually used before other tasks. E.g., clean and build:

```
nox -s clean build
```

{#nox-preview}

### preview

Build and serve the docs with automatic reload on change. If not specified on the commandline, it uses default builder and language.

Preview allows users to see changes made to documents immediately. It starts the web server (by default at http://localhost:8000) and watches for changes. If a document is edited, the preview rebuilds the documents and refreshes the webpage.

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

Gettext task extracts text strings from documents to message templates (`.pot` files) and creates/updates existing messages (`.po`).

In multi-lingual documentation, the gettext task should be performed after every document change.

```
nox -s gettext
```

After completion, POT files are temporarily stored at `<OUTDIR>/gettext/` and PO files at `source/locales/`. For example, for {confval}`LANGUAGES` set to `["cs", "he"]`, the following messages are created:

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

:::{seealso}
Learn more about [PO/POT formats](https://documatt.com/blog/21/gettext-po-format/) and [gettext translation process](https://documatt.com/blog/21/gettext-translation/) at Tech writer at work blog.
:::
