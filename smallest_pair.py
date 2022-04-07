t= int(input())
for i in range(t):
    n= int(input())
    lst= []
    for j in range(n):
        lst.append(int(input()))
    lst.sort()
    print(lst[0]+lst)
