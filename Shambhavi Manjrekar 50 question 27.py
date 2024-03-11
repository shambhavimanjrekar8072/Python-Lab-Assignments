n = int(input("Enter the number to be used to check divisibility: "))
my_list = [10,20,30,40,50]
new_list = [x//n for x in my_list if x%n == 0]
if len(my_list) == len(new_list):
    print("All the numbers in the list are divisible by ",n)
print(new_list)
