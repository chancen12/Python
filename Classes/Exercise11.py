class ex11():
    def __init__(self):
        self.radius=int(input())

    def area(self):
        return pow(self.radius,2)*3.14
    
    
    def perimeter(self):
        return round(self.radius*2*3.14,2)
        

ex = ex11()
print("area is: ",ex.area())
print("perimeter is: ",ex.perimeter())
