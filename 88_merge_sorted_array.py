
class solution(object):
  def merge(self,nums1,m,nums2,n):
    i,j= m-1, n-1
    while j>=0:
      if i>=0 and nums1[i]>nums2[j]:
        nums1[i+j+1]=nums1[i]
        i -= 1
      else:
        nums1[i+j+1]=nums2[j]
        j -= 1
    while j>=0:
      nums1[j]=nums2[j]
      j -= 1
      k-=1