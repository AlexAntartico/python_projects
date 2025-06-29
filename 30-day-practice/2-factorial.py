def factorial(number):
    if number == 1 or number == 0:
        return 1
    elif number < 0:
        print("Number can only be a positive integer")
        exit(1)
    else:
        return number * factorial(number - 1)


number = int(input("Write the number to calculate factorial and press enter\n"))
result = factorial(number)
print(f"The factorial of {number} is {result}")
