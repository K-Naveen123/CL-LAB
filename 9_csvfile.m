% Writing to a CSV file
data = [
    "Name", "Age", "City";
    "John", 30, "New York";
    "Alice", 25, "Los Angeles";
    "Bob", 35, "Chicago"
];

csvwrite('data.csv', data);

