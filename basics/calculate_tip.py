# Prompt the user for the total bill amount
try:
    total_bill = float(input("What is the total bill? "))
except ValueError:
    # If input is not a number, keep prompting until valid
    while True:
        try:
            total_bill = float(input("Please enter a numerical value: "))
            break
        except ValueError:
            pass

# Prompt the user for the tip percentage
try:
    tip = float(input("What percent would you like to tip? "))
except ValueError:
    # If input is not a number, keep prompting until valid
    while True:
        try:
            tip = float(input("Please enter a numerical value: "))
            break
        except ValueError:
            pass

# Calculate the total amount including tip
total_bill_plus_tip = total_bill + (total_bill * tip / 100)

# Display the final amount to the user
print(total_bill_plus_tip)