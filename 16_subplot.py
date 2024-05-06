import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create subplots
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)  # (rows, columns, plot_number)
plt.plot(x, y1)
plt.title('Sin Wave')

plt.subplot(2, 1, 2)
plt.plot(x, y2)
plt.title('Cosine Wave')

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()

