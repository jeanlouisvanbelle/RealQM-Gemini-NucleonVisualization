import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for smooth continuous integration
omega_1 = 1.0
omega_2 = np.sqrt(2)
t = np.linspace(0, 35, 6000)

# Continuous harmonic polar oscillation to eliminate pixelated steps
theta = np.pi/2 + (np.pi/2 - 0.06) * np.sin(omega_1 * t)

# Numerical integration of the phase-velocity compensation
phi = np.zeros_like(t)
dt = t[1] - t[0]
for i in range(1, len(t)):
    phi[i] = phi[i-1] + (omega_2 / np.sin(theta[i])) * dt

# Convert to 3D Cartesian coordinates
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# Setup presentation figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 1. Light Reference Envelope (The Bounded Shell Boundary)
u, v = np.mgrid[0:2*np.pi:40j, 0:np.pi:40j]
ax.plot_surface(np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v), color='teal', alpha=0.03, edgecolor='teal', lw=0.1)

# 2. Inward Field Vectors (Showing Local Confinement)
num_vectors = 6
p_vec = np.linspace(0, 2*np.pi, num_vectors, endpoint=False)
th_vec = np.linspace(np.pi/4, 3*np.pi/4, num_vectors)
for p in p_vec:
    for th in th_vec:
        vx, vy, vz = np.sin(th)*np.cos(p), np.sin(th)*np.sin(p), np.cos(th)
        ax.quiver(vx, vy, vz, -0.2*vx, -0.2*vy, -0.2*vz, color='crimson', alpha=0.35, lw=1.2, arrow_length_ratio=0.2)

# 3. Plot the perfectly smooth fluid trajectory
ax.plot(x, y, z, color='darkorange', lw=1.0, alpha=0.8, label=r'Self-Sustaining Path ($v=c$)')

# Formatting and layout
ax.set_title("Self-Sustaining Equilibrium: No Field Separation", fontsize=13, fontweight='bold', pad=20)
ax.set_xlim([-1.1, 1.1]); ax.set_ylim([-1.1, 1.1]); ax.set_zlim([-1.1, 1.1])
ax.grid(True, linestyle='--', alpha=0.3)
ax.legend(loc='upper right')
ax.view_init(elev=22, azim=45)

plt.tight_layout()
plt.show()
