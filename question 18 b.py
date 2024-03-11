n = int(input("Enter a number in decimal: "))
def dec_to_oct(num):
    if num<=0:
        return 0
    return(dec_to_oct(num//8)*10) + (num%8)
print(dec_to_oct(n))