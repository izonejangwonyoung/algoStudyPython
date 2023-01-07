n = int(input())
dp = list(map(int, input().split()))
count = 0  # 소수 아닌 놈 카운트합니다
for i in range(0, len(dp)):
    if dp[i] == 1:
        # print('현재 계산중인 값은', dp[i])
        count += 1
    else:
        for k in range(2, dp[i] - 1):
            # print('여기 지나느중')
            if dp[i] % k == 0:  # 나누어떨어지는 순간 소수가 아니게 된다
                # print('여기 계산중입니다')
                count += 1
                break
print(len(dp) - count)
