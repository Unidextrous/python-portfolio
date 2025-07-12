import datetime     # Used to validate and parse date of birth input

# Ask the user for their full name
name = input("Please enter your first and last name: ")
name_as_list = name.split()

# Keep asking until the name is valid (only letters, and exactly 2 words)
while True:
    if any(chr.isdigit() for chr in name) == True:  # Check if there are any numbers in the name
        name = input("Please enter your name in letter form: ")
    elif len(name_as_list) > 2:     # More than first and last name entered
        name = input("Please enter your first and last name only: ")
    elif len(name_as_list) < 2:     # Only one name entered
        name = input("Please enter both your first and last name: ")
    else:
        break
    name_as_list = name.split()     # Re-split the name after re-entry

# Ask the user for their birthdate
dob = input("Please enter your birthdate in the form mm/dd/yyyy: ") # The program will also accept mmddyyyy, mm/dd/yy, and mmddyy

# Try to convert the input into a valid date
while True:
    try:
        dobDateTime = datetime.datetime.strptime(dob, "%m/%d/%Y")   # Try standard format with slashes
        break
    except ValueError:
        try:
            dobDateTime = datetime.datetime.strptime(dob, "%m%d%Y") # Allow numeric input without slashes
            break
        except ValueError:
            dob = input("Please enter a valid birthdate: ") # Ask again if both formats fail

# Ask for the user's address
address = input("Please enter your address (example: 123 Main Street, Pittsburgh, PA 12345) ")
address_as_list = address.split()

# Validate the address format: starts with a number and ends in a valid ZIP code
while True:
    if (
        address_as_list[0].isdigit() == True and    # Street number
        address_as_list[-1].isdigit() == True and len(address_as_list[-1]) == 5 and # ZIP code
        address_as_list[-2].isdigit() == False and len(address_as_list[-2]) == 2):  # State abbreviation
        break
    else:
        address = input("Please enter a valid address: ")
        address_as_list = address.split()

# Ask for personal goals
goals = input("What are your personal goals? ")

# Display the collected and validated information
print(f"Name: {name}")
if "/" in dob:
    print(f"Birthdate: {dob}")
else:
    print(f"Birthdate: {dob[:2]}/{dob[2:4]}/{dob[4:]}")
print(f"Address: {address}")
print(f"Goals: {goals}")