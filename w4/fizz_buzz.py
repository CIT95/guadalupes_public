try:
    num1 = int(input("Pick a number "))
    
except ValueError:
    print('did not enter a number')

else:
    def pickNumber(num1):
        if num1 < 0:
            return 'Number needs to be positive'
        elif num1 % 3 == 0 and num1 % 5 == 0:
            return 'FizzBuzz'
        elif num1 % 3 == 0:
            return 'Fizz'
        elif num1 % 5 == 0:
            return 'Buzz'
        # elif num1 < 0:
        #     return 'Number needs to be positive'
        else:
            return num1
    myNumber = pickNumber(num1)
    print(myNumber)

finally:
    print('All done...')