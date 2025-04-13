import numpy as np
import matplotlib.pyplot as plt

# Constants
k = 10.0      # spring constant
m = 1.0       # mass
L = 1.0       # natural length of springs
dt = 0.01     # time step
t_max = 20    # total time
steps = int(t_max / dt)

# Spring anchors: (x, y) positions of fixed ends
anchors = [(-L, 0), (L, 0), (0, -L), (0, L)]

# Initial conditions
x0, y0 = 0.5, 0.0   # initial displacement
vx0, vy0 = 0.0, 0.5 # initial velocity

# Euler variables
x_e, y_e = x0, y0
vx_e, vy_e = vx0, vy0
x_list_e, y_list_e = [x_e], [y_e]

# Euler-Cromer variables
x_c, y_c = x0, y0
vx_c, vy_c = vx0, vy0
x_list_c, y_list_c = [x_c], [y_c]

# Simulation loop
for _ in range(steps):
    # --------- Euler Method ---------
    Fx, Fy = 0.0, 0.0
    for ax, ay in anchors:
        dx, dy = x_e - ax, y_e - ay
        r = np.sqrt(dx**2 + dy**2)
        F = -k * (r - L)
        Fx += F * (dx / r)
        Fy += F * (dy / r)
    
    ax_e = Fx / m
    ay_e = Fy / m
    x_e += vx_e * dt
    y_e += vy_e * dt
    vx_e += ax_e * dt
    vy_e += ay_e * dt
    x_list_e.append(x_e)
    y_list_e.append(y_e)

    # --------- Euler-Cromer Method ---------
    Fx, Fy = 0.0, 0.0
    for ax, ay in anchors:
        dx, dy = x_c - ax, y_c - ay
        r = np.sqrt(dx**2 + dy**2)
        F = -k * (r - L)
        Fx += F * (dx / r)
        Fy += F * (dy / r)
    
    ax_c = Fx / m
    ay_c = Fy / m
    vx_c += ax_c * dt
    vy_c += ay_c * dt
    x_c += vx_c * dt
    y_c += vy_c * dt
    x_list_c.append(x_c)
    y_list_c.append(y_c)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(x_list_e, y_list_e, label='Euler', color='red')
plt.plot(x_list_c, y_list_c, label='Euler-Cromer', color='blue')
plt.xlabel("x position")
plt.ylabel("y position")
plt.title("2D Oscillator: Trajectory")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()

