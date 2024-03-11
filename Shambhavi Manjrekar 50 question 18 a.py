n = int(input("Enter a number: "))
def dec_to_bin(num):
    if num<=0:
        return 0
    return (dec_to_bin(num//2)*10) + (num%2)
print(dec_to_bin(n))
