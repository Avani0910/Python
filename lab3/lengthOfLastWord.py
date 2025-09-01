# e. Write a Python program to find the length of the last word in a sentence. 

# Program to find the length of the last word in a sentence

def length_of_last_word(sentence):
    words = sentence.strip().split()  # Remove leading/trailing spaces and split into words
    if not words:
        return 0  # If sentence is empty or only spaces
    return len(words[-1])  # Get the last word and return its length

# Example usage
sentence_input = input("Enter a sentence: ")
length = length_of_last_word(sentence_input)
print("The length of the last word is:", length)
