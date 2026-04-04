# class solution():
#   def MoveZeroes(self,nums):
#     l=0
#     for r in range(len(nums)):
#         if nums[r]!=0:
#             nums[l],nums[r]=nums[r],nums[l]
#             l+=1
# n=[1,0,1,1,0,1]
# s=solution()
# s.MoveZeroes(n) 
# print(n)
class solution():
  def MoveZeroes(self,nums):
    l=0
    for r in range(len(nums)):
        if nums[r]!=0:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
n=[1,0,1,1,0,1]
s=solution()
s.MoveZeroes(n) 
print(n)