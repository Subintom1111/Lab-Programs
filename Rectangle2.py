
class Rectangle():
    def __init__(self,l,b):
        self.__length= l
        self.__breadth=b
        self.area=l*b

    def __lt__(self,other):
        if self.area<other.area:
           print("Rectangle 1 is smaller in area")
        else:
           print("Rectangle 2 is smaller in area")

r1=Rectangle(10,5)
r2=Rectangle(30,10)
print(r1<r2)
