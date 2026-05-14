
a = 14
b = 27
c = 9

# Find smallest
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Find largest
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The smallest number is", smallest)
print("Largest number is", largest)
