n = int(input())
a = list(map(int, input().split()))
print(a)

arr2 = sorted(list(set(a)))

dic = {arr2[i]: i for i in range(len(arr2))}
print(dic)
print(dic[-10])
for i in a:
    print(dic[i], end=' ')
