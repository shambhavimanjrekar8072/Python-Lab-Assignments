n = int(input("Enter a number: "))
def fact_number(num):
  if num == 1:
      return 1
  return num*fact_number(num-1)
print(fact_number(n))
