# Count the number of Digits

n = int(input("Enter the number"))
i = 0
while n>0:
    i = i + 1
    n = n // 10
print("Number of digits", i)

# Sum of Digits of a number
number = int(input("Enter the number to find sum of digits"))
sum = 0
while number > 0:
    r = number % 10
    sum = sum + r
    number = number // 10

print("sum is", sum)
