# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 " # this is a string
b = '55' #this is a string
c = "402 Stevens" #this is a string
d = 'Number 5 ' #this is a string


print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

#print(int(a)) #error because a float cant be converted to an integer
print(str(b)) #works by converting a string to a int
#print(int(c)) #error because 402 stevens is a string with stevens in the name and python cant transform that value into an integer.
#print(int(d)) #ValueError: invalid literal for int() with base 10: 'Number 5 '

#print(int(a)) #ValueError: invalid literal for int() with base 10: ' 101.1 '
print(int(b)) #works
#print(int(c)) #ValueError: invalid literal for int() with base 10: '402 Stevens'
#print(int(d)) #ValueError: invalid literal for int() with base 10: 'Number 5 '

print()

print(float(a)) #works
print(float(b)) #works
#print(float(c)) #ValueError: could not convert string to float: '402 Stevens'
#print(float(d)) #ValueError: could not convert string to float: 'Number 5 '

int(float(a)) #works

print(a.strip()) #works
print(d.strip()) #works

