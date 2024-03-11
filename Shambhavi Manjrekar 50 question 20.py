my_list = []
n = int(input("Enter the size of the list: "))
print("Enter the elements of the list: ")
for i in range(0,n):
    elements = int(input())
    my_list.append(elements)
max_num = max(my_list)
min_num = min(my_list) #This is using min and max functions

#Finding minimum number using for loop:
minimum = my_list[0]
for i in my_list:
    if i<minimum:
        minimum = i
#Finding maximum using for loop
maximum = my_list[0]
for i in my_list:
    if i>maximum:
        maximum = i

print("The maximum number using max function is: ",max_num)
print("The minimum number using min function is: ", min_num)
print("The maximum number using for loop is: ", maximum)
print("The minimum number using for loop is: ",minimum)
