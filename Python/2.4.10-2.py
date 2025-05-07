#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

y = np.arange(1.9**2*np.pi, 2.1**2*np.pi, 0.01)
f = 1 / (0.4 * np.sqrt(np.pi*y))

fig, axs = plt.subplots(1, 1, figsize=(6,3))
axs.plot(y, f)
axs.set_xlim([11, 14])
axs.set_ylim([0,1.1])
axs.set_xlabel(r'$y$')
axs.set_ylabel(r'$f_Y$')

plt.tight_layout()
plt.show()
