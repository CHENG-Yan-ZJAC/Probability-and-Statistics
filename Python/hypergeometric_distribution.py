#!/usr/bin/python3

import numpy as np
import scipy.special as spsp
import matplotlib.pyplot as plt

def hypergeometric(M, N, n):
    K = np.arange(n+1, dtype=np.float64) # 0,1,2,...,n
    X = spsp.comb(N-M, n-K) * spsp.comb(M, K) / spsp.comb(N, n)
    return K, X

fig, axs = plt.subplots(2, 2, figsize=(8,4))
M = 6
N = 16

n = 3
K, X = hypergeometric(M, N, n)
axs[0][0].stem(K, X, use_line_collection=True)
axs[0][0].set_xlim([0,n])
axs[0][0].set_ylim([0,1])
axs[0][0].set_title(r'$N={},M={},n={}$'.format(N, M, n))
axs[0][0].set_xlabel(r'$x$')
axs[0][0].set_ylabel(r'$P\{X=x\}$')

n = 5
K, X = hypergeometric(M, N, n)
axs[0][1].stem(K, X, use_line_collection=True)
axs[0][1].set_xlim([0,n])
axs[0][1].set_ylim([0,1])
axs[0][1].set_title(r'$n={}$'.format(n))

n = 10
K, X = hypergeometric(M, N, n)
axs[1][0].stem(K, X, use_line_collection=True)
axs[1][0].set_xlim([0,n])
axs[1][0].set_ylim([0,1])
axs[1][0].set_title(r'$n={}$'.format(n))

n = 16
K, X = hypergeometric(M, N, n)
axs[1][1].stem(K, X, use_line_collection=True)
axs[1][1].set_xlim([0,n])
axs[1][1].set_ylim([0,1])
axs[1][1].set_title(r'$n={}$'.format(n))

plt.tight_layout()
plt.show()
