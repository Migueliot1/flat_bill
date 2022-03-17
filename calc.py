# This file contains all the classes which are needed for this app

class Bill:
    '''Represents a bill object which flatmates need to pay for.
    Contains such data as amount and period of payment'''

    def __init__(self, amount, period):
        '''Create an instance with 2 parameters:
        amount of money to pay and period of time (days) to pay for'''
        self.amount = amount
        self.period = period


class Flatmate:
    '''Represents each individual flatmate
    who needs to pay for a bill'''

    def __init__(self, name, days_in_house):
        '''Create an instance with 2 parameters:
        name of flatmate and days they spent in the house'''

        self.name = name
        self.days_in_house = days_in_house


class PdfReport:
    '''Represents a pdf report file which would be generated 
    with how much each flatmate needs to pay from a bill'''

    def __init__(self, filename):
        '''Create an instance with a filename as a parameter'''

        self.filename = filename

    def generate(self, bill, flatmate1, flatmate2):
        '''Generate a pdf file from given data from bill
        and flatmates'''

        pass
