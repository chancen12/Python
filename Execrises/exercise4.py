products = {
"SMART WATCH": 550,
"PHONE" : 1000,
"PLAYSTATION": 500,
"LAPTOP": 1550,
"MUSIC PLAYER" : 600,
"TABLET" : 400
}
def exercise(d):
    dict2={}
    a=int(input("enter Price"))
    for i in d.keys():
        price=d[i]
        if price<=a:
           dict2[i]=price
    return dict2
print(exercise(products))

                





        
    
    

