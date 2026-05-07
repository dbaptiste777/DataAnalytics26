#3 Restaurant bill

bill = 219 #cost before tex
tax = 11.87 #tax amount
gratuity = .15 #automatic gratuity percent.
bill_total = 230.87
grat_total = 34.63


print( bill + tax )

print(f"{230.87 * gratuity:.2f}")

print(bill_total + grat_total)

print(f"The tip on a {bill} restaurant bill is {grat_total}")

