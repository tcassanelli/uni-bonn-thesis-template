# AUTHOR: TOMAS CASSANELLI

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import golden

# to have the same configuration in font as in your min.tex file, I used a
# plotting style for matplitlib, simply add the line

plt.style.use('master_thesis_sty.mplstyle')

# Width found in LaTeX file
width = 6.85829  # in

# Let's create simple figure

x1 = np.random.normal(0, 10, 1000)
x2 = np.random.normal(0, 10, 1000)


fig, axes = plt.subplots(figsize=(width, width / golden / 2), ncols=2)

axes[0].plot(x1, c='r')
axes[1].plot(x2)

for ax in axes:
    ax.set_xlabel('$x$ [m]')
    ax.set_ylabel('$y$ [m]')

fig.subplots_adjust(left=.08, bottom=.18, right=.99, top=.96)
fig.savefig('../figures/figure_example.pdf')

