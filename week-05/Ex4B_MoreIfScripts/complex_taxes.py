pay_rate = 34  
hours_worked1 = 40

if hours_worked1 > 40:
    overtime_hours = hours_worked1 - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = pay_rate * hours_worked1
print(gross_pay)  #1360 gross pay weekly

print()
 

pay_rate = 34  
hours_worked = 2080

if hours_worked > 2080:
    overtime_hours = hours_worked - 40
    gross_pay2 = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay2 = pay_rate * hours_worked
print(gross_pay2)  #gross pay annually is $70720

print()

annual_gross_pay = 70720

print()

filing = "single"

income_range1 = .05
income_range2 = .1
income_range3 = .15
income_range4 = .2

joint_range1 = 0.5
joint_range2 = .1
joint_range3 = .15
joint_range4 = .2

if income_range3 == .15:  #tax rate for weekly gross pay is 204.0 for single filers. You can change the tax rate and change the income range for single or joint.
    tax_rate = gross_pay * income_range3
else:
    gross_pay = pay_rate * hours_worked
print(tax_rate)


print(f"You worked", (hours_worked1), "hours this period")
print(f"Because you earn",(pay_rate), "per hour, your gross weekly pay is", (gross_pay))
print(f"Your filing status is", ("single"))
print(f"Your tax withholdig for the week is" , (tax_rate))
print (f"Your net pay is", (gross_pay - tax_rate))