from PIL import Image
import csv

# Open the image file
image = Image.open('example_image.jpg')

# Get RGB values
rgb_values = list(image.getdata())

# Write RGB values to a CSV file
with open('rgb_values.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Red', 'Green', 'Blue'])
    for rgb in rgb_values:
        csvwriter.writerow(rgb)

