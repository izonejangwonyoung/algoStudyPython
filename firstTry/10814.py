n = int(input())

a = []
for i in range(n):
    a.append(list(map(str, input().split())))
# print(a)
for i in range(n):
    a[i][0]=int(a[i][0])
b = sorted(a, key=lambda x: x[0])
# print(b)
for i in range(n):
    print(b[i][0], b[i][1])
