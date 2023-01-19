n=int(input("enter the number"))
temp=n
p=0
while(temp!=0):
    q=temp%10
    p=p+(q*q*q)
    temp=temp//10
if p==n:
        print("is an armstrong")
else:
        print("is not an armstrong")
