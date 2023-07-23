import csv

with open('data/reviews.txt', 'r') as f:
    line_number = 1
    for line in f:
        line = line.strip()
        
        if line != 'Trip Verified':
            print(f"Line {line}")  # Print line number and the line content
        
        line_number += 1
    # make csv file
    with open('reviews.csv', 'a') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(line)

