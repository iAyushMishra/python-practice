# Python program to read 5 integers from the user using a while loop and 
# find the largest number among them. 
# Print the maximum number at the end.

# n = 5
# print(f'Enter {n} value')
# max = int(input('Enter number 1:'))
# i = 1

# while n > i:
#     x = int(input(f'Enter number {i + 1}:'))
#     if max < x:
#         max = x
#     i += 1

# print('Enter max element:', max)
n = 5
print(f"Enter {n} numbers")
max = int(input("Enter number 1:"))
i = 1

while n>i:
    x = int(input(f'Enter number {i + 1}:'))
    if max < x:
        max = x
    i += 1

print('Max element is:', max)


