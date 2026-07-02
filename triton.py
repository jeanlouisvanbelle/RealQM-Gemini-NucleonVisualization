import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Setup clean 3D canvas
fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111, projection='3d')

# Angular grid for building the layered structure
u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:20j]
x_unit = np.cos(u) * np.sin(v)
y_unit = np.sin(u) * np.sin(v)
z_unit = np.cos(v)
x0 = 0.569 # Neutron inner core scaling factor

# --- 1. CENTER PIECE: THE PROTON (Stationed at z = 0)
ax.plot_surface(x_unit, y_unit, z_unit, color='crimson', alpha=0.15, edgecolor='darkred', lw=0.3)
t_loop = np.linspace(0, 2*np.pi, 200)
ax.plot(np.cos(t_loop), np.sin(t_loop), np.zeros_like(t_loop), color='red', lw=2.5, label='Central Proton (+e)')

# --- 2. TOP FLANK: NEUTRON 1 (Shifted up to z = +1.1)
z_top = 1.1
ax.plot_surface(x_unit, y_unit, z_unit + z_top, color='cyan', alpha=0.03, edgecolor='teal', lw=0.2)
ax.plot_surface(x0*x_unit, x0*y_unit, x0*z_unit + z_top, color='crimson', alpha=0.15, edgecolor='darkred', lw=0.3)

# --- 3. BOTTOM FLANK: NEUTRON 2 (Shifted down to z = -1.1)
z_bottom = -1.1
ax.plot_surface(x_unit, y_unit, z_unit + z_bottom, color='cyan', alpha=0.03, edgecolor='teal', lw=0.2)
ax.plot_surface(x0*x_unit, x0*y_unit, x0*z_unit + z_bottom, color='crimson', alpha=0.15, edgecolor='darkred', lw=0.3)

# Label the sandwich nodes
ax.scatter([0, 0], [0, 0], [z_top, z_bottom], color='teal', s=35, label='Flanking Neutrons')

# --- 4. THE LONGITUDINAL SHARED COAXIAL AXIS
ax.plot([0, 0], [0, 0], [-2.3, 2.3], color='darkviolet', linestyle='--', lw=2, label='Unified k-Axis')

# Aesthetics, boundaries, and view angle
ax.set_title("Triton Structure: Interleaved Coaxial Sandwich Layout", fontsize=12, fontweight='bold', pad=15)
ax.set_xlim([-1.3, 1.3]); ax.set_ylim([-1.3, 1.3]); ax.set_zlim([-2.3, 2.3])
ax.grid(True, linestyle='--', alpha=0.2)
ax.legend(loc='upper right')
ax.view_init(elev=12, azim=40)

plt.tight_layout()
plt.show()
