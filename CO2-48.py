num=int(input("Enter the Number :"))
copy=num
sum=0
for i in range(0,len(str(num))):
    rem=num%10
    sum=sum+(rem*rem*rem)
    num=num//10

if sum==copy:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong ")
