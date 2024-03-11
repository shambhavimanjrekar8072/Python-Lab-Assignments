n = int(input("Enter a number:"))
n1 = 0
n2 = 1
print(n1, n2 , sep=" ")
for i in range(0,n-2):
    print(n1+n2)
    temp = n1 + n2
    n1 = n2
    n2 = temp
