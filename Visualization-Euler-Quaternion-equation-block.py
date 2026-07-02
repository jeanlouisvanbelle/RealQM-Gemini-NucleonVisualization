import matplotlib.pyplot as plt

# Create a clean, presentation-width figure
fig, ax = plt.subplots(figsize=(10, 4.5))
ax.axis('off')

# Define background panel styling for the comparison boxes
box_props_left = dict(boxstyle='round,pad=1.2', facecolor='#F0F4F8', edgecolor='#3182CE', lw=1.5)
box_props_right = dict(boxstyle='round,pad=1.2', facecolor='#FFF5F5', edgecolor='#E53E3E', lw=1.5)

# Left Box Text (Excluding title)
standard_qm_text = (
    "\n\n"
    r"$\Psi = e^{i\theta} = \cos\theta + i\sin\theta$" + "\n\n"
    "• Wavefunctions act as linear vectors\n"
    "• Combines via ADDITION (Superposition)\n"
    "• Restricted to flat, abstract 2D grid"
)

# Right Box Text (Excluding title)
real_qm_text = (
    "\n\n"
    r"$q = e^{i\theta}e^{j\phi}$" + "\n\n"
    "• Quaternions act as spatial operators\n"
    "• Combines via MULTIPLICATION (Composition)\n"
    r"• Non-commutative: $ij = k$ defines spin axis"
)

# Render the text panels onto the figure canvas
ax.text(0.1, 0.5, standard_qm_text, fontsize=12, va='center', ha='left', bbox=box_props_left, linespacing=1.5)
ax.text(0.55, 0.5, real_qm_text, fontsize=12, va='center', ha='left', bbox=box_props_right, linespacing=1.5)

# Overlay bold headers precisely to avoid text duplication
ax.text(0.12, 0.72, "2D Euler Wave Math (Addition)", fontsize=13, fontweight='bold', color='#2B6CB0')
ax.text(0.57, 0.72, "3D Quaternion Operator Math (Multiplication)", fontsize=13, fontweight='bold', color='#C53030')

# Global Title overlay
ax.text(0.5, 0.95, "The Algebra Shift: From Interference to Spatial Composition", 
        fontsize=14, fontweight='bold', va='center', ha='center', color='#2D3748')

plt.tight_layout()
plt.show()
