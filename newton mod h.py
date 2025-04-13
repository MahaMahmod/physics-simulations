import numpy as np
import matplotlib.pyplot as plt

# Define the analytical solution
def analytical_solution(T0, Ta, k, t):
    return Ta + (T0 - Ta) * np.exp(-k * t)

# Implement Euler's Method
def euler_method(T0, Ta, k, h, t_max):
    n = int(t_max / h)
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

# Start with a large step size and gradually refine
h = 1.0
t_target = 5  # Check convergence at t = 5s
previous_T = None
converged = False
step_sizes = []
errors = []

while not converged:
    # Compute numerical and analytical solutions
    t_values, T_numerical = euler_method(T0, Ta, k, h, t_max)
    T_analytical = analytical_solution(T0, Ta, k, t_values)

    # Find the temperature at the target time
    T_numerical_target = np.interp(t_target, t_values, T_numerical)
    T_analytical_target = analytical_solution(T0, Ta, k, t_target)

    # Compute error at the target time
    error = abs(T_analytical_target - T_numerical_target)
    
    # Store step size and error for analysis
    step_sizes.append(h)
    errors.append(error)

    # Check convergence condition (change in estimated temp < 0.01°C)
    if previous_T is not None and abs(previous_T - T_numerical_target) < 0.01:
        converged = True
    else:
        previous_T = T_numerical_target
        h /= 2  # Reduce step size (increase number of steps)

# Plot step size vs error to show convergence
plt.figure(figsize=(10, 5))
plt.plot(step_sizes, errors, marker="o", linestyle="dashed")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Step Size (h)")
plt.ylabel("Error at t = 5s")
plt.title("Convergence Analysis: Step Size vs. Error")
plt.grid(True)
plt.show()

# Print final step size when convergence is reached
print(f"Converged with step size h = {h:.6f}, error = {error:.6f}")

