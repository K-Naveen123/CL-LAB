% Generate some data
x = linspace(0, 10, 100);
y1 = sin(x);
y2 = cos(x);

% Create subplots
figure;

subplot(2, 1, 1)  % (rows, columns, plot_number)
plot(x, y1)
title('Sin Wave')

subplot(2, 1, 2)
plot(x, y2)
title('Cosine Wave')

