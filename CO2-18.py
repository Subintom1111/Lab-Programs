n=int(input("enter the number"))
temp=n
p=0
while(temp!=0):
    q=temp%10
    p=p*10+q
    temp=temp//10
if p==n:
        print(" palindrome")
else:
        print(" not a palindrome")

