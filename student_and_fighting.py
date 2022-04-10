t= int(input())
for _ in range(t):
    n= int(input())
    for i in range(n):
        lst= list(map(int,input().split()))
    lst.sort()
    for i in range(n):
        if(lst[i]!=lst[i+1]):
            print("peace:)")
        else:
            print("fight:(")
