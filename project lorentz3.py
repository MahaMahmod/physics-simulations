import numpy as np
import matplotlib.pyplot as plt

# Constants
q = 1.6e-19     # Charge (C)
m = 9.11e-31    # Mass of electron (kg)
B = np.array([0, 0, 1])   # Magnetic field (T)
E = np.array([0, 1e3, 0]) # Electric field (V/m)

# Time setup
dt = 1e-11
t_max = 1e-7
N = int(t_max / dt)
time = np.linspace(0, t_max, N)

# Initial velocities for different cases
v0_list = [
    np.array([1e5, 0, 0]),        # case a
    np.array([1e5, 1e5, 0]),      # case b
    np.array([1e5, 0, 1e5]),      # case c
    np.array([1e5, 1e5, 1e5])     # case d
]

labels = ["v0 = [1e5, 0, 0]", "v0 = [1e5, 1e5, 0]", "v0 = [1e5, 0, 1e5]", "v0 = [1e5, 1e5, 1e5]"]

# Euler-Cromer simulation function
def simulate_lorentz(v0, E_field):
    r = np.zeros((N, 3))
    v = np.zeros((N, 3))
    r[0] = np.array([0, 0, 0])
    v[0] = v0

    for i in range(N - 1):
        a = (q / m) * (E_field + np.cross(v[i], B))
        v[i+1] = v[i] + a * dt
        r[i+1] = r[i] + v[i+1] * dt
    return r

# Compare trajectories with and without E
fig = plt.figure(figsize=(16, 12))
E_zero = np.array([0, 0, 0])

for i, v0 in enumerate(v0_list):
    r_with_E = simulate_lorentz(v0, E_field=E)
    r_without_E = simulate_lorentz(v0, E_field=E_zero)

    ax = fig.add_subplot(2, 2, i+1, projection='3d')
    ax.plot(r_with_E[:, 0], r_with_E[:, 1], r_with_E[:, 2], label="With E", color='blue')
    ax.plot(r_without_E[:, 0], r_without_E[:, 1], r_without_E[:, 2], label="Without E", color='red', linestyle='--')
    ax.set_title(f"Trajectory: {labels[i]}")
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("z (m)")
    ax.legend()

plt.suptitle("Part (c): With vs Without Electric Field (Euler-Cromer Method)", fontsize=16)
plt.tight_layout()
plt.show()
