
Python Lab 2

1. Armstrong Number

Aim

To check whether a number is an Armstrong number and print all Armstrong numbers within a given range.

Logic

The program calculates the sum of each digit raised to the power of the number of digits. A number is Armstrong if this sum is equal to the original number. A loop is used to check all numbers in the given range.

Sample Input / Output

Input:

153
100
1000

Output:

153 is an Armstrong number.
Armstrong numbers in the range:
153 370 371 407

⸻

2. Prime Number

Aim

To check whether a number is prime and print all prime numbers up to a given limit.

Logic

A prime number has only two factors: 1 and itself. The program checks divisors only up to the square root of the number because a larger factor would have a corresponding smaller factor already checked.

Sample Input / Output

Input:

17
20

Output:

17 is a prime number.
Prime numbers up to 20:
2 3 5 7 11 13 17 19

⸻

3. Perfect Number

Aim

To check whether a number is perfect and print all perfect numbers up to a given limit.

Logic

The program finds all proper divisors of a number and adds them. If their sum equals the original number, the number is perfect. The same process is repeated for all numbers up to the given limit.

Sample Input / Output

Input:

28
1000

Output:

28 is a perfect number.
Perfect numbers up to 1000:
6 28 496

⸻

4. Palindrome

Aim

To check whether a number and a string are palindromes.

Logic

For the number version, the digits are reversed using division and remainder operations without converting the number into a string. For the string version, the entered text is compared with its reversed form.

Sample Input / Output

Input:

121
madam

Output:

121 is a palindrome.
The string is a palindrome.

⸻

5. Fibonacci Series

Aim

To print the Fibonacci series using a loop and recursion and compare the recursive function calls.

Logic

The loop version generates each term by repeatedly updating two variables. The recursive version calculates each term by calling itself for the previous two terms, and a counter is used to count the function calls.

Sample Input / Output

Input:

10

Output:

Fibonacci using loop:
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

⸻

6. Pattern Printing

Aim

To print a star triangle, number pattern, and centered pyramid using nested loops.

Logic

Nested loops are used to control the rows and columns of each pattern. The number of spaces and stars is changed for each row to create the centered pyramid.

Sample Input / Output

Input:

5

Output:

1. Right-Angled Triangle
* 
* * 
* * * 
* * * * 
* * * * *
2. Number Pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
3. Centered Pyramid
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

⸻

7. Menu-Driven Application

Aim

To combine the programs into a single menu-driven application.

Logic

The program displays a menu containing the different operations. The user’s choice determines which function is executed, and the menu continues until the user chooses Exit. Invalid choices are handled without crashing.

Sample Input / Output

Input:

2
17
8

Output:

It is a prime number.
Exiting the application.

⸻

8. Number Guessing Game

Aim

To create a number guessing game where the user has a maximum of seven attempts.

Logic

The computer randomly selects a number between 1 and 100. After each guess, the program tells the user whether the guess is too high or too low and stops when the correct number is guessed or seven attempts are used.

Sample Input / Output

Example:

I have selected a number between 1 and 100.
You have 7 attempts to guess it.
Enter your guess: 50
Too low.
Enter your guess: 75
Too high.

⸻

Analysis

1. For Loop vs While Loop

I preferred the for loop when the number of repetitions was known, such as Fibonacci series, pattern printing, and checking numbers in a range. I preferred the while loop when repetition depended on a condition, such as prime checking and the palindrome number logic.

2. Fibonacci Loop vs Recursive Version

The recursive version repeats more work as n grows because the same Fibonacci values are calculated multiple times. The loop version calculates each term only once, so it is more efficient.

3. Prime Number Check

The largest divisor that needs to be tested is the square root of the number. If a number has a factor larger than its square root, it must also have a corresponding factor smaller than the square root, which would already have been checked.

4. Number Guessing Game

The best strategy is binary search. The user should choose the middle of the remaining range each time, which eliminates about half of the possible numbers after every guess.