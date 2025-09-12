# Initialize an empty list to store lines
lines_list = []

# Open the file and read line by line
with open(r"C:\Users\Avni Kavathiya\Downloads\ict.txt", 'r') as file:
    for line in file:
        lines_list.append(line.strip())  # Remove newline characters

# Print the list after reading the file
print(lines_list)
