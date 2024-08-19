"""Testing tokenization, making sure the data integrity is not altered."""

from __future__ import annotations

from pathlib import Path

import pytest
from symusic import Score

from loops_nomml import detect_loops

from .utils_tests import MIDI_PATHS_ALL


@pytest.mark.parametrize("file_path", MIDI_PATHS_ALL, ids=lambda p: p.name)
def test_one_track_midi_to_tokens_to_midi(file_path: Path):
    score = Score(file_path)
    _ = detect_loops(score)
