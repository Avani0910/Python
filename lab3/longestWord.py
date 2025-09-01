# Program to find the longest word in a sentence

def find_longest_word(sentence):
    words = sentence.split()  # Split sentence into words
    longest_word = max(words, key=len)  # Find the word with maximum length
    return longest_word

# Example usage
sentence_input = input("Enter a sentence: ")
longest = find_longest_word(sentence_input)
print("The longest word is:", longest)
