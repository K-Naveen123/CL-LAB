x = [1, 2, 3, 4, 5]; % example array
k_values = [0, 1, 2, 3]; % example k values

for k = k_values
    result = sum(x .* cos(2 * pi * (0:length(x)-1) * k));
    fprintf("For k = %d, sum = %f\n", k, result);
end

