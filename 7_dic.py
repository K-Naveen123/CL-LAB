import numpy as np
import matplotlib.pyplot as plt

# Define dictionaries of frequencies and amplitudes
frequencies = {'A': 1, 'B': 2, 'C': 3}  # in Hz
amplitudes = {'A': 1, 'B': 0.5, 'C': 0.2}

# Define the common parameters
duration = 1  # in seconds
sampling_rate = 1000  # in samples per second

# Generate the time vector
t = np.linspace(0, duration, duration * sampling_rate, endpoint=False)

# Initialize the sum wave
sum_wave = np.zeros_like(t)

# Generate and add the sine waves
for key, freq in frequencies.items():
    amplitude = amplitudes[key]
    sin_wave = amplitude * np.sin(2 * np.pi * freq * t)
    sum_wave += sin_wave

# Plot the sum wave
plt.plot(t, sum_wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sum of Sine Waves')
plt.grid(True)
plt.show()

