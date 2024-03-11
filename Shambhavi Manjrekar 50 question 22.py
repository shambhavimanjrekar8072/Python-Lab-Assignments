n = int(input("Enter the range: "))
sample_list = ['p','q']
new_list = ['{}{}'.format(x,y) for y in range(1,n+1) for x in sample_list]
print(new_list)
