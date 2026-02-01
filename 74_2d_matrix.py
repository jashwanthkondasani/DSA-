class solution(object):
   def searchMatrix(self,matrix,target):
      for row in matrix:
         for col in row:
            if target==col:
               return True
      return False