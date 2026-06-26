# Range Function
a = range(5)
# print(a)
b = range(-2,-3)
# print(b)

#  for loop

a = 'Ayush'

for char in a:
    print(char)

# Sum of first n natural numbers

n = int(input('Enter the number'))
sum = 0 

for i in range(1, n+1):
    sum = sum + i
print('Sum is:', sum)

# Factorial of a number

number = int(input('Enter a number to find the factorial'))
fact = 1

for i in range(1, n+1):
    fact = fact*i
print(f'Factorial of {number}:', fact) 