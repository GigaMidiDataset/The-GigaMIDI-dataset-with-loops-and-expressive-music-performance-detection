"""Test validation methods."""

from __future__ import annotations

from pathlib import Path

SEED = 777

HERE = Path(__file__).parent
MIDI_PATHS_ALL = sorted((HERE / "midi_files").rglob("*.mid"))
# MIDI_PATHS_ALL = [MIDI_PATHS_ALL[-1]]
TEST_LOG_DIR = HERE / "test_logs"
