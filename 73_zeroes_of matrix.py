class solution(object):
  def setZeroes(self,matrix):
    m=len(matrix)
    n=len(matrix[0])
    rows=set()
    cols=set()
    for i in range(m):
      for j in range(m):
        if matrix[i][j]==0:
          rows.add(i)
          cols.add(j)
    for r in rows:
      for i in range(n):
        matrix[i][j]=0
    for c in cols:
      for j in range(m):
        matrix[i][j]=0