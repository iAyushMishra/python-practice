
# Pattern 1: Square Pattern

# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *


# for i in range(1, 6):
#     for j in range(1, 6):
#         print('*', end=' ')
#     print()
    

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# for i in range(1, 6):
#     for j in range(i):
#         print('*', end=' ')
#     print()

# for i in range(1, 6):
#     print('* ' * i)


#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# n = 5
# for i in range(1, n + 1):
#     print(' ' * (n - i), end='')
#     print('* ' * i)


# * * * * * 
# * * * *  
# * * *   
# * *    
# *  

# n = 5
# for i in range(0, n):
#     print('* ' * (n-i), end='')
#     print(' ' * (i))

n = 5
for i in range(0, n+1):
    print('* ' * (n-i), end=' ')
    print()
