import numpy as np
import matplotlib.pyplot as plt

def projectile_motion(v0, theta, g=9.81, dt=0.01):
    theta_rad = np.radians(theta)
    t_flight = 2 * v0 * np.sin(theta_rad) / g  # Time of flight
    
    t_values = np.arange(0, t_flight, dt)  # Time steps
    x_values = v0 * t_values * np.cos(theta_rad)  # Horizontal positions
    y_values = v0 * t_values * np.sin(theta_rad) - 0.5 * g * t_values**2  # Vertical positions
    
    max_height = (v0**2 * np.sin(theta_rad)**2) / (2 * g)
    range_of_projectile = v0**2 * np.sin(2 * theta_rad) / g

    return t_values, x_values, y_values, max_height, range_of_projectile, t_flight

# Parameters
v0 = 50  # Initial velocity in m/s
theta = 45  # Launch angle in degrees
g = 98.81  # Gravitational acceleration in m/s²

# Simulate the projectile motion
t_values, x_values, y_values, max_height, range_of_projectile, t_flight = projectile_motion(v0, theta)

# Print key results
print(f"Time of flight: {t_flight:.2f} s")
print(f"Maximum height: {max_height:.2f} m")
print(f"Range: {range_of_projectile:.2f} m")

# Plotting the trajectory
plt.plot(x_values, y_values)
plt.title("Projectile Motion")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.grid(True)
plt.show()


