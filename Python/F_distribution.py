#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f as f_d

fig, axs = plt.subplots(2, 2, figsize=(8,4))

# degree of freedom, and the corresponding colors
dfs1   = [3, 5, 10, 20]
dfs2   = [3, 5, 10, 20]
colors = plt.cm.viridis(np.linspace(0, 1, len(dfs1)))

# add lines
for i in [0,1,2,3]:
	for n1,color in zip(dfs1, colors):
		x = np.linspace(f_d.ppf(0.01, n1, dfs2[i]), f_d.ppf(0.99, n1, dfs2[i]), 1000)
		f = f_d.pdf(x, n1, dfs2[i])
		axs[i//2][i%2].plot(x, f, color=color, label='n1={} n2={}'.format(n1,dfs2[i]))
# set axs
axs[0][0].set_xlim([-0.5, 10])
axs[0][0].set_ylim([0, 1.1])
axs[0][0].set_title(r'$F\ Distribution$')
axs[0][0].set_ylabel(r'$f$')
axs[0][0].legend(title='Degrees of Freedom')

axs[0][1].set_xlim([-0.5, 10])
axs[0][1].set_ylim([0, 1.1])
axs[0][1].legend(title='Degrees of Freedom')

axs[1][0].set_xlim([-0.5, 10])
axs[1][0].set_ylim([0, 1.1])
axs[1][0].set_xlabel(r'$x$')
axs[1][0].set_ylabel(r'$f$')
axs[1][0].legend(title='Degrees of Freedom')

axs[1][1].set_xlim([-0.5, 10])
axs[1][1].set_ylim([0, 1.1])
axs[1][1].set_xlabel(r'$x$')
axs[1][1].legend(title='Degrees of Freedom')

# show
plt.tight_layout()
plt.show()
