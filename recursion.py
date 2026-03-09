# def fact(n):
#   if n==0:
#     return 1
#   return n*fact(n-1)
# print(fact(3))

# def fib(n):
#   if n==0:
#     return 0
#   if n==1:
#     return 1
#   return fib(n-1)+fib(n-2)
# n=5
# for i in range(0,n):
#   print(fib(i))
# names = ["Alice", "Bob", "Charlie"] 
# def len_list(lst):
#   print(len(lst))
# len_list(names)
# def len_list(lst):
#   for names in lst:
#     print(names,end=" ")
# n=5
# fact=1
# for i in range(1,n+1):
#   fact*=i 
# print(fact)
# def fact(n):
#   if n==0:
#     return 1
#   return n*fact(n-1)
# print(fact(3)
def converter(usd_value):
  inr_value=usd_value*82.74
  print(f"{usd_value} USD is equal to {inr_value} INR")
converter(100)
# print(converter(100)  )