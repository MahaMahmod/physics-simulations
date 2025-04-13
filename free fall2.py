import numpy as np
import matplotlib.pyplot as plt

# Given parameters
y0 = 100  # Initial height (m)
v0 = 0    # Initial velocity (m/s)
a = -9.8  # Acceleration due to gravity (m/s^2)
t_max = 10
steps = 1000
dt = t_max / steps

# Arrays for storing results
t = np.zeros(steps+1)
y_euler = np.zeros(steps+1)
v_euler = np.zeros(steps+1)
y_cromer = np.zeros(steps+1)
v_cromer = np.zeros(steps+1)

# Initial conditions
t[0] = 0
y_euler[0] = y0
v_euler[0] = v0
y_cromer[0] = y0
v_cromer[0] = v0

# Euler and Euler-Cromer Methods with ground check
for n in range(steps):
    t[n+1] = t[n] + dt
    
    # Euler Method
    y_euler[n+1] = y_euler[n] + v_euler[n] * dt
    v_euler[n+1] = v_euler[n] + a * dt
    if y_euler[n+1] <= 0:
        break
    
    # Euler-Cromer Method
    v_cromer[n+1] = v_cromer[n] + a * dt
    y_cromer[n+1] = y_cromer[n] + v_cromer[n+1] * dt
    if y_cromer[n+1] <= 0:
        break

# Print table
print("Step\tTime (s)\tEuler y (m)\tEuler v (m/s)\tCromer y (m)\tCromer v (m/s)")
for i in range(n+1):
    print(f"{i}\t{t[i]:.4f}\t{y_euler[i]:.4f}\t{v_euler[i]:.4f}\t{y_cromer[i]:.4f}\t{v_cromer[i]:.4f}")

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(t[:n+1], y_euler[:n+1], label='Euler', linestyle='dashed')
plt.plot(t[:n+1], y_cromer[:n+1], label='Euler-Cromer')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.legend()
plt.title('Free Fall: Euler vs Euler-Cromer')
plt.grid()
plt.show()

