# User's interface is here
from calc import Bill, Flatmate, PdfReport

# DEBUG
bill = Bill(120, 'March 2022')
batman = Flatmate('Batman', 20)
thanos = Flatmate('Thanos', 25)

pdf1 = PdfReport('bill.pdf')
pdf1.generate(bill, batman, thanos)
