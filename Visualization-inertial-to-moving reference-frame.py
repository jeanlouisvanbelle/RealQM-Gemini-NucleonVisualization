import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(12, 5))

# Left Subplot: Resting Particle Core (Spherical Ring Structure)
ax1 = fig.add_subplot(121, projection='3d')
t1 = np.linspace(0, 10*np.pi, 1000)
# A simple spherical-wrap baseline trajectory
x1 = np.sin(t1/5) * np.cos(t1)
y1 = np.sin(t1/5) * np.sin(t1)
z1 = np.cos(t1/5)

ax1.plot(x1, y1, z1, color='crimson', lw=1.5, label='Resting Clock ($\Omega$)')
ax1.set_title("Particle at Rest ($v = 0$)", fontsize=12, fontweight='bold')
ax1.set_xlim([-1.2, 1.2]); ax1.set_ylim([-1.2, 1.2]); ax1.set_zlim([-1.2, 1.2])
ax1.view_init(elev=25, azim=45)
ax1.legend(loc='upper right')

# Right Subplot: Moving Particle Wavepacket Trace (Ellipsoidal Helix)
ax2 = fig.add_subplot(122, projection='3d')
t2 = np.linspace(0, 10*np.pi, 1000)
velocity_translation = t2 * 0.25 # Linear translation through space along X-axis

# Elongating geometry and modulating coordinates via translation transformation
x2 = np.sin(t2/5) * np.cos(t2) + velocity_translation
y2 = np.sin(t2/5) * np.sin(t2) * 0.8  # Slight Lorentz lateral compression effect
z2 = np.cos(t2/5) * 0.8

ax2.plot(x2, y2, z2, color='darkorange', lw=1.5, label=r'Traveling Phase Pattern ($\lambda = h/p$)')
ax2.set_title("Moving Wavepacket: Spacetime Trace ($v > 0$)", fontsize=12, fontweight='bold')
ax2.set_xlim([0, 9]); ax2.set_ylim([-1.2, 1.2]); ax2.set_zlim([-1.2, 1.2])
ax2.view_init(elev=20, azim=-60)
ax2.legend(loc='upper right')

plt.tight_layout()
plt.show()
