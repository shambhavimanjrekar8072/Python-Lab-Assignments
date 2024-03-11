n = int(input("Enter the number: "))
s = 0
while(n>0):
    r = n % 10
    n = n//10
    s = s + r
print("The sum of digits of given number is: ",s)
