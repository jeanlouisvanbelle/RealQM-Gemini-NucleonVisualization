import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Setup a focused 3D canvas for a single cluster
fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111, projection='3d')

# ============================================================
# ALPHA PARTICLE COUPLING GEOMETRY (From your June 2026 Paper)
# ============================================================
d_alpha = 1.0    # Optimal internal tetrahedral edge length (1.0 fm)
r_loop = 0.42    # Visual radius for individual ZBW loop meshes for clear clarity

# Define the 4 tetrahedral vertices centered at the origin (0,0,0)
R_t = np.sqrt(3/8) * d_alpha
vertices = [
    np.array([0.0, 0.0, R_t]),                                  # Proton 1 (Top)
    np.array([R_t, 0.0, -R_t / 3.0]),                           # Proton 2 (Base Front)
    np.array([-R_t / 2.0, R_t * np.sqrt(3)/2.0, -R_t / 3.0]),   # Neutron 1 (Base Back Left)
    np.array([-R_t / 2.0, -R_t * np.sqrt(3)/2.0, -R_t / 3.0])   # Neutron 2 (Base Back Right)
]

# Grid for building the spherical loop boundary shells
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:15j]
x_sphere = r_loop * np.cos(u) * np.sin(v)
y_sphere = r_loop * np.sin(u) * np.sin(v)
z_sphere = r_loop * np.cos(v)

# ============================================================
# 1. DRAW RIGID TETRAHEDRAL WIREFRAME (To anchor distance intuition)
# ============================================================
# Connect all 4 vertices to each other to outline the solid skeleton
for i in range(4):
    for j in range(i + 1, 4):
        ax.plot([vertices[i][0], vertices[j][0]], 
                [vertices[i][1], vertices[j][1]], 
                [vertices[i][2], vertices[j][2]], 
                color='gray', linestyle='-', lw=2.0, alpha=0.6, zorder=1)

# Add a label across one edge indicating the physical size constraint
edge_midpoint = (vertices[1] + vertices[2]) / 2
ax.text(edge_midpoint[0], edge_midpoint[1] - 0.1, edge_midpoint[2], 
        r"$d_\alpha = 1.0\ \mathrm{fm}$", color='dimgray', fontsize=11, fontweight='bold', ha='center')

# ============================================================
# 2. PLOT NUCLEON LOOPS
# ============================================================
for idx, pos in enumerate(vertices):
    # Color assignments matching your single-nucleon slides
    if idx < 2:
        n_color, mesh_color, n_label = 'crimson', 'darkred', 'Proton Loop (+e)'
    else:
        n_color, mesh_color, n_label = 'cyan', 'teal', 'Neutron Core-Shell'
        
    # Plot core location coordinate point
    ax.scatter(pos[0], pos[1], pos[2], color=n_color, s=80, edgecolor='black', zorder=5)
    
    # Overlay the overlapping 3D current distribution shell
    ax.plot_surface(x_sphere + pos[0], y_sphere + pos[1], z_sphere + pos[2], 
                    color=n_color, alpha=0.15, edgecolor=mesh_color, lw=0.3, zorder=3)

# ============================================================
# PRESENTATION LABELS & PERSPECTIVE ADJUSTMENT
# ============================================================
ax.set_title("The RealQM Alpha Particle (4He) Structural Element", fontsize=13, fontweight='bold', pad=20)

# Clean, tightly framed scale limits to capture the micro-scale context perfectly
ax.set_xlim([-0.9, 0.9]); ax.set_ylim([-0.9, 0.9]); ax.set_zlim([-0.8, 0.9])
ax.set_xlabel("X (fm)"); ax.set_ylabel("Y (fm)"); ax.set_zlabel("Z (fm)")

# Formulate custom legend labels to match presentation slides
from matplotlib.lines import Line2D
custom_legend = [
    Line2D([0], [0], color='crimson', marker='o', markersize=8, linestyle='', label='Proton Loop (+e)'),
    Line2D([0], [0], color='cyan', marker='o', markersize=8, linestyle='', label='Neutron Core-Shell'),
    Line2D([0], [0], color='gray', linestyle='-', lw=2, label='Tetrahedral Structural Bonds')
]
ax.legend(handles=custom_legend, loc='upper right')

# Set standard viewer angles to show the 3D depth of the tetrahedron base
ax.view_init(elev=20, azim=45)
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.show()
