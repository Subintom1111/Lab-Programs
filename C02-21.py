print("Select the Operation. \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division\n")
choice = input("Enter the Choice  : ")

if choice in ('1', '2', '3', '4'):
    x = float(input("\nEnter First Number: "))
    y = float(input("Enter Second Number: "))
    if choice == '1':
        print(x + y)
    elif choice == '2':
        print(x - y)
    elif choice == '3':
        print(x * y)
    elif choice == '4':
        print(x / y)
else:
    print("Invalid ")
