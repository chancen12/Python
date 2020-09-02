class ex10():
    def __init__(self):
        self.length=int(input())
        self.width=int(input())

    def area(self):
        return self.length*self.width
        

ex = ex10()
print("area is: ",ex.area())
