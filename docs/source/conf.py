from datetime import date

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Copier Sphinx Documentation Template"
author = "Documatt.com, s.r.o."
version = "0.1.0"
copyright = f"{date.today().year}, {author}"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # builtin
    # "sphinx.ext.todo",
    # 3rd party
    "myst_parser",
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "sphinx_reredirects",
    "sphinx_sitemap",
]

nitpicky = True

highlight_language = "none"

exclude_patterns = [
    # Hide files beginning with a dot
    "[.]*",
    # List remaining to exclude from the build
    "Thumbs.db",
    ".DS_Store",
]

# -- Options for internationalisation ----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-internationalisation

language = "en"
locale_dirs = ["locales/"]
gettext_compact = False
translation_progress_classes = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = project

html_baseurl = "https://documatt.com/copier-sphinx-doc-template"
if not html_baseurl.endswith("/"):
    html_baseurl += "/"

html_permalinks_icon = "#"
html_copy_source = False
html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.svg"
html_static_path = ["_static"]
html_extra_path = ["robots.txt"]

html_theme = "furo"
html_theme_options = {}

templates_path = ["_templates"]


# -- Options for Markdown ----------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    "attrs_inline",
    "attrs_block",
    "deflist",
    "tasklist",
    "linkify",
    "substitution",
    "html_image",
]

myst_substitutions = {
    "project": project,
    "author": author,
    "version": version,
}

# Auto-generated heading anchors
# Allows
#       See settings's [HOME option](../ref/settings.md#HOME).
myst_heading_anchors = 6

# Linky only those that begin with a schema (http://, etc.). Now `documatt.com` will not be converted to a link.
myst_linkify_fuzzy_links = False


# -- Options for Mermaid ----------------------------------------------------
# https://pypi.org/project/sphinxcontrib-mermaid/

mermaid_version = "11.0.1"

# -- Options for sitemap ----------------------------------------------------
# https://sphinx-sitemap.readthedocs.io/

# Turn off language alternatives in sitemap
# https://github.com/documatt/cookiecutter-sphinx-docs-template/issues/1
sitemap_locales = [None]

# Default is {lang}{version}{link}, but version is not used in URLs in this project
sitemap_url_scheme = "{lang}{link}"

sitemap_excludes = [
    "search.html",
    "genindex.html",
]
