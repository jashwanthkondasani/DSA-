class solution:
  def twoSum(self,nums:list[int],target:int)->list[int]:
    prevMap={}

    for i in enumerate(nums):
      diff=target-nums
      if diff in prevmap:
        return[prevMap[diff],i]
      prevMap[n]=i
    return []
