n=int(input())

a=[]
for i in range(n):
    a.append(list(map(int,input().split())))


for i in range(n):
    a[i][0],a[i][1]=a[i][1],a[i][0]

a.sort()
for i in range(n):
    print(a[i][1],a[i][0])