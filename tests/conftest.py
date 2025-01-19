import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def workaround_tmp_path():
    """Create and cleanup a temporary directory."""
    # We can't use Pytest tmp_path because of bug in pytest-datadir that does not work with tmp_path.
    # https://github.com/gabrielcnr/pytest-datadir/issues/83

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        yield tmp_path
