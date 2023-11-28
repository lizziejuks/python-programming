#creating class and object
class Circle:
    def _init_(self,radius):
        self.radius=radius
    #calculate perimeter 
    def perimeter(self):
        p=2*3.14*self.radius
        return p
    #calculate area
    def area(self):
        a=2*3.14*self.radius*self.radius
        return a
    #display the output
    radius=Circle(5)
    print(radius.perimeter())
    print(radius.area())