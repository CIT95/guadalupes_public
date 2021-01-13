print("Enter a number")
val1 = int(input())

print("Now enter another number")
val2 = int(input())

for i in range(val1, val2 + 1):     # here I setup the code
    if i > 1:                       # this sets the loop to start if the first number is geater than 1
        for num in range(2, i):     # this for loop sets up the iteration to start from 2 up through the range of the first for loop
            if i % num == 0:        # this if statement tests if the division has a remainder equal to 0. if it does then the code stops and starts the loop again.
                break
        else:                       # when the loop no longer is true for any iteration with a division of equal 0 it will print the intergers.
            print(i)

# I needed to look this up. Just by the videos alone I couldn't figure this out.
# I got the code from here https://www.javatpoint.com/pyhton-print-all-prime-number-in-an-interval