
# This program checks whether a number is a perfect number
# and prints all perfect numbers up to a given limit.


def is_perfect(number):
    if number <= 0:
        return False

    total = 0

    # Proper divisors are numbers that divide the number except the number itself.
    for divisor in range(1, number):
        if number % divisor == 0:
            total += divisor

    return total == number


num = int(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number.")
elif is_perfect(num):
    print(num, "is a perfect number.")
else:
    print(num, "is not a perfect number.")


limit = int(input("Enter the limit: "))

if limit <= 0:
    print("Please enter a positive limit.")
else:
    print("Perfect numbers up to", limit, ":")

    for number in range(1, limit + 1):
        if is_perfect(number):
            print(number, end=" ")