from pathlib import Path

import nox

# *****************************************************************************
# *** Settings ***
# *****************************************************************************

INDIR = "source"
OUTDIR = "build"

DEFAULT_SPHINX_OPTS = [
    # Speed up the build by using multiple cores
    "-j",
    "auto",
    # Print traceback
    "-T",
    # Be quiet
    "-q",
]

BUILDERS = ["html"] + []
DEFAULT_BUILDER = "html"

LANGUAGES = ["en"] + []
DEFAULT_LANGUAGE = "en"

# Speed up builds by reusing virtualenvs
nox.options.reuse_existing_virtualenvs = True

# Read dependencies from pyproject.toml
dependencies = nox.project.load_toml("pyproject.toml")["project"]["dependencies"]

# No default sessions when "nox" is run (explicit is better than implicit)
nox.options.sessions = []


# *****************************************************************************
# *** Helpers ***
# *****************************************************************************


def construct_path(*args: list[str]) -> str:
    """Constructs a string path from the given list of path components.

    - Prevents using OS-specific path separator.
    - Normalize "" or "/". E.g., ["a", "", "", "/", "b"] to ["a", "b"]
    """
    return str(Path(*args))


def get_outdir_path(builder: str, lang: str) -> str:
    """Constructs the output path."""
    return construct_path(OUTDIR, builder, lang)


def get_sphinx_opts(lang: str) -> list[str]:
    """Generate a default list of Sphinx options for a given language."""
    return DEFAULT_SPHINX_OPTS + [
        # Set lang
        "-D",
        f"language={lang}",
        # Add the tag for including based on a language
        # https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#including-content-based-on-tags
        "-t",
        f"language_{lang}",
    ]


def get_builder_langauge(session) -> tuple[str, str]:
    """Get builder and language. Either defaults or from commandline."""
    if session.posargs:
        return session.posargs[0], session.posargs[1]
    else:
        return DEFAULT_BUILDER, DEFAULT_LANGUAGE


# *****************************************************************************
# *** Nox sessions ***
# *****************************************************************************
# To invoke session(s), use "nox -s <name1>" or "nox -s <name1> <name2>"


def _run_sphinx_builder(session, builder, language):
    session.run(
        "sphinx-build",
        "-b",
        builder,
        INDIR,
        get_outdir_path(builder, language),
        *get_sphinx_opts(language),
        # Warning as error
        "-W",
    )


@nox.session
@nox.parametrize("builder", BUILDERS)
@nox.parametrize("language", LANGUAGES)
def build_all(session, builder, language):
    """Build documentation for all builders/languages."""
    session.install(*dependencies)
    _run_sphinx_builder(session, builder, language)


@nox.session
@nox.parametrize("builder", BUILDERS)
def redirect(session, builder):
    """Create a redirect from the root to the default language."""
    Path(construct_path(OUTDIR, builder, "index.html")).write_text(
        f'<html><head><meta http-equiv="refresh" content="0; url={DEFAULT_LANGUAGE}/index.html"></head></html>'
    )


@nox.session
def build(session):
    """Build documentation for a builder/language."""
    builder, language = get_builder_langauge(session)
    session.install(*dependencies)
    _run_sphinx_builder(session, builder, language)


@nox.session
def clean(session):
    """Clean the build directory."""
    session.run("rm", "-rf", OUTDIR, external=True)


@nox.session
def preview(session):
    """Build and serve the docs with automatic reload on change."""
    builder, language = get_builder_langauge(session)

    session.install(*dependencies, "sphinx-autobuild==2024.10.3")

    clean(session)

    # Build sample and serve
    AUTOBUILD_ARGS = []
    session.run(
        "sphinx-autobuild",
        "-b",
        builder,
        INDIR,
        get_outdir_path(builder, language),
        *get_sphinx_opts(language),
        *AUTOBUILD_ARGS,
    )


@nox.session
def gettext(session):
    """Generate .pot files and update .po files."""
    session.install(*dependencies, "sphinx-intl==2.2.0")

    # Generate .pot files from Sphinx
    session.run(
        "sphinx-build",
        "-b",
        "gettext",
        INDIR,
        construct_path(OUTDIR, "gettext"),
        *DEFAULT_SPHINX_OPTS,
    )

    # Prepare "-l" param for sphinx-intl but exclude default lang
    l_params = []
    langs_without_default = LANGUAGES.copy()
    langs_without_default.remove(DEFAULT_LANGUAGE)
    for lang in langs_without_default:
        l_params.append("-l")
        l_params.append(lang)

    # Update .po from .pot templates
    session.run(
        "sphinx-intl",
        # update .po files
        "update",
        # from .pot files at
        "-p",
        construct_path(OUTDIR, "gettext"),
        # for supported languages
        *l_params,
        # no line wrapping
        "-w",
        "0",
    )
