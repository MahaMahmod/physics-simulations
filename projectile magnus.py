import numpy as np
import matplotlib.pyplot as plt

# Given parameters
m = 0.2  # kg
c = 0.05  # drag coefficient (kg/m)
g = 9.81  # gravity (m/s^2)
v0 = 50.0  # initial velocity (m/s)
theta0 = 45.0 * (np.pi / 180)  # convert degrees to radians
dt = 0.01  # time step
S = 0.01  # Magnus force coefficient
omega = np.array([0, 0, 4*22/7])  # Spin vector (only z-component)

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
    drag_force_euler = - (c/m) * v_euler
    magnus_force_euler = S * np.cross(omega, np.array([vx_euler, vy_euler, 0])) / m
    ax_euler = drag_force_euler * vx_euler + magnus_force_euler[0]
    ay_euler = -g + drag_force_euler * vy_euler + magnus_force_euler[1]
    
    v_cromer = np.sqrt(vx_cromer**2 + vy_cromer**2)
    drag_force_cromer = - (c/m) * v_cromer
    magnus_force_cromer = S * np.cross(omega, np.array([vx_cromer, vy_cromer, 0])) / m
    ax_cromer = drag_force_cromer * vx_cromer + magnus_force_cromer[0]
    ay_cromer = -g + drag_force_cromer * vy_cromer + magnus_force_cromer[1]
    
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
plt.title('Projectile Motion with Air Resistance and Magnus Effect')
plt.legend()
plt.grid()
plt.show()
