# User's interface is here
from calc import Bill, Flatmate, PdfReport

# Get all input from user
amount = float(input("Enter bill's amount: "))
period = input("Enter bill's period: ")

fl1_name = input("Enter 1st flatmater's name: ")
fl2_name = input("Enter 2nd flatmate's name: ")

fl1_days = float(input("Enter how many days 1st flatmate stayed in the flat: "))
fl2_days = float(input("Enter how many days 2nd flatmate stayed in the flat: "))

bill = Bill(amount=amount, period=period)
fl1 = Flatmate(name=fl1_name, days_in_house=fl1_days)
fl2 = Flatmate(name=fl2_name, days_in_house=fl2_days)

pdf1 = PdfReport('bill.pdf')
pdf1.generate(bill, fl1, fl2)
