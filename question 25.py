mat1= [[1,2,3],[4,5,6]]
mat2 = [[-1,6,7],[8,12,10]]
if len(mat1)!=len(mat2):
    print("Matrix multiplication is not possible!")
else:
    a = len(mat1)
    b = len(mat2[0])
    c = len(mat2)
    ans = []
    for i in range(a):
        temp = []
        for j in range(b):
            t = 0
            for k in range(c):
                t += mat1[i][k]*mat2[k][j]
            temp.append(t)
        ans.append(temp)
    print(ans)