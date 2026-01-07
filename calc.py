num1=int(input("Enter first number: "))
operator=input("Enter operator (+, -, *, /): ") 
num2=int(input("Enter second number: "))
if operator=='+':
   print("result:",num1+num2)
elif operator=='-':
   print("result:",num1-num2)
elif operator=='*':
   print("result:",num1*num2)
elif operator=='/':
   if num2!=0:
       print("result:",num1/num2)
   else:
       print("Error: Division by zero is not allowed.")
else:
   print("Error: Invalid operator.")
