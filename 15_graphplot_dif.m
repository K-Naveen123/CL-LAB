% Define the differential equation function
function dydt = model(t, y)
    dydt = -y + 1;  % Example: dy/dt = -y + 1
end

% Initial condition
y0 = 0;

% Time points
t = linspace(0, 5, 100);

% Solve the differential equation
y = ode45(@model, t, y0);

% Plot the solution
plot(t, y)
xlabel('Time')
ylabel('y(t)')
title('Solution of the Differential Equation')
grid on

