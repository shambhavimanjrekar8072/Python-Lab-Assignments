n = int(input("Enter the number of 3 digit: "))
a = n
sop = 0
while(n>0):
    r = n % 10
    sop = sop + r**3
    n = n//10
if a == sop:
    print("The number is an Armstrong Number!")
else:
    print("The number is not an Armstrong Number!")
