# """Practice examples for Python `for` loops and the `range()` function.

# Notes:
#     - The examples below are kept as simple top-level programs for practice.
#     - Commented print statements can be enabled when you want to view that
#       particular output.
#     - Program logic and output text have intentionally been kept unchanged.
# """


# # ---------------------------------------------------------------------------
# # Range Function
# # ---------------------------------------------------------------------------

# a = range(5)
# # print(a)
# b = range(-2, -3)
# # print(b)


# # ---------------------------------------------------------------------------
# # Iterating Over a String
# # ---------------------------------------------------------------------------

# # Uncomment this block to print each character from the string one by one.
# # a = 'Ayush'

# # for char in a:
# #     print(char)


# # ---------------------------------------------------------------------------
# # Sum of First n Natural Numbers
# # ---------------------------------------------------------------------------

# n = int(input('Enter the number'))
# sum = 0

# for i in range(1, n + 1):
#     sum = sum + i
# # print('Sum is:', sum)


# # ---------------------------------------------------------------------------
# # Factorial of a Number
# # ---------------------------------------------------------------------------

# number = int(input('Enter a number to find the factorial'))
# fact = 1

# for i in range(1, number + 1):
#     fact = fact * i
# # print(f'Factorial of {number}:', fact)


# # ---------------------------------------------------------------------------
# # Fibonacci Series
# # ---------------------------------------------------------------------------

# numFibo = int(input('Fibonacci Series of:'))
# a = 0
# b = 1

# if numFibo <= 0:
#     print('Invalid Input')

# elif numFibo == 1:
#     print(a)

# else:
#     print(a, end=' ')
#     print(b, end=' ')

#     for i in range(2, numFibo):
#         c = a + b
#         print(c, end=' ')
#         a = b
#         b = c

# print()

# # ---------------------------------------------------------------------------
# # Prime Number Check
# # ---------------------------------------------------------------------------

# numPrime = int(input('Enter number to check Prime:'))

# if numPrime % 2 == 0:
#     print("Prime")
# else:
#     print("Not Prime")

# # ---------------------------------------------------------------------------
# # Factorial
# # ---------------------------------------------------------------------------
# numFact = int(input('Enter number to know factorial'))
# for num in range(1, numFact+1):
#     if numFact % num == 0:
#         print(num, end= ' ')
# print()


for n in range(2, 101):
    divisor_count = 0
    if n == 2:
        print(n)
        continue
    if n % 2 == 0:
        continue

    for divisor in range(3, int(n ** 0.5) + 1, 2):
        if n % divisor == 0:
            divisor_count += 1
            break
    else:
        print(n)
    
