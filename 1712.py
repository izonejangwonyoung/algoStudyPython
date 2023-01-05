value = input().split()
a = int(value[0])
b = int(value[1])
c = int(value[2])
# print(a)
# print(b)
# print(c)
result = 0;
n = 0;
if c <= b:
    result = -1

# elif b<c:
#     while True:
#
#         if n*(c - b) > a:
#             result = n
#             break
#
#         else:
#             pass
#         n += 1

elif b < c:

    temp = a % (c - b)
    result = (a // (c - b))
    if temp == 0:
        result = result + 1
    else:
        result = result + 1
print(result)
