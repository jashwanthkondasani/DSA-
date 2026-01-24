# class Solution:
#     def findSum(self, A, N): 
#         # If only one element
#         if N == 1:
#             return A[0] + A[0]

#         # Initialize min and max
#         if A[0] > A[1]:
#             maxi = A[0]
#             mini = A[1]
#         else:
#             maxi = A[1]
#             mini = A[0]

#         # Traverse remaining elements
#         for i in range(2, N):
#             if A[i] > maxi:
#                 maxi = A[i]
#             elif A[i] < mini:
#                 mini = A[i]

#         return maxi + mini

print("Find the sum of minimum and maximum number in an array")
       
      
