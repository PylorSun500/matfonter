import os
from pathlib import Path

import pytest


MPLCONFIGDIR = Path(__file__).parent / ".mplconfig"
MPLCONFIGDIR.mkdir(exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIGDIR))

import matplotlib


matplotlib.use("Agg")


@pytest.fixture(autouse=True)
def restore_rcparams():
    import matplotlib.pyplot as plt

    original_family = plt.rcParams["font.family"]
    original_unicode_minus = plt.rcParams["axes.unicode_minus"]
    try:
        yield
    finally:
        plt.rcParams["font.family"] = original_family
        plt.rcParams["axes.unicode_minus"] = original_unicode_minus
