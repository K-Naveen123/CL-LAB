import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the differential equation function
def model(y, t):
    dydt = -y + 1  # Example: dy/dt = -y + 1
    return dydt

# Initial condition
y0 = 0

# Time points
t = np.linspace(0, 5, 100)

# Solve the differential equation
y = odeint(model, y0, t)

# Plot the solution
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.title('Solution of the Differential Equation')
plt.grid(True)
plt.show()

