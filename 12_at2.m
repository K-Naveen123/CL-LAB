% Define parameters
duration = 10; % seconds
sampling_rate = 1000; % Hz
lx = duration * sampling_rate; % length of the window
time = linspace(0, duration, lx); % time vector

% Define sinusoidal signals
frequency1 = 10; % Hz
sinusoidal1 = sin(2 * pi * frequency1 * time);

frequency2 = 15; % Hz
sinusoidal2 = sin(2 * pi * frequency2 * time);

% Combine sinusoidal signals
x = sinusoidal1 + sinusoidal2;

% Compute y
y = (1 / lx) * sum(x);

% Plot y
plot(y);
xlabel('Samples');
ylabel('y');
title('Plot of y');

