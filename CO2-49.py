s=int(input("Enter the Number :"))
sum=0
for i in range(0,len(str(s))):
    rem=s%10
    sum=(sum*10)+rem
    s=s//10
print("The Reverse is ",sum)
