try:
    total_bill = float(input("What is the total bill? "))
except ValueError:
    while True:
        try:
            total_bill = float(input("Please enter a numerical value: "))
            break
        except ValueError:
            pass
try:
    tip = float(input("What percent would you like to tip? "))
except ValueError:
    while True:
        try:
            tip = float(input("Please enter a numerical value: "))
            break
        except ValueError:
            pass
total_bill_plus_tip = total_bill + (total_bill * tip / 100)
print(total_bill_plus_tip)