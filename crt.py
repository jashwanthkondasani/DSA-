# from numpy import *
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
# def jash():
#   print("jashwanth kumar reddy")
#   jash()
# def add(a,b):
#     return a+b
# print(add(2,3))
# def evenOdd(x):
#     if x % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# evenOdd(4)
# def add(a,b):
#     print(a+b)
# add(2,7)

# def multiple(a,b):
#     return a*b
# print(multiple(33,77))
# def student(name,age,section):
#     print(name,age,section)
# student("jashwanth",21,"csm")
# def divide(a,b):
#     return a/b
# print(divide(100,10))
# def maximum(a,b,c):
#   if a>b and a>c:
#       return a
#   elif b>c:
#       return b
#   else:
#      return c
# print(maximum(119,32,875))
# def minimum(a,b,c):
#   if a<b and a<c:
#       return a
#   elif b<c:
#       return b
#   else:
#       return c
# print(minimum(19,32,8))
# def leap_year(n):
#     if (n%4==0 and n%100!=0) or (n%400==0):
#         return True
#     else:
#         return False
# print(leap_year(2026))
# def simpleIntrest(p,r,t):
#      return(p*r*t)/100
# print(simpleIntrest(1000,43,2))
# def perfectNum(n):
#    total=0
#    for i in range(1,n):
#       if n%i==0:
#          total+=i
#       return total ==n
# print(perfectNum(28))
# def jash(*args):
#     return args
# print(jash(1,2,3,4,5,6,7,8,9))

# def test(a,b):
#     return a+b
# t=test("s","v")
# print(t)
# def test(a,b):
#     return a+b
# t=test(3.3,76)
# print(t)
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact *=i
#     return fact
# print(factorial(5))
# def greet(n):
#     if n==0:
#       return n
#     print(" kondasani jashwanth kumar reddy ")
#     greet(n-1)
# greet(5)    

# def jash(n):
#   if n==0:
#      return n
#   print(n)
#   jash(n-1)
# jash(6)
# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# print(fibo(7))
# n=input()
# for i in range(n):
#   for j in range(i):
#     print("*",end=" ")
# a=" "
# if a:
#   print("something ")
# else:
#   print("none")
# a=[]
# if a:
#   print("something ")
# else:
#   print("none")
# a=2
# def jash():
#   global a
#   a=a+6
#   print(a)
# jash()
# def sq(n):
#   x=lambda n: n**2
#   return x(n)
# print(sq(5))
# add = lambda a,b: a+b
# print(add(3,7))
# x=lambda a: a%2==0
# print(x(4))
# print(x(5))
# n=[1,2,3,4,5,6]
# x=map(lambda n: n%2==0,n)
# print(list(x))
# n=input()
# m=input()
# for i in range(n):
#   for j in range(m):
#     print(f"{i} {j}",end=" ")
#   print()
# rows=7
# num=143
# for i in range(rows,0,-1):
#     for j in range(0,i):
#         print(num,end=" ")
#     print('')
# n=6
# for i in range(n):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
# n=6
# for i in range(1,n+1):
#     for j in range(i-1):
#         print(j,end=' ')
#     print()
# rows=5
# for i in range(rows+1,0,-1):
#   for j in range(0,i-1):
#       print("*",end=" ")
#   print()
# numbers=[1,2,3,4,5]
# for i in numbers:
#     square=i**2
# print("square:",i, "is", square)
# numbers=[1,2,3,4,5,6]
# size=len(numbers)
# for i in range(size):
#   print("index:", i, "value:", numbers[i])


# numbers=[11,23,34,55,66,77,85]
# for i in numbers:
#      if i >15:
#           break
#      else:
#           print(i)
# name="jashwanth kumar reddy"
# count=0
# for char in name:
#     if char=="a":
#         count+=1
# print("count of a in name is:", count)
# numbers=[1,2,34,55,6]
# for i in numbers:
#   pass
# age=18
# if age <18 and age==0:
#   print("not eligible to vote")
# else:
#   print("eligible to vote")

# marks=56
# if marks>=90:
#   print("a grade")
# elif marks>=80:
#   print("b grade")
# elif marks>=70:
#   print("c grade")
# elif marks>=60:
#   print(" d grade")
# else:
#   print("fail")

# num=[1,2,3,4,5]
# for i in num:
#    if i %2==0:
#     break
# print(i)
# num=[22,33,44,55,66]
# for i in num:
#   if i==33:
#     continue

#   print(i)
# num=[22,33,44,55,66]
# for i in num:
#   if i==33:
#     pass

#   print(i)
# for i in range(1,100):
#   if i %5==0:
#     pass
#   print(i)
# n=4
# i=0
# while i<n:
#   print("jai sri ram")
#   i+=1
# marks = 92

# if marks >= 90:
#     if marks >= 95:
#         print("S grade")
#     else:
#         print("A grade")
# else:
#     print("Just pass")

#  loops in python 
# for loop 
# for i in range(1,4):
#   print(i)
# for i in range(1,30):
#   if i%2==0:
#     print("even number:" , i)
#   else:
#     print("odd number:" , i)
# def multiplication_sum(num1,num2):
#     product=num1*num2
#     if product <=1000:
#        return product
#     else:
#        return num1+num2
# result=(multiplication_sum(20,830))  
# print("the product is:",result)
# result=(multiplication_sum(40,30))
# print("the sum of numbers is:",result)
# print("printing current and oprevious number sum for range in (10)")
# previous_num=0
# for i in range(10):
#     sum=previous_num+i
#     print(f"current number: {i} previous number: {previous_num} sum: {sum}")
#     previous_num=i
# global_var = 10

# def modify_global_var():
#     global global_var
#     global_var = 20
#     print("Inside function:", global_var)

# modify_global_var()
# print("Outside function:", global_var)
# m=int(input("Rows :-"))
# n=int(input("Colums:-"))
# for i in range(1,m+1):
#   if(i %2==0):
#     print(n* " -")
#   else:
#     print(n* " +")
# j="jashwanth kumar reddy "

# print(type(j))
# n=  iam from madanapalli i am studying at sri venkateswara college of engineeringg tirupatho
# print(j[9])
# n="kondasani jashwanth kumar reddy"
# print(n[0])
# print(len(n))
# for i in range(len(n)):
#     print(n[i])

#  string methods in python 
# n="jashwanth kumar reddy"
# print(n.upper())
# print(n.lower())
# print(n.strip())
# print(n.replace("jashwanth","kondasani"))
# print(n.replace("jashwanth","kondasani"))
# print(n.split())
# print(n.capitalize())
# print(n.center(50))
# print(n.count("a"))
# print(n.startswith("nani"))
# print(n.endswith("reddy"))
# print(n.find("kumar"))  
# print(n.index("jash"))
# print(n.swapcase())
# print(n.isalpha())
# print(n.isalnum())
# print(n.isprintable())
# print(ord('A'))
# print(chr(65))

# n=input("Enter a number to find its factorial: ")
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print("Factorial:",fact)
