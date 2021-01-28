try:
    print("Enter a number")
    val1 = int(input())
    
    print("Now enter another number")
    val2 = int(input())

except ValueError:
    print('Needs to be a number')

else:
    for i in range(val1, val2 + 1):
        if i > 1:
            for num in range(2, i):
                if i % num == 0:
                    break
            else:
                print(i)

finally:
    print('Here are the prime numbers between ' + str(val1) + " & " + str(val2))