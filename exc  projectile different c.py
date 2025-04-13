import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81     # gravity (m/s²)
m = 1.0      # mass (kg)
dt = 0.01
steps = 5000
angles = np.radians(45)
v0 = 50

# Initial velocity components
v0x = v0 * np.cos(angles)
v0y = v0 * np.sin(angles)

# Drag coefficients to test
c_values = [0.0, 0.1, 0.5]

for c in c_values:
    x, y = 0.0, 0.0
    vx, vy = v0x, v0y

    x_list, y_list = [], []
    vx_list, vy_list = [], []
    energy_list = []
    flight_time = 0
    max_height = 0
    energy_lost = 0

    for i in range(steps):
        v = np.array([vx, vy])
        speed = np.linalg.norm(v)
        air_resist = -c * speed * v / m
        
        ax = air_resist[0]
        ay = air_resist[1] - g

        # Euler-Cromer update
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

        # Stop if projectile hits the ground
        if y < 0:
            break

        # Store data
        x_list.append(x)
        y_list.append(y)
        vx_list.append(vx)
        vy_list.append(vy)

        KE = 0.5 * m * (vx**2 + vy**2)
        PE = m * g * y
        energy = KE + PE
        energy_list.append(energy)

        flight_time += dt
        max_height = max(max_height, y)

    energy_lost = energy_list[-1] - energy_list[0]
    print(f"\nAir resistance c = {c}")
    print(f"Time of flight: {flight_time:.2f} s")
    print(f"Range: {x_list[-1]:.2f} m")
    print(f"Max height: {max_height:.2f} m")
    print(f"Energy lost: {energy_lost:.2f} J")

    time_array = np.arange(0, flight_time, dt)[:len(energy_list)]

    # Plot y vs x
    plt.figure(figsize=(15, 4))

    plt.subplot(1, 3, 1)
    plt.plot(x_list, y_list, label=f"c = {c}")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.title("Trajectory")
    plt.grid()
    plt.legend()

    # Plot total energy
    plt.subplot(1, 3, 2)
    plt.plot(time_array, energy_list, label=f"c = {c}")
    plt.xlabel("Time (s)")
    plt.ylabel("Energy (J)")
    plt.title("Total Energy vs Time")
    plt.grid()
    plt.legend()

    # Plot height vs time
    plt.subplot(1, 3, 3)
    plt.plot(time_array, y_list, label=f"c = {c}")
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")
    plt.title("Height vs Time")
    plt.grid()
    plt.legend()

    plt.tight_layout()
    plt.show()

