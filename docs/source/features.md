# Features

```{include} ../../README.md
:start-after: <!-- features -->
:end-before: <!-- .features -->
```

Some of the features are described in more detail below.

## Mixing MD and RST

The template configures Sphinx to mix writing in Markdown and reStructuredText syntax freely. The detection is based on the `.md` or `.rst` file extension.

## Multiple outputs

The template supports output to multiple formats (called _builders_ in Sphinx). By default, only HTML-based builders are tested:

- html - from `features.md` creates `features.html`
- dirhtml - from `features.md` creates `features/index.html` making nicer URLs like (`features/`) because `index.html` is served automatically.
- singlehtml - all documents are in a single long HTML page

Builders are configured with {confval}`DEFAULT_BUILDER` and {confval}`BUILDERS` variables in `noxfile.py`.

## Preview

The template can launch a web server for local development, watch for document changes, rebuild HTML pages, and refresh a browser automatically.

See [preview task](#nox-preview).

<!-- TODO: Screenshot / video (animovaný png/webp?) -->

## Popular Sphinx extensions

The template comes with a few of the most popular Sphinx extensions. Extensions are configured to the sane settings.

- [myst-parser](https://myst-parser.readthedocs.io/en/latest/) - Markdown support
- linkify-it-py - Turns URLs like http://documatt.com into links.
- [sphinx-design](https://sphinx-design.readthedocs.io/en/latest/) - For creating grids, cards, dropdowns, tabs, and badges.
- [sphinx_copybutton](https://sphinx-copybutton.readthedocs.io/en/latest/) - adds "Copy to clipboard" button to code examples.
- [sphinxcontrib.mermaid](https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest/) - Allows you to embed Mermaid graphs in your documents, including general flowcharts, sequence diagrams, Gantt diagrams, and more.
- [sphinx-reredirects](https://documatt.com/sphinx-reredirects/) - manage redirects for moved pages in `conf.py`
- [sphinx-sitemap](https://sphinx-sitemap.readthedocs.io/en/latest/) - generate `sitemap.xml`

### Adding more extensions

1. Add extension to `pyproject.toml`.
1. Add extension to `extensions` list in `source/conf.py`.
