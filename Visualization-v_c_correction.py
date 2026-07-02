import numpy as np
import matplotlib.pyplot as plt

# Integration setup
omega_1 = 1.0
dt = 0.001
t_max = 25.0
steps = int(t_max / dt)

theta = np.zeros(steps)
phi = np.zeros(steps)
theta[0] = np.pi / 2 # Start at equator
epsilon = 0.05       # Thomson-scale polar boundary cutoff
polar_dir = 1

# Numerical integration over time
for i in range(1, steps):
    theta_next = theta[i-1] + polar_dir * omega_1 * dt
    if theta_next >= (np.pi - epsilon):
        polar_dir = -1
        theta_next = np.pi - epsilon
    elif theta_next <= epsilon:
        polar_dir = 1
        theta_next = epsilon
    theta[i] = theta_next
    
    # Dynamic velocity scaling component to enforce constant local velocity v=c
    phi[i] = phi[i-1] + (np.sqrt(2) * omega_1 / np.sin(theta[i])) * dt

# Convert to Cartesian space
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# Plotting the 2D Projection framework
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label='XY projection (Equatorial view)', color='royalblue', lw=0.8, alpha=0.7)
ax.plot(x, z, label='XZ projection (Polar view)', color='forestgreen', lw=0.8, alpha=0.7)
ax.set_title("Phase-Corrected Projections ($v=c$)", fontsize=12, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')
ax.set_aspect('equal')

plt.tight_layout()
plt.show()
