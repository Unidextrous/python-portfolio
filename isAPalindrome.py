word = input("Please type a word: ")
if word == word[::-1]:
    print("This word is a palindrome!")
else:
    print("This word is not a palindrome.")