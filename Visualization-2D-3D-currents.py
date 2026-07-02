import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Setup figure
fig = plt.figure(figsize=(12, 5))

# Left Subplot: 2D Ring Current (Electron Model)
ax1 = fig.add_subplot(121)
t = np.linspace(0, 2*np.pi, 300)
ax1.plot(np.cos(t), np.sin(t), color='royalblue', lw=3, label=r'2D Ring Current ($A = \pi r^2$)')
ax1.scatter([0], [0], color='red', s=50, zorder=5, label='Center of Mass')
ax1.set_title("Electron: Planar Oscillation", fontsize=12, fontweight='bold')
ax1.set_xlim([-1.5, 1.5]); ax1.set_ylim([-1.5, 1.5])
ax1.set_aspect('equal')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='lower center')

# Right Subplot: 3D Spherical Field Shell (Proton Model)
ax2 = fig.add_subplot(122, projection='3d')
u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:40j]
xs = np.cos(u) * np.sin(v)
ys = np.sin(u) * np.sin(v)
zs = np.cos(v)
ax2.plot_surface(xs, ys, zs, color='crimson', alpha=0.15, edgecolor='darkred', lw=0.3)
ax2.set_title(r"Proton: 3D Spherical Shell ($A = 4\pi r^2$)", fontsize=12, fontweight='bold')
ax2.set_xlim([-1.2, 1.2]); ax2.set_ylim([-1.2, 1.2]); ax2.set_zlim([-1.2, 1.2])
ax2.view_init(elev=20, azim=45)

plt.tight_layout()
plt.show()
