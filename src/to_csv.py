import csv

with open('reviews.txt', 'r') as f:
    line_number = 1
    for line in f:
        line = line.strip()
        
        if line == 'Trip Verified':
            print(f"Line {line_number}: {line}")  # Print line number and the line content
        
        line_number += 1
