import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 1.0      # Gravitational constant (scaled units)
M = 1.0      # Mass of the star (scaled units)
m = 1.0      # Mass of the planet (scaled units)

# Initial conditions (planet's position and velocity)
r_euler = np.array([1.0, 0.0])  # Initial position (AU)
v_euler = np.array([0.0, 1.0])  # Initial velocity (AU/yr)

r_cromer = r_euler.copy()
v_cromer = v_euler.copy()

# Time setup
dt = 0.01    # Time step
t_max = 10.0
steps = int(t_max / dt)

# Lists to store positions, energy, and angular momentum
trajectory_euler = [r_euler.copy()]
trajectory_cromer = [r_cromer.copy()]
energy_euler = []
energy_cromer = []
L_euler = []
L_cromer = []

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

    # Compute Energy and Angular Momentum
    kinetic_energy_euler = 0.5 * m * np.linalg.norm(v_euler) ** 2
    potential_energy_euler = -G * M * m / r_mag_euler
    energy_euler.append(kinetic_energy_euler + potential_energy_euler)

    kinetic_energy_cromer = 0.5 * m * np.linalg.norm(v_cromer) ** 2
    potential_energy_cromer = -G * M * m / r_mag_cromer
    energy_cromer.append(kinetic_energy_cromer + potential_energy_cromer)

    angular_momentum_euler = m * (r_euler[0] * v_euler[1] - r_euler[1] * v_euler[0])
    angular_momentum_cromer = m * (r_cromer[0] * v_cromer[1] - r_cromer[1] * v_cromer[0])
    L_euler.append(angular_momentum_euler)
    L_cromer.append(angular_momentum_cromer)

# Convert to NumPy arrays
trajectory_euler = np.array(trajectory_euler)
trajectory_cromer = np.array(trajectory_cromer)
energy_euler = np.array(energy_euler)
energy_cromer = np.array(energy_cromer)
L_euler = np.array(L_euler)
L_cromer = np.array(L_cromer)

# Plot results
fig, ax = plt.subplots(2, 2, figsize=(12, 10))

# Plot orbits
ax[0, 0].plot(trajectory_euler[:, 0], trajectory_euler[:, 1], label="Euler", color="red")
ax[0, 0].scatter(0, 0, color="yellow", marker="o", label="Star")
ax[0, 0].set_title("Euler Method Orbit")
ax[0, 0].set_xlabel("x (AU)")
ax[0, 0].set_ylabel("y (AU)")
ax[0, 0].legend()

ax[0, 1].plot(trajectory_cromer[:, 0], trajectory_cromer[:, 1], label="Euler-Cromer", color="blue")
ax[0, 1].scatter(0, 0, color="yellow", marker="o", label="Star")
ax[0, 1].set_title("Euler-Cromer Method Orbit")
ax[0, 1].set_xlabel("x (AU)")
ax[0, 1].set_ylabel("y (AU)")
ax[0, 1].legend()

# Plot Energy
ax[1, 0].plot(np.arange(steps) * dt, energy_euler, label="Euler", color="red")
ax[1, 0].plot(np.arange(steps) * dt, energy_cromer, label="Euler-Cromer", color="blue")
ax[1, 0].set_title("Total Energy Over Time")
ax[1, 0].set_xlabel("Time (years)")
ax[1, 0].set_ylabel("Energy")
ax[1, 0].legend()

# Plot Angular Momentum
ax[1, 1].plot(np.arange(steps) * dt, L_euler, label="Euler", color="red")
ax[1, 1].plot(np.arange(steps) * dt, L_cromer, label="Euler-Cromer", color="blue")
ax[1, 1].set_title("Angular Momentum Over Time")
ax[1, 1].set_xlabel("Time (years)")
ax[1, 1].set_ylabel("Angular Momentum")
ax[1, 1].legend()

plt.tight_layout()
plt.show()
