# This file contains all the classes which are needed for this app

# Represents a bill which flatmates need to pay for
class Bill:

    # Create an instance with 2 parameters: amount of money to pay and period of time to pay for
    def __init__(self, amount, period):

        self.amount = amount
        self.period = period

# Represents each flatmate who needs to pay for a bill
class Flatmate:

    # Create an instance with 2 parameters: name of flatmate and days they spent in the house
    def __init__(self, name, days_in_house):

        self.name = name
        self.days_in_house = days_in_house

# Represents a pdf report file which would be generated with how much each flatmate needs to pay
class PdfReport:

    def __init__(self, filename):

        self.filename = filename

    def generate(self, bill, flatmate1, flatmate2):

        return