class solution(object):
     def moveZeros(self, nums):
          n=len(nums)
          non_zeros=[num for num in nums if num!=0]
          zeros=n-len(non_zeros)
          result=non_zeros+[0]*zeros
          for i in range(n):
               nums[i]=result[i]
          return nums 
     