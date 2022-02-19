t= int(input())
for i in range(t):
    a,b,c= input().split()
    x= int(a)
    y= int(b)
    z= int(c)
    if((x>y and x<z) or (x>z and x<y)):
        print(x)
    elif((y>x and y<z) or (y>z and y<x)):
        print(y)
    elif((z>x and z<y) or (z>y and z<x)):
        print(z)
