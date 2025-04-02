import numpy as np
import matplotlib.pyplot as plt

def ebbinghaus_forgetting_curve(time, a=100, b=1):
    """
    Calculate retention based on Ebbinghaus's forgetting curve using a power function.
    
    Args:
    - time (float or np.ndarray): Time in days since learning.
    - a (float): Constant determining the initial retention (default is 100).
    - b (float): Exponent determining the rate of forgetting (default is 1).
    
    Returns:
    - retention (float or np.ndarray): Retention percentage at the given time.
    """
    # Ensure time is a positive value
    time = np.maximum(time, 1e-6)  # Avoid division by zero
    retention = a * np.power(time, -b)
    return retention

# Example: Plotting the forgetting curve for the first 30 days
time_points = np.linspace(1, 30, 100)  # Time from 1 day to 30 days
retention_values = ebbinghaus_forgetting_curve(time_points, a=100, b=1)

# Plotting
plt.plot(time_points, retention_values, label="Ebbinghaus Forgetting Curve")
plt.title("Ebbinghaus Forgetting Curve")
plt.xlabel("Time (days)")
plt.ylabel("Retention (%)")
plt.grid(True)
plt.legend()
plt.show()
