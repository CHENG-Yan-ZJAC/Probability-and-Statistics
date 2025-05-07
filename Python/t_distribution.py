#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

fig, axs = plt.subplots(1, 1, figsize=(8,4))

# degree of freedom, and the corresponding colors
dfs    = [1, 3, 5, 1000]
colors = plt.cm.viridis(np.linspace(0, 1, len(dfs)))

# add lines
for n,color in zip(dfs, colors):
	x = np.linspace(t.ppf(0.01, n), t.ppf(0.99, n), 1000)
	f = t.pdf(x, n)
	axs.plot(x, f, color=color, label='n={}'.format(n))
# set axs
axs.set_xlim([-10, 10])
axs.set_ylim([0, 0.5])
axs.set_title(r'$t\ Distribution$')
axs.set_xlabel(r'$x$')
axs.set_ylabel(r'$f$')
axs.legend(title='Degrees of Freedom')

# show
plt.tight_layout()
plt.show()
