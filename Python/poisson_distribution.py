#!/usr/bin/python3

import numpy as np
import scipy.special as spsp
import matplotlib.pyplot as plt

def poisson(n, lmd):
    N = np.arange(n+1, dtype=np.float64) # 0,1,2,...,n
    X = np.emath.power(lmd, N) / spsp.factorial(N) * np.exp(-lmd)
    return N, X

fig, axs = plt.subplots(2, 2, figsize=(8,4))

n   = 20
lmd = 2
N, X = poisson(n, lmd)
axs[0][0].stem(N, X, use_line_collection=True)
axs[0][0].set_xlim([0,n])
axs[0][0].set_ylim([0,1])
axs[0][0].set_title(r'$n={}, \lambda={}$'.format(n, lmd))
axs[0][0].set_xlabel(r'$x$')
axs[0][0].set_ylabel(r'$P\{X=x\}$')

n   = 20
lmd = 20
N, X = poisson(n, lmd)
axs[0][1].stem(N, X, use_line_collection=True)
axs[0][1].set_xlim([0,n])
axs[0][1].set_ylim([0,1])
axs[0][1].set_title(r'$n={}, \lambda={}$'.format(n, lmd))

n   = 100
lmd = 2
N, X = poisson(n, lmd)
axs[1][0].stem(N, X, use_line_collection=True)
axs[1][0].set_xlim([0,n])
axs[1][0].set_ylim([0,1])
axs[1][0].set_title(r'$n={}, \lambda={}$'.format(n, lmd))

n   = 100
lmd = 20
N, X = poisson(n, lmd)
axs[1][1].stem(N, X, use_line_collection=True)
axs[1][1].set_xlim([0,n])
axs[1][1].set_ylim([0,1])
axs[1][1].set_title(r'$n={}, \lambda={}$'.format(n, lmd))

plt.tight_layout()
plt.show()
