import numpy as np
import matplotlib.pyplot as plt

# Parameters
I0 = 100  # Initial intensity
mu = 0.05  # Attenuation coefficient
Z = 50  # Maximum depth
n = 1000  # Number of steps
dz = Z / n  # Step size

# Depth array
z_values = np.linspace(0, Z, n)
I_values = np.zeros(n)
I_values[0] = I0  # Initial condition

# Euler's method
for i in range(1, n):
    I_values[i] = I_values[i-1] - mu * I_values[i-1] * dz

# Analytical solution
I_exact = I0 * np.exp(-mu * z_values)

# Plot
plt.plot(z_values, I_values, label="Euler Method", linestyle="--")
plt.plot(z_values, I_exact, label="Analytical Solution", linestyle="-")
plt.xlabel("Depth (z)")
plt.ylabel("Light Intensity (I)")
plt.legend()
plt.title("Light Intensity Attenuation using Euler's Method")
plt.grid()
plt.show()

