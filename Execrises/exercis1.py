list1=[86,86,85,85,85,83,23,45,84,1,2,0]
def exercise3(arr):
    a=set(arr)
    a=list(a)
    a.sort(reverse=True)
    return a[0],a[1]

print(exercise3(list1))

