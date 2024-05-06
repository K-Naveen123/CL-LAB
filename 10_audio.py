import librosa
import matplotlib.pyplot as plt

# Load the audio file
audio_path = librosa.example('trumpet')
signal, sr = librosa.load(audio_path, sr=None)

# Create a time vector
t = librosa.times_like(signal, sr=sr)

# Plot the signal
plt.plot(t, signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal')
plt.show()

