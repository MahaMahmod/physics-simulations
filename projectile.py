import numpy as np
import matplotlib.pyplot as plt

# Given parameters
x0, y0 = 0, 0   # Initial position (m)
vx0, vy0 = 10, 20  # Initial velocity components (m/s)
ax, ay = 0, -9.8   # Acceleration (m/s^2)
t_max = 10
steps = 1000
dt = t_max / steps

# Arrays for storing results
t = np.zeros(steps+1)
x_euler = np.zeros(steps+1)
y_euler = np.zeros(steps+1)
vx_euler = np.zeros(steps+1)
vy_euler = np.zeros(steps+1)

x_cromer = np.zeros(steps+1)
y_cromer = np.zeros(steps+1)
vx_cromer = np.zeros(steps+1)
vy_cromer = np.zeros(steps+1)

# Initial conditions
t[0] = 0
x_euler[0], y_euler[0] = x0, y0
vx_euler[0], vy_euler[0] = vx0, vy0
x_cromer[0], y_cromer[0] = x0, y0
vx_cromer[0], vy_cromer[0] = vx0, vy0

max_height = 0
range_projectile = 0
time_of_flight = 0

# Euler and Euler-Cromer Methods with ground check
for n in range(steps):
    t[n+1] = t[n] + dt
    
    # Euler Method
    x_euler[n+1] = x_euler[n] + vx_euler[n] * dt
    y_euler[n+1] = y_euler[n] + vy_euler[n] * dt
    vx_euler[n+1] = vx_euler[n] + ax * dt
    vy_euler[n+1] = vy_euler[n] + ay * dt
    max_height = max(max_height, y_euler[n+1])
    if y_euler[n+1] <= 0:
        range_projectile = x_euler[n+1]
        time_of_flight = t[n+1]
        break
    
    # Euler-Cromer Method
    vx_cromer[n+1] = vx_cromer[n] + ax * dt
    vy_cromer[n+1] = vy_cromer[n] + ay * dt
    x_cromer[n+1] = x_cromer[n] + vx_cromer[n+1] * dt
    y_cromer[n+1] = y_cromer[n] + vy_cromer[n+1] * dt
    if y_cromer[n+1] <= 0:
        break

# Print max height, range, and time of flight
print(f"Maximum Height: {max_height:.4f} m")
print(f"Range: {range_projectile:.4f} m")
print(f"Time of Flight: {time_of_flight:.4f} s")

# Print table
print("Step\tTime (s)\tEuler x (m)\tEuler y (m)\tEuler vx (m/s)\tEuler vy (m/s)\tCromer x (m)\tCromer y (m)\tCromer vx (m/s)\tCromer vy (m/s)")
for i in range(n+1):
    print(f"{i}\t{t[i]:.4f}\t{x_euler[i]:.4f}\t{y_euler[i]:.4f}\t{vx_euler[i]:.4f}\t{vy_euler[i]:.4f}\t{x_cromer[i]:.4f}\t{y_cromer[i]:.4f}\t{vx_cromer[i]:.4f}\t{vy_cromer[i]:.4f}")

# Plot results
plt.figure(figsize=(10, 5))
plt.plot(x_euler[:n+1], y_euler[:n+1], label='Euler', linestyle='dashed')
plt.plot(x_cromer[:n+1], y_cromer[:n+1], label='Euler-Cromer')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.legend()
plt.title('Projectile Motion: Euler vs Euler-Cromer')
plt.grid()
plt.show()

