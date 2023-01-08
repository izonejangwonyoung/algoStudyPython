# n = int(input())
# # dx = [[0 for _ in range(2)] for _ in range(n)]
# # dy = [[0 for _ in range(2)] for _ in range(n)]
# # for i in range(0, n):
# #     a, b = map(int, input().split())
# #     dx[i][0]=a
# #     dx[i][1]=a+10
# #     dy[i][0]=b
# #     dy[i][1]=b+10
# # value=[]
# # count=0
# # for i in range(0,n):
# #     for j in range(i+1,n):
# #         if dx[i][1]<dx[j][0]: #겹치지않는다면?
# #             count+=1
# #
# #         else:
# #             value.append(dx[i][1]-dx[j][0])
# #             count+=1
# #     if count==n*(n-1)/2:
# #         break
# # print(dx)
# # print(dy)
# # print(value)
# temp = []
# dp = [[0 for _ in range(2)] for _ in range(n)]
# for i in range(0, n):
#     a, b = map(int, input().split())
#     dp[i][0] = a
#     dp[i][1] = b
#
# square = 0
#
# for i in range(0, n):
#     for j in range(i + 1, n):
#         if dp[j][0] + 10 > dp[i][0] + 10 > dp[j][0]:  # x축 구간이 겹친다면
#             if dp[j][1] + 10 > dp[i][1] > dp[j][1]:  # y축 구간도 겹친다면
#                 a = (dp[i][0] + 10 - dp[j][0])
#                 b = (dp[j][1] + 10 - dp[i][1])
#
#                 square = square + (a * b)
#
# print(100*n - square)
# #     dp[i][0] = a
# #     dp[i][1] = a + 10
# #     dp[i][2] = b
# #     dp[i][3] = b + 10
# # xvalue = 0
# # yvalue = 0
# # print(dp)
# # for i in range(0, n):
# #     for j in range(0, n):
# #         if i==j:
# #             pass
# #         if dp[i][1] > dp[j][0]:
# #             print(i)
# #             print(j)
# #             xvalue = int(dp[j][0] - dp[i][1])
# #             print('zz',xvalue)
# #             if dp[i][2] < dp[j][2]:
# #                 yvalue = int(dp[j][2] - dp[i][2])
# #                 print(yvalue)
n = int(input())
dp = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n):
    a, b = map(int, input().split())
    for k in range(a, a + 10):
        for j in range(b, b + 10):
            dp[k][j] += 1
countarray = []
count = 0
for i in range(100):
    for j in range(100):
        if dp[i][j] > 0:
            count += 1

print(count)
# for i in range(100):
#     for k in range(2,n+1):
#         if dp[i].count(k)>0:
#             countarray.append(dp[i].count(k))
#             countarray.append(k)
# # print(countoftwo)
# # print(countofthree*2)
# # print(countarray)
# sum=0
# for i in range(len(countarray)//2):
#     sum+=countarray[2*i]*(countarray[2*i+1]-1)
#
# print(sum)
