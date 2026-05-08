# matfonter

`matfonter` is a tiny helper package for loading a `.ttf` or `.otf` font file into `matplotlib`
and applying it globally before plotting.

## Install

### Local development install

```bash
pip install -e .
```

### PyPI install

```bash
pip install matfonter
```

## Usage

```python
matfonter(path_to_font, unicode_minus=False)
```

- `path_to_font`: path to a `.ttf` or `.otf` font file
- `unicode_minus`: value assigned to `plt.rcParams["axes.unicode_minus"]`
- returns: the resolved matplotlib font family name

```python
from matfonter import matfonter
import matplotlib.pyplot as plt

matfonter("/path/to/your/font.ttf", unicode_minus=False)

plt.plot([1, 2, 3], [3, 1, 4])
plt.title("Custom Font Demo")
plt.show()
```

## Example Font

For CJK examples, a good default is `Source Han Sans SC Heavy` (`思源黑体`), which is
open source under `SIL Open Font License 1.1`, and also easy to find out the effect - obsolutely bold.

- Official project: <https://github.com/adobe-fonts/source-han-sans>
- License: <https://github.com/adobe-fonts/source-han-sans/blob/master/LICENSE.txt>

If you only reference the font in examples, your project license can stay `MIT`.
If you redistribute the font file with your package or repo, keep the font under its
own `OFL-1.1` terms and include the required license notice.