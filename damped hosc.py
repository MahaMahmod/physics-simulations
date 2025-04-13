import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1.0  # Mass (kg)
k = 1.0  # Spring constant (N/m)
b = 0.2  # Damping coefficient (kg/s)
steps = 1000  # Number of time steps
t_max = 20  # Total simulation time (s)
dt = t_max / steps  # Time step size

# Initial conditions
x_0 = 1.0  # Initial position (m)
v_0 = 0.0  # Initial velocity (m/s)

# Arrays for storing results
x_euler = np.zeros(steps+1)
v_euler = np.zeros(steps+1)
x_cromer = np.zeros(steps+1)
v_cromer = np.zeros(steps+1)
time = np.linspace(0, t_max, steps+1)

# Set initial values
x_euler[0] = x_0
v_euler[0] = v_0
x_cromer[0] = x_0
v_cromer[0] = v_0

# Euler Method Simulation
for n in range(steps):
    v_euler[n+1] = v_euler[n] + (- (k/m) * x_euler[n] - (b/m) * v_euler[n]) * dt
    x_euler[n+1] = x_euler[n] + v_euler[n] * dt

# Euler-Cromer Method Simulation
for n in range(steps):
    v_cromer[n+1] = v_cromer[n] + (- (k/m) * x_cromer[n] - (b/m) * v_cromer[n]) * dt
    x_cromer[n+1] = x_cromer[n] + v_cromer[n+1] * dt  # Use updated velocity

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(time, x_euler, label='Euler Method', linestyle='dashed')
plt.plot(time, x_cromer, label='Euler-Cromer Method')
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend()
plt.title("Damped Harmonic Oscillator: Euler vs Euler-Cromer")
plt.grid()
plt.show()

