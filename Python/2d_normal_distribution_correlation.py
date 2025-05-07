#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mu_x    = 0.
mu_y    = 0.
sigma_x = 1.
sigma_y = 1.
rho1   = 0.
rho2   = 0.3
rho3   = 0.7
rho4   = 0.99

x = np.arange(-5, 5, 0.2)
y = np.arange(-5, 5, 0.2)
x,y = np.meshgrid(x, y)

f1 = np.exp(
		-0.5/(1-rho1**2) * ( ((x-mu_x)/sigma_x)**2 - 2*rho1*(x-mu_x)*(y-mu_y)/sigma_x/sigma_y + ((y-mu_y)/sigma_y)**2 )
		) / (2*np.pi * sigma_x * sigma_y * np.sqrt(1-rho1**2))
f2 = np.exp(
		-0.5/(1-rho2**2) * ( ((x-mu_x)/sigma_x)**2 - 2*rho2*(x-mu_x)*(y-mu_y)/sigma_x/sigma_y + ((y-mu_y)/sigma_y)**2 )
		) / (2*np.pi * sigma_x * sigma_y * np.sqrt(1-rho2**2))
f3 = np.exp(
		-0.5/(1-rho3**2) * ( ((x-mu_x)/sigma_x)**2 - 2*rho3*(x-mu_x)*(y-mu_y)/sigma_x/sigma_y + ((y-mu_y)/sigma_y)**2 )
		) / (2*np.pi * sigma_x * sigma_y * np.sqrt(1-rho3**2))
f4 = np.exp(
		-0.5/(1-rho4**2) * ( ((x-mu_x)/sigma_x)**2 - 2*rho4*(x-mu_x)*(y-mu_y)/sigma_x/sigma_y + ((y-mu_y)/sigma_y)**2 )
		) / (2*np.pi * sigma_x * sigma_y * np.sqrt(1-rho4**2))

fig, axs = plt.subplots(2, 2, figsize=(8,8), subplot_kw={'projection':'3d'})

axs[0][0].plot_wireframe(x, y, f1, rstride=2, cstride=2)
axs[0][0].set_xlim([-5, 5])
axs[0][0].set_ylim([-5, 5])
axs[0][0].set_zlim([0, 1.1])
axs[0][0].set_xlabel(r'$x$')
axs[0][0].set_ylabel(r'$y$')
axs[0][0].set_title(r'$\rho={}$'.format(rho1))

axs[0][1].plot_wireframe(x, y, f2, rstride=2, cstride=2)
axs[0][1].set_xlim([-5, 5])
axs[0][1].set_ylim([-5, 5])
axs[0][1].set_zlim([0, 1.1])
axs[0][1].set_xlabel(r'$x$')
axs[0][1].set_ylabel(r'$y$')
axs[0][1].set_title(r'$\rho={}$'.format(rho2))

axs[1][0].plot_wireframe(x, y, f3, rstride=2, cstride=2)
axs[1][0].set_xlim([-5, 5])
axs[1][0].set_ylim([-5, 5])
axs[1][0].set_zlim([0, 1.1])
axs[1][0].set_xlabel(r'$x$')
axs[1][0].set_ylabel(r'$y$')
axs[1][0].set_title(r'$\rho={}$'.format(rho3))

axs[1][1].plot_wireframe(x, y, f4, rstride=2, cstride=2)
axs[1][1].set_xlim([-5, 5])
axs[1][1].set_ylim([-5, 5])
axs[1][1].set_zlim([0, 1.1])
axs[1][1].set_xlabel(r'$x$')
axs[1][1].set_ylabel(r'$y$')
axs[1][1].set_title(r'$\rho={}$'.format(rho4))

plt.tight_layout()
plt.show()
