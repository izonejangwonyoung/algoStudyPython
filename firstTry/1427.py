n = input()

a = list(n)
b = list(map(int, a))
b.sort(reverse=True)
for i in range(len(b)):
    print(b[i],end='')