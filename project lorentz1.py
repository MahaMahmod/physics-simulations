import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
m = 1.67e-27  # mass of proton in kg
q = 1.6e-19   # charge in C
E = np.array([0, 0, 500])     # Electric field (V/m)
B = np.array([0, 0, 0.01])    # Magnetic field (T)
dt = 1e-9                     # Time step (s)
t_max = 1e-6                  # Total simulation time (s)
N = int(t_max / dt)          # Number of time steps

# Lorentz force
def lorentz_force(v, E, B):
    return q * (E + np.cross(v, B))

# Euler-Cromer simulation
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

# Initial condition: velocity along x-axis
v0 = np.array([1e5, 0, 0])  # m/s
r, v = simulate_lorentz(v0, method="euler-cromer")

# Plotting
fig = plt.figure(figsize=(14, 5))

# 3D plot
ax1 = fig.add_subplot(131, projection='3d')
ax1.plot(r[:,0], r[:,1], r[:,2])
ax1.set_title("3D Trajectory")
ax1.set_xlabel("x (m)")
ax1.set_ylabel("y (m)")
ax1.set_zlabel("z (m)")

# 2D projection: x-y
ax2 = fig.add_subplot(132)
ax2.plot(r[:,0], r[:,1])
ax2.set_title("x-y Projection")
ax2.set_xlabel("x (m)")
ax2.set_ylabel("y (m)")
ax2.axis('equal')

# 2D projection: x-z
ax3 = fig.add_subplot(133)
ax3.plot(r[:,0], r[:,2])
ax3.set_title("x-z Projection")
ax3.set_xlabel("x (m)")
ax3.set_ylabel("z (m)")
ax3.axis('equal')

plt.tight_layout()
plt.show()

