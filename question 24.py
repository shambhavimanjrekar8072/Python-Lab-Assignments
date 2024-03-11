rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix1 = []
matrix2 = []
print("Enter the elements of matrix 1: ")
for i in range(0,rows):
    a = []
    for j in range(0,columns):
        e = int(input())
        a.append(e)
    matrix1.append(a)

print("Enter the elements of matrix 2: ")
for i in range(0,rows):
    a = []
    for j in range(0,columns):
        e = int(input())
        a.append(e)
    matrix2.append(a)

sum_matrices = []
for i in range(0,rows):
    b = []
    for j in range(0,columns):
        s = matrix1[i][j] + matrix2[i][j]
        b.append(s)
    sum_matrices.append(b)

print("The sum of 2 matrices is: ")
for i in range(0,rows):
    for j in range(0, columns):
        print(sum_matrices[i][j], end=" ")
    print("\r")