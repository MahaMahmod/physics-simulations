import numpy as np
import matplotlib.pyplot as plt

# Given parameters
T_env = 25  # Ambient temperature (°C)
T_init = 90  # Initial temperature (°C)
T_solid = 70  # Solidification temperature (°C)
m = 0.5  # Mass of wax (kg)
c_liquid = 2100  # J/kgK (Liquid heat capacity)
c_solid = 1800  # J/kgK (Solid heat capacity)
L = 200000  # J/kg (Latent heat of fusion)
h = 1.7  # W/K (Heat transfer coefficient)
A = 0.1  # Surface area (m^2)
dt = 10  # Time step (s)

# Function to simulate the cooling process
def cooling_process():
    T = T_init  # Start at 90°C
    t = 0  # Initial time
    latent_heat_removed = 0  # Track latent heat loss

    time_list = [t]
    temp_list = [T]

    while T > T_env:
        if T > T_solid:
            c = c_liquid  # Liquid phase
        elif T == T_solid and latent_heat_removed < m * L:
            # Phase change: Remove latent heat before cooling continues
            q_lost = h * A * (T - T_env) * dt  # Heat lost in this step
            latent_heat_removed += q_lost
            if latent_heat_removed >= m * L:
                T -= 0.01  # Allow transition to solid phase
            t += dt
            continue  # Skip temperature update
        else:
            c = c_solid  # Solid phase

        # Apply Newton's law of cooling
        dT = (-h * A * (T - T_env) / (m * c)) * dt
        T += dT
        t += dt

        # Store results
        time_list.append(t)
        temp_list.append(T)

    return time_list, temp_list

# Run the cooling simulation
time, temp = cooling_process()

# Plot the cooling curve
plt.figure(figsize=(8, 5))
plt.plot(time, temp, label="Cooling Curve", color="b")
plt.axhline(y=70, color="r", linestyle="--", label="Phase Change Temp (70°C)")
plt.axhline(y=25, color="g", linestyle="--", label="Ambient Temp (25°C)")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Cooling of Wax from 90°C to 25°C with Phase Change")
plt.legend()
plt.grid()
plt.show()

