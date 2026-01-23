task=[]
while True:
   print(" 1.add 2.view 3.remove 4.exit")
   ch=int(input("choose:"))
   
   if ch==1:
      task.append(input("task: "))

   elif ch==2:
      print(task)

   elif ch==3:
      task.pop(int(input("index")))

   else:
      break   

