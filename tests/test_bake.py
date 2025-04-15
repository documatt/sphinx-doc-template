"""
Tests if generating template works.
"""

import difflib
import os
import subprocess
from pathlib import Path

from copier import run_copy
from deep_dircmp import DeepDirCmp

PROJECT_ROOT = str(Path(__file__).parent.parent)

# Sync with the date in tests/test_bake/defaults/LICENSE
TEST_YEAR = "2025"


def deep_compare_dirs(
    left: Path, right: Path, diff_files=[], left_only=[], right_only=[]
):
    """Compare dirs recursively, including file content, and ignore .pickle and .doctree files."""
    cmp = DeepDirCmp(left, right)

    def ignored_names(name):
        # binary or files which always differ
        ignored_names = [".pickle", ".doctree", ".doctrees", ".copier-answers.yml"]
        return not any(name.endswith(ignored) for ignored in ignored_names)

    def get_diff_files(cmp):
        """Filter out files based on the ignored names list."""
        diff_files = list(filter(ignored_names, cmp.get_diff_files_recursive()))

        # show diff of diff_files
        for file in diff_files:
            show_diff(cmp.left / file, cmp.right / file)

        return diff_files

    def get_left_files(cmp):
        return list(filter(ignored_names, cmp.get_left_only_recursive()))

    def get_right_files(cmp):
        return list(filter(ignored_names, cmp.get_right_only_recursive()))

    assert get_diff_files(cmp) == diff_files, "Different file contents"
    assert get_left_files(cmp) == left_only, "Left only files"
    assert get_right_files(cmp) == right_only, "Right only files"


def shallow_compare_dirs(dir1, dir2):
    def get_files(directory):
        file_set = set()
        for root, _, files in os.walk(directory):
            for file in files:
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                file_set.add(relative_path)
        return file_set

    files_in_dir1 = get_files(dir1)
    files_in_dir2 = get_files(dir2)

    assert files_in_dir1 == files_in_dir2


def show_diff(file1: Path, file2: Path):
    """Show the diff between two files."""
    with open(file1, "r") as f1, open(file2, "r") as f2:
        f1_lines = f1.readlines()
        f2_lines = f2.readlines()

    diff = difflib.unified_diff(
        f1_lines, f2_lines, fromfile=str(file1), tofile=str(file2)
    )
    for line in diff:
        print(line, end="")


def copier_copy(workaround_tmp_path, **kwargs):
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
    copier_copy(workaround_tmp_path, defaults=True)

    # *** Assert ***
    deep_compare_dirs(workaround_tmp_path, datadir / "default__source")


def test_default__flat(workaround_tmp_path: Path, datadir: Path):
    """Test if defaults with the flat layout works."""
    # *** Arrange ***

    # *** Act ***
    copier_copy(workaround_tmp_path, defaults=True, data={"flat": True})

    # *** Assert ***
    deep_compare_dirs(workaround_tmp_path, datadir / "default__flat")


def test_with_sample__source(workaround_tmp_path: Path, datadir: Path):
    """Test if the source layout with samples works."""
    # *** Arrange ***

    # *** Act ***
    copier_copy(workaround_tmp_path, defaults=True, data={"with_sample": True})

    # *** Assert ***
    deep_compare_dirs(workaround_tmp_path, datadir / "with_sample__source")


def test_with_samples__flat(workaround_tmp_path: Path, datadir: Path):
    """Test if the flat layout with samples works."""
    # *** Arrange ***

    # *** Act ***
    copier_copy(
        workaround_tmp_path, defaults=True, data={"flat": True, "with_sample": True}
    )

    # *** Assert ***
    deep_compare_dirs(workaround_tmp_path, datadir / "with_sample__flat")


def test_no_license(workaround_tmp_path: Path):
    # *** Arrange ***

    # *** Act ***
    copier_copy(
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
    copier_copy(workaround_tmp_path, defaults=True)

    # *** Assert ***
    subprocess.run(["nox", "-s", "build"], check=True, cwd=workaround_tmp_path)


def test_nox_build_flat(workaround_tmp_path: Path):
    """Test if `nox -s build` of flat layout does not crash."""
    # *** Arrange ***

    # *** Act ***
    copier_copy(workaround_tmp_path, defaults=True, data={"flat": True})

    # *** Assert ***
    subprocess.run(["nox", "-s", "build"], check=True, cwd=workaround_tmp_path)


def test_nox_build_all_redirect(workaround_tmp_path: Path, datadir: Path):
    """Test if `nox -s build_all redirect` works."""
    # *** Arrange ***

    # *** Act ***
    copier_copy(
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
    copier_copy(
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
