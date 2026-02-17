import time
print("Please insert your card")
time.sleep(2)
password=1234
pin=int(input("Please enter your pin: "))
balance=10000
if(pin==password):
  print("""
        1) Check Balance
        2) Withdraw
        3) Deposit
        4) Exit
  """)
  try:
      option=int(input("Please select an option: "))
  except:
      print("Invalid input. Please enter a number.")
  if(option==1):
      print("Your balance is:", balance)
      print("-------------------------")
 

  if(option==2):
     amount=int(input("Enter the amount to withdraw: "))
     if(amount<=balance):
        balance-=amount
        print(f"\n amount withdrawl is{amount}")
        print(f"Your new balance is: {balance}")
     else:
        print("Insufficient funds")

elif(option==3):
    amount=int(input("Enter the amount to deposit: "))
    balance+=amount
    print(f"Your new balance is: {balance}")
elif(option==4):
    print("Thank you for using the ATM.")
else:
  print("Invalid PIN")