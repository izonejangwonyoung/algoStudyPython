#
# for i in range(0, len(dp)):
#     for k in range(2, 100000):
#         if dp[i] % k == 0:
#             print(dp[i])
#             print(k)
#             print('나머지값은', dp[i] % k)
#             print('i=', i)
#             print('k=', k)
#             for j in range(2, 1000):
#                 if (j*dp[i]) > dp[-1]:
#                     break
#                 else:
#                     # dp[i + (j * dp[i])] = 0
#                     print(j)
#                     try:a=dp.index(j*dp[i])
#                     except: pass
#                     dp[a]=0
#                     print('실행완료')
#             print(dp)
#             print('-------------')
#             break
#         else:
#             pass
# print(dp)

#
# m, n = map(int, input().split())
#
# dp = [x for x in range(m, n + 1)]
# for i in range(0, len(dp)):
#     for k in range(2, n):  # k의 배수를 배열에서 모두 제거하기 위해서 반복문에 삽입함
#         for j in range(2, 100000):
#             try:
#                 a = dp.index(k * j)
#             except:
#                 pass
#             # print(a)
#             dp[a] = 0
#
#             if k * j > n:
#                 break
#
# newlist = [x for x in dp if x != 0]
#
# for i in range(0, len(newlist)):
#     print(newlist[i])
# ##내 코드는 동작하지만 시간 초과로 나타남
import math

m, n = map(int, input().split())
number = int(math.sqrt(n))  ##2부터 a의 배수까지만 지워주면 된다
print(number)

for i in range(m, n + 1):
    if i == 1:
        continue

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break

    else:
        print(i)
#에라토스테네스의 체는 소수 구하기 문제일 때 무조건 이용해야한다!!! 시간 복잡도의 클래스가 달라진다