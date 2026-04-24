# matfonter

`matfonter` is a tiny helper package for loading a `.ttf` font file into `matplotlib`
and applying it globally before plotting.

## Install

### Local development install

```bash
pip install -e .
```

### Regular install

```bash
pip install .
```

## Usage

```python
from matfonter import matfonter
import matplotlib.pyplot as plt

matfonter("/path/to/your/font.ttf", unicode_minus=False)

plt.plot([1, 2, 3], [3, 1, 4])
plt.title("Custom Font Demo")
plt.show()
```

## API

```python
matfonter(path_to_ttf, unicode_minus=False)
```

- `path_to_ttf`: path to a `.ttf` font file
- `unicode_minus`: value assigned to `plt.rcParams["axes.unicode_minus"]`
- returns: the resolved matplotlib font family name