import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Setup a wide presentation figure for side-by-side 3D panels
fig = plt.figure(figsize=(14, 7))
r_loop = 0.25 # Clean visual current shell radius

# ============================================================
# DATA GENERATION: OXYGEN-16 CONFIGURATIONS (A = 16)
# ============================================================
A = 16
R_drop = 1.2 * (A**(1/3)) # Classical liquid drop radius (~3.02 fm)

# Base nucleon current shell sphere template
u, v = np.mgrid[0:2*np.pi:12j, 0:np.pi:10j]
x_sph = r_loop * np.cos(u) * np.sin(v)
y_sph = r_loop * np.sin(u) * np.sin(v)
z_sph = r_loop * np.cos(v)

# --- 1. LEFT PANEL: INITIAL RANDOM STATE ---
ax1 = fig.add_subplot(121, projection='3d')

# Seed a fixed random layout for reproducibility
np.random.seed(42)
for i in range(A):
    # Distribute nucleon loop centers randomly inside the liquid drop sphere volume
    phi_r = np.random.uniform(0, 2*np.pi)
    costh_r = np.random.uniform(-1, 1)
    sinth_r = np.sqrt(1 - costh_r**2)
    r_r = R_drop * (np.random.uniform(0.1, 0.95)**(1/3))
    
    pos_rand = r_r * np.array([sinth_r*np.cos(phi_r), sinth_r*np.sin(phi_r), costh_r])
    rx, ry, rz = pos_rand[0], pos_rand[1], pos_rand[2]
    
    # Alternating color-coding (8 Protons, 8 Neutrons)
    n_color, mesh_color = ('crimson', 'darkred') if i < 8 else ('cyan', 'teal')
    
    ax1.scatter(rx, ry, rz, color=n_color, s=25, edgecolor='black', zorder=5)
    ax1.plot_surface(x_sph + rx, y_sph + ry, z_sph + rz, 
                    color=n_color, alpha=0.07, edgecolor=mesh_color, lw=0.1)

# Overlay a light bounding sphere indicating the liquid drop horizon boundary
u_d, v_d = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
ax1.plot_wireframe(R_drop*np.cos(u_d)*np.sin(v_d), R_drop*np.sin(u_d)*np.sin(v_d), R_drop*np.cos(v_d), 
                   color='indigo', alpha=0.05, lw=0.5)

ax1.set_title(f"1. Blind Initialization\nRandom Liquid Drop Sphere ($R \approx {R_drop:.2f}$ fm)", 
              fontsize=11, fontweight='bold', color='indigo')
ax1.set_xlim([-3.5, 3.5]); ax1.set_ylim([-3.5, 3.5]); ax1.set_zlim([-3.5, 3.5])
ax1.view_init(elev=20, azim=45)
ax1.grid(True, linestyle='--', alpha=0.15)


# --- 2. RIGHT PANEL: OPTIMIZED RELAXED STATE ---
ax2 = fig.add_subplot(122, projection='3d')

# Structural coordinates from your Oxygen-16 tetrahedral alpha network paper
R_aa = 2.8
d_alpha = 1.0
R_radius = np.sqrt(3/8) * R_aa
alpha_centers = [
    np.array([0.0, 0.0, R_radius]),
    np.array([R_radius, 0.0, -R_radius / 3.0]),
    np.array([-R_radius / 2.0, R_radius * np.sqrt(3) / 2.0, -R_radius / 3.0]),
    np.array([-R_radius / 2.0, -R_radius * np.sqrt(3) / 2.0, -R_radius / 3.0])
]
R_t = np.sqrt(3/8) * d_alpha
local_vertices = [
    np.array([0.0, 0.0, R_t]), np.array([R_t, 0.0, -R_t / 3.0]),
    np.array([-R_t / 2.0, R_t * np.sqrt(3) / 2.0, -R_t / 3.0]),
    np.array([-R_t / 2.0, -R_t * np.sqrt(3) / 2.0, -R_t / 3.0])
]

# Draw the macro regular tetrahedron structural bonds
for i in range(4):
    for j in range(i + 1, 4):
        ax2.plot([alpha_centers[i][0], alpha_centers[j][0]], 
                 [alpha_centers[i][1], alpha_centers[j][1]], 
                 [alpha_centers[i][2], alpha_centers[j][2]], 
                 color='forestgreen', linestyle='-', lw=2.5, alpha=0.6, zorder=1)

# Populate localized optimized loop clusters
for center in alpha_centers:
    for i in range(4):
        global_pos = center + local_vertices[i]
        gx, gy, gz = global_pos[0], global_pos[1], global_pos[2]
        
        # Micro-skeleton internal bonds
        for j in range(i + 1, 4):
            v2 = center + local_vertices[j]
            ax2.plot([gx, v2[0]], [gy, v2[1]], [gz, v2[2]], 
                     color='gray', linestyle='-', lw=1.0, alpha=0.4, zorder=2)
            
        n_color, mesh_color = ('crimson', 'darkred') if i < 2 else ('cyan', 'teal')
        ax2.scatter(gx, gy, gz, color=n_color, s=25, edgecolor='black', zorder=5)
        ax2.plot_surface(x_sph + gx, y_sph + gy, z_sph + gz, 
                        color=n_color, alpha=0.08, edgecolor=mesh_color, lw=0.1, zorder=3)

ax2.set_title("2. Ground State Convergence\nRelaxed Multi-Alpha Matrix ($U_{mag} = +12.94$ MeV)", 
              fontsize=11, fontweight='bold', color='darkgreen')
ax2.set_xlim([-3.5, 3.5]); ax2.set_ylim([-3.5, 3.5]); ax2.set_zlim([-3.5, 3.5])
ax2.view_init(elev=20, azim=45)
ax2.grid(True, linestyle='--', alpha=0.15)

# Global layout styling adjustments
plt.suptitle("", fontsize=14, fontweight='bold', y=0.96)
plt.tight_layout()
plt.show()

