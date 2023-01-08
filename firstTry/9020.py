dp = []

for i in range(1, 10000):
    if i == 1:
        continue
    for k in range(2, int(i ** 0.5) + 1):
        if i % k == 0:  # 소수가 아니라면
            break
    else:
        dp.append(i)

# print(dp)  #
turnnumber = int(input())
totaltrynumber = list(input() for _ in range(turnnumber))
newnewlist = list(map(int, totaltrynumber))
for p in range(0, turnnumber):
    if p == turnnumber:
        exit()
    n = newnewlist[p]
    number = n
    k = 0
    for j in range(0, len(dp) - 1):
        if dp[j] < n < dp[j + 1]:
            n = j

    # print(n, '=n는 ', dp[n], '~', dp[n + 1], '사이에 있음')
    array_i = []
    array_k = []
    stop = 0
    # print(dp[0]+dp[0])
    for i in range(0, len(dp)):
        for k in range(0, len(dp)):
            # print('i=', i, 'k=', k)
            if int(dp[i] + dp[k]) == number:
                # print(i, k)
                # stop = 1
                array_i.append(dp[i])
                array_k.append(dp[k])

        # if stop == 1:
        #     print('최종답')
        #     print(array_i)
        #     print(array_k)
        #     break
    # print(array_i)
    # print(array_k)
    save = []
    savetemp = []
    for i in range(0, len(array_i)):
        h = abs(array_i[i] - array_k[i])
        save.append(h)

    minmin = min(save)
    temp = save.index(minmin)
    # savetemp.append(temp)
    print(array_i[temp], array_k[temp])

# for i in range(len(savetemp)):
#     print(array_i[temp], array_k[temp])
