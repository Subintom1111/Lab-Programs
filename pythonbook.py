class publisher():
    def getpublisher(self):
        self.name=input("Enter the Name::")
    def display1(self):
        print("My Name ::",self.name)
class book(publisher):
    def title(self):
        self.title=input("Enter the Title::")
    def author(self):
        self.author=input("Enter the Author::")
    def display2(self):
        print("My Title ::",self.title)
        print("My Book author ::",self.author)
class python(book):
    def price(self):
        self.price=float(input("Enter the Price::"))
    def pageno(self):
        self.pageno=int(input("Enter the Pageno::"))
    def display(self):
        print("The Price ::",self.price)
        print("The pages ::",self.pageno)
sub=python()
sub.getpublisher()
sub.title()
sub.author()
sub.price()
sub.pageno()
sub.display1()
sub.display2()
sub.display()


