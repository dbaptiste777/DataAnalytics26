starting_bal = 5700
savings_goal = 12500
weekly_savings = 120

balance = starting_bal + weekly_savings


while balance < savings_goal: #compare bank balance to savings goal.
    balance = balance + weekly_savings
    print("This week my balance increased to", balance)

print("Goal met! My current balance is", balance)

print()

halfway = savings_goal * 0.5
seventy_five = savings_goal * 0.75

treat = 50

while balance < savings_goal:
    balance = balance + weekly_savings

    if balance >= seventy_five:
        balance = balance - treat
        print("So close! After treating myself, my balance is up to", balance)
    elif balance > halfway:
        print("Almost there! This week my balance is up to", balance)
    else:
        print("This week my balance increased to", balance)

print("Goal met! My current balance is", balance)

