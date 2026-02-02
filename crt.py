from numpy import *
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
# n=121213
# temp=0
# rev=0

# while n>0:
#   digit=n%10
#   rev=rev*10+digit
#   n//=10
# if temp==rev:
#    print("it is an palindrome ")
# else:
#     print("it is not an palindrome")

# x="jashwanth kumar reddy "
# print(x.split("-"))
# x='A-n-v--c-s-h'
# print(x.split("-"))
# x='Python Program'
# print(x.split())
# words=["python", "is", "easy"]
# result="  ".join(words)
# print(result)

# words=["jash" , "csm" ,"svce"]
# result="-".join(words)
# print(result)

# words=["jash" , "csm" ,"svce"]
# result="\n".join(words)
# print(result)
# x='A-n-v--c-s-h'
# print(x.split(  ))
# n=4
# for i in range(1,n+1):
#    for j in range(1,i+1):
#           print(j, end=' ')
#    print()

# for i in range(1,5):
#   x=" ".join(str(j) for j in range(1, i+1))
#   print(type(x))
#   print(x)
# matrix=[[1,2,3], [4,5,6]]
# transpose=[]
# for j in range(len(matrix[0])):
#   row=[]
#   for i in range(len(matrix)):
#      row.append(matrix[i][j])
#   transpose.append(row)
#   print(transpose)
# arr1=array([
#          [4,1,3,6,2,9]
#          [4,5,6,7,5,5]

# ])
# m=matrix(arr1)
# print(memoryview)
# rows, cols = (3, 5)
# arr = [[0]*cols]*rows
# print(arr)
