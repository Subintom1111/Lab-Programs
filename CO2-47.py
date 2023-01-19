r= int(input("Enter the Limit:"))

n1, n2 = 0, 1
for i in range(r):

       print(n1,end=' ')
       nth = n1 + n2

       n1 = n2
       n2 = nth
