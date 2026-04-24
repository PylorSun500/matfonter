from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager


def matfonter(path_to_ttf, unicode_minus=False):
    """Load a TTF font file into matplotlib and apply it globally."""
    font_path = Path(path_to_ttf).expanduser().resolve()

    if not font_path.is_file():
        raise FileNotFoundError(f"TTF file not found: {font_path}")

    if font_path.suffix.lower() != ".ttf":
        raise ValueError(f"Expected a .ttf file, got: {font_path.suffix}")

    font_manager.fontManager.addfont(str(font_path))
    font_name = font_manager.FontProperties(fname=str(font_path)).get_name()

    plt.rcParams["font.family"] = [font_name]
    plt.rcParams["axes.unicode_minus"] = bool(unicode_minus)

    return font_name
