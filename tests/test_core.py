from pathlib import Path

import matplotlib.pyplot as plt
import pytest
from matplotlib import font_manager

from matfonter import matfonter


def test_missing_file_raises_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        matfonter("does-not-exist.ttf")


def test_non_font_suffix_raises_value_error(tmp_path):
    not_a_font = tmp_path / "not-a-font.txt"
    not_a_font.write_text("placeholder", encoding="utf-8")

    with pytest.raises(ValueError):
        matfonter(not_a_font)


def test_valid_font_sets_global_matplotlib_font_and_unicode_minus():
    font_path = Path(font_manager.findfont("DejaVu Sans"))

    returned_name = matfonter(font_path, unicode_minus=True)

    assert returned_name == "DejaVu Sans"
    assert plt.rcParams["font.family"] == ["DejaVu Sans"]
    assert plt.rcParams["axes.unicode_minus"] is True
