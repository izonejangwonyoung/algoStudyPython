#블로그 참고했음.. 어렵다

a, b, v = map(int, input().split())
result = 0

k=(v-b)/(a-b)
print(int(k) if k == int(k) else int(k)+1)
# for i in range(0, 200000000):
#     if v - a <= i * (a - b) < v:
#         result = i
#         break
# print(i+1)




# result=(v-a)/(a-b)
# print(result)
# if a - b > v:
#     result = 0
# if 0 < result < 1:
#     result = 1
# # print(result)
# if ((v - a) / (a - b)).is_integer() or result == 1 or result == 0:
#     print('딱 떨어져서 바로 표현합니다')
#     print(round(result + 1))
#
# else:
#     for i in range(1, 1000000000):
#         if i <= (v / result) < i + 1:
#             real = i
#             # print(i)
#             break
#
#     print(i + 1)
