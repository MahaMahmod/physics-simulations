import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 1.0      # Gravitational constant (scaled units)
M = 1.0      # Mass of the star (scaled units)

# Initial conditions (planet's position and velocity)
r_euler = np.array([1.0, 0.0])  # Initial position (AU)
v_euler = np.array([0.0, 1.0])  # Initial velocity (AU/yr)

r_cromer = r_euler.copy()
v_cromer = v_euler.copy()

# Time setup
dt = 0.01    # Time step
t_max = 10.0
steps = int(t_max / dt)

# Lists to store positions
trajectory_euler = [r_euler.copy()]
trajectory_cromer = [r_cromer.copy()]

# Euler & Euler-Cromer methods
for _ in range(steps):
    r_mag_euler = np.linalg.norm(r_euler)
    r_mag_cromer = np.linalg.norm(r_cromer)

    # Compute acceleration
    a_euler = -G * M * r_euler / r_mag_euler**3
    a_cromer = -G * M * r_cromer / r_mag_cromer**3

    # Euler method
    r_euler += v_euler * dt
    v_euler += a_euler * dt
    trajectory_euler.append(r_euler.copy())

    # Euler-Cromer method
    v_cromer += a_cromer * dt
    r_cromer += v_cromer * dt
    trajectory_cromer.append(r_cromer.copy())

# Convert to NumPy arrays
trajectory_euler = np.array(trajectory_euler)
trajectory_cromer = np.array(trajectory_cromer)

# Plot results
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].plot(trajectory_euler[:, 0], trajectory_euler[:, 1], label="Euler", color="red")
ax[0].scatter(0, 0, color="yellow", marker="o", label="Star")
ax[0].set_title("Euler Method")
ax[0].set_xlabel("x (AU)")
ax[0].set_ylabel("y (AU)")
ax[0].legend()

ax[1].plot(trajectory_cromer[:, 0], trajectory_cromer[:, 1], label="Euler-Cromer", color="blue")
ax[1].scatter(0, 0, color="yellow", marker="o", label="Star")
ax[1].set_title("Euler-Cromer Method")
ax[1].set_xlabel("x (AU)")
ax[1].set_ylabel("y (AU)")
ax[1].legend()

plt.show()

