import csv

# Writing to a CSV file
data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

