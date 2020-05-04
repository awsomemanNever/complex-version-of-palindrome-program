import math

x = 0
y = -1
z = 0
booleanValue = False
halfLength = 0

string = input("enter the string for palindrome check: ")

if len(string) % 2 == 0:
    halfLength = len(string) / 2
    for i in range(len(halfLength)):
        if string[x] == string[y]:
            z += 1
        else:
            booleanValue = True
        x += 1
        y -= 1

if len(string) % 2 != 0:
    halfLength = len(string) / 2
    for i in range(len(halfLength)):
        if string[x] == string[y]:
            z += 1
        else:
            booleanValue = True
        x += 1
        y -= 1

if z == halfLength:
    print("it is a palindrome")

else:
    print("It is not a palindrome")
