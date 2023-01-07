from builtins import range

t = int(input())


dp=[[0]*15 for _ in range(15)]      #15짜리 배열이 15개 있는 배열을 초기화시킴
dp[0]=[x for x in range(15)]        #0층 초기화

for i in range(1,15):
    for j in range(1,15):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]
for _ in range(t):
    k = int(input())
    n = int(input())
    print(dp[k][n])


##다이나믹 프로그래밍에 대해서
