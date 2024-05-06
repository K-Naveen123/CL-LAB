% Read the image file
image = imread('example_image.jpg');

% Get RGB values
[rows, cols, ~] = size(image);
rgb_values = reshape(image, [], 3);

% Write RGB values to a CSV file
csvwrite('rgb_values.csv', rgb_values);

