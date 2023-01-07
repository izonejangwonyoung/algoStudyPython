N = int(input())
result = 0

count = 0
while True:
    if N % 5 == 0:
        break
    count += 1
    N = N - 3
# print(N)
fivekgcount = int((N/5))
# print('3kg짜리는', count, '봉지')
# print('5kg짜리는', fivekgcount)
result=count+fivekgcount
if N<0:
    result=-1

print(result)