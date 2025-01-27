# Key Features

```{include} ../../README.md
:start-after: <!-- features -->
:end-before: <!-- .features -->
```

Some of features are described in more detail bellow.

## Mixing MD and RST

The template configures Sphinx to freely mix writting in Markdown and reStructuredText syntax. The detection is based on `.md` or `.rst` file extension.

## Multiple outputs

The template supports output to multiple formats (called _builders_ in Sphinx). By default, only HTML-based builders are tested:

- html - from `features.md` creates `features.html`
- dirhtml - from `features.md` creates `features/index.html` which makes nicer URLs like (`features/`) because `index.html` is served automatically.
- singlehtml - all documents are in single long HTML page

Builders are configured with {confval}`DEFAULT_BUILDER` and {confval}`BUILDERS` variables in `noxfile.py`.

## Preview

For local development, the template can launch webserver, watch for changes in documents, rebuild HTML pages and refresh a browser automatically.

See [preview task](#nox-preview).

<!-- TODO: Screenshot / video (animovaný png/webp?) -->

## Popular Sphinx extensions

The template comes with a few of the most popular Sphinx extension. Extensions are configured to the sane settings.

- [myst-parser](https://myst-parser.readthedocs.io/en/latest/) - Markdown support
- linkify-it-py - Turns URLs like http://documatt.com into links.
- [sphinx-design](https://sphinx-design.readthedocs.io/en/latest/) - For creating grids, cards, dropdowns, tabs, and badges.
- [sphinx_copybutton](https://sphinx-copybutton.readthedocs.io/en/latest/) - adds "Copy to clipboard" button to code examples.
- [sphinxcontrib.mermaid](https://sphinxcontrib-mermaid-demo.readthedocs.io/en/latest/) - Allows to embed [Mermaid](https://mermaid.js.org) graphs in your documents, including general flowcharts, sequence diagrams, gantt diagrams and more.
- [sphinx-reredirects](https://documatt.com/sphinx-reredirects/) - manage redirects for moved pages in `conf.py`
- [sphinx-sitemap](https://sphinx-sitemap.readthedocs.io/en/latest/) - generate `sitemap.xml`

### Adding more extensions

1. Add extension to `pyproject.toml`.
1. Add extension to `extensions` list in `source/conf.py`.
