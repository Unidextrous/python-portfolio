# Prompt the user for various words to fill in the blanks of the story
animal_singular = input("Animal: ")
animal_plural = input("Same Animal (Plural): ")
name = input("Name: ")
verb = input("Verb: ")
noun = input("Noun: ")
food = input("Food: ")

# Print out the completed story using an f-string with the user’s inputs
print(f"Today, I took my {animal_singular}, {name}, for a walk.\n"
    f"{name} is a smart {animal_singular}. I taught them to sit, shake, and even {verb}!\n"
    f"{name} loves their toy {noun}, playing with other {animal_plural}, and especially {food}!\n"
    f"I am very glad that {name} is in my life.")