n = int(input("Enter the number: "))
a = n
rev = 0
while(n>0):
    rem = n%10
    rev = rev*10 + rem
    n = n//10
if a == rev:
    print("The number is a Palindrome!")
else:
    print("The number is not a Palindrome!")
