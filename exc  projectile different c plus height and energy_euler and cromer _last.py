import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81     # gravity (m/s²)
m = 1.0      # mass (kg)
dt = 0.01
steps = 5000
theta = np.radians(45)
v0 = 50
v0x = v0 * np.cos(theta)
v0y = v0 * np.sin(theta)

# Drag coefficients to compare
c_values = [0.0, 0.1, 0.5]

for c in c_values:
    # Initialize state for both methods
    x_eul, y_eul, vx_eul, vy_eul = 0, 0, v0x, v0y
    x_crm, y_crm, vx_crm, vy_crm = 0, 0, v0x, v0y

    # Storage
    x_eul_list, y_eul_list, e_eul_list = [], [], []
    x_crm_list, y_crm_list, e_crm_list = [], [], []

    flight_time = 0
    max_h_eul, max_h_crm = 0, 0

    for step in range(steps):
        # Euler Method
        v_eul = np.array([vx_eul, vy_eul])
        speed_eul = np.linalg.norm(v_eul)
        air_res_eul = -c * speed_eul * v_eul / m

        ax_eul = air_res_eul[0]
        ay_eul = air_res_eul[1] - g

        x_eul += vx_eul * dt
        y_eul += vy_eul * dt
        vx_eul += ax_eul * dt
        vy_eul += ay_eul * dt

        if y_eul < 0:
            break

        x_eul_list.append(x_eul)
        y_eul_list.append(y_eul)
        KE_eul = 0.5 * m * (vx_eul**2 + vy_eul**2)
        PE_eul = m * g * y_eul
        e_eul_list.append(KE_eul + PE_eul)
        max_h_eul = max(max_h_eul, y_eul)

        # Euler-Cromer Method
        v_crm = np.array([vx_crm, vy_crm])
        speed_crm = np.linalg.norm(v_crm)
        air_res_crm = -c * speed_crm * v_crm / m

        ax_crm = air_res_crm[0]
        ay_crm = air_res_crm[1] - g

        vx_crm += ax_crm * dt
        vy_crm += ay_crm * dt
        x_crm += vx_crm * dt
        y_crm += vy_crm * dt

        if y_crm < 0:
            break

        x_crm_list.append(x_crm)
        y_crm_list.append(y_crm)
        KE_crm = 0.5 * m * (vx_crm**2 + vy_crm**2)
        PE_crm = m * g * y_crm
        e_crm_list.append(KE_crm + PE_crm)
        max_h_crm = max(max_h_crm, y_crm)

        flight_time += dt

    # Final metrics
    energy_loss_eul = e_eul_list[-1] - e_eul_list[0]
    energy_loss_crm = e_crm_list[-1] - e_crm_list[0]

    print(f"\n=== Air Resistance c = {c} ===")
    print(f"Euler      -> Range: {x_eul_list[-1]:.2f} m, Max Height: {max_h_eul:.2f} m, Time: {flight_time:.2f} s, Energy Lost: {energy_loss_eul:.2f} J")
    print(f"Euler-Cromer -> Range: {x_crm_list[-1]:.2f} m, Max Height: {max_h_crm:.2f} m, Time: {flight_time:.2f} s, Energy Lost: {energy_loss_crm:.2f} J")

    # Time array with correct length
    t_arr_eul = np.arange(0, len(e_eul_list)) * dt
    t_arr_crm = np.arange(0, len(e_crm_list)) * dt
    # ========== Plotting ==========
    plt.figure(figsize=(16, 4))

    # Trajectory
    plt.subplot(1, 3, 1)
    plt.plot(x_eul_list, y_eul_list, label="Euler")
    plt.plot(x_crm_list, y_crm_list, label="Euler-Cromer", linestyle='--')
    plt.title(f"Trajectory (c = {c})")
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.grid()
    plt.legend()

    # Total Energy
    plt.subplot(1, 3, 2)
    plt.plot(t_arr_eul, e_eul_list, label="Euler")
    plt.plot(t_arr_crm, e_crm_list, label="Euler-Cromer", linestyle='--')
    plt.title("Total Energy vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Energy (J)")
    plt.grid()
    plt.legend()

    # Height vs Time
    plt.subplot(1, 3, 3)
    plt.plot(t_arr_eul, y_eul_list, label="Euler")
    plt.plot(t_arr_crm, y_crm_list, label="Euler-Cromer", linestyle='--')
    plt.title("Height vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")
    plt.grid()
    plt.legend()


    plt.tight_layout()
    plt.show()
