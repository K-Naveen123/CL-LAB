import numpy as np
import matplotlib.pyplot as plt

# Define parameters
duration = 10  # seconds
sampling_rate = 1000  # Hz
lx = duration * sampling_rate  # length of the window
time = np.linspace(0, duration, lx)  # time vector

# Define sinusoidal signals
frequency1 = 10  # Hz
sinusoidal1 = np.sin(2 * np.pi * frequency1 * time)

frequency2 = 15  # Hz
sinusoidal2 = np.sin(2 * np.pi * frequency2 * time)

# Combine sinusoidal signals
x = sinusoidal1 + sinusoidal2

# Compute y
y = 1 / lx * np.sum(x)

# Plot y
plt.plot(y)
plt.xlabel('Samples')
plt.ylabel('y')
plt.title('Plot of y')
plt.show()

