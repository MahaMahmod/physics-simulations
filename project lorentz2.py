import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
m = 1.67e-27  # kg
q = 1.6e-19   # C
E = np.array([0, 0, 500])     # V/m
B = np.array([0, 0, 0.01])    # T
dt = 1e-9                     # s
t_max = 1e-6
N = int(t_max / dt)

def lorentz_force(v, E, B):
    return q * (E + np.cross(v, B))

def simulate_lorentz(v0, method="euler-cromer", E=E, B=B):
    v = np.zeros((N, 3))
    r = np.zeros((N, 3))
    v[0] = v0
    for i in range(1, N):
        a = lorentz_force(v[i-1], E, B) / m
        if method == "euler":
            v[i] = v[i-1] + a * dt
            r[i] = r[i-1] + v[i-1] * dt
        elif method == "euler-cromer":
            v[i] = v[i-1] + a * dt
            r[i] = r[i-1] + v[i] * dt
    return r, v

# Initial velocities for each case
v0_list = [
    np.array([1e5, 0, 0]),            # along x
    np.array([0, 0, 1e5]),            # along z
    np.array([1e5, 1e5, 0]),          # in x-y plane
    np.array([1e5, 1e5, 1e5])         # in 3D space
]

labels = [
    "v0 = (1e5, 0, 0)",
    "v0 = (0, 0, 1e5)",
    "v0 = (1e5, 1e5, 0)",
    "v0 = (1e5, 1e5, 1e5)"
]

# Plotting all four cases
fig = plt.figure(figsize=(16, 12))

for i, v0 in enumerate(v0_list):
    r, _ = simulate_lorentz(v0, method="euler-cromer")

    ax = fig.add_subplot(2, 2, i+1, projection='3d')
    ax.plot(r[:, 0], r[:, 1], r[:, 2])
    ax.set_title(labels[i])
    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_zlabel('z (m)')

plt.suptitle("3D Trajectories for Different Initial Velocities", fontsize=16)
plt.tight_layout()
plt.show()

