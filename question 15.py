n = int(input("Enter the number between 500 and 1000: "))
a = n
rev = 0
if (n>=500 and n<=1000):
    while n>0:
        rem = n%10
        rev = rev*10 + rem
        n = n//10
    if a == rev:
        print("The given number is a palindrome")
    else:
        print("The given number is not a palindrome")
else:
    print("The number doesn't lie in the given range")

