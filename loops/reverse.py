# Reverse Number
n = int(input("Enter a number to reverse"))
original = n
reverseNumber = 0
while n > 0:
    r = n % 10
    reverseNumber = reverseNumber * 10 + r
    n=n//10

print("rev number is", reverseNumber)

# Palindrome
def isPalindrome(num):
    return reverseNumber == num

print("Palindrome", isPalindrome(original))