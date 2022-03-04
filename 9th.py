n= int(input())
m= int(input())
for i in range(1,n+1):
    if(i%m==0):
        print(i)
        if(i%2==0):
            print(i,"is even number ")
        else:
            print(i,"is odd number")
            