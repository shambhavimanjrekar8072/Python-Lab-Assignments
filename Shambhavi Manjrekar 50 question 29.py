n = int(input("Enter the steps you want to see the table in: "))
#using list comprehension:
table = ["10 * {} = {}".format(x,x*10) for x in range(1,n+1)]
print(table)
#using lambda function:
table_new = list(map(lambda x:x*10, range(1,n+1)))
print(table_new)
