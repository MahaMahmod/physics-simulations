import numpy as np
import matplotlib.pyplot as plt

# Parameters
N0 = 100  # Initial number of atoms
lambda_ = 0.1  # Decay constant
T = 50  # Total time
n = 1000  # Number of steps
dt = T / n  # Step size

# Time array
t_values = np.linspace(0, T, n)
N_values = np.zeros(n)
N_values[0] = N0  # Initial condition

# Euler's method
for i in range(1, n):
    N_values[i] = N_values[i-1] - lambda_ * N_values[i-1] * dt

# Analytical solution
N_exact = N0 * np.exp(-lambda_ * t_values)

# Plot
plt.plot(t_values, N_values, label="Euler Method", linestyle="--")
plt.plot(t_values, N_exact, label="Analytical Solution", linestyle="-")
plt.xlabel("Time")
plt.ylabel("Number of Atoms (N)")
plt.legend()
plt.title("Radioactive Decay using Euler's Method")
plt.grid()
plt.show()

