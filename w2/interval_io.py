""" print("Enter a number")
val1 = input()

print('Enter another number')
val2 = input()

if val1 > val2:
    print("First number is greater than the second")
else:
    for num in range(int(val1), int(val2)): #need to change value to interger from user input because it is a string
        print(num) """

print("Enter a number")
val1 = int(input())

print("Now enter another number")
val2 = int(input())

if val1 > val2:
    print(str(val1) + ' is larger than ' + str(val2))

else:
    for num in range(val1, val2 + 1): #added + 1 to show the full range from the 1st number to the 2nd
        print('Here is the range ' + str(num))
