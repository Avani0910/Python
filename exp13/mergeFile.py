with open(r"C:\Users\Avni Kavathiya\Downloads\ict.txt", 'w') as merged_file:
    
    with open(r"C:\Users\Avni Kavathiya\Downloads\ict.txt", 'r') as file1:
        for line in file1:
            merged_file.write(line)
    
    with open(r"C:\Users\Avni Kavathiya\Downloads\ict.txt", 'r') as file2:
        for line in file2:
            merged_file.write(line)

print("Files merged successfully into 'merged.txt'.")
