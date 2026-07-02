import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Setup figure
fig = plt.figure(figsize=(12, 5))

# Left Subplot: 2D Complex Limit (Flat Grid)
ax1 = fig.add_subplot(121)
theta = np.linspace(0, 2*np.pi, 200)
ax1.plot(np.cos(theta), np.sin(theta), color='royalblue', lw=2, label=r'$\Psi = e^{i\theta}$')
ax1.quiver(0, 0, 1, 0, angles='xy', scale_units='xy', scale=1, color='red', label='Real Axis')
ax1.quiver(0, 0, 0, 1, angles='xy', scale_units='xy', scale=1, color='blue', label='Imaginary Axis (i)')
ax1.set_title("Standard QM: Flat 2D Complex Plane", fontsize=12, fontweight='bold')
ax1.set_xlim([-1.5, 1.5]); ax1.set_ylim([-1.5, 1.5])
ax1.set_aspect('equal')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend(loc='lower left')

# Right Subplot: 3D Quaternion Axis Generation (ij = k)
ax2 = fig.add_subplot(122, projection='3d')
# Draw a light grid for context
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
ax2.plot_wireframe(np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v), color='gray', alpha=0.1)

# Draw quaternion unit operators as spatial basis vectors
ax2.quiver(0, 0, 0, 1.2, 0, 0, color='red', lw=3, arrow_length_ratio=0.15, label='i operator')
ax2.quiver(0, 0, 0, 0, 1.2, 0, color='blue', lw=3, arrow_length_ratio=0.15, label='j operator')
ax2.quiver(0, 0, 0, 0, 0, 1.2, color='darkviolet', lw=3, arrow_length_ratio=0.15, label='k axis (ij = k)')

ax2.set_title("RealQM: 3D Operational Space", fontsize=12, fontweight='bold')
ax2.set_xlim([-1.5, 1.5]); ax2.set_ylim([-1.5, 1.5]); ax2.set_zlim([-1.5, 1.5])
ax2.view_init(elev=20, azim=35)
ax2.legend(loc='lower left')

plt.tight_layout()
plt.show()
