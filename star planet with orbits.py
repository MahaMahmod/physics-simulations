import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 1.0
M = 1.0
m = 1.0
dt = 0.01
steps = 5000

# Function to classify orbit type based on energy
def classify_orbit(energy):
    if energy < 0:
        return "Bound Orbit (Elliptical)"
    elif np.isclose(energy, 0, atol=1e-2):
        return "Parabolic Escape Orbit"
    else:
        return "Hyperbolic Escape Orbit"

# Initial speeds for 3 cases
initial_speeds = [1.0, np.sqrt(2), 2.0]
labels = ["Elliptical (E<0)", "Parabolic (E≈0)", "Hyperbolic (E>0)"]

plt.figure(figsize=(15, 5))

for idx, speed in enumerate(initial_speeds):
    r = np.array([1.0, 0.0])
    v = np.array([0.0, speed])
    r_list = []
    energy_list = []

    for i in range(steps):
        dist = np.linalg.norm(r)
        a = -G * M * r / dist**3
        v += dt * a        # Euler-Cromer
        r += dt * v
        r_list.append(r.copy())

        kinetic = 0.5 * m * np.dot(v, v)
        potential = -G * M * m / np.linalg.norm(r)
        total_energy = kinetic + potential
        energy_list.append(total_energy)

    r_arr = np.array(r_list)
    final_energy = energy_list[-1]
    orbit_type = classify_orbit(final_energy)

    # Plot each orbit in subplot
    plt.subplot(1, 3, idx + 1)
    plt.plot(r_arr[:, 0], r_arr[:, 1], label=orbit_type)
    plt.plot(0, 0, 'yo', label='Star')
    plt.title(f"{labels[idx]}\n{orbit_type}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axis("equal")
    plt.grid()
    plt.legend()

plt.tight_layout()
plt.show()
