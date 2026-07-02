import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 9))
ax = fig.add_subplot(111, projection='3d')

# --- PHYSICAL DIMENSIONS (From your June 2026 O-16 Paper) ---
R_aa = 2.8       # Macro-scale: Alpha-Alpha center separation (fm)
d_alpha = 1.0    # Micro-scale: Internal Alpha edge length (fm)
r_loop = 0.28    # Translucent mesh radius

# 1. Macro-Centers (Regular Tetrahedron vertices for the 4 Alphas)
R_radius = np.sqrt(3/8) * R_aa
alpha_centers = [
    np.array([0.0, 0.0, R_radius]),
    np.array([R_radius, 0.0, -R_radius / 3.0]),
    np.array([-R_radius / 2.0, R_radius * np.sqrt(3) / 2.0, -R_radius / 3.0]),
    np.array([-R_radius / 2.0, -R_radius * np.sqrt(3) / 2.0, -R_radius / 3.0])
]

# 2. Micro-Vertices (Tetrahedron coordinates for inside each Alpha)
R_t = np.sqrt(3/8) * d_alpha
local_vertices = [
    np.array([0.0, 0.0, R_t]),
    np.array([R_t, 0.0, -R_t / 3.0]),
    np.array([-R_t / 2.0, R_t * np.sqrt(3) / 2.0, -R_t / 3.0]),
    np.array([-R_t / 2.0, -R_t * np.sqrt(3) / 2.0, -R_t / 3.0])
]

# Nucleon surface layout
u, v = np.mgrid[0:2*np.pi:16j, 0:np.pi:12j]
x_sph = r_loop * np.cos(u) * np.sin(v)
y_sph = r_loop * np.sin(u) * np.sin(v)
z_sph = r_loop * np.cos(v)

# --- RENDERING CYCLE ---
# A. DRAW THE MACRO-TETRAHEDRON SKELETON (Connecting the 4 Alphas)
for i in range(4):
    for j in range(i + 1, 4):
        ax.plot([alpha_centers[i][0], alpha_centers[j][0]], 
                [alpha_centers[i][1], alpha_centers[j][1]], 
                [alpha_centers[i][2], alpha_centers[j][2]], 
                color='forestgreen', linestyle='-', lw=3.0, alpha=0.7, zorder=1)

# Populate the Nucleons and Inner Alpha Bones
for a_idx, center in enumerate(alpha_centers):
    ax.text(center[0], center[1], center[2] + 0.8, f"Alpha {a_idx}", 
            color='darkgreen', fontsize=11, fontweight='bold', ha='center')

    # B. DRAW MICRO-SKELETON (Tetrahedral bonds inside each Alpha)
    for i in range(4):
        v1 = center + local_vertices[i]
        for j in range(i + 1, 4):
            v2 = center + local_vertices[j]
            ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], 
                    color='gray', linestyle='-', lw=1.2, alpha=0.5, zorder=2)

        # C. PLOT NUCLEON CURRENT SHELLS
        n_color, mesh_color = ('crimson', 'darkred') if i < 2 else ('cyan', 'teal')
        ax.scatter(v1[0], v1[1], v1[2], color=n_color, s=40, zorder=5, edgecolor='black')
        ax.plot_surface(x_sph + v1[0], y_sph + v1[1], z_sph + v1[2], 
                        color=n_color, alpha=0.09, edgecolor=mesh_color, lw=0.15, zorder=3)

# Text marker highlighting the macro tetrahedron separation size
ax.text(0.0, 0.0, -R_radius/3.0 - 0.3, r"$R_{\alpha\alpha} = 2.8\ \mathrm{fm}$", 
        color='forestgreen', fontsize=11, fontweight='bold', ha='center')

ax.set_title("Oxygen-16 Magic Shell: Tetrahedral Packing of 4 Alphas", fontsize=13, fontweight='bold', pad=15)
ax.set_xlim([-2.2, 2.2]); ax.set_ylim([-2.2, 2.2]); ax.set_zlim([-1.5, 2.0])
ax.view_init(elev=22, azim=45)
ax.grid(True, linestyle='--', alpha=0.2)
plt.tight_layout()
plt.show()
