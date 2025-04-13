import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1.0        # Mass
k = 10.0       # Spring constant
L = 1.0        # Natural length of springs
dt = 0.01      # Time step
T = 10         # Total time
steps = int(T / dt)

# Anchor points of the springs
anchors = [(0, L), (0, -L), (L, 0), (-L, 0)]

def spring_force(x, y, a, b):
    dx = x - a
    dy = y - b
    dist = np.sqrt(dx**2 + dy**2)
    stretch = dist - L
    if dist == 0:
        return 0, 0
    fx = -k * stretch * (dx / dist)
    fy = -k * stretch * (dy / dist)
    return fx, fy

def simulate(method='euler'):
    # Initial conditions
    x, y = 0.5, 0.0
    vx, vy = 0.0, 1.0

    pos_x, pos_y = [x], [y]

    for _ in range(steps):
        fx_total, fy_total = 0.0, 0.0
        for a, b in anchors:
            fx, fy = spring_force(x, y, a, b)
            fx_total += fx
            fy_total += fy

        ax = fx_total / m
        ay = fy_total / m

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

        pos_x.append(x)
        pos_y.append(y)

    return np.array(pos_x), np.array(pos_y)

# Run both simulations
x_euler, y_euler = simulate('euler')
x_ec, y_ec = simulate('euler-cromer')

# Plot trajectories
plt.figure(figsize=(8, 6))
plt.plot(x_euler, y_euler, label='Euler')
plt.plot(x_ec, y_ec, label='Euler-Cromer')
plt.plot(0, 0, 'ko', label='Equilibrium')
for a, b in anchors:
    plt.plot(a, b, 'rx')
plt.xlabel('x')
plt.ylabel('y')
plt.title('2D Oscillator: Trajectories')
plt.legend()
plt.axis('equal')
plt.grid()
plt.show()

