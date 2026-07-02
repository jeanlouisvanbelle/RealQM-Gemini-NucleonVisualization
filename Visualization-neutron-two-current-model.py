import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Setup presentation-ready figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 1. Outer Negative Shell (Radius R2 = 1.0)
u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:20j]
x_outer = np.cos(u) * np.sin(v)
y_outer = np.sin(u) * np.sin(v)
z_outer = np.cos(v)

# Plot Outer Shell as a highly transparent cyan mesh grid
ax.plot_surface(x_outer, y_outer, z_outer, color='cyan', alpha=0.05, edgecolor='teal', lw=0.3)

# 2. Inner Positive Core (Radius R1 = x0 = 0.569)
x0 = 0.569
x_inner = x0 * np.cos(u) * np.sin(v)
y_inner = x0 * np.sin(u) * np.sin(v)
z_inner = x0 * np.cos(v)

# Plot Inner Core as a distinct, semi-transparent crimson mesh grid
ax.plot_surface(x_inner, y_inner, z_inner, color='crimson', alpha=0.25, edgecolor='darkred', lw=0.4)

# 3. Formatting, Axis Limits, and Perspective Angles
ax.set_title("Neutron RealQM Core-Shell Variational Model", fontsize=14, fontweight='bold', pad=20)
ax.set_xlim([-1.2, 1.2]); ax.set_ylim([-1.2, 1.2]); ax.set_zlim([-1.2, 1.2])

# Clean up axis markings for a more stylized, professional slide appearance
ax.grid(True, linestyle='--', alpha=0.3)

# 4. Presentation On-Screen Text Callouts
ax.text2D(0.05, 0.95, r"Net Charge = 0", transform=ax.transAxes, color='black', fontsize=12, fontweight='bold')
ax.text2D(0.05, 0.90, r"Outer Shell Energy Radius: $R_2 = 1.0$", transform=ax.transAxes, color='teal', fontsize=11)
ax.text2D(0.05, 0.85, r"Inner Core Energy Radius: $R_1 \approx 0.569$", transform=ax.transAxes, color='darkred', fontsize=11)
ax.text2D(0.05, 0.80, r"Net Magnetic Moment $\mu_n = -1.913\,\mu_N$", transform=ax.transAxes, color='teal', fontsize=11)

# Rotate view to elegantly capture the nested concentricity
ax.view_init(elev=22, azim=40)

plt.tight_layout()
plt.show()
