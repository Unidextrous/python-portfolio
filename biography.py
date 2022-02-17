import datetime
import sys

name = input("Please enter your first and last name: ")
name_as_list = name.split()
while True:
    if any(chr.isdigit() for chr in name) == True:
        name = input("Please enter your name in letter form: ")
        name_as_list = name.split()
    elif len(name_as_list) > 2:
        name = input("Please enter your first and last name only: ")
        name_as_list = name.split()
    elif len(name_as_list) < 2:
        name = input("Please enter both your first and last name: ")
        name_as_list = name.split()
    else:
        break
dob = input("Please enter your birthdate in the form mm/dd/yyyy: ") #although the prompt suggests slashes, the program will accept input without them
while True:
    try:
        dobDateTime = datetime.datetime.strptime(dob, "%m/%d/%Y")
        break
    except ValueError:
        try:
            dobDateTime = datetime.datetime.strptime(dob, "%m%d%Y")
            break
        except ValueError:
            pass
        dob = input("Please enter a valid birthdate: ")
address = input("Please enter your address (example: 123 Main Street, Pittsburgh, PA 12345) ")
address_as_list = address.split()
while True:
    if address_as_list[0].isdigit() == True and address_as_list[-1].isdigit() == True and len(address_as_list[-1]) == 5 and address_as_list[-2].isdigit() == False and len(address_as_list[-2]) == 2:
        break
    else:
        address = input("Please enter a valid address: ")
        address_as_list = address.split()
goals = input("What are your personal goals? ")
print(f"Name: {name} \nBirthdate: {dob[0:2]}/{dob[2:4]}/{dob[4:8]} \nAddress: {address} \nGoals: {goals}")