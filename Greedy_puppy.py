t= int(input())
for i in range(t):
    n,k= map(int,input().split())
    y=0
    for j in range(1,k+1):
        x= n%j
        y= max(y,x)
    print(y)
