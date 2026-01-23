
arr=[1,2,3,2,4,1,5]
unique_arr=[]

for x in arr:
   if x not in unique_arr:
      unique_arr.append(x)

print("Array without duplicates:", unique_arr)