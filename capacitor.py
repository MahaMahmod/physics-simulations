import numpy as np
import matplotlib.pyplot as plt

# Parameters
V0 = 10  # Initial voltage (for discharge)
Vs = 12  # Supply voltage (for charge)
R = 1000  # Resistance in ohms
C = 0.001  # Capacitance in farads
T = 5 * R * C  # Simulation time (~5 time constants)
n = 1000  # Number of steps
dt = T / n  # Step size

# Time array
t_values = np.linspace(0, T, n)
V_discharge = np.zeros(n)
V_charge = np.zeros(n)
V_discharge[0] = V0  # Initial condition for discharge
V_charge[0] = 0  # Initial condition for charging

# Euler's method for discharging
for i in range(1, n):
    V_discharge[i] = V_discharge[i-1] - (V_discharge[i-1] / (R * C)) * dt

# Euler's method for charging
for i in range(1, n):
    V_charge[i] = V_charge[i-1] + ((Vs - V_charge[i-1]) / (R * C)) * dt

# Analytical solutions
V_discharge_exact = V0 * np.exp(-t_values / (R * C))
V_charge_exact = Vs * (1 - np.exp(-t_values / (R * C)))

# Plot
plt.plot(t_values, V_discharge, label="Euler Discharge", linestyle="--")
plt.plot(t_values, V_discharge_exact, label="Analytical Discharge", linestyle="-")
plt.plot(t_values, V_charge, label="Euler Charge", linestyle="--")
plt.plot(t_values, V_charge_exact, label="Analytical Charge", linestyle="-")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.legend()
plt.title("Capacitor Charging/Discharging using Euler's Method")
plt.grid()
plt.show()

