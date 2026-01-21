def brute(arr):
  for i in range(len(arr)-1):
     if(arr[i]>arr[i+1]):
       return False
  return True

arr=[11,12,13,14,15,16,17,18]
print("sorted ':",brute(arr))