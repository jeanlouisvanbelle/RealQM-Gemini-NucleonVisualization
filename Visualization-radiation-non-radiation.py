import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Normalized parameters for the irrational bounded flow
omega_1 = 1.0
omega_2 = np.sqrt(2)
t = np.linspace(0, 45, 2500)

# Generate the 3D charge trajectory
x = np.sin(omega_1 * t) * np.cos(omega_2 * t)
y = np.sin(omega_1 * t) * np.sin(omega_2 * t)
z = np.cos(omega_1 * t)

# Setup presentation-ready figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 1. Reference Ghost Sphere (The Boundary Envelope)
u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:40j]
sphere_x = np.cos(u) * np.sin(v)
sphere_y = np.sin(u) * np.sin(v)
sphere_z = np.cos(v)
ax.plot_surface(sphere_x, sphere_y, sphere_z, color='teal', alpha=0.04, edgecolor='teal', lw=0.1)

# 2. Local Field Force Vectors (Showing field re-entry lines)
# Generating a few inward-pointing vectors to symbolize trapped field energy
num_vectors = 8
phi_vec = np.linspace(0, 2*np.pi, num_vectors)
theta_vec = np.linspace(np.pi/4, 3*np.pi/4, num_vectors)
for p in phi_vec:
    for th in theta_vec:
        vx, vy, vz = np.sin(th)*np.cos(p), np.sin(th)*np.sin(p), np.cos(th)
        # Vector points slightly inward/along the shell to show reinforcement
        ax.quiver(vx, vy, vz, -0.2*vx, -0.2*vy, -0.2*vz, color='crimson', alpha=0.4, lw=1, arrow_length_ratio=0.2)

# 3. Plot the bounded charge trajectory
ax.plot(x, y, z, color='darkorange', lw=1.5, alpha=0.9, 
        label=r'Non-Radiating Path ($\omega_2 = \sqrt{2}\omega_1$)')

# Formatting and layout
ax.set_title("Self-Sustaining Equilibrium: No Field Separation", fontsize=14, fontweight='bold', pad=20)
ax.set_xlim([-1.2, 1.2]); ax.set_ylim([-1.2, 1.2]); ax.set_zlim([-1.2, 1.2])

# Descriptive on-screen labels to simulate PowerPoint callouts
ax.text(0, 0, 1.3, "No Field Detachment", color='darkgreen', fontweight='bold', ha='center')
ax.text(1.2, -1.2, 0, "Continuous Field Re-entry", color='crimson', fontweight='bold', ha='center')

ax.legend(loc='upper right')
ax.view_init(elev=20, azim=45)

plt.tight_layout()
plt.show()
