
a=[0 for _ in range(5)]
for i in range(0,5):
    a[i]=int(input())

a.sort()
print(int(sum(a)/5))
print(a[2])