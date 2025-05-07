#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
f = (1 / np.sqrt(2*np.pi)) * np.exp(-0.5 * (x**2))
F = np.cumsum(f) / 100

fig, axs = plt.subplots(1, 2, figsize=(8,2))

axs[0].plot(x, f)
axs[0].set_xlim([-10, 10])
axs[0].set_ylim([0, 0.5])
axs[0].set_xlabel(r'$x$')
axs[0].set_ylabel(r'$\varphi(x)$')
axs[0].axhline(1/(np.sqrt(2*np.pi)), color='r', ls='--', lw=1)
axs[0].axvline(0,  color='r', ls='--', lw=1)
axs[0].axvline(-1, color='r', ls='--', lw=1)
axs[0].axvline(1,  color='r', ls='--', lw=1)

axs[1].plot(x, F)
axs[1].set_xlim([-10, 10])
axs[1].set_ylim([0, 1.1])
axs[1].set_xlabel(r'$x$')
axs[1].set_ylabel(r'$\Phi(x)$')

plt.tight_layout()
plt.show()

