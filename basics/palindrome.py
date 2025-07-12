# Prompt the user to enter a word
word = input("Please type a word: ")

# Check if the word is the same forward and backward
if word == word[::-1]:
    print("This word is a palindrome!")
else:
    print("This word is not a palindrome.")