import librosa
import matplotlib.pyplot as plt
import numpy as np

# Load the audio file
audio_path = librosa.example('trumpet')
signal, sr = librosa.load(audio_path, sr=None)

# Reverse the signal
reversed_signal = np.flipud(signal)

# Create a time vector
t = librosa.times_like(signal, sr=sr)

# Plot the original and reversed signals
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(t, reversed_signal)
plt.title('Reversed Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

