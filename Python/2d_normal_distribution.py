#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mu1    = 0.
mu2    = 0.
sigma1 = 1.
sigma2 = 1.
rho1   = 0.
rho2   = 0.7

x = np.arange(-5, 5, 0.2)
y = np.arange(-5, 5, 0.2)
x,y = np.meshgrid(x, y)

f1 = np.exp(
		-0.5/(1-rho1**2) * ( ((x-mu1)/sigma1)**2 - 2*rho1*(x-mu1)*(y-mu2)/sigma1/sigma2 + ((y-mu2)/sigma2)**2 )
		) / (2*np.pi * sigma1 * sigma2 * np.sqrt(1-rho1**2))
f2 = np.exp(
		-0.5/(1-rho2**2) * ( ((x-mu1)/sigma1)**2 - 2*rho2*(x-mu1)*(y-mu2)/sigma1/sigma2 + ((y-mu2)/sigma2)**2 )
		) / (2*np.pi * sigma1 * sigma2 * np.sqrt(1-rho2**2))

fig, axs = plt.subplots(1, 2, figsize=(4,6), subplot_kw={'projection':'3d'})
axs[0].plot_wireframe(x, y, f1, rstride=2, cstride=2)
axs[0].set_xlim([-5, 5])
axs[0].set_ylim([-5, 5])
axs[0].set_zlim([0, 0.3])
axs[0].set_xlabel(r'$x$')
axs[0].set_ylabel(r'$y$')
#axs[0].set_zlabel(r'$f1$')
axs[0].set_title(r'$\rho={}$'.format(rho1))
axs[1].plot_wireframe(x, y, f2, rstride=2, cstride=2)
axs[1].set_xlim([-5, 5])
axs[1].set_ylim([-5, 5])
axs[1].set_zlim([0, 0.3])
axs[1].set_xlabel(r'$x$')
axs[1].set_ylabel(r'$y$')
#axs[1].set_zlabel(r'$f2$')
axs[1].set_title(r'$\rho={}$'.format(rho2))

plt.tight_layout()
plt.show()
