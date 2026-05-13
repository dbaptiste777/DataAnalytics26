pay_rate = 34  
hours_worked = 40

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    gross_pay = (40 * pay_rate) + (overtime_hours * pay_rate * 1.5)
else:
    gross_pay = pay_rate * hours_worked
print(gross_pay)  #1360 gross pay

print()

pay_rate2 = 17.30
hours_worked2 = 45
overtime_hours = 5


if hours_worked2 > 40:
    overtime_hours = hours_worked2 - 40
    gross_pay = (40 * pay_rate2) + (overtime_hours * pay_rate2 * 1.5)
else:
    gross_pay = pay_rate2 * hours_worked2
print(gross_pay)  #821.75 gross pay


