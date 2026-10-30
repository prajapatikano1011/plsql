A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[9,8,7],[6,5,4],[3,2,1]]

rows=len(A)
cols=len(A[0])

c=[[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

for row in c:
    print(row)