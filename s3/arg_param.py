""" def myFunction(name, altName="Unknown"):
    print("hello " + name + " And Hello " + altName)

myFunction('Lupe', "Mike") """


def letsAdd(num1, num2=15):
    num3 = num1 * num2
    if num3 < 100:
        return num3
    else:
        return "That\'s a big number"

answer = letsAdd(15)
""" answer = letsAdd(4) """
print(answer)
""" print(answer + 3) """ #forgot to comment this out to test the else statement