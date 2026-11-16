
# This program checks whether a number and a string are palindromes.
# The number palindrome check uses arithmetic operations only.


def is_number_palindrome(number):
    if number < 0:
        return False

    original = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return original == reversed_number


def is_string_palindrome(text):
    text = text.lower()
    return text == text[::-1]


# Number palindrome
num = int(input("Enter a number: "))

if is_number_palindrome(num):
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")


# String palindrome
text = input("Enter a string: ")

if is_string_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")