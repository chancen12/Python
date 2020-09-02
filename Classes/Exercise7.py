class ex7:
   def exponent(self):
       exp=1
       b=int(input("enter base"))
       ex=int(input("enter exponent:"))
       for _ in range(ex):
            exp=exp*b
       return(exp)
    
print(ex7().exponent())