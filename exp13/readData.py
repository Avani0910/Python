import csv

# Open the CSV file in read mode
with open(r"C:\Users\Avni Kavathiya\Downloads\ict.txt", 'r') as file:
    reader = csv.reader(file)
    
    # Loop through each row and print it
    for row in reader:
        print(row)
