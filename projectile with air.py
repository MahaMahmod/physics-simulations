import numpy as np
import matplotlib.pyplot as plt

# Given parameters
m = 0.2  # kg
c = 0.05  # drag coefficient (kg/m)
g = 9.81  # gravity (m/s^2)
v0 = 50.0  # initial velocity (m/s)
theta0 = 45.0 * (np.pi / 180)  # convert degrees to radians
dt = 0.01  # time step

# Initial conditions
x_euler, y_euler = 0.0, 0.0
vx_euler, vy_euler = v0 * np.cos(theta0), v0 * np.sin(theta0)

x_cromer, y_cromer = 0.0, 0.0
vx_cromer, vy_cromer = v0 * np.cos(theta0), v0 * np.sin(theta0)

t = 0.0

# Lists to store values
time, x_vals_euler, y_vals_euler = [], [], []
x_vals_cromer, y_vals_cromer = [], []

# Simulation loop
while y_euler >= 0 or y_cromer >= 0:
    v_euler = np.sqrt(vx_euler**2 + vy_euler**2)
    ax_euler = - (c/m) * v_euler * vx_euler
    ay_euler = -g - (c/m) * v_euler * vy_euler
    
    v_cromer = np.sqrt(vx_cromer**2 + vy_cromer**2)
    ax_cromer = - (c/m) * v_cromer * vx_cromer
    ay_cromer = -g - (c/m) * v_cromer * vy_cromer
    
    # Euler method update
    x_euler += vx_euler * dt
    y_euler += vy_euler * dt
    vx_euler += ax_euler * dt
    vy_euler += ay_euler * dt
    
    # Euler-Cromer method update
    vx_cromer += ax_cromer * dt
    vy_cromer += ay_cromer * dt
    x_cromer += vx_cromer * dt
    y_cromer += vy_cromer * dt
    
    # Store values
    if y_euler >= 0:
        x_vals_euler.append(x_euler)
        y_vals_euler.append(y_euler)
    
    if y_cromer >= 0:
        x_vals_cromer.append(x_cromer)
        y_vals_cromer.append(y_cromer)
    
    time.append(t)
    t += dt

# Plot results
plt.figure(figsize=(8, 6))
plt.plot(x_vals_euler, y_vals_euler, label='Euler Method', linestyle='dashed')
plt.plot(x_vals_cromer, y_vals_cromer, label='Euler-Cromer Method', linestyle='solid')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Projectile Motion with Air Resistance: Euler vs Euler-Cromer')
plt.legend()
plt.grid()
plt.show()

