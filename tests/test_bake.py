"""
Tests if generating template works.
"""

import subprocess
from pathlib import Path

from copier import run_copy

from tests.conftest import deep_compare_dirs, shallow_compare_dirs

PROJECT_ROOT = str(Path(__file__).parent.parent)


def call_copier(workaround_tmp_path, **kwargs):
    """Run copier to generate the project."""
    run_copy(
        PROJECT_ROOT,
        workaround_tmp_path,
        # ! When running test locally (on dirty repo), add vcs_ref="HEAD" to run_copy()
        vcs_ref="HEAD",
        # Equivalent to --trust
        unsafe=True,
        **kwargs,
    )


def test_default__source(workaround_tmp_path: Path, datadir: Path):
    """Test if defaults with the source layout works."""
    # *** Arrange ***

    # *** Act ***
    call_copier(workaround_tmp_path, defaults=True)

    # *** Assert ***
    deep_compare_dirs(workaround_tmp_path, datadir / "default__source")


def test_default__flat(workaround_tmp_path: Path, datadir: Path):
    """Test if defaults with the flat layout works."""
    # *** Arrange ***

    # *** Act ***
    call_copier(workaround_tmp_path, defaults=True, data={"flat": True})

    # *** Assert ***
    deep_compare_dirs(workaround_tmp_path, datadir / "default__flat")


def test_with_sample__source(workaround_tmp_path: Path, datadir: Path):
    """Test if the source layout with samples works."""
    # *** Arrange ***

    # *** Act ***
    call_copier(workaround_tmp_path, defaults=True, data={"with_sample": True})

    # *** Assert ***
    deep_compare_dirs(workaround_tmp_path, datadir / "with_sample__source")


def test_with_samples__flat(workaround_tmp_path: Path, datadir: Path):
    """Test if the flat layout with samples works."""
    # *** Arrange ***

    # *** Act ***
    call_copier(
        workaround_tmp_path, defaults=True, data={"flat": True, "with_sample": True}
    )

    # *** Assert ***
    deep_compare_dirs(workaround_tmp_path, datadir / "with_sample__flat")


def test_no_license(workaround_tmp_path: Path):
    # *** Arrange ***

    # *** Act ***
    call_copier(
        workaround_tmp_path,
        defaults=True,
        data={"license": "None"},
    )

    # *** Assert ***
    assert (workaround_tmp_path / "LICENSE").exists() is False, (
        "LICENSE file should not be created"
    )


def test_nox_build_source(workaround_tmp_path: Path):
    """Test if `nox -s build` of source layout does not crash."""
    # *** Arrange ***

    # *** Act ***
    call_copier(workaround_tmp_path, defaults=True)

    # *** Assert ***
    subprocess.run(["nox", "-s", "build"], check=True, cwd=workaround_tmp_path)


def test_nox_build_flat(workaround_tmp_path: Path):
    """Test if `nox -s build` of flat layout does not crash."""
    # *** Arrange ***

    # *** Act ***
    call_copier(workaround_tmp_path, defaults=True, data={"flat": True})

    # *** Assert ***
    subprocess.run(["nox", "-s", "build"], check=True, cwd=workaround_tmp_path)


def test_nox_build_all_redirect(workaround_tmp_path: Path, datadir: Path):
    """Test if `nox -s build_all redirect` works."""
    # *** Arrange ***

    # *** Act ***
    call_copier(
        workaround_tmp_path,
        defaults=True,
        data={"other_languages": ["cs", "he"], "other_builders": ["html"]},
    )
    subprocess.run(
        ["nox", "-s", "build_all", "redirect"], check=True, cwd=workaround_tmp_path
    )

    # *** Assert ***
    deep_compare_dirs(
        workaround_tmp_path / "build", datadir / "nox_build_all_redirect" / "build"
    )


def test_nox_gettext(workaround_tmp_path: Path, datadir: Path):
    """Test if `nox -s gettext` works."""
    # *** Arrange ***

    # *** Act ***
    call_copier(
        workaround_tmp_path,
        defaults=True,
        data={"other_languages": ["cs", "he"]},
    )
    subprocess.run(["nox", "-s", "gettext"], check=True, cwd=workaround_tmp_path)

    # *** Assert ***
    # Does it creates expected .po files in source/locales?
    # Do not compare contens because they contain different `POT-Creation` header values.
    shallow_compare_dirs(
        workaround_tmp_path / "source" / "locales",
        datadir / "nox_gettext" / "source" / "locales",
    )
    # Does it creates expected .pot file in build/gettext?
    shallow_compare_dirs(
        workaround_tmp_path / "build" / "gettext",
        datadir / "nox_gettext" / "build" / "gettext",
    )
