import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import matfonter as mf

# Recommended CJK example font:
# Source Han Sans SC Heavy (SIL OFL 1.1)
# https://github.com/adobe-fonts/source-han-sans
mf.matfonter(PROJECT_ROOT / "third_party/fonts/SourceHanSansCN-Heavy.otf")

y1 = np.array([12, 5, 15, 10, 6])
y2 = [6, 8, 16, 11, 7]
x = np.arange(len(y1))
tk = [chr(i) for i in range(97, 97+5)]
bar_width = 0.4
bar0A = plt.bar(x, y1, width=0.4, label = "产品A", tick_label = "tk")
bar0B = plt.bar(x, y2, width=0.4, label = "产品B",bottom=y1)
for bA, bB in zip(bar0A, bar0B):
    plt.text(bA.get_x() + bar_width/3, bA.get_height(), bA.get_height())
    plt.text(bA.get_x() + bar_width/3, bB.get_height() + bA.get_height(), bB.get_height())
plt.legend()
plt.xlabel('产品说明')
plt.ylabel('产量')
plt.title('两组柱形图示例')

plt.show()
