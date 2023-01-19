class Rectangle():
    def __init__(self,l,b):
        self.length= l
        self.breadth= b

    def rectangle_area(self):
        return self.length*self.breadth

    def rectangle_perimeter(self):
        return 2*(self.length+self.breadth)
l1=float(input("Enter length of Rectangle:"))
b1=float(input("Enter the Breadth of Rectangle:"))
l2=float(input("Enter the length of Rectangle:"))
b2=float(input("Enter the Breadth of Rectangle:"))
rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)
print("Area of rectangle 1 is {} and perimeter is {}:".format(rect1.rectangle_area(),rect1.rectangle_perimeter()))
print("Area of rectangle 2 is {} and perimeter is {}:".format(rect2.rectangle_area(),rect2.rectangle_perimeter()))
print(rect1.rectangle_area()>rect2.rectangle_area())



