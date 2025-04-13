import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 10.0   # Resistance (Ohms)
L = 1.0    # Inductance (H)
C = 0.1    # Capacitance (F)
V0 = 10.0  # External voltage amplitude (V)
omega = 5.0  # Angular frequency (rad/s)

steps = 1000  # Number of time steps
t_max = 10    # Total simulation time (s)
dt = t_max / steps  # Time step size

# Initial conditions
Q_0 = 0.0  # Initial charge (C)
I_0 = 0.0  # Initial current (A)

# Arrays for storing results
Q_euler = np.zeros(steps+1)
I_euler = np.zeros(steps+1)
Q_cromer = np.zeros(steps+1)
I_cromer = np.zeros(steps+1)
time = np.linspace(0, t_max, steps+1)

# Set initial values
Q_euler[0] = Q_0
I_euler[0] = I_0
Q_cromer[0] = Q_0
I_cromer[0] = I_0

# Euler Method Simulation
for n in range(steps):
    V_t = V0 * np.cos(omega * time[n])  # External voltage at time t
    I_euler[n+1] = I_euler[n] + ((V_t - R * I_euler[n] - Q_euler[n] / C) / L) * dt
    Q_euler[n+1] = Q_euler[n] + I_euler[n] * dt

# Euler-Cromer Method Simulation
for n in range(steps):
    V_t = V0 * np.cos(omega * time[n])  # External voltage at time t
    I_cromer[n+1] = I_cromer[n] + ((V_t - R * I_cromer[n] - Q_cromer[n] / C) / L) * dt
    Q_cromer[n+1] = Q_cromer[n] + I_cromer[n+1] * dt  # Use updated current

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(time, Q_euler, label='Charge (Euler)', linestyle='dashed')
plt.plot(time, Q_cromer, label='Charge (Euler-Cromer)')
plt.xlabel("Time (s)")
plt.ylabel("Charge (C)")
plt.legend()
plt.title("RLC Circuit: Charge vs Time")
plt.grid()
plt.show()

