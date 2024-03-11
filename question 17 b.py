n = int(input("Enter the number: "))
def sum(n):
    s = 0
    for i in range(1, n+1):
        s = s + i
    print("The sum of ",n,"natural numbers is : ",s)
sum(n)