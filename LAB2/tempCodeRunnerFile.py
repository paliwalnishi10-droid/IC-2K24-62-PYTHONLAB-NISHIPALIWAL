



def is_armstrong(number):
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == number


# Check a single number
num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a non-negative number.")
else:
    if is_armstrong(num):
        print(num, "is an Armstrong number.")
    else:
        print(num, "is not an Armstrong number.")


# Print Armstrong numbers in a range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

if start < 0 or end < 0 or start > end:
    print("Invalid range. Enter non-negative numbers with start <= end.")
else:
    print("Armstrong numbers in the range:")

    for number in range(start, end + 1):
        if is_armstrong(number):
            print(number, end=" ")