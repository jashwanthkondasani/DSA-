class solution():
  def MaxConsOnes(self,nums):
    maxi=0
    count=0
    for i in range(len(nums)):
       if nums[i]==1:
           count+=1
           maxi=max(maxi,count)
       else:
           count=0
    return maxi
n=[1,1,0,1,1,1]
s=solution()
print(s.MaxConsOnes(n))

print("hello world")
 
 