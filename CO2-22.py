limit = int(input("Enter your limit  :"))
a = 1
sumodd = 0
sumeven = 0
while a <= limit:
    if a%2 == 0:
        sumeven = sumeven + a
    else:
        sumodd = sumodd + a
    a = a+1
print("sum of odd numbers:",sumodd)
print("sum of even numbers:",sumeven)

