% Define dictionaries of frequencies and amplitudes
frequencies = containers.Map({'A', 'B', 'C'}, {1, 2, 3});  % in Hz
amplitudes = containers.Map({'A', 'B', 'C'}, {1, 0.5, 0.2});

% Define the common parameters
duration = 1;  % in seconds
sampling_rate = 1000;  % in samples per second

% Generate the time vector
t = 0:1/sampling_rate:duration-1/sampling_rate;

% Initialize the sum wave
sum_wave = zeros(size(t));

% Generate and add the sine waves
keys = frequencies.keys;
for i = 1:length(keys)
    key = keys{i};
    freq = frequencies(key);
    amplitude = amplitudes(key);
    sin_wave = amplitude * sin(2 * pi * freq * t);
    sum_wave = sum_wave + sin_wave;
end

% Plot the sum wave
plot(t, sum_wave);
xlabel('Time (s)');
ylabel('Amplitude');
title('Sum of Sine Waves');
grid on;

