import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Setup clean 3D canvas
fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111, projection='3d')

# Angular grid for generating the concentric shells
u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:20j]
x_unit = np.cos(u) * np.sin(v)
y_unit = np.sin(u) * np.sin(v)
z_unit = np.cos(v)

# --- 1. PLOT THE PROTON (Upper Node, shifted to z = +0.5)
z_offset_p = 0.5
ax.plot_surface(x_unit, y_unit, z_unit + z_offset_p, color='crimson', alpha=0.15, edgecolor='darkred', lw=0.3)
# Draw an equatorial current loop indicator for the proton
t_loop = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(t_loop), np.sin(t_loop), np.zeros_like(t_loop) + z_offset_p, color='red', lw=2.5, label='Proton Loop (+e)')

# --- 2. PLOT THE NEUTRON (Lower Node, shifted to z = -0.5)
z_offset_n = -0.5
# Outer Negative Shell (Radius = 1.0)
ax.plot_surface(x_unit, y_unit, z_unit + z_offset_n, color='cyan', alpha=0.04, edgecolor='teal', lw=0.2)
# Inner Positive Core (Radius = 0.569)
x0 = 0.569
ax.plot_surface(x0*x_unit, x0*y_unit, x0*z_unit + z_offset_n, color='crimson', alpha=0.2, edgecolor='darkred', lw=0.3)
# Label the composite neutron center
ax.scatter([0], [0], [z_offset_n], color='teal', s=40, label='Neutron Center (Net 0)')

# --- 3. THE SHARED COAXIAL AXIS (The k-axis)
ax.plot([0, 0], [0, 0], [-1.8, 1.8], color='darkviolet', linestyle='--', lw=2, label='Shared Spin Axis (k)')

# Aesthetics, boundaries, and view angle
ax.set_title("Deuteron Structure: Coaxial Electro-Magnetic Phase-Locking", fontsize=12, fontweight='bold', pad=15)
ax.set_xlim([-1.3, 1.3]); ax.set_ylim([-1.3, 1.3]); ax.set_zlim([-1.8, 1.8])
ax.grid(True, linestyle='--', alpha=0.2)
ax.legend(loc='upper right')
ax.view_init(elev=15, azim=30)

plt.tight_layout()
plt.show()
