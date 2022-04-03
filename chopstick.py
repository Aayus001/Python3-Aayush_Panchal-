n,d= map(int,input().split())
lst= []
for i in range(n):
    lst.append(int(input()))
lst.sort()
cnt= 0
j= 0
while(j<n-1):
    if (lst[j+1]-lst[j]<=d):
        cnt+=1
        j+=2
    else:
        j+=1
print(cnt)
