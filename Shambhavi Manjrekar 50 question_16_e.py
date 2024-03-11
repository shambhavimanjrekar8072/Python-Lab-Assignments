rows = int(input("Enter the number of rows: "))
from math import factorial
for n in range(rows):
    for space in range(1,rows - n):
        print(end=" ")
    for r in range(n+1):
        print(factorial(n)//(factorial(r)*factorial(n-r)),end = " ")
    print("\r")
