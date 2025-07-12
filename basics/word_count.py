# Continuously prompt the user for input
while True:
    user_input = input("Please enter a phrase or sentence: ")

    # Split the input string into a list of words
    words_as_list = user_input.split()

    # Print the number of words entered
    print(f"Word count = {str(len(words_as_list))}")