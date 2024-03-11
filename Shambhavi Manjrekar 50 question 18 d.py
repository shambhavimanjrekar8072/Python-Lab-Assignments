n = int(input("Enter the steps you want to print: "))
def fab(prv1,prv2,count):
    if count ==0:
        return
    temp = prv1 + prv2
    print(temp)
    prv1 = prv2
    prv2 = temp
    fab(prv1,prv2,count-1)

def fab_generator(num):
    if num>=2:
        print("0")
        print("1")
        fab(0,1,num-2)
    elif num == 1:
        print("0")
    else:
        return

print(fab_generator(n))
