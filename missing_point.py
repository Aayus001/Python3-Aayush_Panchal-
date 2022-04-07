t= int(input())
for i in range(t):
    n= int(input())
    d1= {}
    d2= {}
    for j in range(4*n-1):
        x,y = map(int,input().split())
        d1[x]= d1.get(x,0) + 1 
        d2[y]= d2.get(y,0) + 1
    for k,v in d1.items():
        if v%2!=0:
            x= k 
            break
    for k,v in d2.items():
        if v%2!=0:
            y= k 
            break
    print(x,y)
