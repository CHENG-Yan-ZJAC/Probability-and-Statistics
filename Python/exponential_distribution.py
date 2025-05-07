#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

lmd_1 = 0.5
lmd_2 = 2.0

x = np.arange(-2, 10, 0.01)

f_1 = lmd_1 * np.exp(-lmd_1 * x)
f_1[f_1>lmd_1] = 0
F_1 = 1 - np.exp(-lmd_1 * x)
F_1[F_1<0] = 0

f_2 = lmd_2 * np.exp(-lmd_2 * x)
f_2[f_2>lmd_2] = 0
F_2 = 1 - np.exp(-lmd_2 * x)
F_2[F_2<0] = 0

fig, axs = plt.subplots(2, 2, figsize=(8,4))
axs[0][0].plot(x, f_1)
axs[0][0].set_xlim([-2,10])
axs[0][0].set_ylim([0,2.5])
axs[0][0].set_xlabel(r'$x$')
axs[0][0].set_ylabel(r'$f(x)$')
axs[0][0].set_title(r'$\lambda={}$'.format(lmd_1))
axs[0][1].plot(x, F_1)
axs[0][1].set_xlim([-2,10])
axs[0][1].set_ylim([0,1.1])
axs[0][1].set_xlabel(r'$x$')
axs[0][1].set_ylabel(r'$F(x)$')
axs[1][0].plot(x, f_2)
axs[1][0].set_xlim([-2,10])
axs[1][0].set_ylim([0,2.5])
axs[1][0].set_xlabel(r'$x$')
axs[1][0].set_ylabel(r'$f(x)$')
axs[1][0].set_title(r'$\lambda={}$'.format(lmd_2))
axs[1][1].plot(x, F_2)
axs[1][1].set_xlim([-2,10])
axs[1][1].set_ylim([0,1.1])
axs[1][1].set_xlabel(r'$x$')
axs[1][1].set_ylabel(r'$F(x)$')

plt.tight_layout()
plt.show()
