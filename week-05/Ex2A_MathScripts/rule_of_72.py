current_sav = 7200
int_rate = 8

formula = 72 / int_rate

print(72/int_rate)


print(f"Your current savings is {current_sav:.2f}. At a {int_rate}% interest rate, your savings account will be worth {current_sav*2:.2f} in {formula} years.")

print()

bank_bal = input("What is your current bank balance? ")
print("Your balance is " + bank_bal)