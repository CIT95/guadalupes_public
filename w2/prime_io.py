print("Enter a number")
val1 = int(input())

print("Now enter another number")
val2 = int(input())

for i in range(val1, val2 + 1):     # here I setup the range by using the 2 numbers received from the user
    if i > 1:                       # this sets the loop to start with a variable greater than 1
        for num in range(2, i):     # this for loop checks all integers within the specified range
            if i % num == 0:        # and the if statement tests if the division has a remainder equal to 0. If it does not then the break is executed. If there is a remainder then the number is not a prime and the loop stops.
                break
        else:                       # when the loop no longer is true for any iteration with a division of equal 0 it will print the intergers.
            print(i)

# I needed to look this up. Just by the videos alone I couldn't figure this out.
# I got the code from here https://www.javatpoint.com/pyhton-print-all-prime-number-in-an-interval