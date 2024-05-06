% Load the audio file
[audio, fs] = audioread('trumpet');

% Create a time vector
t = (0:length(audio)-1) / fs;

% Plot the signal
plot(t, audio)
xlabel('Time (s)')
ylabel('Amplitude')
title('Audio Signal')

