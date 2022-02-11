
def maximum(y):
    i=0
    a=0
    while i<len(y):
        if y[i]>a:
            a=y[i]
        i=i+1
    print(a)    
maximum([8, 5, 76, 34, 2, 67, 29, 55]) 
