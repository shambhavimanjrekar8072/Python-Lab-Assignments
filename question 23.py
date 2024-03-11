rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []
for i in range(0,rows):
    a = []
    for j in range(0,columns):
        e = int(input())
        a.append(e)
    matrix.append(a)

for i in range(0,rows):
    for j in range(0,columns):
        print(matrix[i][j], end = " ")
    print("\r")

print("The transpose of a matrix is: ")
for i in range(0,rows):
    for j in range(0,columns):
        print(matrix[j][i], end = " ")
    print("\r")