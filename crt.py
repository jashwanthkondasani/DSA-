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
# arr=[1,2,3,4,5]
# left=0
# right=len(arr)-1
# while left<right:
#     arr[left],arr[right]=arr[right],arr[left]
#     left+=1
#     right-=1
# print("Reversed array:",arr)  
# arr=[1,2,3,4,5]
# # n=len(arr)
# for i in range(0,n-1):
#      print(i)year=int(input("Enter a year to check if it is a leap year: ")
         

#  27/02/2026
# year=int(input("enter the year:-"))
# if(year%4==0 and year%100!=0) or(year%400==0):
#   print("it is a leap year")
# else:
#   print("not an leap year")

# a=int(input("enter the  side of s triangle:-"))
# b=int(input("enter the side of the triangle:-"))
# c=int(input("enter the side of the triangle:-"))
# if(a+b>c and a+c>b and b+c>a):
#   print("it is a valid triangle")
# if(a==b==c):
#   print("it is an equliatoral triangle")
# else:
#   print("it is an scalar triangle")
# Units consumed:
# 	•	0–100 → ₹5 per unit
# 	•	101–200 → ₹7 per unit
# 	•	Above 200 → ₹10 per unit

# Additionally:
# 	•	If total bill > ₹2000 → add 10% surcharge

# Print final bill.
# bill=int(input("enter the total bill amount:-"))
# if bill<100:
#   print("the bill is:",bill*5)
# elif bill<200:
#   print("the bill is:",bill*7)
# else:
#   print("the bill is:",bill*10)
# if bill>2000:
#   print("the final bill is:",bill*1.1)


#  largest and smalest of 4
# a=int(input("enter the first number:-"))
# b=int(input(" enter the second number:-"))
# c=int(input(" enter the third number:-"))
# d=int(input(" enter the fourth number:-"))
# largest=a
# smallest=a
# if b>largest:
#   largest=b
# if c>largest:
#   largest=c
# if d>largest:
#   largest=d
# if b<smallest:
#   smallest=b
# if c<smallest:
#   smallest=c
# if d<smallest:
#   smallest=d
# print("largest number is:",largest)
# print("smallest number is:",smallest)

# age = int(input("Enter age: "))
# is_weekend = input("Is it weekend? (yes/no): ").lower()
# is_student = input("Are you a student? (yes/no): ").lower()

# Base price
# if age < 5:
#     price = 0
# elif age <= 18:
#     price = 100
# elif age <= 60:
#     price = 200
# else:
#     price = 150

# # Weekend charge
# if is_weekend == "yes":
#     price += 50

# # Student discount
# if is_student == "yes":
#     price -= price * 0.10

# print("Final Ticket Price:", price)

# Input:
# 	•	Age
# 	•	Salary
# 	•	Credit Score (300–900)
# 	•	Existing Loan? (yes/no)

# Rules:
# 	1.	Age must be between 21 and 60
# 	2.	Salary ≥ 25,000
# 	3.	Credit Score:
# 	•	≥ 750 → Excellent
# 	•	650–749 → Good
# 	•	600–649 → Average
# 	•	< 600 → Poor

# Loan Decision:
# 	•	Excellent → Approved
# 	•	Good → Approved only if no existing loan
# 	•	Average → Approved only if salary ≥ 50,000 AND no existing loan
# 	•	Poor → Rejected

age=int(input("Enter age: "))
salary=int(input("Enter salary: "))
credit_score=int(input("Enter credit score (300-900): "))
existing_loan=input("Do you have an existing loan? (yes/no): ").lower()
if age < 21 or age > 60:
    print("Loan Rejected: Age criteria not met.")

elif salary < 25000:
    print("Loan Rejected: Salary criteria not met.")
elif credit_score < 300 or credit_score > 900:
    print("Loan Rejected: Credit score must be between 300 and 900.")
elif existing_loan == "yes":
    print("Loan Rejected: Existing loan found.")
else:
    print("Loan Approved.")
    if credit_score >= 750:
        print("Credit Score: Excellent")
    elif credit_score >= 650:
        print("Credit Score: Good")
    elif credit_score >= 600:
        print("Credit Score: Average")
    else:
        print("Credit Score: Poor")