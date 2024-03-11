list1 = [8,9,3,5,1,9,4,3]
list2 = []
for num in list1:
    if num not in list2:
        list2.append(num)
print("The final list is: ",list2)