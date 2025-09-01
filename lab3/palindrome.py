# Program to check if a string is a palindrome

# Taking input from the user
text = input("Enter a string: ")

# Remove spaces and convert to lowercase for accurate checking
cleaned_text = text.replace(" ", "").lower()

# Check if string is same forwards and backwards
if cleaned_text == cleaned_text[::-1]:
    print("Yes! The string is a palindrome.")
else:
    print("No! The string is not a palindrome.")
