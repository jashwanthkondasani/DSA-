# arr=[1, 2, 3, 4, 5]
# for i in arr:
#   print(i)

# arr=[10,20,30,40,50]
# print("sum:",sum(arr))
# print("max:",max(arr))
# print("min:",min(arr))

# arr=[50,60,70,80,90]
# arr.reverse()
# print(arr)

# arr=[4,5,40,50]
# even=odd=0
# for i in arr:
#   if i%2==0:
#     even +=1
#   else:
#     odd +=1
# print("even :" ,even ,"odd :",odd)

# arr=[1,2,3,4,5,6,7,8,1,9]
# seen=set()
# for i in arr:
#   if i in seen:
#     print("duplicate:",i)
#   seen.add(i)

#  largest element in arraay
# def largest_element(arr):
#    largest=arr[0]
#    for i in range(1,len(arr)):
#       if arr[i]>largest:
#           largest=arr[i]
#    return largest
# arr=[2,5,67,88,77]
# print("largest element is:",largest_element(arr))

# arr=[33,54,43,65,99]
# print("second largest element is:",second_largest_element(arr))


# second largest element in array 
# arr=[12,34,67,97,64]
# largest=-1
# second_largest=-1
# for i in range(len(arr)):
#     if arr[i]>largest:
#         second_largest=largest
#         largest=arr[i]
#     elif arr[i]<largest and arr[i]>second_largest:
#         second_largest=arr[i]
# print("second largest element is:",second_largest)

# arr=[12,34,67,97,64]
# largest=-1
# third_largest=-1
# for i in range(len(arr)):
#     if arr[i]>largest:
#         third_largest=largest
#         largest=arr[i]
#     elif arr[i]<largest and arr[i]>third_largest:
#         third_largest=arr[i]
# print("third largest element is:",third_largest)


# arr=[0,1,0,3,12,887,0]
# index=0

# for num in arr:
#     if num !=0:
#         arr[index]=num
#         index +=1
#     for i in range(index,len(arr)):
#         arr[i]=0
# print(arr)

# arr=[1,2,3,4,5]
# freq={}

# for i in arr:
#     freq[i]=freq.get(i,0)+1
# print(freq)

def is_sorted(arr):
  return arr==sorted(arr)
print(is_sorted([1,2,3,4,5]))
print(is_sorted([5,4,3,2,1]))





