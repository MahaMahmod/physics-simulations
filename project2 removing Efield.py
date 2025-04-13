import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.6e-19    # Charge (C)
m = 1.67e-27   # Mass (kg)
E = np.array([0, 0, 0])         # Electric field turned off
B = np.array([0, 0, 0.01])      # Magnetic field (T)
v0_magnitude = 1e5              # Initial speed (m/s)

# Time settings
dt = 1e-9
t_max = 5e-6
steps = int(t_max / dt)

# Initial velocity cases
initial_velocities = [
    np.array([v0_magnitude, 0, 0]),        # Along x-axis
    np.array([0, 0, v0_magnitude]),        # Along z-axis
    np.array([v0_magnitude, v0_magnitude, 0]),  # In x-y plane
    np.array([v0_magnitude]*3),            # Diagonal
]

labels = ['x-axis', 'z-axis', 'x-y plane', 'x=y=z']

fig = plt.figure(figsize=(18, 12))

for i, v0 in enumerate(initial_velocities):
    r = np.array([0.0, 0.0, 0.0])    # Initial position
    v = v0.copy()
    
    trajectory = [r.copy()]
    
    for _ in range(steps):
        a = (q / m) * (E + np.cross(v, B))
        v += a * dt
        r += v * dt
        trajectory.append(r.copy())
    
    trajectory = np.array(trajectory)
    
    ax = fig.add_subplot(2, 2, i+1, projection='3d')
    ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2])
    ax.set_title(f'3D trajectory (E=0): {labels[i]}')
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_zlabel('z (m)')
    ax.grid()

plt.tight_layout()
plt.show()

