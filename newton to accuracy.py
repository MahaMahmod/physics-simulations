import numpy as np
import matplotlib.pyplot as plt

# Define the analytical solution
def analytical_solution(T0, Ta, k, t):
    return Ta + (T0 - Ta) * np.exp(-k * t)

# Implement Euler's Method with n steps
def euler_method(T0, Ta, k, n, t_max):
    h = t_max / n  # Step size
    T = np.zeros(n+1)
    T[0] = T0
    t_values = np.linspace(0, t_max, n+1)

    for i in range(n):
        T[i+1] = T[i] + h * (-k * (T[i] - Ta))

    return t_values, T

# Parameters
T0 = 100   # Initial temperature
Ta = 25    # Ambient temperature
k = 0.1    # Cooling constant
t_max = 10 # Maximum time
t_target = 5  # Time to check convergence

# Start with a small number of steps
n = 10
previous_T = None
converged = False
steps = []
errors = []

while not converged:
    # Compute numerical and analytical solutions
    t_values, T_numerical = euler_method(T0, Ta, k, n, t_max)
    T_analytical = analytical_solution(T0, Ta, k, t_values)

    # Interpolate temperature at target time (t = 5s)
    T_numerical_target = np.interp(t_target, t_values, T_numerical)
    T_analytical_target = analytical_solution(T0, Ta, k, t_target)

    # Compute absolute error
    error = abs(T_analytical_target - T_numerical_target)

    # Store n and error for analysis
    steps.append(n)
    errors.append(error)

    # Check convergence condition (change in estimated temp < 0.01°C)
    if previous_T is not None and abs(previous_T - T_numerical_target) < 0.01:
        converged = True
    else:
        previous_T = T_numerical_target
        n *= 2  # Double the number of steps

# Plot steps vs error to show convergence
plt.figure(figsize=(10, 5))
plt.plot(steps, errors, marker="o", linestyle="dashed")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Number of Steps (n)")
plt.ylabel("Error at t = 5s")
plt.title("Convergence Analysis: Steps vs. Error")
plt.grid(True)
plt.show()

# Print final number of steps
print(f"Converged with n = {n}, error = {error:.6f}")

