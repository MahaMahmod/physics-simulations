import numpy as np
import matplotlib.pyplot as plt

# Parameters
g = 9.8  # Gravity (m/s^2)
L = 1.0  # Length of pendulum (m)
steps = 1000  # Number of time steps
t_max = 10  # Total simulation time (s)
dt = t_max / steps  # Time step size

# Initial conditions
theta_0 = np.radians(30)  # Initial angle (30 degrees in radians)
omega_0 = 0.0  # Initial angular velocity

# Arrays for storing results
theta_euler = np.zeros(steps+1)
omega_euler = np.zeros(steps+1)
theta_cromer = np.zeros(steps+1)
omega_cromer = np.zeros(steps+1)
time = np.linspace(0, t_max, steps+1)

# Set initial values
theta_euler[0] = theta_0
omega_euler[0] = omega_0
theta_cromer[0] = theta_0
omega_cromer[0] = omega_0

# Euler Method Simulation
for n in range(steps):
    omega_euler[n+1] = omega_euler[n] - (g/L) * np.sin(theta_euler[n]) * dt
    theta_euler[n+1] = theta_euler[n] + omega_euler[n] * dt

# Euler-Cromer Method Simulation
for n in range(steps):
    omega_cromer[n+1] = omega_cromer[n] - (g/L) * np.sin(theta_cromer[n]) * dt
    theta_cromer[n+1] = theta_cromer[n] + omega_cromer[n+1] * dt  # Use updated velocity

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(time, np.degrees(theta_euler), label='Euler Method', linestyle='dashed')
plt.plot(time, np.degrees(theta_cromer), label='Euler-Cromer Method')
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.legend()
plt.title("Simple Pendulum: Euler vs Euler-Cromer")
plt.grid()
plt.show()

