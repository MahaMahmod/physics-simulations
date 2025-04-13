import numpy as np
import matplotlib.pyplot as plt

# Given parameters
k = 10.0  # Spring constant (N/m)
m1 = 1.5  # Mass of first oscillator (kg)
m2 = 2.0  # Mass of second oscillator (kg)

# Initial conditions
x1_0 = 0.1  # Initial position of mass 1
x2_0 = 0.1  # Initial position of mass 2
v1_0 = 0.0  # Initial velocity of mass 1
v2_0 = 0.0  # Initial velocity of mass 2

t_max = 10.0  # Maximum simulation time
steps = 1000  # Number of steps
dt = t_max / steps  # Time step

# Initialize arrays for Euler and Euler-Cromer
x1_euler, x2_euler = np.zeros(steps), np.zeros(steps)
v1_euler, v2_euler = np.zeros(steps), np.zeros(steps)
x1_cromer, x2_cromer = np.zeros(steps), np.zeros(steps)
v1_cromer, v2_cromer = np.zeros(steps), np.zeros(steps)

time = np.linspace(0, t_max, steps)

# Set initial conditions
x1_euler[0], x2_euler[0] = x1_0, x2_0
v1_euler[0], v2_euler[0] = v1_0, v2_0
x1_cromer[0], x2_cromer[0] = x1_0, x2_0
v1_cromer[0], v2_cromer[0] = v1_0, v2_0

# Euler and Euler-Cromer iterations
for i in range(steps - 1):
    # Compute accelerations
    a1 = - (k / m1) * (2 * x1_euler[i] - x2_euler[i])
    a2 = - (k / m2) * (2 * x2_euler[i] - x1_euler[i])
    
    # Euler Method
    x1_euler[i + 1] = x1_euler[i] + v1_euler[i] * dt
    x2_euler[i + 1] = x2_euler[i] + v2_euler[i] * dt
    v1_euler[i + 1] = v1_euler[i] + a1 * dt
    v2_euler[i + 1] = v2_euler[i] + a2 * dt
    
    # Euler-Cromer Method
    v1_cromer[i + 1] = v1_cromer[i] + a1 * dt
    v2_cromer[i + 1] = v2_cromer[i] + a2 * dt
    x1_cromer[i + 1] = x1_cromer[i] + v1_cromer[i + 1] * dt
    x2_cromer[i + 1] = x2_cromer[i] + v2_cromer[i + 1] * dt

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(time, x1_euler, 'r--', label='Euler: x1')
plt.plot(time, x2_euler, 'b--', label='Euler: x2')
plt.plot(time, x1_cromer, 'r-', label='Euler-Cromer: x1')
plt.plot(time, x2_cromer, 'b-', label='Euler-Cromer: x2')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.legend()
plt.title('Coupled Oscillators: Euler vs Euler-Cromer')
plt.grid()
plt.show()

