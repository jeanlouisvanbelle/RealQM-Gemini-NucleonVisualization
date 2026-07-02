import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Normalized parameters
omega_1 = 1.0
omega_2 = np.sqrt(2) # Fundamental Euclidean irrational ratio
t = np.linspace(0, 60, 3000) # Extended time to show surface-filling

# Calculate paths
x = np.sin(omega_1 * t) * np.cos(omega_2 * t)
y = np.sin(omega_1 * t) * np.sin(omega_2 * t)
z = np.cos(omega_1 * t)

# Plotting
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Reference ghost sphere
u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:30j]
ax.plot_surface(np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v), color='gray', alpha=0.05)

# Bounded non-closing trace
ax.plot(x, y, z, color='darkorange', lw=1.2, alpha=0.85, label=r'$\omega_2/\omega_1 = \sqrt{2}$')
ax.set_title("Quasi-Periodic Bounded Rotational Flow", fontsize=14, fontweight='bold')
ax.set_xlim([-1, 1]); ax.set_ylim([-1, 1]); ax.set_zlim([-1, 1])
ax.legend(loc='upper right')
ax.view_init(elev=25, azim=30)

plt.show()
