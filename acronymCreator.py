expanded_form = input("Enter some words and I'll turn them into an acronym! ")
words = expanded_form.split()
acronym = ""

for word in words:
    if word[0] == "w":
        if word == "without" or word == "Without": #for some reason, "if word.lower() == "without":" didn't work here.
            acronym += "WO"
        else:
            acronym+= "W"
    else:
        acronym += word[0].upper()
print(acronym)