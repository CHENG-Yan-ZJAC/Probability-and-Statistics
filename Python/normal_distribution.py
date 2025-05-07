#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

mu_1    = -3
sigma_1 = 0.5

mu_2    = 2
sigma_2 = 4

mu_3    = 0
sigma_3 = 1

x = np.arange(-10, 10, 0.01)

f_1 = (1 / (np.sqrt(2*np.pi)*sigma_1)) * np.exp(-1 * ((x-mu_1)**2) / (2 * sigma_1**2))
F_1 = np.cumsum(f_1) / 100
f_2 = (1 / (np.sqrt(2*np.pi)*sigma_2)) * np.exp(-1 * ((x-mu_2)**2) / (2 * sigma_2**2))
F_2 = np.cumsum(f_2) / 100
f_3 = (1 / (np.sqrt(2*np.pi)*sigma_3)) * np.exp(-1 * ((x-mu_3)**2) / (2 * sigma_3**2))
F_3 = np.cumsum(f_3) / 100

fig, axs = plt.subplots(3, 2, figsize=(8,6))
axs[0][0].plot(x, f_1)
axs[0][0].set_xlim([-10, 10])
axs[0][0].set_ylim([0, 1.0])
axs[0][0].set_xlabel(r'$x$')
axs[0][0].set_ylabel(r'$f(x)$')
axs[0][0].set_title(r'$\mu={},\sigma={}$'.format(mu_1, sigma_1))
axs[0][0].axhline(1/(np.sqrt(2*np.pi)*sigma_1), color='r', ls='--', lw=1)
axs[0][0].axvline(mu_1,         color='r', ls='--', lw=1)
axs[0][0].axvline(mu_1-sigma_1, color='r', ls='--', lw=1)
axs[0][0].axvline(mu_1+sigma_1, color='r', ls='--', lw=1)
axs[0][1].plot(x, F_1)
axs[0][1].set_xlim([-10, 10])
axs[0][1].set_ylim([0, 1.1])
axs[0][1].set_xlabel(r'$x$')
axs[0][1].set_ylabel(r'$F(x)$')

axs[1][0].plot(x, f_2)
axs[1][0].set_xlim([-10, 10])
axs[1][0].set_ylim([0, 1.0])
axs[1][0].set_xlabel(r'$x$')
axs[1][0].set_ylabel(r'$f(x)$')
axs[1][0].set_title(r'$\mu={},\sigma={}$'.format(mu_2, sigma_2))
axs[1][0].axhline(1/(np.sqrt(2*np.pi)*sigma_2), color='r', ls='--', lw=1)
axs[1][0].axvline(mu_2,         color='r', ls='--', lw=1)
axs[1][0].axvline(mu_2-sigma_2, color='r', ls='--', lw=1)
axs[1][0].axvline(mu_2+sigma_2, color='r', ls='--', lw=1)
axs[1][1].plot(x, F_2)
axs[1][1].set_xlim([-10, 10])
axs[1][1].set_ylim([0, 1.1])
axs[1][1].set_xlabel(r'$x$')
axs[1][1].set_ylabel(r'$F(x)$')

axs[2][0].plot(x, f_3)
axs[2][0].set_xlim([-10, 10])
axs[2][0].set_ylim([0, 1.0])
axs[2][0].set_xlabel(r'$x$')
axs[2][0].set_ylabel(r'$\varphi(x)$')
axs[2][0].set_title(r'$\mu={},\sigma={}$'.format(mu_3, sigma_3))
axs[2][0].axhline(1/(np.sqrt(2*np.pi)*sigma_3), color='r', ls='--', lw=1)
axs[2][0].axvline(mu_3,         color='r', ls='--', lw=1)
axs[2][0].axvline(mu_3-sigma_3, color='r', ls='--', lw=1)
axs[2][0].axvline(mu_3+sigma_3, color='r', ls='--', lw=1)
axs[2][1].plot(x, F_3)
axs[2][1].set_xlim([-10, 10])
axs[2][1].set_ylim([0, 1.1])
axs[2][1].set_xlabel(r'$x$')
axs[2][1].set_ylabel(r'$\Phi(x)$')

plt.tight_layout()
plt.show()

