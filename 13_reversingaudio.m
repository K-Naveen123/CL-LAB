% Load the audio file
[audio, fs] = audioread('trumpet');

% Reverse the signal
reversed_audio = flipud(audio);

% Create a time vector
t = (0:length(audio)-1) / fs;

% Plot the original and reversed signals
subplot(2, 1, 1)
plot(t, audio)
title('Original Signal')
xlabel('Time (s)')
ylabel('Amplitude')

subplot(2, 1, 2)
plot(t, reversed_audio)
title('Reversed Signal')
xlabel('Time (s)')
ylabel('Amplitude')

