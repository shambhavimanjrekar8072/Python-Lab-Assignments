n = int(input("Enter the number: "))
flag = True
for i in range(2,n):
    if n%i==0:
        flag = False
        break
if flag == True:
    print("The given number is prime!")
else:
    print("The given number is composite!")




