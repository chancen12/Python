def function2(m):
    a=0
    b=0
    for i in m:
        if i.isupper():
           a=a+1
        if i.islower():
            b+=1     
    return(a,b) 
n=input("enter a word")
print(function2(n))
