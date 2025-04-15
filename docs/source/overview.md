# Overview

:::{include} ../../README.md
:start-after: <!-- overview -->
:end-before: <!-- .overview -->
:::

{#file-structure}

## File layout structure

{{ project }} follows a fairly specific file system layout. This standardized structure eases maintenance and switching between multiple projects.

All tasks, like build and preview, are in the [noxfile.py file](#nox-tasks), and this documentation assumes the structure.

```
.
├── build/                  ┐
│   └── <builder>/          | Output files
│       └── <language>/     |
│           └── ...         ┘
├── source/                 ┐
│   ├── _static/            |
│   │   ├── favicon.svg     |
│   │   └── logo.svg        |
│   ├── _templates/         | Sphinx project sources
│   ├── conf.py             | (documents, images, conf.py)
│   ├── index.md            |
│   ├── overview.md         |
│   └── ...                 ┘
├── .gitignore              ┐
├── CHANGELOG.md            |
├── LICENSE                 |
├── noxfile.py              | Meta files
├── package-lock.json       |
├── package.json            |
└── pyproject.toml          ┘
```

The files and folders are for three purposes:

- Sphinx project sources. Regular files found in Sphinx projects like .md, .rst, images, conf.py.
- When built by [tasks](#nox-tasks), output goes to (by default) to `build/`.
- Meta files. Not the documentation itself. Like dependencies in `pyproject.toml`, license, standard `.gitignore`, etc.

Everything except the output directory should be versioned.

{#outdir-structure}

## Output directory structure

The output directory (the {confval}`OUTDIR`) is organized to `<builder>/<language>/` directory layout.

For example, for builders dirhtml and html, and languages en, cs, and he, the following folder and files are created (irrelevant files omitted):

```
.
├── build/
    ├── dirhtml/
    │    ├── cs/
    │    │    ├── index.html
    │    │    ├── sample/
    │    │    │   └── index.html
    │    │    ├── search/
    │    │    │   └── index.html
    │    │    └── sections/
    │    │    └── index.html
    │    ├── en/
    │    │   ├── index.html
    │    │   ├── sample/
    │    │   │   └── index.html
    │    │   ├── search/
    │    │   │   └── index.html
    │    │   └── section/
    │    │   └── index.html
    │    └── he/
    │        ├── index.html
    │        ├── sample/
    │        │   └── index.html
    │        ├── search/
    │        │   └── index.html
    │        └── sections/
    │        └── index.html
    └── html/
        ├── cs/
        │   ├── index.html
        │   ├── sample.html
        │   ├── search.html
        │   └── sections.html
        ├── en/
        │   ├── index.html
        │   ├── sample.html
        │   ├── search.html
        │   └── sections.html
        └── he/
            ├── index.html
            ├── sample.html
            ├── search.html
            └── sections.html
```
