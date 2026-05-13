dept_code = 5

if dept_code == 1:
    print("Marketing")
elif dept_code == 5:
    print("Human Resources")
elif dept_code == 10:
    print("Accounting")
elif dept_code == 12:
    print("Legal")
elif dept_code == 18:
    print("IT")
elif dept_code == 20:
    print("Customer Relations")
else:
    print("Invalid department code") #Each dept code runs however, if you try running a dept code thats not listed it will return an error


dept_code = 10


match dept_code: 
    case 1:
        print("Marketing")
    case 5:
        print("Human Resources")
    case 10:
        print("Accounting")
    case 12:
        print("Legal")
    case 18:
        print("IT")
    case 20:
        print("Customer Relations")
    case _:
        print("Invalid department code") #Code runs smoothly

