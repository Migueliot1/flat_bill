# This file contains all the classes which are needed for this app
from fpdf import FPDF

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

    def pays(self, bill, other_flatmate):
        '''Calculate how much this flatmate
        needs to pay for his share'''

        # Calculate weight of payment by finding coefficient
        weight = self.days_in_house/ (self.days_in_house + other_flatmate.days_in_house)
        return bill.amount * weight 


class PdfReport:
    '''Represents a pdf report file which would be generated 
    with how much each flatmate needs to pay from a bill'''

    def __init__(self, filename):
        '''Create an instance with a filename as a parameter'''

        self.filename = filename

    def generate(self, bill, flatmate1, flatmate2):
        '''Generate a pdf file from given data from bill
        and flatmates'''

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Calculate how much each flatmate needs to pay
        # and make these values ready to be inserted in pdf
        fl1_pay = flatmate1.pays(bill, flatmate2)
        fl1_pay = str(round(fl1_pay, 2))
        fl2_pay = flatmate2.pays(bill, flatmate1)
        fl2_pay = str(round(fl2_pay, 2))

        # Add a title
        pdf.set_font(family='Arial', size=28, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=0, align='C', ln=1)

        # Add Period label and its value
        pdf.set_font(family='Arial', size = 18, style='BI')
        pdf.cell(w=150, h=40, txt='Period', border=0, align='C')
        pdf.cell(w=0, h=40, txt=bill.period, border=0, align='C', ln=1)

        # Add flatmates' names and how much they need to pay
        pdf.set_font(family='Arial', size = 14, style='I')
        pdf.cell(w=150, h=25, txt=flatmate1.name, border=0, align='C')
        pdf.cell(w=0, h=25, txt=fl1_pay, border=0, align='C', ln=1)

        pdf.cell(w=150, h=25, txt=flatmate2.name, border=0, align='C')
        pdf.cell(w=0, h=25, txt=fl2_pay, border=0, align='C', ln=1)

        print('New PDF file', self.filename, 'was succesfully generated :)')
        pdf.output(self.filename)



# DEBUG
bill = Bill(120, 'March 2022')
batman = Flatmate('Batman', 20)
thanos = Flatmate('Thanos', 25)

pdf1 = PdfReport('bill.pdf')
pdf1.generate(bill, batman, thanos)