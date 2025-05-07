#!/usr/bin/python3

import numpy as np
import scipy.special as spsp
import matplotlib.pyplot as plt

def binomial(n, p):
    N = np.arange(n+1, dtype=np.float64) # 0,1,2,...,n
    X = spsp.comb(n, N) * np.emath.power(p, N) * np.emath.power((1-p), (n-N))
    return N, X

fig, axs = plt.subplots(2, 2, figsize=(8,4))

n = 10
p = 0.3
N, X = binomial(n, p)
axs[0][0].stem(N, X, use_line_collection=True)
axs[0][0].set_xlim([0,n])
axs[0][0].set_ylim([0,1])
axs[0][0].set_title(r'$n={}, p={}$'.format(n, p))
axs[0][0].set_xlabel(r'$x$')
axs[0][0].set_ylabel(r'$P\{X=x\}$')

n = 10
p = 0.9
N, X = binomial(n, p)
axs[0][1].stem(N, X, use_line_collection=True)
axs[0][1].set_xlim([0,n])
axs[0][1].set_ylim([0,1])
axs[0][1].set_title(r'$n={}, p={}$'.format(n, p))

n = 5
p = 0.3
N, X = binomial(n, p)
axs[1][0].stem(N, X, use_line_collection=True)
axs[1][0].set_xlim([0, n])
axs[1][0].set_ylim([0, 1])
axs[1][0].set_title(r'$n={}, p={}$'.format(n, p))

n = 5
p = 0.9
N, X = binomial(n, p)
axs[1][1].stem(N, X, use_line_collection=True)
axs[1][1].set_xlim([0, n])
axs[1][1].set_ylim([0, 1])
axs[1][1].set_title(r'$n={}, p={}$'.format(n, p))

plt.tight_layout()
plt.show()
