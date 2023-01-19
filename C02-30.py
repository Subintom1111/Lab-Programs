n = int(input("Enter no. of lines :"))
a = 0

while (a < n):
    k = 0
    while (k <= (n - a)):
        print(" ", end=" ")
        k = k + 1

    j = 0
    while (j <= a):
        print(" * ", end=" ")
        j = j + 1
    a = a + 1
    print("\n")


