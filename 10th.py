lst= []
n= int(input())
for i in range(n):
    lst.append(int(input()))
print(lst)
lst.sort()
print(lst)
print("Maximum element in the list is: ",lst[-1])