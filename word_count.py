while True:
    user_input = input("Please enter a phrase or sentence: ")
    words_as_list = user_input.split()
    print(f"Word count = {str(len(words_as_list))}")