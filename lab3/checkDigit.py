# Program to check if a string contains only digits

def check_only_digits(s):
    if s.isdigit():
        print("The string contains only digits.")
    else:
        print("The string does not contain only digits.")

# Example usage
string_input = input("Enter a string: ")
check_only_digits(string_input)
