m = int(input())
n = int(input())

dp = list([x for x in range(m, n + 1)])
value = int
for i in range(0, len(dp)):  # 리스트 속 모든 숫자를 순회한다
    value = dp[i]
    if value == 1:
        dp[i] = 0
    else:
        pass
    for j in range(2, value - 1):
        if value % j == 0:
            dp[i] = 0
            break

new = [i for i in dp if i != 0]
if len(new) == 0:
    print(-1)
else:
    print(sum(new))
    print(new[0])
    # dp.pop(1) 로 인덱스 속 요소 제거 가능
