import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 9))
ax = fig.add_subplot(111, projection='3d')

# ============================================================
# REALQM PHYSICS PARAMETERS (From your June 2026 Paper)
# ============================================================
R_aa = 2.7       # Macro-scale: Alpha-Alpha separation triangle (fm)
d_alpha = 1.0    # Micro-scale: Internal Alpha edge length (fm)
r_loop = 0.28    # Translucent mesh radius for clarity

# 1. Define the 3 Alpha Particle Macro-Centers (Equilateral Triangle in XY plane)
R_centroid = R_aa / np.sqrt(3)
alpha_centers = [
    np.array([0.0, R_centroid, 0.0]),
    np.array([-R_aa / 2.0, -R_centroid / 2.0, 0.0]),
    np.array([R_aa / 2.0, -R_centroid / 2.0, 0.0])
]

# 2. Define the 4 Nucleon Micro-Vertices (Tetrahedron layout relative to center)
R_t = np.sqrt(3/8) * d_alpha
local_vertices = [
    np.array([0.0, 0.0, R_t]),                                  # Proton 1
    np.array([R_t, 0.0, -R_t / 3.0]),                           # Proton 2
    np.array([-R_t / 2.0, R_t * np.sqrt(3)/2.0, -R_t / 3.0]),   # Neutron 1
    np.array([-R_t / 2.0, -R_t * np.sqrt(3)/2.0, -R_t / 3.0])   # Neutron 2
]

# Grid for drawing the individual nucleon shell meshes
u, v = np.mgrid[0:2*np.pi:16j, 0:np.pi:12j]
x_sph = r_loop * np.cos(u) * np.sin(v)
y_sph = r_loop * np.sin(u) * np.sin(v)
z_sph = r_loop * np.cos(v)

# ============================================================
# RENDERING CYCLE
# ============================================================
# A. DRAW THE THICK MACRO-SKELETON (Connecting the 3 Alphas)
for i in range(3):
    next_idx = (i + 1) % 3
    ax.plot([alpha_centers[i][0], alpha_centers[next_idx][0]], 
            [alpha_centers[i][1], alpha_centers[next_idx][1]], 
            [alpha_centers[i][2], alpha_centers[next_idx][2]], 
            color='darkslateblue', linestyle='-', lw=3.5, alpha=0.8, zorder=1)

# Populate the Nucleons and Inner Alpha Bones
for a_idx, center in enumerate(alpha_centers):
    # Label Alpha clusters cleanly
    ax.text(center[0], center[1], center[2] + 0.9, f"Alpha {a_idx}", 
            color='darkblue', fontsize=11, fontweight='bold', ha='center')

    # B. DRAW MICRO-SKELETON (Rigid tetrahedral bones inside each Alpha cluster)
    for i in range(4):
        v1 = center + local_vertices[i]
        for j in range(i + 1, 4):
            v2 = center + local_vertices[j]
            ax.plot([v1[0], v2[0]], [v1[1], v2[1]], [v1[2], v2[2]], 
                    color='gray', linestyle='-', lw=1.5, alpha=0.6, zorder=2)

    # C. PLOT NUCLEON CURRENT SHELLS
    for i in range(4):
        global_pos = center + local_vertices[i]
        n_color, mesh_color = ('crimson', 'darkred') if i < 2 else ('cyan', 'teal')
        
        # Plot center core coordinate point
        ax.scatter(global_pos[0], global_pos[1], global_pos[2], color=n_color, s=40, zorder=5, edgecolor='black')
        
        # Overlay translucent current shell mesh
        ax.plot_surface(x_sph + global_pos[0], y_sph + global_pos[1], z_sph + global_pos[2], 
                        color=n_color, alpha=0.10, edgecolor=mesh_color, lw=0.15, zorder=3)

# Text marker highlighting the macro separation size gap
ax.text(0.0, -R_centroid/2.0 - 0.4, 0.1, r"$R_{\alpha\alpha} = 2.7\ \mathrm{fm}$", 
        color='darkslateblue', fontsize=11, fontweight='bold', ha='center')

# ============================================================
# PRESENTATION AESTHETICS & DISPLAY CALIBRATION
# ============================================================
ax.set_title("Carbon-12 Model: Triangle Network of 3 Tetrahedral Alphas", fontsize=13, fontweight='bold', pad=15)
ax.set_xlim([-2.2, 2.2]); ax.set_ylim([-2.2, 2.2]); ax.set_zlim([-1.2, 1.5])
ax.set_xlabel("X (fm)"); ax.set_ylabel("Y (fm)"); ax.set_zlabel("Z (fm)")

# Unified layout legends
from matplotlib.lines import Line2D
custom_legend = [
    Line2D([0], [0], color='darkslateblue', linestyle='-', lw=3, label=r'Macro-Alpha Gap ($R_{\alpha\alpha} = 2.7$ fm)'),
    Line2D([0], [0], color='gray', linestyle='-', lw=1.5, label='Micro-Tetrahedral Bonds')
]
ax.legend(handles=custom_legend, loc='upper right')

ax.view_init(elev=26, azim=35)
ax.grid(True, linestyle='--', alpha=0.2)

plt.tight_layout()
plt.show()


