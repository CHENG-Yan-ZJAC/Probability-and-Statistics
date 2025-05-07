#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 10, 0.01)

f = np.exp(-1 * (x + 1))
f[f>1] = 0
F = 1 - np.exp(-1 * (x + 1))
F[F<0] = 0

fig, axs = plt.subplots(1, 2, figsize=(8,2))
axs[0].plot(x, f)
axs[0].set_xlim([-2,10])
axs[0].set_ylim([0,2.5])
axs[0].set_xlabel(r'$x$')
axs[0].set_ylabel(r'$f(x)$')
axs[0].set_title(r'$Standardization$')
axs[1].plot(x, F)
axs[1].set_xlim([-2,10])
axs[1].set_ylim([0,1.1])
axs[1].set_xlabel(r'$x$')
axs[1].set_ylabel(r'$F(x)$')

plt.tight_layout()
plt.show()
