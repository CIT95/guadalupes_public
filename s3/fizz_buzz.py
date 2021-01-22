num1 = int(input("Pick a number "))
def pickNumber(num1):
    if num1 % 3 == 0 and num1 % 5 == 0:
        return 'FizzBuzz'
    elif num1 % 3 == 0:
        return 'Fizz'
    elif num1 % 5 == 0:
        return 'Buzz'
    else:
        return num1

myNumber = pickNumber(num1)
print(myNumber)