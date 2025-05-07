#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

lmd = 1./600.
x   = np.arange(0, 5000, 0.1)
P1  = np.exp(-3*lmd*x)
P2  = 1 - ((1 - np.exp(-1*lmd*x)) ** 3)

fig, axs = plt.subplots(1, 2, figsize=(8,2))
axs[0].plot(x, P1)
axs[0].set_xlim([0,5000])
axs[0].set_ylim([0,1.1])
axs[0].set_xlabel(r'$x$')
axs[0].set_ylabel(r'$P$')
axs[0].set_title(r'$P(\bar{A}_1\bar{A}_2\bar{A}_3)$')
axs[1].plot(x, P2)
axs[1].set_xlim([0,5000])
axs[1].set_ylim([0,1.1])
axs[1].set_xlabel(r'$x$')
axs[1].set_title(r'$P(\bar{A}_1+\bar{A}_2+\bar{A}_3)$')

plt.tight_layout()
plt.show()
