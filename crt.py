# n=4
# for i in range(1,n+1):
#   for j in range(i):
#          print('*', end='')
#   print()
# n=4
# for i in range(n,0,-1):
#   for j in range(i):
#          print('*', end='')
#   print()

# n=8
# for i in range(1,n+1):
#   for j in range(1,i+1):
#          print(j, end='')
#   print()

#  same number in each row 
# n=5
# for i in range(1,n+1):
#    for j in range(1,i+1):
#           print(i, end='')
#    print()

# pyramid pattern

# n=5
# for i in range(1,n+1):
#   print( " " *(n-i), end=' ' )
#   for j in range(i):
#     print('*', end=' ')
#   print()

# n=5
# for i in range(n):
#    for j in range(n):
#       if i==0 or i==n-1 or j==0 or j==n-1:
#          print('*', end=' ')  
#       else:
#          print(' ', end=' ')
#    print() 

# n = 5

# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n-1 or j == 0 or j == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()   

# n = 5

# for i in range(n):
#     for j in range(i+1):
#         if  i == n-1 or j == 0 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# n = 5

# for i in range(n):
#     for j in range(i + 1):
#         if j == 0 or j == i or i == n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# n = 4

# # upper half
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("* " * i)

# # lower half
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
#     print("* " * i)

#  reverse of a number 

# n=1500
# rev=0
 
# while n>0:
#   digit=n%10
#   rev=rev*10+digit
#   n//=10
# print(rev)

#  palindrome of a number 
n=121213
temp=0
rev=0

while n>0:
  digit=n%10
  rev=rev*10+digit
  n//=10
if temp==rev:
   print("it is an palindrome ")
else:
    print("it is not an palindrome")

