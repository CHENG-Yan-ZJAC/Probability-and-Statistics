#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

def geometric(n, p):
    N = np.arange(n+1, dtype=np.float64) # 0,1,2,...,n
    X = np.emath.power((1-p), (N-1)) * p
    return N, X

fig, axs = plt.subplots(2, 2, figsize=(8,4))

n = 20
p = 0.3
N, X = geometric(n, p)
axs[0][0].stem(N, X, use_line_collection=True)
axs[0][0].set_xlim([0,n])
axs[0][0].set_ylim([0,1])
axs[0][0].set_title(r'$n={}, p={}$'.format(n, p))
axs[0][0].set_xlabel(r'$x$')
axs[0][0].set_ylabel(r'$P\{X=x\}$')

n = 20
p = 0.9
N, X = geometric(n, p)
axs[0][1].stem(N, X, use_line_collection=True)
axs[0][1].set_xlim([0,n])
axs[0][1].set_ylim([0,1])
axs[0][1].set_title(r'$n={}, p={}$'.format(n, p))

n = 100
p = 0.3
N, X = geometric(n, p)
axs[1][0].stem(N, X, use_line_collection=True)
axs[1][0].set_xlim([0,n])
axs[1][0].set_ylim([0,1])
axs[1][0].set_title(r'$n={}, p={}$'.format(n, p))

n = 100
p = 0.9
N, X = geometric(n, p)
axs[1][1].stem(N, X, use_line_collection=True)
axs[1][1].set_xlim([0,n])
axs[1][1].set_ylim([0,1])
axs[1][1].set_title(r'$n={}, p={}$'.format(n, p))

plt.tight_layout()
plt.show()
