import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 4 * np.pi**2       # Gravitational constant in AU^3 / (yr^2 * solar mass)
M = 1.0                # Mass of Sun (solar mass)
m = 3e-6               # Mass of planet (Earth ~ 3e-6 solar masses)
dt = 0.001             # Time step in years
T = 1.0                # Total simulation time (years)
N = int(T / dt)        # Number of steps

def simulate_orbit(method='euler', vx0=0.0):
    # Initial conditions
    x, y = 1.0, 0.0                 # 1 AU from the Sun
    vx, vy = 0.0, vx0               # vy0 defines shape of orbit

    traj_x, traj_y = [x], [y]
    energy = []

    for _ in range(N):
        r = np.sqrt(x**2 + y**2)
        ax = -G * M * x / r**3
        ay = -G * M * y / r**3

        if method == 'euler':
            x += vx * dt
            y += vy * dt
            vx += ax * dt
            vy += ay * dt
        elif method == 'euler-cromer':
            vx += ax * dt
            vy += ay * dt
            x += vx * dt
            y += vy * dt

        traj_x.append(x)
        traj_y.append(y)

        # Energy calculations
        v2 = vx**2 + vy**2
        K = 0.5 * m * v2
        U = -G * M * m / r
        E = K + U
        energy.append(E)

    return np.array(traj_x), np.array(traj_y), np.array(energy)

# Try different initial velocities
v_values = [2 * np.pi * f for f in [0.7, 1.0, 1.4]]  # AU/year (0.7: ellipse, 1: circle, 1.4: hyperbola)

# Plot trajectories
plt.figure(figsize=(10, 6))
for v0 in v_values:
    for method in ['euler', 'euler-cromer']:
        x, y, _ = simulate_orbit(method=method, vx0=v0)
        label = f'{method} v0={v0:.2f}'
        plt.plot(x, y, label=label)

plt.plot(0, 0, 'yo', label='Sun')  # Sun at origin
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.title('Planetary Orbits using Euler and Euler-Cromer Methods')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()

# Plot Energy
plt.figure(figsize=(10, 5))
for v0 in v_values:
    for method in ['euler', 'euler-cromer']:
        _, _, E = simulate_orbit(method=method, vx0=v0)
        plt.plot(E, label=f'{method} v0={v0:.2f}')

plt.xlabel('Time Step')
plt.ylabel('Total Energy (AU²/year²)')
plt.title('Total Mechanical Energy Over Time')
plt.grid(True)
plt.legend()
plt.show()

