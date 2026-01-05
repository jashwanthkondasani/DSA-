limit=int(input("Enter the limit: "))
a,b=0,1
print("Fibonacci Series:")
while a<=limit:
   print(a,end=" ")
   a,b=b,a+b