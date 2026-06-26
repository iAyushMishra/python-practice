# Python program to read 5 integers from the user using a while loop and 
# find the largest number among them. 
# Print the maximum number at the end.

n = 5
print(f"Enter {n} numbers")
max = int(input("Enter number 1:"))
min = max
i = 1

while n>i:
    x = int(input(f'Enter number {i + 1}:'))
    if max < x:
        max = x
    if min > x:
        min = x
    i += 1

print('Max element is:', max)
print('Min element is:', min)

# Also below

numbers = [12, 45, 7, 89, 23]  # You can change these values for testing

n = len(numbers)


i = 0
# Start with the smallest possible value. So the first input automatically becomes the maximum.
Max = float('-inf')
# Start with the largest possible value. So the first input automatically becomes the minimum.
Min = float('inf')

while n > i:
    x = numbers[i]
    if x > Max:
        Max = x
    if x < Min:
        Min = x
    i += 1


print(f'Max Element from {numbers}:', Max)
print(f'Min Element from {numbers}:', Min)



