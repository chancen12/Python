class myMath():
    def addition(self,a,b):
        return(a+b)
    def substraction(self,a,b):
        return(a-b)
    def division(self,a,b):
        return(a/b)
    def multiplication(self,a,b):
        return(a*b)
    def power1(self,a,b):
        return(pow(a,b))

a=myMath()
x=int(input("1st nmbr:"))
y=int(input("2nd nmbr:"))
print(a.addition(x,y))
print(a.substraction(x,y))
print(a.division(x,y))
print(a.multiplication(x,y))
print(a.power1(x,y))





