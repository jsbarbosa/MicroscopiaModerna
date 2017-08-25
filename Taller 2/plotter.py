import numpy as np
import matplotlib.pyplot as plt

n_i = 1.0
theta_i = np.linspace(0, np.pi*0.5)

n_t = 1.5
theta_t = np.arcsin(np.sin(theta_i)*n_i/n_t)

theta_i = np.rad2deg(theta_i)
theta_t = np.rad2deg(theta_t)

plt.plot(theta_i, theta_t)
plt.xlabel(r"$\theta_i$ ($^\circ$)")
plt.ylabel(r"$\theta_t$ ($^\circ$)")

plt.savefig("418.pdf")
