
# This program prints three patterns using nested loops:
# a star triangle, a number triangle, and a centered pyramid.


n = int(input("Enter the number of rows: "))

if n <= 0:
    print("Please enter a positive number.")
else:

    print("\n1. Right-Angled Triangle")

    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()


    print("\n2. Number Pattern")

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


    print("\n3. Centered Pyramid")

    for i in range(1, n + 1):
        # Spaces center the stars to form a pyramid.
        for j in range(n - i):
            print(" ", end=" ")

        for j in range(2 * i - 1):
            print("*", end=" ")

        print()