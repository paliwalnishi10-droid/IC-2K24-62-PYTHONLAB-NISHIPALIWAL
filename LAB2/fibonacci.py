
# This program prints Fibonacci series using a loop and recursion.
# It also counts the function calls made by the recursive version.


def fibonacci_loop(n):
    series = []

    a = 0
    b = 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


recursive_calls = 0


def fibonacci_recursive(n):
    global recursive_calls
    recursive_calls += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_recursive_series(n):
    series = []

    for i in range(n):
        series.append(fibonacci_recursive(i))

    return series


n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci using loop:")
    print(fibonacci_loop(n))

    recursive_calls = 0

    print("Fibonacci using recursion:")
    print(fibonacci_recursive_series(n))

    print("Number of recursive function calls:", recursive_calls)