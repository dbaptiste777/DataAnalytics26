x = 100
y = 20

print(x / y == 5) # Answer


if x / y == 5: # Section A
    print(x/y is 5)
    x = 1
else:
    print("Are the variables set up correctly?")
print()

if x * y == y: #Section B
    print("Now x times y is y")
    x = 10
else:
    print("Whoops, x equals", + "the value of x")


print()

if x < y == y: #Section C
    print("x is less than y")
    x = x*2
else:
    print("uh oh, x is not less than y")

    print()


if x > y == y: #Section D
    print("how is x greater than y??")
else:
    print("x is NOT greater than y")

print("The value of x is 20 and the final value of y is 20")