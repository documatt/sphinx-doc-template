"""
Tests if generating template works.
"""

import difflib
import os
import subprocess
from pathlib import Path

from copier import run_copy
from deep_dircmp import DeepDirCmp
from freezegun import freeze_time

PROJECT_ROOT = str(Path(__file__).parent.parent)

# Sync with the date in tests/test_bake/defaults/CHANGELOG.md
FROZEN_TEST_DATE = "2025-01-25"


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


@freeze_time(FROZEN_TEST_DATE)
def test_defaults(workaround_tmp_path: Path, datadir: Path):
    # *** Arrange ***

    # *** Act ***
    run_copy(PROJECT_ROOT, workaround_tmp_path, unsafe=True, defaults=True)

    # *** Assert ***
    deep_compare_dirs(workaround_tmp_path, datadir / "defaults")


def test_license_other(workaround_tmp_path: Path):
    # *** Arrange ***

    # *** Act ***
    run_copy(
        PROJECT_ROOT,
        workaround_tmp_path,
        unsafe=True,
        defaults=True,
        data={"license": "Other"},
    )

    # *** Assert ***
    assert (
        workaround_tmp_path / "LICENSE"
    ).read_text() == "PLEASE REPLACE THIS FILE WITH YOUR LICENSE FILE"


def test_nox_build(workaround_tmp_path: Path):
    """Test if `nox -s build` does not crash."""
    # *** Arrange ***

    # *** Act ***
    run_copy(PROJECT_ROOT, workaround_tmp_path, unsafe=True, defaults=True)

    # *** Assert ***
    subprocess.run(["nox", "-s", "build"], check=True, cwd=workaround_tmp_path)


@freeze_time(FROZEN_TEST_DATE)
def test_nox_build_all_redirect(workaround_tmp_path: Path, datadir: Path):
    """Test if `nox -s build_all redirect` works."""
    # *** Arrange ***

    # *** Act ***
    run_copy(
        PROJECT_ROOT,
        workaround_tmp_path,
        unsafe=True,
        defaults=True,
        data={"other_languages": ["cs", "he"], "other_builders": ["dirhtml"]},
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
    run_copy(
        PROJECT_ROOT,
        workaround_tmp_path,
        unsafe=True,
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
