#!/usr/bin/python3

import numpy as np
import scipy.special as spsp
import matplotlib.pyplot as plt

def poisson(n, lmd):
    N = np.arange(n+1, dtype=np.float64) # 0,1,2,...,n
    X = np.emath.power(lmd, N) / spsp.factorial(N) * np.exp(-lmd)
    return N, X

fig, axs = plt.subplots(2, 2, figsize=(8,4))

n     = 200

mu    = 1
sigma = 199/200
x     = np.arange(-10, 200, 0.01)
f     = (1 / (np.sqrt(2*np.pi)*sigma)) * np.exp(-1 * ((x-mu)**2) / (2 * sigma**2))
F     = np.cumsum(f) / 100
axs[0][0].plot(x, f)
axs[0][0].set_xlim([0, n])
axs[0][0].set_ylim([0, 1.1])
axs[0][0].set_xlabel(r'$x$')
axs[0][0].set_ylabel(r'$f(x)$')
axs[0][0].set_title(r'normal distribution, $\mu={},\sigma={}$'.format(mu, sigma))
axs[0][1].plot(x, F)
axs[0][1].set_xlim([0, n])
axs[0][1].set_ylim([0, 1.1])
axs[0][1].set_xlabel(r'$x$')
axs[0][1].set_ylabel(r'$F(x)$')

lmd   = 1
N, X  = poisson(n, lmd)
X_sum = np.cumsum(X)
axs[1][0].plot(N, X)
axs[1][0].set_xlim([0,n])
axs[1][0].set_ylim([0,1.1])
axs[1][0].set_title(r'poisson distribution, $n={}, \lambda={}$'.format(n, lmd))
axs[1][0].set_xlabel(r'$x$')
axs[1][0].set_ylabel(r'$P\{X=x\}$')
axs[1][1].plot(N, X_sum)
axs[1][1].set_xlim([0,n])
axs[1][1].set_ylim([0,1.1])
axs[1][1].set_xlabel(r'$x$')
axs[1][1].set_ylabel(r'$P\{X \leqslant x\}$')

plt.tight_layout()
plt.show()

