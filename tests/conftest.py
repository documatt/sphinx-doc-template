import difflib
import os
import tempfile
from pathlib import Path

import pytest
from deep_dircmp import DeepDirCmp


@pytest.fixture
def workaround_tmp_path():
    """Create and cleanup a temporary directory."""
    # We can't use Pytest tmp_path because of bug in pytest-datadir that does not work with tmp_path.
    # https://github.com/gabrielcnr/pytest-datadir/issues/83

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        yield tmp_path


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
