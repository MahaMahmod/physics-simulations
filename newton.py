import numpy as np
import matplotlib.pyplot as plt

def analytical_solution(T0, Ta, k, t):
    return Ta + (T0 - Ta) * np.exp(-k * t)

def euler_method(T0, Ta, k, h, t_max):
    n = int(t_max / h)  # Number of steps
    T = np.zeros(n+1)
    T[0] = T0
    t_values = np.linspace(0, t_max, n+1)
    
    for i in range(n):
        T[i+1] = T[i] + h * (-k * (T[i] - Ta))
    
    return t_values, T

def compute_error(T_numerical, T_analytical):
    return np.abs(T_numerical - T_analytical)

# Parameters
T0 = 100  # Initial temperature
Ta = 25   # Ambient temperature
k = 0.1   # Cooling rate
h = 0.5   # Step size
t_max = 50  # Total time

# Compute solutions
t_values, T_numerical = euler_method(T0, Ta, k, h, t_max)
T_analytical = analytical_solution(T0, Ta, k, t_values)
error = compute_error(T_numerical, T_analytical)

# Plot solutions
plt.figure(figsize=(10, 5))
plt.plot(t_values, T_analytical, label='Analytical Solution', linestyle='dashed', color='black')
plt.plot(t_values, T_numerical, label='Euler’s Method', marker='o', markersize=4, linestyle='-', color='blue')
plt.xlabel('Time (t)')
plt.ylabel('Temperature (T)')
plt.legend()
plt.title("Newton's Law of Cooling: Analytical vs Numerical (Euler)")
plt.grid()
plt.show()

# Error analysis
plt.figure(figsize=(10, 5))
plt.plot(t_values, error, label='Error (|T_analytical - T_numerical|)', color='red')
plt.xlabel('Time (t)')
plt.ylabel('Error')
plt.legend()
plt.title("Error Analysis of Euler’s Method")
plt.grid()
plt.show()

# Step size sensitivity analysis
step_sizes = [1.0, 0.5, 0.1, 0.05, 0.01]
final_errors = []
for h in step_sizes:
    t_values, T_numerical = euler_method(T0, Ta, k, h, t_max)
    T_analytical = analytical_solution(T0, Ta, k, t_values)
    final_errors.append(np.max(compute_error(T_numerical, T_analytical)))

plt.figure(figsize=(10, 5))
plt.plot(step_sizes, final_errors, marker='o', linestyle='-', color='purple')
plt.xlabel('Step Size (h)')
plt.ylabel('Max Error')
plt.xscale('log')
plt.yscale('log')
plt.title("Step Size Sensitivity: Error vs Step Size")
plt.grid()
plt.show()

