import math

a = []
number = int(input())

for i in range(0, number):
    h, w, n = map(int, input().split())
    if n % h == 0:
        row = int((n / h))
    else:
        row = int(math.ceil(n / h))

    if row * h == n:
        column = h
    else:
        column = int(n-(h*(row-1)))
    # if math.floor(n / h)==1:
    #     row=math.ceil(n/h)
    #     print('걸러짐')
    # else:
    #     row = math.floor(n / h) + 1   ##호수
    # column = n - ((row - 1) * h)    ###층수
    #
    a.append(column*100+row)
    # print(column)
    # print(row)
for i in range(0, len(a)):
    print(a[i])
