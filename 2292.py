number = int(input())
result = 0;
test = []
for i in range(1, 1000000000):
    a = 1 + (3 * (i) * (i - 1))
    test.append(a)
    b = 1 + (3 * (i + 1) * (i))
    if b >= number > a:
        result = i + 1
        break
    elif a == number:
        result = i
        break
print(result)

#점화식이라는 개념.. 다시 떠올려야만해!!