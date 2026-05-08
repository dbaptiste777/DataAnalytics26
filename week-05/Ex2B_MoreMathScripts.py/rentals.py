import math
import cmath


tourists = 42
van_cost = 250
driver_pay = 95
available_seats = 15
daily_cost = 1035 



#There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost $250 per day to rent (including the driver’s pay). How many vans do you need?

print(f"{math.ceil(tourists / available_seats)}") # We will need at leat 3 vans for 42 people.

#How much will it cost to rent vans?

print(f"{(van_cost + driver_pay) * 3}") #It will cost 1035 a day to rent 3 vans.

print(f"{daily_cost / tourists:.2f}") #It will cost 24.64/person.

tourists = 38
van_cost = 250
driver_pay = 95
available_seats = 15
daily_cost = 1035.12


#Test your script with 38 tourists. Now do some separate calculations to check your
#work:

print(f"{daily_cost / tourists:.2f}")  #The script said to charge 27.24/person

print(f"{tourists * 27.24}") #b) If you multiply that out you get 1035.12

print(f"{daily_cost * 3:.2f}") #c) The vans were 3105.36 for 3 vans with 38 people. 


# In this case I dont have left over money
