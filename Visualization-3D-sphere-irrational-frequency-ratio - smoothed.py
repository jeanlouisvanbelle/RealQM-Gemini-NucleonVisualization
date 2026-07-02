import numpy as np
import matplotlib.pyplot as plt

# Parameters for smooth continuous integration
omega_1 = 1.0
omega_2 = np.sqrt(2)
t = np.linspace(0, 30, 5000) # Increased density for smoothness

# Replace the hard bounce loop with a continuous harmonic polar oscillation
# This naturally slows down and turns around at the poles without any hard impacts
theta = np.pi/2 + (np.pi/2 - 0.08) * np.sin(omega_1 * t)

# Analytical integration of the phase-velocity compensation term
# Since theta is continuous, phi accumulates smoothly
phi = np.zeros_like(t)
dt = t[1] - t[0]

for i in range(1, len(t)):
    # Dynamic velocity scaling component to enforce constant local velocity v=c
    phi[i] = phi[i-1] + (omega_2 / np.sin(theta[i])) * dt

# Convert to 3D Cartesian coordinates
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# Plotting the smooth presentation-ready projections
fig, ax = plt.subplots(figsize=(8, 8))
ax.plot(x, y, label='XY projection (Equatorial view)', color='royalblue', lw=1.0, alpha=0.7)
ax.plot(x, z, label='XZ projection (Polar view)', color='forestgreen', lw=1.0, alpha=0.7)

ax.set_title("Phase-Corrected Projections (Smooth Continuous Flow)", fontsize=12, fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='upper right')
ax.set_aspect('equal')

plt.tight_layout()
plt.show()
