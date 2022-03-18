# User's interface is here
from calc import Bill, Flatmate, PdfReport

def shut_msg():
    print('Wrong input. Shutting down.')

# Get all input from user
try:
    user_amount = float(input("Enter bill's amount: "))
except:
    shut_msg()
    quit()

user_period = input("Enter bill's period (e.g. December 2021): ")

fl1_name = input("Enter 1st flatmater's name: ")
fl2_name = input("Enter 2nd flatmate's name: ")

try:
    fl1_days = float(input(f'Enter how many days {fl1_name} stayed in the flat: '))
except:
    shut_msg()
    quit()

try:
    fl2_days = float(input(f'Enter how many days {fl2_name} stayed in the flat: '))
except:
    shut_msg()
    quit()


bill = Bill(amount=user_amount, period=user_period)
fl1 = Flatmate(name=fl1_name, days_in_house=fl1_days)
fl2 = Flatmate(name=fl2_name, days_in_house=fl2_days)

# Printing out results in a console
print(f'{fl1_name} pays:', fl1.pays(bill, fl2))
print(f'{fl2_name} pays:', fl2.pays(bill, fl1))

# Generate a pdf file
pdf1 = PdfReport('bill.pdf')
pdf1.generate(bill, fl1, fl2)